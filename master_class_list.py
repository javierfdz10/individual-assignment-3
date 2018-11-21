# -*- coding: utf-8 -*-

#%%
#
#Create a Student class that has the following attributes:
#name
#last name
#age
#master (either MCSBT or MDBI)
# Make sure you parametrize all those fields in the constructor.
 
#%%
 
class Student:     
    
    def __init__(self, name, last_name, age, master):     
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
        
tancredi = Student("Tancredi", "Bernard Lita Modignani", "21", "MCSBT")


#%%

#Add a print_student method in the Student class that prints a line like 
# follows for the object:
#
#Pepe García is a 55 year old student of the MCSDBI masters programme
#
#Create a list of all 28 Students representing all students in this class.  
#Then iterate over all of them and call print_student on each one to 
#print its description.
 
class Student:
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
   
class Master:
    
    master_students = []
    
    def __init__(self, name):
        self.name = name
                
    def add_master_students_list(self, master_students_list):
        self.master_students += master_students_list
        
    def print_student(self):
        for student in self.master_students:      
            print(student.name + " " + student.last_name + " is a "+ student.age + " years old student of the " + student.master + " masters program")      
         
mcsbt_mdbi = Master("MCSBT & MDBI")

master_students_list = [
                        Student('Alejandro', 'Meneses', '27', 'MCSBT'),
                        Student('Agata', 'Kaczmarek', '31', 'MDBI'),
                        Student('Anastasia', 'Lasunina', '25', 'MDBI'),
                        Student('Anikken', 'Barstad Gjeruldsen', '27', 'MDBI'),
                        Student("Arthur", "Maroquene-Froissart", "23", "MCSBT"),
                        Student('Candela', 'Noya', '24', 'MDBI'),
                        Student('Daniil', 'Osipov', '21', 'MDBI'),
                        Student('David', 'Barrero González', '31', 'MCSBT'),
                        Student('Edem', 'Francois', '28', 'MCSBT'),
                        Student('Eduardo', 'Paraja', '23', 'MDBI'),
                        Student('Felix', 'Fastrich', '23', 'MDBI'),
                        Student('Florian', 'Diegruber', '25', 'MCSBT'),
                        Student('Hannah', 'Oldorf', '23', 'MCSBT'),
                        Student('Isabella', 'Rosenthal', '27', 'MDBI'),
                        Student('Javier', 'Fernández Iglesias', '24', 'MCSBT'),
                        Student('Julie', 'De Neys', '23', 'MDBI'),
                        Student('Lukas', 'Hauser', '28', 'MDBI'),
                        Student('Leila', 'Tazi', '27', 'MCSBT'),
                        Student('Laura', 'Kageneck', '23', 'MCSBT'),
                        Student('Marius', 'Diedrich', '23', 'MDBI'),
                        Student('Monica', 'Alvarenga', '28', 'MDBI'),
                        Student('Natalie', 'Cedeño', '26', 'MDBI'),
                        Student('Octavio', 'Ramírez', '28', 'MDBI'),
                        Student('Tancredi', 'Bernard Lita Modignani', '21', 'MCSBT'),
                        Student('Thibault', 'Moeyersoms', '21', 'MDBI'),
                        Student('Yasmine', 'Lyagoubi', '23', 'MDBI'),
                        Student('Zineb', 'Mezzour', '22', 'MCSBT')
                        ]

mcsbt_mdbi.add_master_students_list(master_students_list)

mcsbt_mdbi.print_student()