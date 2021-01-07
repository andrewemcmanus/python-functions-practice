def fizzbuzz(n):
    # create an array of numbers for the number of inputs
    arr = list(range(1, n))
    for i in range(len(arr)):
        a = i + 1
        if ( a % 3 == 0 and a % 5 == 0):
            print('fizzbuzz')
        elif (a % 3 == 0):
            print('fizz')
        elif (a % 5 == 0):
            print('buzz')
        else:
            print(i)
input = input('What do you want to fizzbuzz? ')
number = int(input)
fizzbuzz(number)
