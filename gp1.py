class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis, dateOfAdmit):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.date_of_admission = dateOfAdmit

    def __str__(self):
        return (
            f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
            f"Gender: {self.gender}, Diagnosis: {self.diagnosis}, "
            f"Date of Admission: {self.date_of_admission}"
        )


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
        if patient.patient_id in self.patients:
            print("Patient ID already exists!")
        else:
            self.patients[patient.patient_id] = patient
            print("Patient added successfully.")

    def view_all_patients(self):
        if not self.patients:
            print("No patient records found.")
        else:
            for patient in self.patients.values():
                print(patient)

    def search_patient_by_id(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print(patient)
        else:
            print("Patient not found.")

    def search_patient_by_name(self, name):
        found = False
        for patient in self.patients.values():
            if patient.name == name:
                print(patient)
                found = True
        if not found:
            print("Patient not found.")

    def update_patient(
        self, patient_id, name=None, age=None, gender=None, diagnosis=None
    ):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            if name:
                patient.name = name
            if age:
                patient.age = age
            if gender:
                patient.gender = gender
            if diagnosis:
                patient.diagnosis = diagnosis
            print("Patient record updated.")
        else:
            print("Patient ID not found.")
