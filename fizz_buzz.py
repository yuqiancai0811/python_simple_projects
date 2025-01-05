def fizz_buzz():
    try:
        user_input = int(input("Enter a number: "))
        if user_input % 3 == 0 and user_input % 5 == 0:
            return 'FizzBuzz'
        if user_input % 3 == 0:
            return 'Fizz'
        if user_input % 5 == 0:
            return 'Buzz'

        return user_input
    except ValueError:
        print('Invalid value.')


print(fizz_buzz())
