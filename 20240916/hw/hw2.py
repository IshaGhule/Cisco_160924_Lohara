import json

def add_patient_dict(patient_dict, patient_name):
    if patient_name not in patient_dict:
        patient_dict[patient_name] = len(patient_name)  # Example value: length of name
        print(f'Patient {patient_name} added.')
    else:
        print(f'Patient {patient_name} already exists.')

def remove_patient_dict(patient_dict, patient_name):
    if patient_name in patient_dict:
        del patient_dict[patient_name]
        print(f'Patient {patient_name} removed.')
    else:
        print(f'Patient {patient_name} does not exist.')

def write_dict_to_json(patient_dict, filename):
    with open(filename, 'w') as file:
        json.dump(patient_dict, file)
    print('Dictionary written to JSON file.')


patients_dict = {'Alice': 5, 'Bob': 3, 'Charlie': 7}
add_patient_dict(patients_dict, 'David')
remove_patient_dict(patients_dict, 'Alice')
write_dict_to_json(patients_dict, 'patients_dict.json')

