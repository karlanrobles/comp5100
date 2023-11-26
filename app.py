<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session
#py
=======
# app.py
import time
from flask import Flask, render_template, request, redirect, url_for
import openai

>>>>>>> c53615d (sentiment analysis with openAI connected)
app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

# Function for sentiment analysis using ChatGPT (OpenAI)
def analyze_sentiment(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Sentiment analysis for the following text: \"{user_input}\"",
        max_tokens=50  # Adjust as needed
    )

    result = response.choices[0].text.strip()
    return result

# Input page route
@app.route('/', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        # Rate limiting - allow 3 entries every 20 seconds
        if 'last_request_time' not in app.config:
            app.config['last_request_time'] = time.time()

        elapsed_time = time.time() - app.config['last_request_time']
        if elapsed_time < 20 and app.config.get('request_count', 0) >= 3:
            return "Rate limit exceeded. Try again later."

        app.config['last_request_time'] = time.time()
        app.config['request_count'] = app.config.get('request_count', 0) + 1

        user_input = request.form.get('user_input')

        # Perform sentiment analysis using ChatGPT (OpenAI)
        sentiment_result = analyze_sentiment(user_input)

        # Store the results (you may want to save in a database)
        app.sentiment_results = [user_input, sentiment_result]

        return redirect(url_for('input_page'))

    return render_template('input_page.html')

# Display page route
@app.route('/display')
def display_results():
    # Retrieve sentiment analysis results from the global variable
    sentiment_results = app.sentiment_results if hasattr(app, 'sentiment_results') else None

    return render_template('display_page.html', sentiment_results=sentiment_results)

if __name__ == "__main__":
    app.run(debug=True)

