# approach for assignment:

# 1. class patient (id, name)

class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f'[id = {self.id}, name = {self.name}]'
    def __repr__(self): # function used for repetition of string.
        return self.__str__()
    
#patients[]

patients = []
        
# 2. patient_add(id, name)

def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)

# 3. patient_remove(id)

def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
              patients.remove(patient)
              print('Patient deleted successfully')
            return 
    print(f'No such id {id}')

# 4. patient_display()

def patient_display():
    global patients
    for patient in patients:
        print(patient)

# 5. Menu 

def menu():
    choice = int(input('''1-Add Patient
2-Remove Patient by id
3-Display all Patients
4-End
Your choice: '''))
    if choice == 1:
        id = input('Enter patient id: ')
        name = input('Enter patient name: ')
        patient_add(id, name)
    elif choice == 2:
        id = input('Enter patient id: ')
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice == 4:
        pass
    else:
        print('Invalid menu')
    return choice

# 6. menus

def menus():
    choice = menu()
    while choice != 4:
      choice = menu()
    print('Thank You for using the app')

# 7. driver program

menus()

