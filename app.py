from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Route: Quiz Page (direct access, no login)
@app.route('/', methods=['GET'])
def quiz():
    return render_template('quiz.html')

# Route: Submission of Quiz
@app.route('/submit', methods=['POST'])
def submit():
    answers = dict(request.form)
    file_exists = os.path.isfile('responses.csv')

    with open('responses.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=answers.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(answers)

    return "✅ Thank you for submitting the quiz!"

if __name__ == '__main__':
    app.run(host='172.22.51.185', port=8888)
