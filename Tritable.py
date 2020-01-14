lastNumber = 10 # print out 9 lines
for i in range(1, lastNumber): # i ranges from 1 to the last number which is 10
    
    for j in range(-1+i, -1,-1):
        print(format(2**j, "4d"), end=' ')
    print("")