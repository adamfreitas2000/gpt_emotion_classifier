from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    Responda com apenas uma das seguintes palavras: alegria, tristeza, raiva, medo, nojo, surpresa ou neutro.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    emotion = response['choices'][0]['message']['content'].strip().lower()
    return {"emotion": emotion}
