import random

def my_random():
    return random.randint(-30,30);




numbers=[];

for x in range (30):
    numbers.append(my_random());

print(numbers);


i=0;
j=0;
y=0;


print("The numbers are: \n");


def results(numbers):
    exist= True
    for i in range (len(numbers)-2):
        for j in range (i+1,len(numbers)-1):
            for y in range (j+1,len(numbers)):
                if ((numbers[i]+numbers[j]+numbers[y])==0):
                    print(numbers[i], "," ,numbers[j], "," ,numbers[y]);
                    exist= True

    if (exist==False):
        print("There are mo numbers!")


results(numbers)


