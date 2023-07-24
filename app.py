import os
import openai
import constants

from flask import Flask, render_template, request

app = Flask(__name__)

# API imported from constants.py file
os.environ["OPENAI_API_KEY"] = constants.APIKEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_query():
    prompt = request.form['query']
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100
    )
    answer = response.choices[0].text.strip()
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
