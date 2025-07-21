class Patient:
    """
    Represents a patient in the Patient Management System.
    Attributes:
        patient_id (int or str): Unique identifier for the patient.
        name (str): Full name of the patient.
        age (int): Age of the patient.
        gender (str): Gender of the patient.
        diagnosis (str): Diagnosis information for the patient.
        date_of_admission (str or datetime): Date when the patient was
        admitted.
    Methods:
        __str__(): Returns a string representation of the patient details.
    """
    def __init__(self, patient_id, name, age, gender, diagnosis,
                 date_of_admission):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.date_of_admission = date_of_admission

    def __str__(self):
        return (
            f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
            f"Gender: {self.gender}, Diagnosis: {self.diagnosis}, "
            f"Date of Admission: {self.date_of_admission}"
        )
