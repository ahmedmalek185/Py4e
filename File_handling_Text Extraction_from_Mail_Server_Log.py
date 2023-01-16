fname = input("Enter file name: ")
fh = open(fname)
count=0
fl=0
s=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    colpos=line.find(' ')
    s=s+float(line[colpos+1:])
avg=float(s/count)
print('Average spam confidence:', avg)
