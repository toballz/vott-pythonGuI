#!/usr/bin/env python3
from tkinter import *
import os

def shredr(path):
 import subprocess
 def _run_cmd_write(cmd_args, s):
    # write a file using sudo
    p = subprocess.Popen(cmd_args,
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                shell=False, universal_newlines=True)
    p.stdin.write(s)
    p.stdin.close()
    p.wait()
 _run_cmd_write(("/usr/bin/sudo", "/usr/bin/tee", path), "0")
 os.system("mv "+path+" /tmp/123__xxr.Shreding")
 print("File Shredded..........\n")

def selectFileDialogr():
 from tkinter.filedialog import askopenfilename
 return askopenfilename() 


def generateQR(txt):
    import qrcode
    # generate the qrcode
    qr = qrcode.QRCode(5, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(txt)
    qr.make()
    im = qr.make_image()

    qr_img_path = os.path.join("/home/kali/Desktop/qrcode_ratatatahtah_xtr.png")

    if os.path.isfile(qr_img_path):
        os.remove(qr_img_path)
    # save the image out
    im.save(qr_img_path, format='png')
    return qr_img_path

import hashlib
def sha256Hash(dataByte):
  m = hashlib.sha256()
  m.update(dataByte)
  m.digest()
  return m.hexdigest()
def md5Hash(dataByte):
  m = hashlib.md5()
  m.update(dataByte)
  m.digest()
  return m.hexdigest()	
def sha224Hash(dataByte):
  m = hashlib.sha224()
  m.update(dataByte)
  m.digest()
  return m.hexdigest()	
def  sha1Hash(dataByte):
  m = hashlib.sha1()
  m.update(dataByte)
  m.digest()
  return m.hexdigest()	
