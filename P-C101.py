import dropbox
import os
from dropbox.files import WriteMode

class FolderTransfer:
    def __init__(self,accessKey,):
        self.accessKey=accessKey
    def foldTransfer(self,source,dest):
        dbx = dropbox.Dropbox(self.accessKey)
        for root, dirs, files in os.walk(source):

            for filename in files:

                local_path = os.path.join(root, filename)
    
                relative_path = os.path.relpath(local_path, source)
                dropbox_path = os.path.join(dest, relative_path)
            
                with open(local_path, 'rb') as f:
                 dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))    

def main():
    access='86YFEBfrvaAAAAAAAAAAAXnB5JLdNu1ZoN4k7woG3fhKlTSr3Br5WRTPSpcrd4XU'
    Transfer=FolderTransfer(access)

    src= str(input('source folder? '))
    des = input('destination folder? ')

    Transfer.foldTransfer(src,des)

main()