
from patient_service import patient_add,patient_display,patient_remove,patient_update
from patient_service import patient_update,patient_remove
def menu():
    choice = int(input('''1- Add Patient
2- Remove Patient by id
3- Display all Patients
4- Update Patient name
5- End
Your choice: '''))
    if choice == 1:
        id = input('Enter patient id: ')
        name = input('Enter patient name: ')
        patient_add(id, name)
    elif choice == 2:
        id = input('Enter patient id: ')
        patient_remove(id)
    elif choice == 3:
        id = int(input('Enter patient id: '))
        patient_display(id)
    elif choice == 4:
        id = input('Enter patient id: ')
        new_name = input('Enter new patient name: ')
        patient_update(id, new_name)
    elif choice == 5:
        pass
    else:
        print('Invalid menu')
    return choice

# 8. menus

def menus():
    choice = menu()
    while choice != 5:
      choice = menu()
    print('Thank You for using the application.')

