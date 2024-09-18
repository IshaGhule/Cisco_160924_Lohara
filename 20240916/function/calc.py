def find_diff(first:int = 1, second:int = 2):
    return first - second

print(find_diff(20,10)) #10
print(find_diff(second=10,first=20)) #10
print(find_diff(second=10))  #-9
print(find_diff())  #-1

def change_name(names, index, name):
    names[index] = name

names = ['rahul', 'modi']
print(names)
change_name(names,1,'modiji')
print(names)
