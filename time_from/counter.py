from datetime import datetime, timedelta
import notify2


def show_days():

    the_date = "10-08-2024"

    days_to_spent = 50

    converted_date: datetime = datetime.strptime(the_date, '%d-%m-%Y')

    end_day = converted_date+timedelta(days=days_to_spent)

    print(f"end day: {end_day}")

    notify2.init('days counter')

    msg_summary = 'ATTENTION:'

    msg_body = f"You have {end_day - datetime.utcnow()} left"

    n = notify2.Notification(msg_summary,msg_body)

    n.show()

    print(msg_summary)

    print(msg_body)
