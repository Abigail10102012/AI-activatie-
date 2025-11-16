import requests

api_url = "https://router.huggingface.co/hf-inference/models/tabularisai/multilingual-sentiment-analysis"

headers = {"Authorization": "Bearer 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"}

text = "I am jelouse"

response = requests.post(api_url, headers=headers, json={"inputs": text})

if response.status_code == 200:
    result = response.json()
    label = result[0][0]['label']
    score = result[0][0]['score']
    print(f"Sentiment: {label} with confidence score: {score: .4f}")
else: 
    print(f"Error: {response.status_code} - {response.text}")