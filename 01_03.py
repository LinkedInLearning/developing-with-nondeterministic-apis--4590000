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
    messages=[
      {
        "role": "system", 
        "content": f"You're a sentiment analyst. Analyze the sentiment of the provided statement."
      # "content": f"You're a sentiment analyst. Analyze the sentiment of the provided statement. Give it a classification of positive, neutral, or negative. Give me only the classification, nothing else.",
      },
      {"role": "user", "content": prompt}
    ]
  )
  print("Message: \n" + str(completion.choices[0].message.content))

# repeat generate_completion() five times
for i in range(5):
  generate_completion(
    client, f"Look at the broad wingspan of this duck!"
  )