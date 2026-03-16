# Define a class Patient and a class Medicine. Each patient consists of a name,
# age and a set containing what substances he/she is allergic to. The class 
# medicine instead consist of a set of allergens. Within the class Patient, 
# define a method to check whether the patient is allergic to a medicine i.e. 
# any of its allergens

class Patient:
    def __init__(self, name, age, allergies):
        self.name = name
        self.age = age
        self.allergies = allergies
    
    def check(self, medicine):
        return len(self.allergies & medicine.allergens) != 0

class Medicine:
    def __init__(self, name, allergens):
        self.name = name
        self.allergens = allergens

patients = [
    Patient("Luca", 23, {"penicillina", "ibuprofene"}),
    Patient("Fabio", 25, {"ibuprofene"}),
    Patient("Giulia", 31, {"aspirina"}),
    Patient("Marco", 40, {"paracetamolo"}),
    Patient("Anna", 29, {"penicillina"}),
    Patient("Paolo", 50, {"ibuprofene", "aspirina"}),
    Patient("Chiara", 35, {"lattosio"}),
    Patient("Davide", 27, {"paracetamolo", "ibuprofene"}),
]

medicines = [
    Medicine("Tachipirina", {"paracetamolo"}),
    Medicine("Antibiotico", {"penicillina"}),
    Medicine("Moment", {"ibuprofene"}),
    Medicine("Aspirina", {"aspirina"}),
    Medicine("Sciroppo", {"lattosio"}),
    Medicine("Antidolorifico", {"paracetamolo", "ibuprofene"}),
]

results = [
    (patient, medicine, patient.check(medicine)) 
    for patient in patients
    for medicine in medicines    
]

result_strings = [
    f"{patient.name} è allergico/a a {medicine.name}"
    for patient, medicine, check in results if patient.check(medicine)
]

for result in result_strings:
    print(result)
