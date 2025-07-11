class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis, dateOfAdmit):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.date_of_admission = dateOfAdmit


"""
# Patient registration

# Viewing all patients

# Searching patients by ID

# Updating patient records

# Deleting records#
# number of patient admitted and discharged to predict future trends

 """


class GP_Practice:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        count = 0
        if patient.patient_id in self.patients:
            print("Patient ID already exists!")
        else:
            self.patients[patient.patient_id] = patient
            print("Patient added successfully.")
        count += 1
