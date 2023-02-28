import random


# ---------- helpers ----------


def friends_number():
    try:
        number = int(input('Enter the number of friends joining (including you):\n'))
    except ValueError:
        print('Incorrect input. Please enter integer number.')
        friends_number()
    else:
        if number < 1:
            raise ValueError('No one is joining for the party')
    return number


def dict_init(number):
    friends_dict = {}
    print('Enter the name of every friend (including you), each on a new line:')
    friends_dict.update({input(): 0 for _ in range(number)})
    return friends_dict


def get_total_bill():
    try:
        total = float(input('Enter the total bill value:\n'))
    except ValueError:
        print('Incorrect input. Please enter float number.')
        get_total_bill()
    else:
        return total
    

def lucky_friend(friend_list):
    try:
        is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if is_lucky not in ("Yes", "No"):
            raise ValueError
        
        if is_lucky == "No":
            print('No one is going to be lucky')
            return None
        
        person = random.choice(friend_list)
        print(f'{person} is the lucky one!')
        return person
    
    except ValueError:
        print('Unxpected value.')
        lucky_friend(friend_list)


def split_bill(friends_dict, total_bill, lucky, friends_number):
    if lucky:
        friends_number -= 1
    
    personal_bill = round(total_bill / friends_number, 2)

    for key in friends_dict:
        if key == lucky:
            continue
        friends_dict[key] = personal_bill
    
    return friends_dict


# ---------- script -----------


try:
    num = friends_number()
except ValueError as err:
    print(err)
else:
    friends = dict_init(num)
    total = get_total_bill()
    lucky = None
    if num > 1:
        lucky = lucky_friend(list(friends.keys()))
    friends = split_bill(friends, total, lucky, num)
    print(friends)
