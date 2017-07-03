def fizz_buzz(number):
  if number in range(1001):
    if number % 3 == 0 and number % 5 == 0:
      return "Fizz Buzz"
    if number % 3 == 0:
      return "Fizz"
    if number % 5 == 0:
      return "Buzz"
    else:
      return number
  else:
    print 'Wrong number!'
