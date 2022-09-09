#!/usr/bin/env python3

from flask import Flask, request
import os

Relay_Control_Command = "./RLY2UH_control.py "

app = Flask(__name__)

@app.route("/relay_control", methods=["GET"])
def relay_control():
    try:
        relay_num = int(request.args["relay"])
        action = str(request.args["action"])
        os.system(Relay_Control_Command + "-r " + str(relay_num) + " " + action)
        return "Relay " + str(relay_num) + ": " + action
    except KeyError:
        return "Missing parameters"
    except:
        return "Unhandled error"

if __name__ == "__main__":
    app.debug = True
    app.run()
