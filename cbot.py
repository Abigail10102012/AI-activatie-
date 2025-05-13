def greet_user():
    print("Hello! I'm ChatBuddy.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    return name

def ask_mood():
    print("\nHow are you feeling today?")
    print("1. Good")
    print("2. Bad")
    print("3. Neutral")
    
    choice = input("Enter the number corresponding to your mood: ")
    
    if choice == "1":
        print("That's awesome to hear!")
        hobby = input("What do you love doing in your free time? ")
        print(f"{hobby} sounds like a lot of fun!")
    elif choice == "2":
        print("I'm sorry to hear that.")
        cheer = input("Is there anything you enjoy that might cheer you up? ")
        print(f"Maybe doing some {cheer} could help brighten your day.")
    elif choice == "3":
        print("Sometimes neutral is just peaceful.")
        activity = input("Is there something small that could improve your day? ")
        print(f"{activity} might be just what you need.")
    else:
        print("Oops, I didn't understand that. Let's try again.")
        ask_mood()

def farewell(name):
    print(f"\nIt was great chatting with you, {name}! Have a wonderful day!")

def chatbot():
    name = greet_user()
    
    while True:
        ask_mood()
        
        again = input("\nWould you like to keep chatting? (yes/no): ").lower()
        if again != "yes":
            farewell(name)
            break


chatbot()