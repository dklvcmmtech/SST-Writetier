from flask import Flask
from flask import request
import os
from flask import jsonify
from write_handler.write_event import *
app = Flask(__name__)

@app.route("/")
def hello():
    print('Hello World')
    return "Hello World!"


@app.route("/events",methods=['POST'])
def postEvents():
    print("GETEVENTS")
    print(a)
    #validate_Function()
    #val1 = request.form["Pod"]
    #val2 = request.form["Msg"]
    #validate(request)
    req = request.get_json(force=True)
    val1 = req['pod_id']
    val2 = req['msg']
    reObj = write_sql()
    db_result = reObj.write_data(val1,val2)
    ret_obj = {'write_result':db_result}
    return jsonify(ret_obj)


