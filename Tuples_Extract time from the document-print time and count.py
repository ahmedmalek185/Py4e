#open and read file
fname = input("Enter file name: ")
fh = open(fname)

#initialize doctionary
rushour=dict()
#seq=list()
#Data collection and cleaning
for line in fh:
    if not line.startswith('From'): continue
    line=line.rstrip()
    if not line.endswith('2008'):continue
    words=line.split()
    #print(words)
    time=words[5]
    hours=time.split(':')
    hour=hours[0]
    #print(hour)
    rushour[hour]=rushour.get(hour,0)+1
for k,v in sorted(rushour.items()):
    print(k,v)
    #seq.append((v,k))
    #seq=sorted(seq, reverse=True)
#print(rushour.values())
#for v, k in seq:
    #print(v,k)
#looking for the most prolific committer
#bigcount= None
#bigmail= None
#for email,count in senders.items():
#    if bigcount is None or count>bigcount:
#        bigmail=email
#        bigcount=count
#print(bigmail, bigcount)
