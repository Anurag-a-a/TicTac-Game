from flask import Flask, render_template
#Anurag Athwale 20012263

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')