def calc(first:int, second:int)->int:
    sum = first + second
    diff = first - second
    product = first * second
    quotient = first // second
    return sum, diff, product, quotient

s,d,p,q = calc(20,6)
print(s,d,p,q)
