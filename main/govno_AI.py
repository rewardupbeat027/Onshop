import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZDdhNmFmNTUtY2I4NS00NjM3LWE2OGItZmFjODkwNTRjMjRjIiwidHlwZSI6ImFwaV90b2tlbiJ9.6b5b_p7vQDVKaJyGIf-fmsJX3QX6mqv2X02FKAly83E"}

url = "https://api.edenai.run/v2/image/generation"
payload = {
    "providers": "openai",
    "text": "1000000000 Spartans with blood",
    "resolution": "1792x1024",
    "fallback_providers": ""
}

response = requests.post(url, json=payload, headers=headers)
result = json.loads(response.text)
# print(result['openai']['items'])
print(result)