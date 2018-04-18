import ftplib
import os

filename = "a.jpg"
ftp=ftplib.FTP()
ftp.connect("168.188.39.232",111)
ftp.login("pi","123123")
ftp.cwd("./")
os.chdir(r"./")
myfile = open(filename,'rb')
ftp.storbinary('STOR ' +filename, myfile )
myfile.close()
ftp.close