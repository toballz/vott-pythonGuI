from tkinter import *
import appr.functr as functrr
import appr.dictr as dictrr
import os

window = Tk()
def c():
 return
#........1 cq
def shred_click1():
 file2shred=functrr.selectFileDialogr()
 shredOption=dictrr.askyesno(title="Shredder!!!", message="Are you sure to shred this file\n"+file2shred)
 if shredOption == True:
   functrr.shredr(file2shred)
#.........0

##......1
def generateQr(): 
   popup= Toplevel(window)
   popup.grab_set()
   popup.geometry("450x130")
   popup.title("Generate QR code !!!")
    
   qrlabel=Label(popup, text="Input text to generate!!!" ) 
   qrlabel.pack(side = TOP)
   qrTxt=Entry(popup, bd =2, width=440 ) 
   qrTxt.pack(side = TOP,ipady=9)
   def genQQQr():
    if len(qrTxt.get())>0:
     pathfile=functrr.generateQR(qrTxt)
     dictrr.showinfo(title=None, message=pathfile) 
   qrBtn=Button(popup,text="GENERATE",padx=90, pady=35, command=genQQQr) 
   qrBtn.pack(side = BOTTOM)
    ## 
##......0

def hashbtnClick():
   file2hash=functrr.selectFileDialogr()
   in_file = open(file2hash, "rb")
   bytedata = in_file.read()
   in_file.close()

   print("SHA256: "+functrr.sha256Hash(bytedata)+";")
   print("MD5   : "+functrr.md5Hash(bytedata)+";")
   print("SHA1  : "+functrr.sha1Hash(bytedata)+";")
   print("SHA224: "+functrr.sha224Hash(bytedata)+";\n")

## text   inserttext = Entry(root, width=50)
## button mb_button1=Button(root,text="bgg", pady=50, command=c) 

mb_button1=Button(window,text="bgg",padx=90, pady=50, command=c) 
mb_button2=Button(window,text="bgg",padx=90, pady=50, command=c) 
mb_button3=Button(window,text="phishing",padx=90, pady=50, command=c) 
mb_button4=Button(window,text="Spoof",padx=90, pady=50, command=c) 
mb_button5=Button(window,text="Shred",padx=90, pady=50, command=shred_click1) 
mb_button6=Button(window,text="Generate txt QR",padx=90, pady=50, command=generateQr ) 
mb_button7=Button(window,text="Ph",padx=90, pady=50, command=c) 
mb_button8=Button(window,text="HasH",padx=90, pady=50, command=hashbtnClick) 
mb_button9=Button(window,text="bgg",padx=90, pady=50, command=c) 
 
mb_button1.grid(row=0, column=0)
mb_button2.grid(row=0, column=1)
mb_button3.grid(row=0, column=2)

mb_button4.grid(row=1, column=0)
mb_button5.grid(row=1, column=1)
mb_button6.grid(row=1, column=2)


mb_button7.grid(row=2, column=0)
mb_button8.grid(row=2, column=1)
mb_button9.grid(row=2, column=2)

window.mainloop()
