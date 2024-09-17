patients = []

def patient_add(name):
    global patients
    patients.append(name)
    print(f"Patient added.")

def patient_delete(name):
    global patients
    try:
        patients.remove(name)
        print(f"Patient removed.")
    except ValueError:
        print('No such patient.')

def patient_list():
    global patients
    if patients:
        print("Current patients:")
        for patient in patients:
            print(f"- {patient}")
    else:
        print("No patients in the list.")


def menu():
    choice = int(input('''1-Add Patient
2-Remove Patient
3-List Patients
4-End
Your choice: '''))
    
    if choice == 1:
        name = input('Enter patient name: ')
        patient_add(name)
    elif choice == 2:
        name = input('Enter patient name: ')
        patient_delete(name)
    elif choice == 3:
        patient_list()
    elif choice == 4:
        return choice
    
    return choice


def menus():
    choice = menu()
    while choice != 4:
        choice = menu()
    print('Application Ended')


menus()
