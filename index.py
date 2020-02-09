from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

users = [
    {
        "Name":"Andres",
        "Email":"andres@gmail.com",
        "Id":"2341",
        "Status":"ok"
    },
    {
        "Name":"Nancy",
        "Email":"nancy@gmail.com",
        "Id":"9876",
        "Status":"ok"
    },
    {
        "Name":"javier",
        "Email":"javier@gmail.com",
        "Id":"2641",
        "Status":"ok"
    }
]
@app.route('/search/<nombre>/<Id>', methods=["GET"])
def search(nombre,Id):
    for user in users:
        print(user)
        print(nombre)
        if user["Name"] == nombre:
            print (Id)
            return json.dumps(user)

    return json.dumps({"error":"No se encontro el email"})    

@app.route('/login/<user>/<password>', methods=["GET"])
def login(user,password):
    print (user)
    usuario = {"Name":"francisco" , "Email":"fran@gmail.com", "Id":1234, "Status":"ok"}
    error = {"status":"error","message":"no se encuentra"}

    if user == usuario["Name"] and password == "123":
        return json.dumps(usuario)
    else:
        return json.dumps(error)

if __name__ == '__main__':    
    app.run(debug=True)
