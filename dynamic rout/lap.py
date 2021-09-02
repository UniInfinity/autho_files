# from flask import Flask, jsonify, request, redirect, url_for, session

# app = Flask(__name__)

# app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = 'VaibhavKnowIt'


# @app.route("/")
# def index():
#     session.pop('name', None)
#     return "<h1> Welcome to my Blog </h1>"


# @app.route("/home", methods=['GET','POST'])
# def home():
#     return "<h1> Welcome to Home Page </h1>"


# @app.route('/person', methods=['GET','POST'], defaults={"name":"vaibhav"})
# @app.route("/person/<name>", methods=['GET','POST'])
# def person(name):
#     session['name'] = name
#     return "My name is {} Welcome to My Page".format(name)


# @app.route("/json")
# def json():
#     # if 'name' in session:
#     l1 = [10,2,3]
#     name = session['name']
    
#     # else:
#     #     name = "Name Not Available"    
    
#     return jsonify({"key1":"value","key3":"22",'name':name})

# @app.route("/query")
# def query():
#     name = request.args.get("name")
#     location = request.args.get("location")
#     return "<h1> My name {} and i am from {} this is query page<h1>".format(name, location)


# @app.route("/theform", methods=['GET','POST'])
# def theform():


#     if request.method == 'GET':
#         return '''<form method="POST" action="/theform">
#                     <input type="text" name="name">
#                     <input type="text" name="location">
#                     <input type="submit" value="Submit">
#                 </form>'''
    
#     else:
#         name = request.form["name"]
#         location = request.form["location"]
#         # return "<h1> My name {} and i am from {} <h1>".format(name, location)
#         return redirect(url_for('form', name=name, location=location))


# # @app.route("/process", methods=["POST"])
# # def process():
# #     name = request.form["name"]
# #     location = request.form["location"]
# #     return "<h1> My name {} and i am from {} <h1>".format(name, location)

# @app.route("/requestjason", methods=["POST"])
# def requestjason():

#     data = request.get_json()

#     name = data['name']
#     location = data['location']
#     randomlist = data['randomlist']

#     return jsonify({'result':'successfull', 'name':name, 'location':location, 'randomlist':randomlist[2]})

# if __name__=="__main__":
#     app.run()