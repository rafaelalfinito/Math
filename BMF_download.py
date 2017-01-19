from ftplib import FTP
import zipfile
import os

def downloadFTP(FTPurl, FTPURLDir, estinationFolder, startFileNumber):
    # os.chdir(destinationFolder)
    ftp = FTP(FTPurl)
    ftp.login()
    for dir in FTPURLDir:
        ftp.cwd(dir)

    filenames = ftp.nlst() # get filenames within the directory

    countTotalFiles = 0
    for filename in filenames:
        date = filename[-12:-4]
        year = date[:4]
        if int(year) >= 2016:
            countTotalFiles += 1

    countFileDownload = 0
    for filename in filenames:
        date = filename[-12:-4]
        year = date[:4]
        if int(year) >= 2016:
            if countFileDownload >= startFileNumber:
                local_filename = os.path.join(destinationFolder, filename)
                print('downloading ' + filename + ' - Downloading ' + str(countFileDownload + 1) + ' of ' + str(countTotalFiles) + ' files' )
                file = open(local_filename, 'wb')
                ftp.retrbinary('RETR '+ filename, file.write)
                file.close()
            countFileDownload += 1

    print('--------------------------------------------------')
    print('DOWNLOADED ' + str(countFileDownload) + ' FILES')
    print('--------------------------------------------------')
    ftp.quit()


def decompressZip(zipFilePath, destinationDir):
    zip_ref = zipfile.ZipFile(zipFilePath, 'r')
    zip_ref.extractall(destinationDir)
    zip_ref.close()

def decompressAllZipInDir(zipFileFolder):
    for item in os.listdir(zipFileFolder):
        if item.endswith('.zip'):
            print('unpacking ' + os.path.relpath(item))
            file_name = zipFileFolder + '\\'+ os.path.relpath(item) # get full path of files
            decompressZip(file_name,zipFileFolder+ '\\extract\\')
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.close()
            os.remove(file_name)  # delete zipped file





FTPurl = 'ftp.bmf.com.br'
FTPURLDir = []
FTPURLDir.append('MarketData')
FTPURLDir.append('BMF')
destinationFolder = 'C:\\Users\\alfinira\\PycharmProjects\\Math\\BMFData\\zip'
startFileNumber = 306
#downloadFTP(FTPurl,FTPURLDir, destinationFolder, startFileNumber)
decompressAllZipInDir(destinationFolder)