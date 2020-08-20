from flask import Flask, render_template, redirect, url_for, request
import subprocess, os
from glob import glob

app = Flask(__name__)

def find_ext(dr, ext):
    return glob(os.path.join("{}".format(dr),"*.{}".format(ext)))

list_files = find_ext("./ansible","yml")
for x in range(len(list_files)):
    print(('{}'+") "+"{}").format(x+1, list_files[x][10:]))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/program/<string:prog>',  methods=['GET'])
def uninstall(prog):
    print('Script: '+prog+' from IP: '+request.remote_addr)
    subprocess.Popen(["ansible-playbook", "./ansible/"+prog+".yml", "-i", request.remote_addr+",", "-i", "conf.txt"],  stdout=subprocess.PIPE)
    return redirect(url_for('scheduled'))


@app.route('/scheduled')
def scheduled():
    return render_template('scheduled.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
