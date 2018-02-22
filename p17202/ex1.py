import random



def my_random():
    return random.randint(1,80)


table=[]

for x in range(100):
    players=[x]
    numbers=[my_random(),my_random(),my_random(),my_random(),my_random()]
    table.append(numbers)

print(table)
print(table[0][1])

for y in range (1000):

        
        winningnumbers=[my_random(),my_random(),my_random(),my_random(),my_random()]
        print("The winning numbers are  ",winningnumbers,"\n" * 2)
        k=0 #it eliminates k each time we get the next five numbers
        l=0

        for i in range(100):
                for j in range (5):
                    while (l<5):
                        while (table[i][j] == winningnumbers[l]):
                            k=k+1
                            if k == 5: print("the quota is: ", (y+1)/1000 )
                            

                        l+=1

#a function to find if each players numbers match with the winning numbers
def matched_numbers():
    
