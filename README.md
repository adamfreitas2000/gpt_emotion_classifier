# Emotion Classifier API (via OpenAI)

API para classificar emoções em frases de texto em português, usando GPT-3.5 da OpenAI.

## ✨ Como usar

### Enviar requisição:
POST `/classify`

### Headers:
- `Content-Type: application/json`
- `x-api-key: seu_token_definido`

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
