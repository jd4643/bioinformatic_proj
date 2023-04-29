from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# start the development server
if __name__ == '__main__':
    app.run(debug=True)
