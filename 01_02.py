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

quiz_template = '''
  What do ducks eat?

  A) Only plants  
  B) Only fish  
  * C) Seeds, small fish, insects, and plants  
  D) Chocolate Cake
'''

from openai import OpenAI
client = OpenAI()

def generate_completion(client, prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
      {
        "role": "system", 
        "content": f"You are a helpful assistant. Use {quiz_template} as a template for your answers."
      },
      {"role": "user", "content": prompt}
    ]
  )
  print("Message: \n" + str(completion.choices[0].message.content))

# repeat generate_completion() five times
for i in range(5):
  generate_completion(
    client, f"Create a multiple-choice question about ducks. Provide four answers A to D where one is correct and the others are plausible distractors. Mark the correct answer with an asterisk."
  )