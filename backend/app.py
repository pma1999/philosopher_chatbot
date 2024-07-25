from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import anthropic
from config import ANTHROPIC_API_KEY
import logging
from translations import translations
from philosophers import philosophers

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['http://localhost:3000'])
# Configuración de la sesión
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = ANTHROPIC_API_KEY  # Asegúrate de cambiar esto en producción
Session(app)

# Configuración del limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Configurar logging
logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def setup_anthropic_client(api_key):
    try:
        return anthropic.Anthropic(api_key=api_key)
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
        return jsonify({"valid": True}), 200
    else:
        return jsonify({"valid": False}), 400

@app.route('/api/philosophers', methods=['GET'])
def get_philosophers():
    language = request.args.get('language', 'en').lower()  # Convertir a minúsculas
    philosopher_list = []
    for key, value in philosophers.items():
        if language in value:
            philosopher_list.append({
                "id": key,
                "name": value[language]['name'],
                "period": value[language]['period']
            })
        else:
            # Si el idioma no está disponible, usar inglés como fallback
            fallback_lang = 'en'
            philosopher_list.append({
                "id": key,
                "name": value[fallback_lang]['name'],
                "period": value[fallback_lang]['period']
            })
    return jsonify(philosopher_list)

@app.errorhandler(Exception)
def handle_exception(e):
    # Registra el error
    app.logger.error(f"Unhandled exception: {str(e)}")
    # Devuelve una respuesta de error genérica
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/start-conversation', methods=['POST'])
def start_conversation():
    language = request.json.get('language')
    philosopher_id = request.json.get('philosopher_id')
    api_key = request.headers.get('x-api-key')

    if not all([language, philosopher_id, api_key]):
        return jsonify({"error": "Missing required parameters"}), 400

    client = setup_anthropic_client(api_key)
    if not client:
        return jsonify({"error": "Invalid API key"}), 400

    philosopher_data = philosophers.get(philosopher_id, {}).get(language)
    if not philosopher_data:
        return jsonify({"error": "Invalid philosopher or language"}), 400

    system_prompt = create_system_prompt(philosopher_data, translations[language])
    session['language'] = language
    session['philosopher_id'] = philosopher_id
    session['api_key'] = api_key
    session['system_prompt'] = system_prompt
    session['conversation'] = []
    session.modified = True

    return jsonify({"message": "Conversation started successfully"}), 200

@app.route('/api/send-message', methods=['POST'])
@limiter.limit("10 per minute")
def send_message():
    message = request.json.get('message')
    api_key = request.headers.get('x-api-key')

    if not message or not api_key:
        return jsonify({"error": "Message and API key are required"}), 400

    if 'conversation' not in session:
        return jsonify({"error": "Conversation not started"}), 400

    client = setup_anthropic_client(api_key)
    if not client:
        return jsonify({"error": "Invalid API key"}), 400

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            system=session['system_prompt'],
            messages=session['conversation'] + [{"role": "user", "content": message}]
        )
        ai_response = response.content[0].text if response.content else "Lo siento, no pude generar una respuesta."
        session['conversation'].append({"role": "user", "content": message})
        session['conversation'].append({"role": "assistant", "content": ai_response})
        session.modified = True
        return jsonify({"response": ai_response}), 200
    except Exception as e:
        logging.error(f"Error in AI response: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)