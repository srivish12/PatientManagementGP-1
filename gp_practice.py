class GPPractice:
    """
    GPPractice class manages patient records for a general practice.
    Attributes:
        patients (dict): Stores patient objects with patient_id as keys.
    Methods:
        add_patient(patient):
            Adds a new patient to the practice. Checks for duplicate patient
            IDs.
        view_all_patients():
            Displays all patient records. Informs if no records are found.
        search_patient_by_id(patient_id):
            Searches and displays a patient by their unique ID.
        search_patient_by_name(name):
            Searches and displays patients by their name.
        update_patient(patient_id, name=None, age=None, gender=None,
        diagnosis=None):
            Updates patient details for a given patient ID.
        delete_patient(patient_id):
            Deletes a patient record by patient ID.
        get_gender_input():
            Prompts user for gender input and validates it.
    """

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
                patient.age = int(age)
            if gender:
                patient.gender = gender
            if diagnosis:
                patient.diagnosis = diagnosis
            print("Patient record updated.")
        else:
            print("Patient ID not found.")

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient record deleted.")
        else:
            print("Patient ID not found.")

    def get_gender_input(self,):
        gender = input("Gender (male/female): ").strip().lower()
        if gender in ["male", "m"]:
            return "male"
        elif gender in ["female", "f"]:
            return "female"
        elif not gender:
            return "invalid value"
        else:
            return "invalid value"
