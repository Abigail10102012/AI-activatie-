import requests

# -----------------------------------------
# 1. Define your categories and endpoints
# -----------------------------------------

CATEGORIES = {
    "Sports": "https://api.sampleapis.com/sports/sports",
    "Music": "https://api.sampleapis.com/music/artists",
    "Movies": "https://api.sampleapis.com/movies/action"
}

# -----------------------------------------
# 2. Fetch data from any endpoint
# -----------------------------------------

def fetch_data(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error fetching data from {url}: {e}")
        return None

# -----------------------------------------
# 3. Display a simple preview
# -----------------------------------------

def show_preview(data):
    if not data:
        print("No data found.\n")
        return

    print("\n--- Preview of Retrieved Data ---")
    if isinstance(data, list):
        for item in data[:5]:   # show first 5 entries
            print(item)
    elif isinstance(data, dict):
        print(data)
    print("-------------------------------\n")

# -----------------------------------------
# 4. Main interactive loop
# -----------------------------------------

def main():
    print("\n=== Explore API Endpoints ===\n")

    while True:
        print("Available Categories:")
        for i, key in enumerate(CATEGORIES.keys(), start=1):
            print(f"  {i}. {key}")
        print("  X. Enter a custom URL")
        print("  Q. Quit\n")

        choice = input("Choose a category: ").strip().lower()

        # Quit
        if choice == "q":
            print("Goodbye!")
            break

        # Custom URL
        if choice == "x":
            custom_url = input("Enter any API URL: ").strip()
            print(f"\nFetching from custom URL: {custom_url}")
            data = fetch_data(custom_url)
            show_preview(data)
            continue

        # Category selected
        try:
            index = int(choice) - 1
            category_name = list(CATEGORIES.keys())[index]
            url = CATEGORIES[category_name]
        except:
            print("❌ Invalid choice. Try again.\n")
            continue

        print(f"\nFetching data for category: {category_name}")
        data = fetch_data(url)
        show_preview(data)

# -----------------------------------------
# Entry point
# -----------------------------------------

if __name__ == "__main__":
    main()
