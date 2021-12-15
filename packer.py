import zipfile
import os
def zip(startdir,file_name):
    z = zipfile.ZipFile(file_name,'w',zipfile.ZIP_DEFLATED) 
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'') 
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print('压缩成功')
    z.close()

if __name__=="__main__":
    startdir = ".\\answer" 
    file_name = 'bundle.zip' 
    zip(startdir,file_name)