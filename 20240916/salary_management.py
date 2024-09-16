salaries = []

def salary_add(salary):
    global salaries
    salaries.append(salary)
def salary_delete(salary):
    global salaries
    try:
        salaries.remove(salary)
    except ValueError as err:
        print('No such salary')
def salary_sum():
    global salaries
    s = 0
    for salary in salaries:
        s += salary
def salary_avg():
    global salaries
    s = sum(salaries)
    count =len(salaries)
    avg = s / count
    return avg
def salary_max(): #global is not used
    return max(salaries)
def salary_min():
    return min(salaries)

def menu():
    choice = int(input('''1-add
2-delete
3-sum
4-avg
5-max
6-min
your choice: '''))
    if choice ==1:
        salary = float(input('Enter salary: '))
        salary_add(salary)
    elif choice ==2:
        salary = float(input('Enter salary: '))
        salary_delete(salary)
        print(salaries)
    elif choice ==3:
        s = salary_sum()
        print(s)
    elif choice ==4:
        avg = salary_avg()
        print(avg)
    elif choice ==5:
        max = salary_max()
        print(max)
    elif choice ==6:
        min = salary_min()
        print(min)
    return choice

def menus():
    choice = menu()
    while choice !=7:
        choice = menu()
    print('App Ended')

menus()