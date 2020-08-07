#pgm to display the numbers from 1 to 10  except from 3,5,7

for i in range(1,11):
    if i ==3:
        continue
    elif i ==5:
        continue
    elif i ==7:
        continue
    print(i, end="")
