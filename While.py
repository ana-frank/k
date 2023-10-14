#Dictionary
Diction={
    'Jan':'January',
    'Feb':'February',
    3:'March'
    }
Diction.values
print(Diction)
Diction.update({'Feb':'Fib'})
print(Diction)
print(Diction[4])
print(Diction['Feb'])
print(Diction[3])
print(Diction.get('Jan'))
print(Diction.get('Ap','Invalid'))
print(Diction.get('Ap'))
Set1={'Farjana','Ana','Mim','Tamanna','Hur','Jam'}
print(Set1)


#set functions
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
Intersect=set1.intersection(set2)
union_set=set1.union(set2)
print(union_set)
print(Intersect)


#Finding max
num=[3,7,8,4,2,3,1,100]
max=num[0]
for number in num:
    if number>max:
        max=number
print(max)



#for loop
#in range last one wont be printed
for index in range(5,15):
    print(index)

for letter in {'Farjana','Rahman',34,79,45,'g'}:
    print(letter)


#Guess number
Correct_num=3
Opportunity=1
while Opportunity<=3:
    Guess=int(input('Put your guess '))
    Opportunity+=1
    if Guess==Correct_num:
        print('You win.')
        break
else:
    print("You lose")
    

# Number table
Number=1
Value=int(input('What is the num ? '))
while Number<=10:
    result=Number*Value
    print(result)
    Number+=1        



