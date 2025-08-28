def main():
    print("Solution for level 1.")
    hello()

def hello():
    """Выводит в консоль приветствие"""
    print("Привет, Python!")

def create_car_variables():
    """Создает переменные с информацией о машине и выводит их значения в консоль."""
    car_color = "синий"
    num_doors = 4
    is_in_use = True
    
    print(f"Цвет машины: {car_color}")
    print(f"Количество дверей: {num_doors}")
    print(f"Используется сейчас: {is_in_use}")

def favorite_color_message():
    """Запрашивает у пользователя любимый цвет и выводит сообщение."""
    color = input("Введите ваш любимый цвет: ")
    print(f"Твой любимый цвет — {color}!")

def calculate_difference():
    """Создает две переменные, вычисляет их разницу и выводит результат."""
    a = 15
    b = 7
    difference = a - b
    print(f"Разница между {a} и {b} равна {difference}")

if __name__ == "__main__":
    main()

