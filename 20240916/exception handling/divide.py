def find_quotient(d,n):
    if n== 0:
        raise ZeroDivisionError()
    return d/n

try:
    number = int(input("Enter a number: "))
    result = find_quotient(10, number)
    
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
    
else:
    print(result)
    
finally:
    print('cleaning up')
print('End of program')
