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

json_template = '''{
  "duck": {
    "id": "1",
    "species": string (species name),
    "common_name": string,
    "given_name": string (pet name of individual duck),
    "birth_date": string (ISO 8601 date),
    "age": integer (years),
    "habitat": string (habitat description),
    "diet": string (diet description),
    "sex": string(male / female),
    "weight_kg": integer,
    "length_cm": integer,
    "wingspan_cm": integer
  }
}'''

from openai import OpenAI
client = OpenAI()

def generate_completion(client, prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
      {
        "role": "system", 
        "content": f"You are a helpful assistant."
      },
      {"role": "user", "content": prompt}
    ]
  )
  print("Message: \n" + str(completion.choices[0].message.content))

# repeat generate_completion() five times
for i in range(5):
  generate_completion(
    client, f"Write a haiku about a duck."
  )