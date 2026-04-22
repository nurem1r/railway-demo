from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
 return '<h1>Railway Deployed!</h1><p>Auto-deployed from GitHub!</p>'
