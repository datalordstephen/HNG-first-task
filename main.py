from flask import Flask, request, jsonify

app = Flask(__name__)
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

        
app.run()
