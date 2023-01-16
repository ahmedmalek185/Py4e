#open and read file
name = "/Users/ahmed/OneDrive/Desktop/Desktop Documents/Python by FreedCodeCamp/Lists/mbox-short.txt"
fh = open(name)

#count=0
#initialize doctionary
senders=dict()

#Data collection and cleaning
for line in fh:
    if not line.startswith('From'): continue
    line=line.rstrip()
    if line.endswith('2008'):continue
    words=line.split()
    email=words[1]
    #person=email.split('@')
    #name=person[0]
    #print(name)
    senders[email]=senders.get(email,0)+1
print(senders.values())
print(senders.index())

#looking for the most prolific committer
bigcount= None
bigmail= None
for email,count in senders.items():
    if bigcount is None or count>bigcount:
        bigmail=email
        bigcount=count
print(bigmail, bigcount)
