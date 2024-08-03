def decorator_key_word_as_str(func):
    def operation_replacing(*args, **kwargs):
        operation = func(*args, **kwargs)
        return {"result": operation}

    return operation_replacing


@decorator_key_word_as_str
def final_word(text1, text2) -> dict:
    return text1 + text2


result = final_word(text1='Салам', text2='Алейкум')
print(result)
