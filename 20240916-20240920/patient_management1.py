# approach for assignment: as per list

# 1. class patient (id, name)

class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f'[id = {self.id}, name = {self.name}]'
    def __repr__(self): # function used for repetition of string.
        return self.__str__()
    
# 2. patients[]

patients = []
        
# 3. patient_add(id, name)

def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)
    print('Patient created successfully')

# 4. patient_remove(id)

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

# 5. patient_display()

def patient_display(id):
    global patients
    for patient in patients:
        #print(patient)
        if patient.id == id:
          print(patient)
          return
    print('Invalid id')    

# 6.patient_update()

def patient_update(id, new_name):
    global patients
    for patient in patients:
        if patient.id == id:
            patient.name = new_name
            print(f'Patient {id} updated successfully')
            return
    print(f'No such id {id}')   

# 7. Menu 

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
        id = input('Enter patient id: ')
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

# 9. driver program

menus()

