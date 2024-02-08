# Baseline example of OpenAI's API
# 
# - OpenAI Python library: https://github.com/openai/openai-python

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Create a client
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

from openai import OpenAI
client = OpenAI()

def generate_completion(client, prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    temperature=1,
    top_p=1,
    seed=42,
    messages=[
      {
        "role": "system", 
        "content": f"You are a helpful assistant."
      },
      {"role": "user", "content": prompt}
    ],
    tools = [
      {
        "type": "function",
        "function": {
          "name": "get_current_weather",
          "description": "Get the current weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location","unit"],
          },
        }
      }
    ],
    tool_choice="auto"
  )
  print("Message: \n" + str(completion.choices[0].message.content))
  print("Function name: \n" + str(completion.choices[0].message.tool_calls[0].function.name))
  print("Function arguments: \n" + str(completion.choices[0].message.tool_calls[0].function.arguments))

# repeat generate_completion() five times
for i in range(5):
  generate_completion(
    client, f"What's the weather like in Burnaby?"
  )