def fizz_buzz(n):
  if isinstance(n, int):
    if n % 3 == 0 and n % 5 == 0:
      return 'FizzBuzz'
    elif n % 5 == 0:
      return 'Buzz'
    elif n % 3 == 0:
      return 'Fizz'
    else:
      return n
  else:
    return 'Invalid input'
