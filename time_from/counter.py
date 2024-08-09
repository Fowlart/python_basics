from datetime import datetime, timedelta


def show_days():

    the_date = "10-08-2024"

    days_to_spent = 50

    converted_date: datetime = datetime.strptime(the_date, '%d-%m-%Y')

    end_day = converted_date+timedelta(days=days_to_spent)

    msg_summary = 'ATTENTION:'

    msg_body = f"You have {end_day - datetime.utcnow()} left"

    print(msg_summary)

    print(msg_body)

if __name__ == "__main__":
    show_days()