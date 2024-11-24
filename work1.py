from datetime import datetime

def get_days_from_today(date):
   try:
      current = datetime.now()
      given_date = datetime.strptime(date, "%Y-%m-%d")
      delta = current - given_date
      return delta.days
   except ValueError:
      print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
      
      
print(get_days_from_today("2020-10-09"))