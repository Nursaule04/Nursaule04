# Importing all classes from doctors.py
from doctors import *
# Importing necessary module
from abc import ABC, abstractmethod
import random
# Defining a base class for doctors
class Doctor(ABC):
   def __init__(self, full_name, experience):
       self.full_name = full_name  # Storing the full name of the doctor
       self.experience = experience      # Storing the years of experience of the doctor


   @abstractmethod
   def recommend_department(self, problem):
       pass     # Abstract method to recommend a department based on a patient's problem
# Defining specific doctor classes
class Therapist(Doctor):
   def recommend_department(self, problem):
       if "headache" in problem or "pain" in problem:
           return "Therapy Department"            # Recommend Therapy Department for headache or pain problems
       else:
           return "Therapy Department"           # Default recommendation is Therapy Department


class Surgeon(Doctor):
   def recommend_department(self, problem):
       if "appendicitis" in problem or "hernia" in problem:
           return "Surgery Department"              # Recommend Surgery Department for appendicitis or hernia problems
       else:
           return "Surgery Department"               # Default recommendation is Surgery Department


class Neurologist(Doctor):
   def recommend_department(self, problem):
       if "headache" in problem or "migraines" in problem:
           return "Neurology Department"         # Recommend Neurology Department for headache or migraines problems
       else:
           return "Neurology Department"         # Default recommendation is Neurology Department


class InfectiousDiseaseSpecialist(Doctor):
   def recommend_department(self, problem):
       if "fever" in problem or "Infectious diseases" in problem:
           return "Infectious Diseases Department"           # Recommend Infectious Diseases Department for fever or infectious diseases problems
       else:
           return "Infectious Diseases Department"          # Default recommendation is Infectious Diseases Department
class Pediatrician(Doctor):
   def recommend_department(self, problem):
       if "Childhood illnesses" in problem or "Vaccinations" in problem:
           return "Pediatrics Department"              # Recommend Pediatrics Department for childhood illnesses or vaccinations problems
       else:
           return "Pediatrics Department"            # Default recommendation is Pediatrics Department
class Traumatologist(Doctor):
   def recommend_department(self, problem):
       if "Fractures" in problem or "Trauma" in problem:
           return "Traumatology Department"          # Recommend Traumatology Department for fractures or trauma problems
       else:
           return "Traumatology Department"          # Default recommendation is Traumatology Department
class Dentist(Doctor):
   def recommend_department(self, problem):
       if "Toothache" in problem or "Dental cavities" in problem:
           return "Dentistry Department"         # Recommend Dentistry Department for toothache or dental cavities problems
       else:
           return "Dentistry Department"         # Default recommendation is Dentistry Department


class Cardiologist(Doctor):
   def recommend_department(self, problem):
          if "heart" in problem or "high blood" in problem:
              return "Cardiology Department"        # Recommend Cardiology Department for heart or high blood problems
          else:
              return "Cardiology Department"        # Default recommendation is Cardiology Department
class Ophthalmologist(Doctor):
   def recommend_department(self, problem):
           if "vision" in problem or "eye" in problem:
               return "Ophthalmology Department"       # Recommend Ophthalmology Department for vision or eye problems
           else:
               return "Ophthalmology Department"       # Default recommendation is Ophthalmology Department
class Gastroenterologist(Doctor):
   def recommend_department(self, problem):
       if "stomach pain" in problem or "digestive disorders" in problem:
           return "Gastroenterology Department"       # Recommend Gastroenterology Department for stomach pain or digestive disorders problems
       else:
           return "Gastroenterology Department"      # Default recommendation is Gastroenterology Department
class Gynecologist(Doctor):
   def recommend_department(self, problem):
       if "Pregnancy-related issues" in problem or "Menstrual disorders" in problem:
           return "Gynecology Department"      # Recommend Gynecology Department for pregnancy-related issues or menstrual disorders problems
       else:
           return "Gynecology Department"      # Default recommendation is Gynecology Department
