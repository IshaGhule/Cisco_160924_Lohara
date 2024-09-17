import json

def add_patient_list(patient_list, patient_name):
    """Add a patient to the list."""
    if patient_name not in patient_list:
        patient_list.append(patient_name)
        print(f'Patient {patient_name} added.')
    else:
        print(f'Patient {patient_name} already exists.')

def remove_patient_list(patient_list, patient_name):
    """Remove a patient from the list."""
    if patient_name in patient_list:
        patient_list.remove(patient_name)
        print(f'Patient {patient_name} removed.')
    else:
        print(f'Patient {patient_name} does not exist.')

def write_list_to_json(patient_list, filename):
    """Write the list of patients to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(patient_list, file)
    print('List written to JSON file.')


patients_list = ['Alice', 'Bob', 'Charlie']
add_patient_list(patients_list, 'David')
remove_patient_list(patients_list, 'Alice')
write_list_to_json(patients_list, 'patients_list.json')

