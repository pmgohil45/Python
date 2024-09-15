"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

#import os
import google.generativeai as genai

#genai.configure(api_key=os.environ["YOUR API KEY IS HERE"])
genai.configure(api_key="YOUR API KEY IS HERE")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 10000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(history=[])

response = chat_session.send_message("YOUR PROMPT IS HERE")

print(response.text)
