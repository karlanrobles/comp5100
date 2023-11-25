from flask import Flask, render_template, request, redirect, url_for, session
#py
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def input_page():
    return render_template('input_page.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('userInput')
    if user_input.strip():
        session['user_inputs'] = session.get('user_inputs', [])  # Initialize list if not present
        session['user_inputs'].append(user_input)
        session.modified = True

    return redirect(url_for('input_page'))

@app.route('/display_page')
def display_page():
    user_inputs = session.get('user_inputs', [])
    return render_template('display_page.html', user_inputs=user_inputs)

if __name__ == '__main__':
    app.run(debug=True)

