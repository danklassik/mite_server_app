from flask import Flask, render_template, redirect, url_for, request
import subprocess

app = Flask(__name__)


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
