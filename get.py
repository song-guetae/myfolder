import ftplib
import os

filename = "a.jpg"
ftp=ftplib.FTP()
ftp.connect("168.188.39.232",111)
ftp.login("pi","123123")
ftp.cwd("./")
fd = open("./" + filename,'wb')
ftp.retrbinary("RETR " + filename, fd.write)
fd.close()
