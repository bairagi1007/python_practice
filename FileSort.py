#this is my first program
#written by Bairagi Muduli

#This program will list the files present in a directory.
#dir='desired directory'
#Filetype='the type of file you want to list. change in '*.pdf' format. If all don't change anything.

#this will import os package
import os

#this will import glob package.
import glob

dir='E:\\bairagi\\Programming Books'
fileType='*'

#this will change the current directory
os.chdir(dir)

#this will list the files present in the dir with *.iso
filesPresent=glob.glob(fileType)

#print the length of the file
print('Number of files present in the directory are : ',len(filesPresent),"\n")

#print sorted list
print("The files are: \n",*(sorted(filesPresent)),sep="\n")