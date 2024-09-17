from Patient import Patient
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
       # print(patient)
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
