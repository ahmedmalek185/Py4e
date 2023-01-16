#import regex library
import re
#read the file
#fh = open("/Users/XXXXXX/regex_sum_1638633.txt")
#Or
fname = input("Enter file name: ")
fh = open(fname)

#Initialize the total function
total=0

#Data Collection
for line in fh:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
#Data Cleaning
    if len(x) <1 : continue
    for num in x:
        #print(num)
#Generating Output
        total=total+int(num)
        #print(total)
#Displaying Output
print(total)
   
    



