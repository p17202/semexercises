months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
cal1=[]
cal2=[]
cal3=[]
week = ['S','M','T','W','T','F','S']


year=int(input("Enter the year : "))
month=input("Enter the month (the first letter in capitals): ")


for i in range(1,31):
    cal1.append(i)

for i in range(1,32):
    cal2.append(i)

for i in range(1,29):
    cal3.append(i)




def is_leap(year):
    """Checks if year is a leap year"""
    if ((year%4) == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False





print('\n',month,' ',year,'\n')

for i in range(7):
    print(week[i], end='\\t')

print('\n')


if (month=='January') or (month=='March') or (month=='May') or (month=='July') or (month=='August') or (month=='October') or (month=='December'):
    for i in range (len(cal1)):
        print(cal1[i], end='\\t')

elif (month=='April') or (month=='June') or (month=='September') or (month=='November'):
    cal2.insert(0,' \\t')
    for i in range (len(cal2)):
        print(cal2[i], end='\\t')

elif (month=='February'):
    cal3.insert(0,' \\t')
    for i in range (len(cal3)):
        print(cal3[i], end='\\t')
