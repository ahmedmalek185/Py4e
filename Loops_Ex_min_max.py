largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
      n=int(num)
      if smallest == 0:
        smallest = n
      elif n < smallest:
            smallest = n
      elif n > largest:
        largest = n
    except:
      print('Invalid input')
      continue
print('Maximum is', largest)
print('Minimum is', smallest)
