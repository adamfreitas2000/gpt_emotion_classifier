from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemma-3n-e4b-it:generateContent?key={GEMINI_API_KEY}"

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/classify")
def classify_emotion(input: InputText, x_api_key: str = Header(...)):
    if x_api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")

    prompt = f"""
    Classifique a emoção dominante neste texto em português:
    Texto: "{input.text}"
    Responda com apenas uma das seguintes palavras em letra minuscula: alegria, tristeza, raiva, medo, nojo, neutro.
    """

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(GEMINI_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Gemini error: {response.text}")

    try:
        emotion = response.json()["candidates"][0]["content"]["parts"][0]["text"].strip().lower()
        return {"emotion": emotion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid Gemini response: {e}")
    
@app.head("/health")
def health_check():
    return


