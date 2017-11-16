def basic_op(operator, value1, value2):
    dict = {
        "+": value1 + value2,
        "-": value1 - value2,
        "*": value1 * value2,
        "/": value1 / value2
    }
    return dict.get(operator)
