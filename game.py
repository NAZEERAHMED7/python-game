import random

# computer enter odd or even
def get_computer_odd_or_even ():
    Computer_decision= random.choice(['odd','even'])
    print (f'computer decision: {Computer_decision}')
    return Computer_decision

# user enter odd or even
def get_user_odd_or_even ():
    User_decision= input(f'''[odd,even] 
Choose your choice: ''')
    print(f'User decision: {User_decision}')
    return User_decision

# computer enter the odd or even number 
def get_computer_number ():
    Computer_no= random.choice([1, 2, 3, 4, 5, 6])
    return Computer_no
#user enter the odd or even number
def get_user_number ():
    User_no= int(input(f'''[1, 2, 3, 4, 5, 6] 
Choose your choice: '''))
    return User_no

Even= [2, 4, 6, 8, 10, 12]
Odd= [1, 3, 5, 7, 9, 11]

# result of odd or even 
def result ():
    result_val=0
    comp_num= get_computer_number()
    user_num=get_user_number()
    result_val= user_num + comp_num
    print(f'The user selected number is: {user_num}')
    print(f'The Computer selected number is: {comp_num} ')
    print(f'The number is: {result_val}')
    return result_val
result()

def match ():
    if result == Odd:
        print('This is even number')
        int(input(f'''Choose to:
1.batting
2.bouling'''))
        
    elif result == Even:
        print('This is odd number')
        int(input(f'''Choose to:
1.batting
2.bouling'''))
    
    else:
        print("invalid Choice")


def get_computer_choice():
    computer_choice = random.choice ([0, 1, 2, 3, 4, 5, 6])
    return computer_choice

def get_user_choice():
    choice =int(input(f'''
[0, 1, 2, 3, 4, 5, 6]
                    
Choose Your number: '''))
    return choice

def conditions(start,computer):
    if start==0 and computer==1 or \
        start==0 and computer==2 or \
        start==0 and computer==3 or \
        start==0 and computer==4 or \
        start==0 and computer==5 or \
        start==0 and computer==6 :
        total += start

    elif start==1 and computer==0 or \
        start==1 and computer==2 or \
        start==1 and computer==3 or \
        start==1 and computer==4 or \
        start==1 and computer==5 or \
        start==1 and computer==6 :
        total += start

    elif start==2 and computer==0 or \
        start==2 and computer==1 or \
        start==2 and computer==3 or \
        start==2 and computer==4 or \
        start==2 and computer==5 or \
        start==2 and computer==6 :
        total += start

    elif start==3 and computer==0 or \
        start==3 and computer==1 or \
        start==3 and computer==2 or \
        start==3 and computer==4 or \
        start==3 and computer==5 or \
        start==3 and computer==6 :
        total += start

    elif start==4 and computer==0 or \
        start==4 and computer==1 or \
        start==4 and computer==2 or \
        start==4 and computer==3 or \
        start==4 and computer==5 or \
        start==4 and computer==6 :
        total += start

    elif start==5 and computer==0 or \
        start==5 and computer==1 or \
        start==5 and computer==2 or \
        start==5 and computer==3 or \
        start==5 and computer==4 or \
        start==5 and computer==6 :
        total += start

    elif start==6 and computer==0 or \
        start==6 and computer==1 or \
        start==6 and computer==2 or \
        start==6 and computer==3 or \
        start==6 and computer==4 or \
        start==6 and computer==5 :
        total += start

    elif start==computer:
        print("You are Out!")
        
    else:
        print("Invalid No")

def game ():
    total = 0
    while True:
        start= get_user_choice()
        print(f"Your Choice: {start}")

        computer = get_computer_choice()
        print(f"Computer choice: {computer}")

        conditions()

        

        print(total)
game()




