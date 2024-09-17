words_list = input("Enter a list of words(seperated by spaces): ").split()

words_tuple = tuple(words_list)
print(f'List: {words_list}')
print(f'Tuple: {words_list}')

with open('fruits.txt','w') as data_file:
    data_file.write(f'List: {words_list}')
    data_file.write(f'Tuple: {words_list}')
print('Data written to file')

with open('fruits.txt','r') as data_file:
    line_list = data_file.readline()
    line_tuple = data_file.readline()
    print(line_list)
    print(line_tuple)


