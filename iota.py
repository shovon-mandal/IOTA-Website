from logging import debug
from flask import Flask, redirect, url_for, render_template
import flask

import iota_client
import os
import hashlib
import subprocess as s
import pyperclip
import time
#flask import
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/payment_iota", methods=["POST", "GET"])
def payment_iota():
    pyperclip.copy('atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n')
    # IOTA
    client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
    IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')
    a = str(client.get_address_balance("atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n")['balance'])
    return render_template("payment_iota.html", bl=a)

#open firefly
@app.route("/payment_iota2", methods=["POST", "GET"])
def payment_iota2():
    # IOTA
    client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
    IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')
    a = str(client.get_address_balance("atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n")['balance'])
    s.Popen('C:\\Users\\SHOVON\\AppData\\Local\\Programs\\desktop\\Firefly.exe')
    return render_template("payment_iota2.html",bl=a)


#balance check
@app.route("/payment_iota3", methods=["POST", "GET"])

def payment_iota3():

    # IOTA
    client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])

    IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')

    a = str(client.get_address_balance("atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n")['balance'])

    return render_template("payment_iota3.html", bl=a)
if __name__ == "__main__":
    app.run(debug=True)




