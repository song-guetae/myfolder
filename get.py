import ftplib
import os

filename = "a.jpg"
ftp=ftplib.FTP()
ftp.connect("server ip ",port number)
ftp.login("id","password")
ftp.cwd("./")
fd = open("./" + filename,'wb')
ftp.retrbinary("RETR " + filename, fd.write)
fd.close()
