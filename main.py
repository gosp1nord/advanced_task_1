from application import people as pp
from application.salary import calculate_salary
from datetime import datetime

def get_time():
    tt = datetime.now().timetuple()
    res = f"{tt[3]}:{tt[4]}:{tt[5]}"
    return res

if __name__ == '__main__':
    print(f"{datetime.now()} -> запуск программы")
    print(f"[{get_time()}] -> Запуск поиска информации о сотрудниках.")
    empl = pp.get_employees()
    print(f"[{get_time()}] -> {empl}")

    print(f"[{get_time()}] -> Запуск подсчета заработной платы.")
    sal = calculate_salary()
    print(f"[{get_time()}] -> {sal}")

