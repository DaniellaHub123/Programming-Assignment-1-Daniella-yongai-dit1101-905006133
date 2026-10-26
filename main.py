class Patient:
    def __init__(self, patient_id, display_name, age, visit_status="Registered"):
        self.patient_id = patient_id
        self.display_name = display_name
        self.age = age
        self.visit_status = visit_status

    def update_record(self, display_name=None, age=None, visit_status=None):
        if display_name is not None and display_name.strip():
            self.display_name = display_name.strip()
        if age is not None:
            if not isinstance(age, int) or age < 0:
                raise ValueError("Age must be a non-negative whole number.")
            self.age = age
        if visit_status is not None and visit_status.strip():
            self.visit_status = visit_status.strip()

    def display_info(self):
        return (
            f"Patient ID: {self.patient_id}\n"
            f"Display name: {self.display_name}\n"
            f"Age: {self.age}\n"
            f"Visit status: {self.visit_status}"
        )


class PatientRecordSystem:
    system_name = "Simple Patient Record System"

    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be added.")
        if self.find_patient(patient.patient_id) is not None:
            print(f"Patient ID {patient.patient_id} already exists.")
            return False
        self.patients.append(patient)
        return True

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def display_all_patients(self):
        if not self.patients:
            print("No patient records are available.")
            return
        for patient in self.patients:
            print("-" * 30)
            print(patient.display_info())

    def update_patient_status(self, patient_id, new_status):
        patient = self.find_patient(patient_id)
        if patient is None:
            print(f"No patient found with ID {patient_id}.")
            return False
        patient.update_record(visit_status=new_status)
        return True

    @classmethod
    def get_system_description(cls):
        return f"{cls.system_name} - demonstration records are held in memory."


def main():
    system = PatientRecordSystem()

    patient_one = Patient("P001", "Demo Patient A", 24, "Registered")
    patient_two = Patient("P002", "Demo Patient B", 31, "Visit Completed")

    system.add_patient(patient_one)
    system.add_patient(patient_two)

    print(PatientRecordSystem.get_system_description())
    print("\nALL PATIENT RECORDS")
    system.display_all_patients()

    print("\nUPDATING P001 VISIT STATUS")
    system.update_patient_status("P001", "Visit Completed")
    found_patient = system.find_patient("P001")
    if found_patient is not None:
        print(found_patient.display_info())


if __name__ == "__main__":
    main()