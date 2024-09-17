from Patient import Patient
patients = {} #dict()
        
# 3. patient_add(id, name)

def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patients.id] = patient #for dict
    #patients.append(patient) for list
    print('Patient created successfully')

# 4. patient_remove(id)

def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient.id == None:
        print(f'No such id {id}')
        return
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
        #patients.remove(patient) for list
        del patients[id] #for dict
        print('Patient deleted successfully')
    #end if

# 5. patient_display()

def patient_display():
    global patients
    for id in patients:
        print(patients[id])

# 6. patient_displaybyid(id)

def patient_displaybyid(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient) 

# 7. patient_update()

def patient_update(id, new_name):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient) 
    name = input(f'Enter new name({patient.name}):')
    patient.name = name
    print('Patient updated successfully') 
