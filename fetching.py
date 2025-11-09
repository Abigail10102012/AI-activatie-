import requests

URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_fact():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        fact_data = response.json()
        print(f"\n💡 Did you know? {fact_data['text']}\n")
    except requests.RequestException as e:
        print(f"⚠️ Failed to fetch fact: {e}")

if __name__ == "__main__":
    while True:
        user_input = input("Press Enter to get a random fact or type 'q' to quit... ")
        if user_input.lower() == 'q':
            print("Goodbye! 👋")
            break
        get_random_fact()
