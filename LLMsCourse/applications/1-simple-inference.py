import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded"
)

resposne = client.chat.completions.create(
    model="phi:latest",
    temperature=0.3,
    messages = [
        {"role" : "system" , "content": "You are a helpful assistant"},
        {"role" : "user" , "content" : "Write a code that generates messages"}
    ]
)

print(f'Response: {resposne.choices[0].message.content}')