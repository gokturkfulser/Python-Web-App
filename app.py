from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Goko')  # Get the 'name' parameter from the request query string
    return render_template('index.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)
