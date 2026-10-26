Simple Patient Record System
Project Description
The Simple Patient Record System is a Python program that demonstrates how patient records can be created, stored, searched, displayed, and updated using object-oriented programming (OOP).

The program uses two classes: Patient, which represents an individual patient, and PatientRecordSystem, which manages the collection of patient records. Records are stored in memory while the program is running.
Features
- Create patient records with a patient ID, display name, age, and visit status.
- Add patient records to the system.
- Prevent duplicate patient IDs.
- Find a patient by their ID.
- Display all patient records.
- Update a patient's visit status.
- Validate ages as non-negative whole numbers.
- Display a description of the system.
Technologies Used
- Python 3
- Object-oriented programming (classes, objects, methods, and class methods)
Requirements
- Python 3 installed on your computer.
- No external packages are required for the current code.
How to Run
1. Open the project in PyCharm.
2. Save the Python code in a file such as main.py.
3. Click Run in PyCharm, or open the terminal and enter:
   python main.py
   If your Python file has a different name, replace main.py with that filename.
How It Works
1. The program creates a PatientRecordSystem object.
2. It creates two demonstration patient records with IDs P001 and P002.
3. It adds the records to the system.
4. It prints the system description and displays all patient records.
5. It updates patient P001 to the visit status Visit Completed.
6. It finds P001 and prints the updated record.
Main Classes
Patient
Represents one patient. It stores a patient ID, display name, age, and visit status. Its methods update a patient's details and return a formatted string containing the patient's information.
PatientRecordSystem
Manages the patient records. Its methods add patients while checking for duplicate IDs, find patients by ID, display all patients, update a patient's visit status, and return a description of the system.
Important Notes
- Records are stored in a Python list in memory.
- The program does not currently use a database or save records to a file. Records are lost when the program ends.
- The included patient names are demonstration data, not real patient records.
- This is a basic educational example, not a complete clinical or hospital record system.
Project Files
- main.py — Python source code.
- README.md — project overview and run instructions.
