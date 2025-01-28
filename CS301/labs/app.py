# import Flask and create an instance of the Flask object
# adapter in order to change any codes into a service
from flask import Flask 
app = Flask(__name__)

# Use Flask's app.route decorator to map the URL route / to the function home
""" Note: To call the home() function, the URL to use would be http://<hostname>:<port>/.
This would be constructed using the hostname of the computer it is being run on (in our case 127.0.0.1),
the port (default 5000) and then the pattern specified in the app.route decorator (in this case /)
"""
@app.route("/", methods=["GET"])
def home():
    
    return "Hello, Flask!"

@app.route("/test")
def hi():
    return "你好<br/>nice to meet u again<br/>Zhiqiu here"

if __name__ == '__main__':
    app.run()