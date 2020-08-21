from flask import Flask, render_template, redirect, url_for, request
import subprocess, os
from glob import glob
from shutil import copyfile

app = Flask(__name__)

if len(os.listdir('./static/conf') ) == 0:
    print('Empty CONF directory. Copy demo data!')
    copyfile('./static/img-demo/*', './static/conf/img/')
    copyfile('./static/playbooks-demo/*', './static/conf/playbooks/')
    copyfile('./static/access-demo/*', './static/conf/access/')


def find_ext(dr, ext):
    return glob(os.path.join("{}".format(dr),"*.{}".format(ext)))


list_files = find_ext("./static/conf/playbooks","yml")
for x in range(len(list_files)):
    print(('{}'+") "+"{}").format(x+1, list_files[x][24:]))

app = Flask(__name__)

def find_files(dr, ext):
    return glob(os.path.join("{}".format(dr),"*.{}".format(ext)))

def app_data(list):
    pack = []
    name = []
    descr = []
    for x in range(len(list)):
        f = open(list[x], encoding="UTF8")
        lines = f.readlines()
        if lines[0][0] == "#":
            name.append(lines[0][1:].strip('\n'))
        else:
            name.append('')
        if lines[1][0] == "#":
            descr.append(lines[1][1:].strip('\n'))
        else:
            descr.append('')
        f.close()
        pack.append(list[x][24:-4])
    return pack, name, descr


app_files = find_files("./static/conf/playbooks","yml")
app_addr, app_name, app_descr = app_data(app_files)



@app.route('/')
def index():
    return render_template('index.html', app_count=len(app_addr), app_addr=app_addr, app_name=app_name, app_descr=app_descr)


@app.route('/<string:work>/<string:prog>',  methods=['GET'])
def program(work, prog):
    print(work+' of program: '+prog+' from IP: '+request.remote_addr)
    subprocess.Popen(["ansible-playbook", "./static/conf/playbooks/"+prog+".yml", "-i", request.remote_addr+",", "-i", "./static/conf/access/conf.txt", "--tags", work],  stdout=subprocess.PIPE)
    return redirect(url_for('scheduled'))


@app.route('/scheduled')
def scheduled():
    return render_template('scheduled.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5003")
