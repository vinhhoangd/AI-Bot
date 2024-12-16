from openai import OpenAi
client = OpenAi(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama'
)

response = client.chat.completions.create(
  model="gemma2:9b",
  messages=[
      {"role": "user", "content": "Hello, bot!"}
  ]
)
reply = response.choices[0].message.content
print(reply)
