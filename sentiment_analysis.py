import openai
import time
import requests

def analyze_sentiment(user_input):
    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    openai.api_key = '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'

    print("Received user_input: ", user_input)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Sentiment analysis for the following text: \"{user_input}\"",
        max_tokens=50  # Adjust as needed
    )

    result = response.choices[0].text.strip()
    print(result)
    return result

analyze_sentiment("This is bad")
