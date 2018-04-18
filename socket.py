import ftplib
import os

filename = "a.jpg"
ftp=ftplib.FTP()
ftp.connect("server ip",port number)
ftp.login("id","password")
ftp.cwd("./")
os.chdir(r"./")
myfile = open(filename,'rb')
ftp.storbinary('STOR ' +filename, myfile )
myfile.close()
ftp.close
