import pytest
from price_function import calculate_discounted_price


def test_calculate_discounted_price():
    assert calculate_discounted_price(100, 10) == 90, "Тест 1 не пройдено"

    assert calculate_discounted_price(100, 0) == 100, "Тест 2 не пройдено"

    assert calculate_discounted_price(100, 100) == 0, "Тест 3 не пройдено"

    with pytest.raises(ValueError, match="Ціна не може бути меншою за 0."):
        calculate_discounted_price(-50, 10)

    with pytest.raises(ValueError, match="Відсоток знижки повинен бути в діапазоні від 0 до 100."):
        calculate_discounted_price(100, -10)

    with pytest.raises(ValueError, match="Відсоток знижки повинен бути в діапазоні від 0 до 100."):
        calculate_discounted_price(100, 110)

    print("Всі тести пройдені успішно.")


test_calculate_discounted_price()
