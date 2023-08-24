from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catfact')
def get_cat_fact():
    res = requests.get("https://catfact.ninja/fact?max_length=140")
    if res.status_code == 200:
        return {"message": res.text}, 200
    elif res.status_code == 404:
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server error!"}, 500
    
if __name__ == "__main__":
    app.run(debug=True)