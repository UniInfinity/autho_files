from flask import Flask, request, jsonify


app = Flask(__name__)

data = [{"name":"shubham"},                                                    
         {"name":"akshay"},                                                    
         {"name":"amol sir"},                                                    
         {"name":"suraj"},                                                                                                        
         {"name":"saurabh"},                                                    
         {"name":"swastik"},                                                    
         {"name":"vaibhav"},                                                    
         {"name":"pratik"}]                         

@app.route('/name/<string:user>',methods=['POST'])
def add_user(user):
    new_user = {"name":user}
    data.append(new_user)

    return jsonify({"data":data})

@app.route('/name',methods=['GET'])
def show_data():
    return jsonify({"data":data})

@app.route('/name/<user>',methods=['PUT'])
def update_user(user):

    got = request.json['name']

    for name in data:
        if name["name"] == user:
            name["name"] = got
    return jsonify({"data":data})

@app.route('/name/<user>',methods=['DELETE'])
def delete_user(user):
    new_data = []
    for name in data:
        if name["name"]!=user:
            new_data.append(name)

    return jsonify({"data":new_data})

if __name__== "__main__":
    app.run(debug=True) 

    