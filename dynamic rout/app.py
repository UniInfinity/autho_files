from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    person = 'vaibhav'
    l1 = list(person)
    d1 = {"name":"vikas"}
    return render_template('index.html', person=person, l1=l1, d1=d1)

if __name__=="__main__":
    app.run()