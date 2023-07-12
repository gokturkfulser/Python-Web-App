from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()

"""from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Goko')  # Get the 'name' parameter from the request query string
    return render_template('index.html', name=name)
    
    
    
    
    <html>
    <head>
        <h1>Hello</h1>
        <!-- head definitions go here -->
    </head>
    <body>
        <h1>{{name}}</h1>
        <!-- the content goes here -->
    </body>
</html>

if __name__ == '__main__':
    app.run(debug=True)
    """