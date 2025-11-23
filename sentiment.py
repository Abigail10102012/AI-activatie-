
import requests


# ✅ New Hugging Face Inference API endpoint (as of 2025)
api_url = "https://router.huggingface.co/hf-inference/models/tabularisai/multilingual-sentiment-analysis"


headers = {"Authorization": "Bearer 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"}


text = "I am verry happy"


response = requests.post(api_url, headers=headers, json={"inputs": text})


if response.status_code == 200:
    result = response.json()
    # The model output is typically [[{'label': 'POSITIVE', 'score': 0.9998}]]
    label = result[0][0]['label']
    score = result[0][0]['score']
    print(f"Sentiment: {label} with confidence score: {score:.4f}")
else:
    print(f"Error: {response.status_code} - {response.text}")

