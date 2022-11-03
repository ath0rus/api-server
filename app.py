from flask import Flask
from flask import request
import subprocess
import logging
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%d-%m-%y %H:%M:%S")

#convert approved ids to list
file = open("approvedIDs.txt", "r")
ids = file.read().split(".")

app = Flask(__name__)

def start():
    subprocess.call([r'D:/Minecraft servers/1.19/test/Run me.bat'])

@app.route("/minecraft/start", methods=["GET"])
def checkID():
    uid = request.args.get("uid")
    logging.info(f"UID: {uid}")
    
    if uid in ids:
        start()
        return "Success"
    
    else:
        return "Fail"