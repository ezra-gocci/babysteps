from tasks.l1 import (
    hello,
    create_car_variables,
    favorite_color_message,
    calculate_difference,
)
from unittest.mock import patch


def test_console_hello_output(capfd):
    hello()
    out, err = capfd.readouterr()

    assert err == ""
    assert out == "Привет, Python!\n"

def test_car_variables(capfd):
    create_car_variables()
    out, err = capfd.readouterr()

    assert err == ""
    assert "Цвет машины: синий" in out
    assert "Количество дверей: 4" in out
    assert "Используется сейчас: True" in out

def test_favorite_color_message(capfd):
    with patch('builtins.input', return_value='синий'):
        favorite_color_message()

    out, err = capfd.readouterr()

    assert err == ""
    assert "Твой любимый цвет — синий!" in out

def test_calculate_difference_output(capfd):
    calculate_difference()
    
    out, err = capfd.readouterr()
    
    assert err == ""
    assert "Разница между 15 и 7 равна 8" in out

