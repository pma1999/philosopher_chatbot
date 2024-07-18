import anthropic
from anthropic.types import ContentBlock
from config import ANTHROPIC_API_KEY
import sys
import io
import codecs
from translations import translations
from philosophers import philosophers

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def select_language():
    while True:
        try:
            choice = int(input(translations['es']['language_selection']))
            if 1 <= choice <= 3:
                return ['es', 'en', 'ca'][choice - 1]
            else:
                print(translations['es']['invalid_language'])
                return 'es'
        except ValueError:
            print(translations['es']['invalid_language'])
            return 'es'

def main():
    language = select_language()
    trans = translations[language]
    
    print(trans['welcome'])
    print(trans['available_philosophers'])
    for i, philosopher in enumerate(philosophers.keys(), 1):
        print(f"{i}. {philosophers[philosopher][language]['name']}")

    while True:
        try:
            choice = int(input(trans['choose_philosopher'])) - 1
            if 0 <= choice < len(philosophers):
                break
            else:
                print(trans['invalid_choice'])
        except ValueError:
            print(trans['invalid_choice'])

    selected_philosopher = list(philosophers.keys())[choice]
    philosopher_data = philosophers[selected_philosopher][language]

    print(f"\n{trans['chatting_with'].format(philosopher_data['name'])}\n")

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    system_prompt = trans['system_prompt'].format(
        philosopher_data['name'],
        philosopher_data['period'],
        ', '.join(philosopher_data['main_ideas'])
    )

    messages = [
        {"role": "user", "content": "Hello, I'd like to learn about your philosophical ideas."}
    ]

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            system=system_prompt,
            messages=messages
        )

        assistant_response = response.content[0].text
        print(f"{philosopher_data['name']}: {assistant_response}")
        messages.append({"role": "assistant", "content": assistant_response})

    except anthropic.APIError as e:
        print(f"{trans['error_occurred'].format(e)}")
        print(trans['try_again'])

    while True:
        user_input = input(f"{trans['you']} ")
        if user_input.lower() in ['exit', 'salir', 'sortir']:
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1000,
                system=system_prompt,
                messages=messages
            )

            assistant_response = response.content[0].text
            print(f"{philosopher_data['name']}: {assistant_response}")
            messages.append({"role": "assistant", "content": assistant_response})

        except anthropic.APIError as e:
            print(f"{trans['error_occurred'].format(e)}")
            print(trans['try_again'])

    print(trans['exit'])

if __name__ == "__main__":
    main()
