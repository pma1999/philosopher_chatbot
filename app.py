import anthropic
from anthropic.types import ContentBlock
from config import ANTHROPIC_API_KEY
import sys
import io
import codecs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def read_philosophers():
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            with codecs.open('philosophers.py', 'r', encoding=encoding) as file:
                content = file.read()
            exec(content, globals())
            return philosophers
        except UnicodeDecodeError:
            continue
    raise ValueError("Unable to read philosophers.py with any of the attempted encodings")

philosophers = read_philosophers()

def main():
    print("Welcome to the Philosopher Chatbot!")
    print("Available philosophers:")
    for i, philosopher in enumerate(philosophers, 1):
        print(f"{i}. {philosopher['name'].encode('utf-8').decode('utf-8')}")

    while True:
        try:
            choice = int(input("Choose a philosopher (enter the number): ")) - 1
            if 0 <= choice < len(philosophers):
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    selected_philosopher = philosophers[choice]

    print(f"\nYou are now chatting with {selected_philosopher['name']}. Type 'exit' to end the conversation.\n")

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    system_prompt = f"You are {selected_philosopher['name']}, the famous philosopher from the {selected_philosopher['period']}. Respond to questions as if you were them, using their ideas, writing style, and philosophical perspective. Your main ideas include: {', '.join(selected_philosopher['main_ideas'])}. Your goal is to help the user learn about your philosophy in an engaging and informative way."

    messages = [
        {"role": "user", "content": "Hello, I'd like to learn about your philosophical ideas."}
    ]

    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            system=system_prompt,
            messages=messages
        )

        assistant_response = response.content[0].text
        print(f"{selected_philosopher['name']}: {assistant_response.encode('utf-8').decode('utf-8')}")
        messages.append({"role": "assistant", "content": assistant_response})

    except anthropic.APIError as e:
        print(f"An error occurred: {e}")
        print("Please try again or type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                system=system_prompt,
                messages=messages
            )

            assistant_response = response.content[0].text
            print(f"{selected_philosopher['name']}: {assistant_response.encode('utf-8').decode('utf-8')}")
            messages.append({"role": "assistant", "content": assistant_response})

        except anthropic.APIError as e:
            print(f"An error occurred: {e}")
            print("Please try again or type 'exit' to end the conversation.")

    print("Thank you for using the Philosopher Chatbot!")

if __name__ == "__main__":
    main()