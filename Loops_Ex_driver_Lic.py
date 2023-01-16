x1=input('Enter your name:')
print('welcome',x1, '!')
while True:
  x2=input('Enter your age:')
  try:
    x3=int(x2)
    break
  except:
    print('Invalid Input, Enter a Numeric Value')
    continue
if x3 < 16:
  print('You should not be here you underage individual!')
elif x3 >= 16 and x3 < 18:
  print('Although you are not a kid anymore, you still have to wait', 18-x3,'more year(s)')
else:
    print('You can now apply for your driving licence')
