#if num/3==0:   ---> fizz
#if num/5==0 ---> buzz
#if num/3==0 and num/5==0 ---> fizzBuzz

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FIzzBuzz")
    elif num%3==0:
        print("FIZZ")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)