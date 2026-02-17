from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from PIL import Image
import torch
import sys


def generate_caption(image_path):
    try:
        # Load model + processor
        model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        # Open image
        image = Image.open(image_path).convert("RGB")

        # Preprocess
        pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

        # Generate caption
        output_ids = model.generate(pixel_values, max_length=20, num_beams=4)
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        print(f"Error generating caption: {e}")
        sys.exit(1)


def expand_caption_with_gpt2(short_caption):
    try:
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        prompt = f"Expand this into a detailed 30-word description:\n{short_caption}"

        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)

        outputs = model.generate(
            inputs,
            max_length=60,
            num_return_sequences=1,
            temperature=0.8,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

        expanded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return expanded

    except Exception as e:
        print(f"Error expanding caption: {e}")
        sys.exit(1)


if __name__ == "__main__":
    image_path = input("Enter image path: ")

    # Step 1 & 2
    caption = generate_caption(image_path)
    print("\nGenerated Caption:")
    print(caption)

    # Step 3
    choice = input("\nDo you want a longer version? (yes/no): ").strip().lower()

    # Step 4
    if choice == "yes":
        long_description = expand_caption_with_gpt2(caption)
        print("\nExpanded Description:")
        print(long_description)
    else:
        print("\nDone.")

