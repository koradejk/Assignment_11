import hashlib
import sys
import os
main_path="C:\\Users\\Administrator\\Desktop\\"
def hashfile(path,blocksize=4096):
    checksum_arr=[]
    dir_path=os.path.join(main_path,path+"\\")
    for file in os.listdir(dir_path):
        afile=open(dir_path+file,"rb")
        hasher=hashlib.md5()
        buf=afile.read(blocksize)
        while len(buf)>0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        afile.close()
        checksum_arr.append(hasher.hexdigest())
    return checksum_arr
user_input=input("Enter the directory name: ")
print("  " .join(hashfile(user_input)))