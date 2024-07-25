from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import random
import string
import os
import anthropic
import logging
from translations import translations
from philosophers import philosophers
import uuid
try:
    from config import ANTHROPIC_API_KEY, SECRET_KEY, SESSION_TYPE, SESSION_PERMANENT, SESSION_USE_SIGNER, RATELIMIT_DEFAULT
except:
    # Si el archivo no existe, lo creamos con valores predeterminados
    config_content = f"""
ANTHROPIC_API_KEY = ''
SECRET_KEY = '{''.join(random.choices(string.ascii_letters + string.digits, k=32))}'
SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True
RATELIMIT_DEFAULT = '10 per minute'
"""
    
    with open('config.py', 'w') as config_file:
        config_file.write(config_content)
    
    print("Se ha creado el archivo config.py con valores predeterminados.")
    
    # Ahora importamos las variables del archivo recién creado
    from config import ANTHROPIC_API_KEY, SECRET_KEY, SESSION_TYPE, SESSION_PERMANENT, SESSION_USE_SIGNER, RATELIMIT_DEFAULT




app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['http://localhost:3000'])

# Session configuration
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SESSION_TYPE'] = SESSION_TYPE
app.config['SESSION_PERMANENT'] = SESSION_PERMANENT
app.config['SESSION_USE_SIGNER'] = SESSION_USE_SIGNER
Session(app)

# Rate limiter configuration
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=[RATELIMIT_DEFAULT]
)

# Logging configuration
logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def get_api_key():
    return session.get('api_key') or os.environ.get('ANTHROPIC_API_KEY') or ANTHROPIC_API_KEY

def setup_anthropic_client(api_key=None):
    try:
        return anthropic.Anthropic(api_key=api_key or get_api_key())
    except Exception as e:
        logging.error(f"Error setting up Anthropic client: {e}")
        return None

def create_system_prompt(philosopher_data, translations):
    return translations['system_prompt'].format(
        philosopher_data['name'],
        philosopher_data['period'],
        philosopher_data['years'],
        ', '.join(philosopher_data['main_ideas']),
        philosopher_data['historical_context'],
        ', '.join(philosopher_data['main_works'])
    )

@app.route('/api/languages', methods=['GET'])
def get_languages():
    return jsonify(list(translations.keys()))

@app.route('/api/validate-api-key', methods=['POST'])
def validate_api_key():
    api_key = request.json.get('api_key')
    client = setup_anthropic_client(api_key)
    if client:
        session['api_key'] = api_key
        return jsonify({"valid": True}), 200
    else:
        return jsonify({"valid": False}), 400

@app.route('/api/check-api-key', methods=['GET'])
def check_api_key():
    api_key = get_api_key()
    return jsonify({"has_api_key": bool(api_key)}), 200

@app.route('/api/update-language', methods=['POST'])
def update_language():
    language = request.json.get('language')
    if language in translations:
        session['language'] = language
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False, "error": "Invalid language"}), 400

@app.route('/api/philosophers', methods=['GET'])
def get_philosophers():
    language = request.args.get('language', 'en').lower()
    philosopher_list = []
    for key, value in philosophers.items():
        if language in value:
            philosopher_list.append({
                "id": key,
                "name": value[language]['name'],
                "period": value[language]['period']
            })
        else:
            fallback_lang = 'en'
            philosopher_list.append({
                "id": key,
                "name": value[fallback_lang]['name'],
                "period": value[fallback_lang]['period']
            })
    return jsonify(philosopher_list)

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Unhandled exception: {str(e)}")
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/start-conversation', methods=['POST'])
def start_conversation():
    language = request.json.get('language')
    philosopher_id = request.json.get('philosopher_id')
    api_key = get_api_key()

    if not all([language, philosopher_id, api_key]):
        return jsonify({"error": "Missing required parameters"}), 400

    client = setup_anthropic_client(api_key)
    if not client:
        return jsonify({"error": "Invalid API key"}), 400

    philosopher_data = philosophers.get(philosopher_id, {}).get(language)
    if not philosopher_data:
        return jsonify({"error": "Invalid philosopher or language"}), 400

    system_prompt = create_system_prompt(philosopher_data, translations[language])
    
    session_id = str(uuid.uuid4())
    session[session_id] = {
        'language': language,
        'philosopher_id': philosopher_id,
        'philosopher_name': philosopher_data['name'],
        'system_prompt': system_prompt,
        'conversation': []
    }
    session.modified = True

    return jsonify({
        "message": "Conversation started successfully",
        "session_id": session_id,
        "philosopher_name": philosopher_data['name']
    }), 200

@app.route('/api/send-message', methods=['POST'])
@limiter.limit("10 per minute")
def send_message():
    session_id = request.json.get('session_id')
    message = request.json.get('message')
    api_key = get_api_key()

    if not all([session_id, message, api_key]):
        return jsonify({"error": "Session ID, message, and API key are required"}), 400

    if session_id not in session:
        return jsonify({"error": "Conversation not started"}), 400

    session_data = session[session_id]

    client = setup_anthropic_client(api_key)
    if not client:
        return jsonify({"error": "Invalid API key"}), 400

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            system=session_data['system_prompt'],
            messages=session_data['conversation'] + [{"role": "user", "content": message}]
        )
        ai_response = response.content[0].text if response.content else translations[session_data['language']]['error_response']
        session_data['conversation'].append({"role": "user", "content": message})
        session_data['conversation'].append({"role": "assistant", "content": ai_response})
        session.modified = True
        return jsonify({
            "response": ai_response,
            "philosopher_name": session_data['philosopher_name']
        }), 200
    except Exception as e:
        logging.error(f"Error in AI response: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
