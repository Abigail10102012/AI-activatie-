import torch
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    VisionEncoderDecoderModel,
    ViTImageProcessor,
    AutoTokenizer
)
from diffusers import StableDiffusionPipeline
from PIL import Image
import os


# --------------------------------------------------
# 1️⃣ TEXT GENERATION (GPT-2)
# --------------------------------------------------
def expand_prompt(user_prompt):
    try:
        print("\n[1] Expanding prompt with GPT-2...")

        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2")

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)

        prompt = f"Expand this idea into a vivid detailed description:\n{user_prompt}"

        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)

        outputs = model.generate(
            inputs,
            max_length=100,
            temperature=0.9,
            top_p=0.95,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

        expanded_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return expanded_text

    except Exception as e:
        print(f"Error in GPT-2 expansion: {e}")
        return None


# --------------------------------------------------
# 2️⃣ IMAGE GENERATION (Stable Diffusion)
# --------------------------------------------------
def generate_image(prompt, output_path="generated_image.png"):
    try:
        print("\n[2] Generating image with Stable Diffusion...")

        device = "cuda" if torch.cuda.is_available() else "cpu"

        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        pipe = pipe.to(device)

        image = pipe(prompt).images[0]
        image.save(output_path)

        print(f"Image saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"Error in image generation: {e}")
        return None


# --------------------------------------------------
# 3️⃣ IMAGE CAPTIONING (ViT-GPT2)
# --------------------------------------------------
def caption_image(image_path):
    try:
        print("\n[3] Generating caption with ViT-GPT2...")

        model = VisionEncoderDecoderModel.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning"
        )
        processor = ViTImageProcessor.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning"
        )
        tokenizer = AutoTokenizer.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning"
        )

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)

        image = Image.open(image_path).convert("RGB")
        pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

        output_ids = model.generate(pixel_values, max_length=30, num_beams=4)
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        print(f"Error in captioning: {e}")
        return None


# --------------------------------------------------
# 🔥 MAIN PIPELINE
# --------------------------------------------------
if __name__ == "__main__":

    user_prompt = input("Enter a short idea: ")

    # Step 1: Expand prompt
    expanded_prompt = expand_prompt(user_prompt)
    if not expanded_prompt:
        exit()

    print("\nExpanded Prompt:")
    print(expanded_prompt)

    # Step 2: Generate image
    image_path = generate_image(expanded_prompt)
    if not image_path:
        exit()

    # Step 3: Caption generated image
    caption = caption_image(image_path)
    if not caption:
        exit()

    print("\nFinal Generated Caption:")
    print(caption)

    print("\n✅ Pipeline Complete!")
