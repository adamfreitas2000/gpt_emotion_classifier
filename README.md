# Emotion Classifier API (via Gemini)

API para classificar emoções em frases de texto em português, usando Gemma 3n E4B da OpenAI.

## Como usar

### Enviar requisição:
POST `/classify`

### Headers:
- `Content-Type: application/json`
- `x-api-key: token`

### Body:
```json
{
  "text": "estou com saudades"
}
```
### Resposta:
```json
{
  "emotion": "tristeza"
}
