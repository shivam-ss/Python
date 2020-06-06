import os
import sys

def main(argv):
    #aList=str(sys.argv)
    first, second=argv
    print("Argumnets list : ", first, second)

    file1=first
    file2=second
   
    print(file1)
    f1=open(file1,"a")
    if(f1):
        print("file1 opened")
    else:
        print("error")

    f2=open(file2,"r+")
    for x in f2:
        f1.write(x)
        
        
    
if __name__=="__main__":
    main(sys.argv[1:])