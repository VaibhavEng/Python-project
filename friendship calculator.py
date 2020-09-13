alphabet='bcghjklmpqrtvwxyz'
score=0
names=input('Enter first name and give space and than enter second name:-')
for character in names:
    if character in 'aeiou':
        score+=5
    if character in 'friends':
        score+=10
    if character in alphabet:
        score+=alphabet.find(character)
    else:
        score+=0

if score>100:
    print('your friendship score is :',score)
    print('Congratulation! you both are best friends')
    for row in range (6):
        for col in range (7):
            if(row==0 and col%3!=0)or (row==1 and col%3==0) or (row-col==2)or (row+col==8):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

else:
    print('your friendship score is:',score)
