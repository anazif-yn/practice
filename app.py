from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>DevOps Docker Project</h1>
    <p>Built by: Anazif Abdulganiu</p>
    <p>Tech Stack: Python + Flask + Docker</p>
    <p>Status: Running in container!</p>
    <p>Hostname: {}</p>
    '''.format(os.uname().nodename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

