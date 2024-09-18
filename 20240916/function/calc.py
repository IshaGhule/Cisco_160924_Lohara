# def find_diff(first:int = 1, second:int = 2):
#     return first - second

# print(find_diff(20,10)) #10
# print(find_diff(second=10,first=20)) #10
# print(find_diff(second=10))  #-9
# print(find_diff())  #-1

# def change_name(names, index, name):
#     names[index] = name

# names = ['rahul', 'modi']
# print(names)
# change_name(names,1,'modiji')
# print(names)

# print(sum([10,20,30]))

# def find_sum(first, second, *others):
#     s = first + second
#     if(len(others) > 0):
#         for num in others:
#             s += num
#         #end for
#     #end if
#     #print(type(others))
#     return s

# print(find_sum(10,20)) #30
# print(find_sum(10,20,30)) #60
# print(find_sum(10,20,30,40,50)) #150


# def find_sum(first, second, **others):
#     s = first + second
#     if(len(others) > 0):
#         for key in others:
#             s += others[key]
#         #end for
#     #end if
#     #print(type(others))
#     return s

# print(find_sum(first=10,second=20)) #30
# print(find_sum(first=10,second=20,third=30)) #60 
# print(find_sum(first=10,second=20,third=30,fourth=40,fifth=50))  #150

# def fact(N):
#     if N <= 1: #base/edge case
#         return 1
#     #endif
#     return N * fact(N-1)

# print(fact(5)) #120
# print(fact(4)) #24

import math
def is_prime(N):
    N_sqrt = int(math.sqrt(N))
    for I in range(2,N_sqrt+1):
        if N % I == 0:
            return False
        #endif
    #endfor
    return True

print(is_prime(5))
print(is_prime(51))
print(is_prime(60))
print(is_prime(61))