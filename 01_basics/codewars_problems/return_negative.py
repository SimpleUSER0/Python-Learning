# Codewars Kata: Returne Negative
# Link: https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
# Difficulty: 8 kyu

def function_name(parameters):
    "convert number into negative"
    def make_negative(number):
        if number == 0:
            return 0
        elif number < 0:
            return number
        else:
            return -abs(number)
        pass

# ტესტები 
print(make_negative(1))  # return -1
print(make_negative(-5)) # return -5
print(make_negative(0))  # return 0