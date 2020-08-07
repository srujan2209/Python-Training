# Display the missing values between 10 and 20 from the list[10,20,11,14,13,16,30]

List = [10,20,11,14,13,16,30]

for i in range(10,21):
    if i not in List:
        print(i,end=" ")
