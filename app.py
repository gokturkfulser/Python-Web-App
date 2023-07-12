"""from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()"""
"""from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Goko')  # Get the 'name' parameter from the request query string
    return render_template('index.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name', 'Goko')  # Get the 'name' value from the submitted form data
    else:
        name = 'Goko'  # Default value if 'name' is not provided
        
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
