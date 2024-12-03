from flask import Flask
from flask import request

personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Lab!"

@app.route('/greet/<name>')
def greet(name):
    return f"Welcome {name}"

@app.route('/personnel/<name>')
def get_personnel(name): 
    name = name.lower()
    if name in personnel:
        return personnel[name]
    else:
        return 'Unknown personnel'

@app.route('/library')
def library():
    title = request.args.get('title')
    author = request.args.get('author')
    if title and author:
        return f"Searching for books titled '{title}' by {author}"
    elif title and not author:
        return f"Searching for books titled '{title}' by Unknown author"
    elif not title and author:
        return f"Searching for books titled Unknown by {author}"
    else:
        return 'Something is missing'

if __name__ == '__main__':
    app.run(debug=True)