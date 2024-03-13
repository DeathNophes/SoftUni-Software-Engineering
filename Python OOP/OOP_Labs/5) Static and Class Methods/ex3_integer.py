class Integer:
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"

        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        result = 0

        for i in range(len(value)):
            if i != 0 and cls.ROMAN[value[i]] > cls.ROMAN[value[i - 1]]:
                result += cls.ROMAN[value[i]] - 2 * cls.ROMAN[value[i - 1]]
            else:
                result += cls.ROMAN[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))
