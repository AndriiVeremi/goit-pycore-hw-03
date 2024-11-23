from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    
    today = datetime.today().date()  
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        difference = (birthday_this_year - today).days

        if 0 <= difference <= 7:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() in (5, 6):  
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Alice Johnson", "birthday": "1995.01.28"},
    {"name": "Bob Brown", "birthday": "1987.01.25"},
    {"name": "Andrii Veremii", "birthday": "1983.11.29"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

        
    