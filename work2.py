import random

def get_numbers_ticket(min, max, quantity):
    
    q = quantity
    list = []
    
    while q != 0:      
        num = random.randint(min, max)
        list.append(num)
        q -= 1
        
    return list

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

