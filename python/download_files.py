# first branch
import ftplib
import os
class momoTools:
    "General Momo tools"
    def FtpDownloadcommonupdater(self, localdir='', ftpdir=''):
        if ftpdir=='': return
        data=[]
        #"ftp://ftp.nai.com/commonupdater/"

        ftp = ftplib.FTP('ftp.nai.com')  # connect to host, default port
        ftp.login()  # user anonymous, passwd anonymous@
        ftp.cwd(ftpdir)  # change into "debian" directory
        #ftp.retrlines('LIST')  # list directory contents
        #ftp.retrbinary('RETR README', open('README', 'wb').write)
        posfilename=55
        ftp.dir(data.append)
        for line in data:
            print(line)
            if 'd' in line[0]:
                pass
            else:
                try:
                    ftpfilename=line[posfilename:]
                    localfilename= localdir+'/' + line[posfilename:]
                    ftp.retrbinary("RETR " + ftpfilename, open(localfilename,'wb').write)
                except ftplib.error_perm:
                    print(" Permisssion error for "+line)



        ftp.quit()
        print("--------------")

localdir='/tmp/momo/ftp'		
#create root directory
if not os.path.exists(localdir):
    os.makedirs(localdir)


ftpsample=momoTools()
ftpsample.FtpDownloadcommonupdater(localdir,'commonupdater')