# Defining a class for managing hospital operations
class Hospital:
   def __init__(self):
       # Initialization of departments and doctors data
       self.departments = {
           "Therapy": ["Headache", "Fever", "Cough", "Pregnancy-related issues", "Menstrual disorders", "Toothache",
                       "Dental cavities", "Migraines", "Vision", "Stomach pain", "Digestive disorders",
                       "Childhood illnesses"],
           "Surgery": ["Fractures", "Trauma", "High blood"],
           "Gynecologist": ["Pregnancy-related issues", "Menstrual disorders"],
           "Traumatologist": ["Fractures", "Trauma"],
           "Dentist": ["Toothache", "Dental cavities"],
           "Infectious Disease Specialist": ["Fever", "Infectious diseases"],
           "Neurologist": ["Headache", "Migraines"],
           "Cardiologist": ["Heart issues", "High blood pressure"],
           "Ophthalmologist": ["Vision problems", "Eye disorders"],
           "Gastroenterologist": ["Stomach pain", "Digestive disorders"],
           "Pediatrician": ["Childhood illnesses", "Vaccinations"]
       }
       # Mapping doctor specialties to lists of associated doctor instances
       self.doctors = {
           "Therapist": [therapist1, therapist2],
           "Surgeon": [surgeon1, surgeon2],
           "Gynecologist": [gynecologist1, gynecologist2],
           "Traumatologist": [traumatologist1, traumatologist2],
           "Dentist": [dentist1, dentist2],
           "Infectious Disease Specialist": [infectious1, infectious2],
           "Neurologist": [neurologist1, neurologist2],
           "Cardiologist": [cardiologist1, cardiologist2],
           "Ophthalmologist": [ophthalmologist1, ophthalmologist2],
           "Gastroenterologist": [gastroenterologist1, gastroenterologist2],
           "Pediatrician": [pediatrician1, pediatrician2]


       }


   # Function to display the main menu and handle user inputs
   def display_menu(self):
       # Displaying hospital information
       print("Welcome to our Hospital!")
       print("Schedule of our Hospital:")
       days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
       for day in days:
           print(f"{day}: 8.00-19.00")
       print("24 hour emergency medical assistance")
       print("+7(775)658-91-01")
       print("+7(775)919-91-91")


       while True:
           # Handling user input choices
           print("\nHospital Management System")
           print("1. Record")
           print("2. View all doctors")
           print("3. Exit")
           choice = input("Enter your choice: ")
           # Implementing functionalities based on user choices
           if choice == "1":
               # Recording patient information and scheduling appointment
               print("\nSymptoms:")
               for index, symptom in enumerate(self.departments["Therapy"], start=1):
                   print(f"{index}. {symptom}")
               for index, symptom in enumerate(self.departments["Surgery"], start=len(self.departments["Therapy"]) + 1):
                   print(f"{index}. {symptom}")
               print(f"{len(self.departments['Therapy']) + len(self.departments['Surgery']) + 1}. Other")


               symptom_choice = input("Select your symptom: ")


               try:
                   symptom_choice = int(symptom_choice)
                   if symptom_choice < 1 or symptom_choice > len(self.departments["Therapy"]) + len(self.departments["Surgery"]) + 1:
                       print("Invalid symptom choice. Please try again.")
                       continue
               except ValueError:
                   print("Invalid input. Please enter a number.")
                   continue


               if symptom_choice <= len(self.departments["Pediatrician"]):
                   department_name = "Pediatrician"
                   department_doctors = self.doctors["Pediatrician"]
               elif symptom_choice <= len(self.departments["Therapy"]) + len(self.departments["Surgery"]):
                   department_name = "Surgeon"
                   department_doctors = self.doctors["Surgeon"]
               else:
                   department_name = "Therapist"
                   department_doctors = self.doctors["Therapist"]
                   symptom = "Other"


               if symptom_choice <= len(self.departments["Therapy"]) + len(self.departments["Surgery"]):
                   symptom = self.departments["Therapy"][symptom_choice - 1] if symptom_choice <= len(self.departments["Therapy"]) else \
                           self.departments["Surgery"][symptom_choice - len(self.departments["Therapy"]) - 1]
               else:
                   symptom = input("Enter your symptom: ")


               patient_name = input("Enter your Full Name: ")
               appointment_date = input("Enter appointment date (YYYY-MM-DD): ")


               print("\nWould you like to schedule the appointment?")
               answer = input("Enter 'Yes' or 'No': ").lower()
               if answer == 'yes':
                   print("\nList of Doctors:")
                   for doctor in department_doctors:
                       print(f"Specialty: {department_name}, Full Name: {doctor.full_name}, Experience: {doctor.experience} years")


                   doctor_choice = input("Select your doctor by entering their Full Name: ")
                   for doctor in department_doctors:
                       if doctor.full_name.lower() == doctor_choice.lower():
                           hour = random.randint(8, 19)  # Random hour from 8 to 19
                           minute = random.randint(0, 59)  # Random minute from 0 to 59


                           print(
                               f"Thank you, {patient_name}, you have scheduled an appointment with {doctor.full_name} for {symptom} "
                               f"on {appointment_date} at {hour:02d}:{minute:02d}, Don't be late.")


                           break
                   else:
                       print("Invalid doctor choice. Please try again.")
                       continue
               elif answer == 'no':
                   print("Thank you, bye!")
               else:
                   print("Invalid input. Returning to the main menu.")


           elif choice == "2":
               # Viewing all doctors and their specialties
               print("\nList of Doctors:")
               for specialty, doctors in self.doctors.items():
                   for doctor in doctors:
                       print(f"Specialty: {specialty}, Full Name: {doctor.full_name}, Experience: {doctor.experience} years")


           elif choice == "3":
               # Exiting the program
               print("Exiting...")      # Informing the user about program exit
               break      # Exiting the loop and terminating the program


           else:
               # Handling invalid input
               print("Invalid choice. Please try again.")    # Prompting the user to enter a valid choice
    

if __name__ == "__main__":
   # Creating an instance of the Hospital class and displaying the menu
   hospital = Hospital()
   hospital.display_menu()

