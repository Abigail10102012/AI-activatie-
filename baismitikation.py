from groq import generate_response

def bais_mitigation_activity():
    print("\n=== BAIS MITTIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to explore bais (e.g., 'Discribe the ideal doctor'): ").strip()
    if not prompt:
        print("Please eneter a prompt to run th eactivity.")
        return

    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI response: {initial_response}")

    modified_ptompt = input(
        "Modify the prompt to make it more neutral (e.g, 'Describe the qualities of a doctor'): "
    ).strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI Response (Neutral): {modified_response}")
    else:
        print("No modified prompt entered. Skipping neutral response.")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt = input(
        "Enter a long prompt (more than 300 words, e.g, a detailed story or discription):"
    ),strip()

    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview = (long_response[:500] + "...") if len(long_responce) > 500 else long_response
        print(f"\nResponse to Long Prompt: {preview}")
    else:
        print("No long prompt entered. Skipping long prompt response.")

    short_prompt = input("Now, condense the prompt to be more concise: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nResponse to Condensed Prompt: {short_response}")
    else:
        print:("No condensed prompt entered. Skipping condensed prompt response.")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Bais Mittigation")
    print("2) Token limits")
    choice = input("> ").strip()

    if choice == "1":
        bais_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()