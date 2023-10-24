from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print('Это dirty_main.py')
    today = datetime.now()
    time_format = "%Y-%m-%d, точное время: %H:%M:%S."
    print(f'Приветствую Вас, сегодня {today:{time_format}}')
    calculate_salary()
    get_employees()
