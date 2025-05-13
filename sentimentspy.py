from textblob import TextBlob
from colorama import Fore, Style, init
import time
import re

init(autoreset=True)


conversation_history = []
sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}

def show_processing_animation():
    print("Analyzing", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = 'positive'
        color = Fore.GREEN
    elif polarity < 0:
        sentiment = 'negative'
        color = Fore.RED
    else:
        sentiment = 'neutral'
        color = Fore.YELLOW

    sentiment_counts[sentiment] += 1
    conversation_history.append((text, sentiment, polarity))
    print(color + f"Sentiment: {sentiment.upper()} (Polarity: {polarity:.2f})" + Style.RESET_ALL)

def execute_command(command):
    if command == "summary":
        print("\nSentiment Summary:")
        for key, value in sentiment_counts.items():
            print(f"{key.capitalize()}: {value}")
    elif command == "reset":
        conversation_history.clear()
        for key in sentiment_counts:
            sentiment_counts[key] = 0
        print("Conversation and sentiment data reset.")
    elif command == "history":
        print("\nConversation History:")
        for idx, (text, sentiment, polarity) in enumerate(conversation_history, 1):
            print(f"{idx}. [{sentiment.upper()}] {text} (Polarity: {polarity:.2f})")
    elif command == "help":
        print("Available commands: summary, reset, history, help, exit")

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if re.fullmatch("[A-Za-z]+", name):
            return name
        print("Invalid name. Please use only alphabetic characters.")

def generate_report(username):
    filename = f"{username}_sentiment_analysis.txt"
    with open(filename, 'w') as f:
        f.write("Sentiment Analysis Report\n")
        f.write("========================\n\n")
        f.write(f"User: {username}\n\n")
        f.write("Summary:\n")
        for key, value in sentiment_counts.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write("\nDetailed Messages:\n")
        for idx, (text, sentiment, polarity) in enumerate(conversation_history, 1):
            f.write(f"{idx}. [{sentiment.upper()}] {text} (Polarity: {polarity:.2f})\n")
    print(f"\nSummary report saved to {filename}")

def main():
    print("Welcome to the Sentiment Analysis Chatbot!")
    username = get_valid_name()

    while True:
        user_input = input("\nType a sentence for sentiment analysis (or a command): ").strip().lower()
        if user_input in ["summary", "reset", "history", "help"]:
            execute_command(user_input)
        elif user_input == "exit":
            print("\nThank you for using the Sentiment Analysis Chatbot!")
            execute_command("summary")
            generate_report(username)
            break
        elif user_input:
            show_processing_animation()
            analyze_sentiment(user_input)

if __name__ == "__main__":
    main()