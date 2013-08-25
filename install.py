import os
import sys
import subprocess
import shutil
import hashlib
from uuid import uuid4

__author__ = 'bluele'

BIN_PATH = '/usr/local/bin'
REPOSITORY_URL = 'https://github.com/bluele/clippy'
SCRIPT_NAME = 'clippy'
SCRIPT_URL = 'https://raw.github.com/bluele/clippy/master/scripts/%s' % SCRIPT_NAME
tmp_dir = '/tmp/' + str(uuid4())
md5_val = 'dffe017d592024c4b5c8e351082121c8'

def md5(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()

def info(message):
    sys.stdout.write('[INFO] ')
    sys.stdout.write(message + '\n')

def emg(message):
    sys.stdout.write('[ERROR] ')
    sys.stdout.write(message + '\n')

def system(*args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, err = process.communicate()
    if err is not None:
        raise Exception(err)
    return out

def download():
    os.chdir(tmp_dir)
    info('Get ' + SCRIPT_URL)
    system('curl', '-O', SCRIPT_URL)
    if md5(SCRIPT_NAME) != md5_val:
        raise Exception('invalid md5 hash value')

def install():
    source = tmp_dir + '/' + SCRIPT_NAME
    target = BIN_PATH + '/' + SCRIPT_NAME
    if os.path.exists(target):
        return emg('Already exists: ' + target)
    system('sudo', 'mv', source, target)
    if not os.path.exists(target):
        raise Exception("Not exists " + target)
    system('sudo', 'chmod', '+x', target)

def main():
    os.mkdir(tmp_dir)
    try:
        download()
        install()
    finally:
        shutil.rmtree(tmp_dir)

main()