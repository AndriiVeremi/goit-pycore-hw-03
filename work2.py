import random

def get_numbers_ticket(min, max, quantity):
    
    q = quantity
    list = []
    
    if not (1 <= min <= 1000 and 1 <= max <= 1000):
        return "Помилка: min і max повинні бути між 1 та 1000."
    
    if quantity > (max - min + 1):
        return "Помилка: quantity перевищує кількість можливих чисел у заданому діапазоні."
    
    while q != 0:      
        num = random.randint(min, max)
        list.append(num)
        q -= 1
        
    return list

lottery_numbers = get_numbers_ticket(1, 49, 6)
#lottery_numbers = get_numbers_ticket(1, 49, 600)
#lottery_numbers = get_numbers_ticket(0, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

