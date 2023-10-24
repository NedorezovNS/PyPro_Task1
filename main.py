from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print('Это main.py')
    today = datetime.now()
    time_format = "%Y-%m-%d, точное время: %H:%M:%S."
    print(f'Приветствую Вас, сегодня {today:{time_format}}')
    calculate_salary()
    get_employees()
