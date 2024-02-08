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

query_type = '''
{
    "sentiment_analysis": "Analyze the sentiment of the provided text. Determine whether the sentiment is positive, negative, or neutral and provide a confidence score.",
    "text_summarization": "Summarize the provided text into a concise version, capturing the key points and main ideas."
}
'''

JSON_schema = '''
"sentiment_analysis": {
    "sentiment": "string (positive, negative, neutral)",
    "confidence_score": "number (0-1)",
    "text_snippets": "array of strings (specific text portions contributing to sentiment)"
},
"text_summarization": {
    "summary": "string",
    "key_points": "array of strings (main points summarized)",
    "length": "number (number of words in summary)"
}
'''

from openai import OpenAI
client = OpenAI()

def generate_completion(client, prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    temperature=1,
    top_p=1,
    seed=42,
    response_format={'type':'json_object'},
    messages=[
      {
        "role": "system", 
        "content": f"You are a data analysis assistant capable of {query_type} analysis. Respond with your analysis in JSON format. The JSON schema should include '{JSON_schema}'."
      },
      {"role": "user", "content": prompt}
    ]
  )
  print("Message: \n" + str(completion.choices[0].message.content))

# repeat generate_completion() five times
for i in range(5):
  generate_completion(
    client, f"Evaluate this customer feedback: The ducks did not seem to enjoy being hugged."
  )