from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key ='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')
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
            
#In-memory data structure (replace with a database in a production environment)
analysis_data = []

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Handle image upload logic here
        # You can access uploaded files using request.files
        image = request.files['image']
        image_path = os.path.join('uploads', image.filename)
        image.save(image_path)

        # Perform sentiment analysis using OpenAI API
        comments = request.form['comments']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'system', 'content': 'What is the sentiment of these comments, positive, negative, or neutral'},
                {'role': 'user', 'content': comments}
            ]
        )

        result = response.choices[0].message.content

        # Save data to the in-memory data structure (replace with database operations)
        analysis_data.append({'image_path': image_path, 'comments': comments, 'analysis': result})

        return render_template('index.html', result=result)

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"An error occurred: {e}")
        return render_template('index.html', result="An error occurred during analysis. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
