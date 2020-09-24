height = int(input("How many lines tall do you want the pyramid to be?: "))
n = 0

for l in range(0, height) : # for each line
    for z in range (0, int(height-l)): # spaces in front
            print (" ", end='')

    for x in range(0, l+1) : # actual numbers
        if n > 9 :
            print(str(n)+" ", end='')
        elif n <= 9 : #this add a 0 to the front of 1 digit numbers
            print("0"+str(n)+" ", end='')
        n = n+1
    print("")