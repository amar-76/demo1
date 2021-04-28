from flask import Flask
from mod1 import hello_world


app = Flask(__name__)

#landing page
@app.route('/')
def index():
    return hello_world()


if __name__ == '__main__':
    app.run(debug=True)
