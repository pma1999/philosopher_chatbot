import anthropic
from config import ANTHROPIC_API_KEY
import sys
import io
import logging
from translations import translations
from philosophers import philosophers

# Configurar logging
logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def configure_language() -> str:
    while True:
        try:
            choice = int(input(translations['es']['language_selection']))
            if 1 <= choice <= 3:
                return ['es', 'en', 'ca'][choice - 1]
            else:
                print(translations['es']['invalid_language'])
        except ValueError:
            print(translations['es']['invalid_language'])
    return 'es'

def select_philosopher(language: str) -> dict:
    trans = translations[language]
    print(trans['available_philosophers'])
    for i, philosopher in enumerate(philosophers.keys(), 1):
        print(f"{i}. {philosophers[philosopher][language]['name']} ({philosophers[philosopher][language]['period']})")

    while True:
        try:
            choice = int(input(trans['choose_philosopher'])) - 1
            if 0 <= choice < len(philosophers):
                selected_philosopher = list(philosophers.keys())[choice]
                return philosophers[selected_philosopher][language]
            else:
                print(trans['invalid_choice'])
        except ValueError:
            print(trans['invalid_choice'])

def setup_anthropic_client() -> anthropic.Anthropic:
    try:
        return anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    except Exception as e:
        logging.error(f"Error setting up Anthropic client: {e}")
        print(f"Error setting up Anthropic client: {e}")
        sys.exit(1)

def create_system_prompt(philosopher_data: dict, translations: dict) -> str:
    return translations['system_prompt'].format(
        philosopher_data['name'],
        philosopher_data['period'],
        philosopher_data['years'],
        ', '.join(philosopher_data['main_ideas']),
        philosopher_data['historical_context'],
        ', '.join(philosopher_data['main_works'])
    )

def handle_user_input(translations: dict) -> str:
    user_input = input(f"{translations['you']} ")
    if user_input.lower() in ['exit', 'salir', 'sortir']:
        return None
    return user_input

def process_ai_response(client: anthropic.Anthropic, messages: list, system_prompt: str, max_tokens: int) -> str:
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages
        )
        logging.info(f"API Response: {response}")
        
        # Verificar si hay contenido en la respuesta
        if response.content:
            # Buscar el primer bloque de texto en el contenido
            for content_block in response.content:
                if hasattr(content_block, 'type') and content_block.type == 'text' and hasattr(content_block, 'text'):
                    return content_block.text
        
        # Si no se encuentra ningún bloque de texto, registrar un error y devolver None
        logging.error("No text content found in API response")
        return None
    except anthropic.APIError as e:
        logging.error(f"API Error: {e}")
        print(f"An error occurred: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")
        return None

def update_conversation(messages: list, role: str, content: str) -> None:
    messages.append({"role": role, "content": content})

def display_philosopher_info(philosopher_data: dict, trans: dict) -> None:
    print(f"\n{trans['philosopher_info']}:")
    print(f"{trans['name']}: {philosopher_data['name']}")
    print(f"{trans['period']}: {philosopher_data['period']} ({philosopher_data['years']})")
    print(f"{trans['main_ideas']}:")
    for idea in philosopher_data['main_ideas']:
        print(f"  - {idea}")
    print(f"{trans['historical_context']}: {philosopher_data['historical_context']}")
    print(f"{trans['main_works']}:")
    for work in philosopher_data['main_works']:
        print(f"  - {work}")
    print(f"{trans['famous_quotes']}:")
    for quote in philosopher_data['famous_quotes']:
        print(f"  \"{quote}\"")
    print("\n")

def main():
    language = configure_language()
    trans = translations[language]
    philosopher_data = select_philosopher(language)

    display_philosopher_info(philosopher_data, trans)

    print(f"\n{trans['chatting_with'].format(philosopher_data['name'])}\n")

    client = setup_anthropic_client()
    system_prompt = create_system_prompt(philosopher_data, trans)

    messages = []
    update_conversation(messages, "user", trans['initial_greeting'])

    while True:
        ai_response = process_ai_response(client, messages, system_prompt, 1000)
        if ai_response:
            print(f"{philosopher_data['name']}: {ai_response}")
            update_conversation(messages, "assistant", ai_response)
        else:
            print(trans['error_occurred'].format(trans['try_again']))

        user_input = handle_user_input(trans)
        if user_input is None:
            break
        update_conversation(messages, "user", user_input)

    print(trans['exit'])

if __name__ == "__main__":
    main()