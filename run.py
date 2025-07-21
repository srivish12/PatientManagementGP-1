from datetime import datetime
from patient import Patient
from gp_practice import GPPractice

"""
run.py
This script implements a command-line Patient Management System for
 a GP Surgery.
It allows users to perform various operations such as adding, viewing,
 searching,updating, and deleting patient records. The system also provides
 statistics on the number of patients admitted overall, per day, and per month.

Features:
- Add new patients with details including ID, name, age, gender, diagnosis,
  and date of admission.
- View all registered patients.
- Search for patients by ID or name.
- Update patient information.
- Delete patient records.
- Display total number of patients.
- Show number of patients admitted per day and per month.
- Input validation for patient details.
- Interactive menu-driven interface.
Dependencies:
- patient.py: Contains the Patient class definition.
- gp_practice.py: Contains the GPPractice class for managing patient records.
Usage:
Run the script and follow the on-screen prompts to manage patient records.
"""


def main():
    gppractice = GPPractice()

    while True:
        print("\n---Patient Management System in GP Surgery---\n")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Search Patient by Name")
        print("5. Update Patient")
        print("6. Delete Patient")
        print("7. Number Of Patients Admitted")
        print("8. Number Of Patients Admitted per Day")
        print("9. Number Of Patients Admitted per Month")
        print("10. Exit")
        print("--------------------------------")

        choice = input("Enter the Number which you want to look: ").strip()

        if choice == "1":
            pid = input("Patient ID: ")
            if not pid:
                print("Patient Id can not be empty")
                input("enter to continue..")
                continue
            name = input("Name: ")
            if not name or name.isdigit():
                print("Name can not be empty or can not be a number")
                input("enter to continue..")
                continue
            age_input = input("Age: ").strip()
            if not age_input.isdigit() or not age_input or int(age_input) <= 0:
                print("age must be a positive number or can not be empty")
                input("enter to continue..")
                continue
            gender = gppractice.get_gender_input()
            if gender == "invalid value":
                print("Invalid gender, please enter male or female")
            else:
                diagnosis = input("Diagnosis: ")
                date_input = input("Date of Admission (YYYY-MM-DD):")

                try:
                    date_of_admission = datetime.strptime(
                        date_input, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    input("Press Enter to continue...")
                    continue
                patient = Patient(pid, name, age_input, gender, diagnosis,
                                  date_of_admission)
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
            gender = gppractice.get_gender_input()
            if gender == "invalid value":
                print("Invalid gender, please enter male or female")
                gender = None
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
            print(f"Total Number of patients Registered : "
                  f"{len(gppractice.patients)}")

        elif choice == "8":
            patient_counts = {}

            for patient in gppractice.patients.values():
                date = patient.date_of_admission
                if date in patient_counts:
                    patient_counts[date] += 1
                else:
                    patient_counts[date] = 1
            if not patient_counts:
                print("No patients were admitted on this day")
            else:
                print("Number of patients admitted per day:")
                for date in patient_counts:
                    print(f"{date}: {patient_counts[date]}")

        elif choice == "9":
            patient_counts = {}

            for patient in gppractice.patients.values():
                month = patient.date_of_admission.strftime("%Y-%m")
                if month in patient_counts:
                    patient_counts[month] += 1
                else:
                    patient_counts[month] = 1

            if not patient_counts:
                print("No patients were admitted in this month")
            else:
                print("Number of patients admitted per month:")
                for month in sorted(patient_counts):
                    print(f"{month}: {patient_counts[month]}")

        elif choice == "10":
            print("Exiting the Program!")
            break

        else:
            print("Invalid choice. Try again.")

        input("Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()
