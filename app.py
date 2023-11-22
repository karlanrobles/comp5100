from flask import Flask, render_template, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)

@app.route('/')
def index():
    if 'user_inputs' not in session:
        session['user_inputs'] = []
    return render_template('index.html', user_inputs=session['user_inputs'])

@app.route('/save_input', methods=['POST'])
def save_input():
    user_input = request.form.get('userInput')
    if user_input.strip():
        session['user_inputs'].append(user_input)
    return render_template('index.html', user_inputs=session['user_inputs'])

if __name__ == '__main__':
    app.run(debug=True)

