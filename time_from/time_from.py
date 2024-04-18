from datetime import datetime, timedelta
import notify2

date_of_law_start = "16-04-2024"

days_to_spent = 70

converted_date: datetime = datetime.strptime(date_of_law_start, '%d-%m-%Y')

end_day = converted_date+timedelta(days=days_to_spent)

notify2.init('app name')
n = notify2.Notification('ATTENTION:', f"You have {end_day - datetime.utcnow()} left")
n.show()