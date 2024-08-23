# import csv library
import csv

#Create empty lists for the various attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst

# look at the data in insurance_csv_dict
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientInfo:
    #inicializamos todas las variables para un sujeto
    def __init__(self,patients_ages,patients_sexes,
                 patients_bmis,patients_num_children,
                 patients_smoker_statuses,patients_regions,
                 patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges  
        
    #calcular la media de todas las edades en el archivo insurance.csv
    def analyze_ages(self):
        #inicializamos una variable para ir guardando la suma de todas las edades
        total_age =  0
        #iteramos en cada una de las edades y la sumamos a total_ages
        for age in self.patients_ages:
            total_age += int(age)
            #imprimimos la media de las edades del archivo
        return print("The Average of ages is: " + str(round(total_age/len(self.patients_ages), 2)) + " years.")
    
    # method that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):
        # initialize number of males and females to zero
        females = 0
        males = 0
        # iterate through each sex in the sexes list
        for sex in self.patients_sexes:
            # if female add to female variable
            if sex == 'female':
                females += 1
            # if male add to male variable
            elif sex == 'male':
                males += 1
        # print out the number of each
        print("Count for female: ", females)
        print("Count for male: ", males)    

    def unique_regions(self):
        #creamos una lista para ir guardando todas las nacionalidades
        unique_regions = []
        #iteramos entre las regiones y las vamos guardando en la lista solo si no han aparecido antes
        for regions in self.patients_regions:
            if regions not in unique_regions:
                unique_regions.append(regions)
        return unique_regions
            
    def average_charges(self):
        #creamos una lista para ir sumando todas las charges
        total_charges = 0
        #iteramos entre todas las charges
        for charge in self.patients_charges:
            total_charges += float(charge)
        return print("The average of the charges is: " + str(round(total_charges/len(self.patients_charges), 2)) + " dollars.")
            
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["ages"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return print(self.patients_dictionary)
    
    
patient_info = PatientInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

patient_info.analyze_ages()
patient_info.analyze_sexes()
patient_info.unique_regions()
patient_info.average_charges()
patient_info.create_dictionary()

            