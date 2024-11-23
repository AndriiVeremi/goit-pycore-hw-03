from datetime import datetime

def get_days_from_today(date):
   current = datetime.now()
   given_date = datetime.strptime(date, "%Y-%m-%d")
   delta = current - given_date
   return delta.days

print(get_days_from_today("2020-10-09"))