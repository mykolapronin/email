def calculate_discounted_price(price: float, discount: float) -> float:
    if price < 0:
        raise ValueError("Ціна не може бути меншою за 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Відсоток знижки повинен бути в діапазоні від 0 до 100.")

    discounted_price = price * (1 - discount / 100)
    return discounted_price


# n = calculate_discounted_price(100, 25)
# print(n)
