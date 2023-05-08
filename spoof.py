#!/usr/bin/python3
import os
import coreDir.core as impCore
import coreDir.dict as impDict

def spoof():
 ##Email as ee
 def EmailSpoof():
 	eeFrom=input(impCore.setprompt("101","From"))
 	eeTo=input(impCore.setprompt("101","To"))
 	eeSubject=input(impCore.setprompt("101","Subject"))
 	eeMessage=input(impCore.setprompt("101","Message"))
 
 ##SMS as ss
 def SMSSpoof():
 	ssFrom=input(impCore.setprompt("102","From"))
 	ssTo=input(impCore.setprompt("102","To"))
 	ssMessage=input(impCore.setprompt("102","Message"))
 
 def DNSSpoof():
 	print(1)
 
 ##mac as mm
 def MACSpoof():
 	print('''(1) View Current\t\t(2) Vendor Change\n(3) Random same vendor\t\t(4) Random number\n(5) Reset\n''')
 	option=input(impCore.setprompt("103",""))
 	if option=="1":
 	  oo="s"
 	elif option=="2":
 	  oo="A"
 	elif option=="3":
 	  oo="a"
 	elif option=="4":
 	  oo="r"
 	elif option=="5":
 	  oo="p"
 	else:
 	  MACSpoof()
 	option=input(impCore.setprompt("103","wifi device (eth0, wlan0 etc.)"))
 	
 	
 	os.system("sudo macchanger -"+oo+" "+option)
 	print("\n\n")

 print (impDict.strr("d")+'''(1) Email\n(2) SMS\n(3) DNS\n(4) MAC Address\n''')
 option=input(impCore.setprompt("100",""))
 
 if option=="1":
  EmailSpoof()
 elif option=="2":
  SMSSpoof()
 elif option=="3":
 	DNSSpoof()
 elif option=="4":
 	MACSpoof()
 
  
  
  
 spoof()