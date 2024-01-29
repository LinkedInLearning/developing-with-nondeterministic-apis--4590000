# Baseline example of OpenAI's Moderation API.
# 
# - OpenAI Moderations API reference: https://platform.openai.com/docs/api-reference/moderations
# - OpenAI Python library: https://github.com/openai/openai-python

import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load the .env file
load_dotenv()

# Create a client
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

# Helper function to pretty print the response object
def print_response(response_obj):
    # Serialize the response object
    def serialize(obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return str(obj)

    # Create a dictionary
    response_dict = response_obj.__dict__

    # Print the dictionary
    print(json.dumps(response_dict, indent=4, default=serialize))

from openai import OpenAI
client = OpenAI()


def generate_completion(client, prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    temperature=1,
    top_p=1,
    # seed=42,
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt}
    ]
  )

  # Print the full response object
  # print_response(completion)
  # Print "finterprint: [fingerprint]"
  print("Fingerprint: \n" + completion.system_fingerprint)
  print("Message: \n" + str(completion.choices[0].message.content))

# repeat generate_completion() five times
for i in range(5):
  generate_completion(client, "Random array of 10 letters. only the array")