# Codewars kata: Even or Odd
# Link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# 8 Kyu

def even_or_odd(number):
    """Returns "Eeven" if the number is even, and "Odd" if the number is odd."""
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"
# testebi

print(even_or_odd(2)) # Even
print(even_or_odd(3)) # Odd
print(even_or_odd(0)) # Even
print(even_or_odd(-1)) # Odd


