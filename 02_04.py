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

feedback_template = '''
# Park Experience
## Positive Feedback:
"Thank you for your wonderful feedback; we're thrilled you enjoyed your visit and look forward to welcoming you back for more fun!"

## Neutral Feedback:
"Thank you for visiting and sharing your thoughts; we're always striving to improve and value your suggestions!"

## Negative Feedback:
"We're sorry to hear about your disappointing experience and would appreciate more details to help us make necessary improvements."

# Food
## Positive Feedback:
"Thank you for your kind words about our food; our culinary team is delighted you enjoyed your meal and can't wait to serve you again!"

## Neutral Feedback:
"We appreciate your feedback on our food and are always looking to expand and improve our menu based on guest suggestions."

## Negative Feedback:
"We apologize for not meeting your expectations with our food and would value more specific feedback to help us enhance our offerings."

# The Ducks
## Positive Feedback:
"We're so glad you enjoyed the ducks; they are a central part of our park's charm and we love sharing them with our visitors!"

## Neutral Feedback:
"Thank you for your feedback on the ducks; we're always looking for ways to improve our guests' experiences with our feathered stars."

## Negative Feedback:
"We regret that your experience with the ducks wasn't as expected and would greatly appreciate more details to help us improve in this area."
'''

from openai import OpenAI
client = OpenAI()

def generate_completion(client, prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    temperature=0,
    top_p=0,
    seed=42,
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
    client, f"Array of ten random numbers. Just the array."
  )