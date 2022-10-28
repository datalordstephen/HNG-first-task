from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False

# defining data to return 
data = {
    "slackUsername" : "steefin",
    "backend" : True,
    "age" : 18,
    "bio" : "Barca fan, AI enthusiast and a frequently intruigued guy. Also a UI student"
    }

@app.route('/api/info', methods=['GET'])
def return_info():
    if (request.method == 'GET'):
        return jsonify(data)

        
app.run() #had to comment this line out when hosting it on the server