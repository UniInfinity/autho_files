from flask import Flask, request, make_response, jsonify
# import jwt
# import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thissecret3'

@app.route('/unprotected')
def unprotected():
    return ''

@app.route('/protected')
def protected():
    return ''    

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})

    return make_response('Could not verify!', 401, {'WWW-Authentificatate' : 'Basic realm="Login Requred"'})

if __name__ == "__main__":
    app.run(debug=True)