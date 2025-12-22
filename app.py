from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Devops Docker Project - BUG VERSION</h1>
    <p>Built by: Anazif Abdulganiu</p>
    <p>Status:This version has a syntax bug!</p>
    <p>Python: {}</p>
    <p>This line is missing closing quote: #BUG HERE
    '''.format(os.popen('python --version').read().strip())

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
