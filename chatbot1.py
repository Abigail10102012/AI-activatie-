import re
import json
from colorama import init, Fore, Style


init(autoreset=True)

memory = []


def save_conversation():
    with open("chat_history.json", "w") as f:
        json.dump(memory, f)

def load_conversation():
    try:
        with open("chat_history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []



def respond_to_weather():
    return "It's currently sunny with a high of 75°F."

def respond_to_news():
    return "Today's headline: Chatbots are transforming education!"

def respond_to_time(city="New York"):
    return f"The current time in {city} is 3:45 PM."  

def respond_default():
    return "I'm not sure how to respond to that. Try asking about the weather, news, or time."



def handle_input(user_input):
    user_input = user_input.lower()
    memory.append({"user": user_input})

    if re.search(r"\bweather\b", user_input):
        response = respond_to_weather()
    elif re.search(r"\bnews\b", user_input):
        response = respond_to_news()
    elif re.search(r"\btime\b", user_input):
        match = re.search(r"in (\w+)", user_input)
        city = match.group(1) if match else "New York"
        response = respond_to_time(city)
    else:
        response = respond_default()

    memory.append({"bot": response})
    return response


def main():
    print(Fore.GREEN + "Welcome to the Smart Chatbot!")
    print("Type 'exit' to end the chat.")
    
    global memory
    memory = load_conversation()

    while True:
        user_input = input(Fore.YELLOW + "You: ")
        if user_input.lower() == "exit":
            print(Fore.CYAN + "Saving conversation... Goodbye!")
            save_conversation()
            break

        response = handle_input(user_input)
        print(Fore.CYAN + "Bot: " + Style.BRIGHT + response)
if __name__ == "__main__":
    main()