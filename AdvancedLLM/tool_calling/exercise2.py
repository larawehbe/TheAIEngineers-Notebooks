from dotenv import load_dotenv
from openai import OpenAI
import json

import requests
load_dotenv()

client = OpenAI()

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']


tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"}
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False
        },
        "strict": True
    }
}]


messages = [{"role" : "user" , "content" : "What is the weather like in Beirut Today?"}]

completion = client.chat.completions.create(
model = "gpt-4o-mini",
messages=messages,
tools=tools
)
print(completion)
tool_call = completion.choices[0].message.tool_calls[0]
args = json.loads(tool_call.function.arguments)

result = get_weather(args['latitude'], args['longitude'])

print(result)

messages.append(completion.choices[0].message)
messages.append({
    "role" : "tool",
    "tool_call_id": tool_call.id,
    "content" : str(result)
})
completion_2 = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages,
    tools=tools
)
print(completion_2.choices[0].message.content)