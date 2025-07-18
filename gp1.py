from datetime import datetime


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

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient record deleted.")
        else:
            print("Patient ID not found.")

    def get_gender_input():
        gender = input("Gender (male/female): ").strip().lower()
        if gender in ["male", "m"]:
            return "male"
        elif gender in ["female", "f"]:
            return "female"
        else:
            return "invalid value"

    def main():
        gppractice = GP_Practice()

        while True:
            print("\n---Patient Management System in GP ---")
            print("1. Add Patient")
            print("2. View All Patients")
            print("3. Search Patient by ID")
            print("4. Search Patient by Name")
            print("5. Update Patient")
            print("6. Delete Patient")
            print("7. Number Of Patients Admitted")
            print("8. Exit")

            choice = input("Enter the Number which you want to look: ")

            if choice == "1":
                pid = input("Patient ID: ")
                name = input("Name: ")
                age = int(input("Age: "))
                gender = gppractice.get_gender_input()
                if gender == "invalid value":
                    print("Invalid gender, please enter male or female")
                else:
                    diagnosis = input("Diagnosis: ")
                    date_input = input("Date of Admission (YYYY-MM-DD):")
                    try:
                        date_Of_admission = datetime.striptime(
                            date_input, "%Y- %m -%d"
                        ).date()
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")

                    patient = Patient(pid, name, age, gender, diagnosis,
                                      date_Of_admission)
                    gppractice.add_patient(patient)

            elif choice == "2":
                gppractice.view_all_patients()

            elif choice == "3":
                pid = input("Enter Patient ID: ")
                gppractice.search_patient_by_id(pid)

            elif choice == "4":
                name = input("Enter Patient Name: ")
                gppractice.search_patient_by_name(name)

            elif choice == "5":
                pid = input("Enter Patient ID to update: ")
                print("Leave field blank if no change is needed.")
                name = input("New Name: ")
                age = input("New Age: ")
                gender = input("New Gender: ")
                diagnosis = input("New Diagnosis: ")
                gppractice.update_patient(
                    pid,
                    name or None,
                    age or None,
                    gender or None,
                    diagnosis or None
                )

            elif choice == "6":
                pid = input("Enter Patient ID to delete: ")
                gppractice.delete_patient(pid)

            elif choice == "7":
                gppractice.view_count = len(gppractice.patients)
                print(f"Total Number of patients Registered : "
                      f"{gppractice.view_count}")

            elif choice == "8":
                patient_counts = {}

                for patient in gppractice.patients.values():
                    date = patient.date_of_admission
                    if date in patient_counts:
                        patient_counts[date] += 1
                    else:
                        patient_counts[date] = 1

                print("Number of patients admitted per day:")
                for date in patient_counts:
                    print(f"{date}: {patient_counts[date]}")
