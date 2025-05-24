from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import os
import openai

client = openai.OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("ROUTER_API_KEY"),
)
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

    response = client.chat.completions.create(
        model="google/gemini-2.0-flash-exp:free",
        messages=[
            {f"{prompt}"}
        ]
    )
    emotion = response.choices[0].message.content.strip().lower()
    return {"emotion": emotion}
