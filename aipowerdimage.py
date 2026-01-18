from config import HF_API_KEY
import requests
from PIL import Image
import io
import os
from colorama import init, Fore, Style
import json

init(autoreset=True)


def query_hf_api(api_url, payload=None, files=None, method="post"):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    try:
        if method.lower() == "post":
            response = requests.post(api_url, headers=headers, json=payload, files=files)
        else:
            response = requests.get(api_url, headers=headers, params=payload)

        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}: {response.text}")

        return response.content
    except Exception as e:
        print(f"{Fore.RED}Error while calling API: {e}")
        raise


def get_basic_caption(image, model="nlpconnect/vit-gpt2-image-captioning"):
    print(f"{Fore.YELLOW}🖼 Generating basic caption...")
    api_url = f"https://api-inference.huggingface.co/models/{model}"

    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    buffered.seek(0)

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url, headers=headers, data=buffered.read())
    result = response.json()

    if isinstance(result, dict) and "error" in result:
        return f"[Error] {result['error']}"

    return result[0].get("generated_text", "No caption generated.")


def generate_text(prompt, model="gpt2", max_new_tokens=60):
    print(f"{Fore.CYAN}✍ Generating text...")
    api_url = f"https://api-inference.huggingface.co/models/{model}"

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": max_new_tokens}
    }

    text_bytes = query_hf_api(api_url, payload=payload)

    try:
        result = json.loads(text_bytes.decode("utf-8"))
    except Exception:
        raise Exception("Failed to decode text generation response.")

    if isinstance(result, dict) and "error" in result:
        raise Exception(result["error"])

    return result[0].get("generated_text", "")


def truncate_text(text, word_limit):
    words = text.strip().split()
    return " ".join(words[:word_limit])


def print_menu():
    print(f"""{Style.BRIGHT}
{Fore.GREEN}================ Image-to-Text Conversion ================
Select output type:
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
===========================================================
""")


def main():
    image_path = input(
        f"{Fore.BLUE}Enter image path (e.g., test.jpg): {Style.RESET_ALL}"
    )

    if not os.path.exists(image_path):
        print(f"{Fore.RED}File does not exist.")
        return

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"{Fore.RED}Failed to open image: {e}")
        return

    basic_caption = get_basic_caption(image)
    print(f"{Fore.YELLOW}📝 Basic caption: {Style.BRIGHT}{basic_caption}\n")

    while True:
        print_menu()
        choice = input(f"{Fore.CYAN}Choice (1-4): {Style.RESET_ALL}")

        if choice == "1":
            caption = truncate_text(basic_caption, 5)
            print(f"{Fore.GREEN}Caption: {Style.BRIGHT}{caption}\n")

        elif choice == "2":
            prompt = (
                f"Expand this caption into exactly 30 words: {basic_caption}"
            )
            try:
                generated = generate_text(prompt, max_new_tokens=50)
                description = truncate_text(generated, 30)
                print(f"{Fore.GREEN}Description: {Style.BRIGHT}{description}\n")
            except Exception as e:
                print(f"{Fore.RED}Failed: {e}")

        elif choice == "3":
            prompt = (
                f"Summarize this image description into exactly 50 words: {basic_caption}"
            )
            try:
                generated = generate_text(prompt, max_new_tokens=70)
                summary = truncate_text(generated, 50)
                print(f"{Fore.GREEN}Summary: {Style.BRIGHT}{summary}\n")
            except Exception as e:
                print(f"{Fore.RED}Failed: {e}")

        elif choice == "4":
            print(f"{Fore.GREEN}👋 Goodbye!")
            break

        else:
            print(f"{Fore.RED}Invalid choice.")


if __name__ == "__main__":
    main()
