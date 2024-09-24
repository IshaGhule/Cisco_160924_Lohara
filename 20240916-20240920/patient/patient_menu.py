
from patient_service import patient_add,patient_display,patient_display_byid,patient_remove,patient_update
from patient_service import patient_update,patient_remove
def menu():
    choice = int(input('''1- Add Patient
2- Delete Patient by id
3- Display all Patients
4- Read by patient id
5- Update Patient by id
6- End
Your choice: '''))
    if choice == 1:
        id = int(input('Enter patient id: '))
        name = input('Enter patient name: ')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id: '))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice == 4:
        id = int(input('Enter patient id:'))
        patient_display_byid(id)
    elif choice == 5:
        id = int(input('Enter patient id: '))
        patient_update(id)
    elif choice == 6:
        pass
    else:
        print('Invalid menu')
    return choice

# 8. menus

def menus():
    choice = menu()
    while choice != 6:
      choice = menu()
    print('Thank You for using the application.')

