class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

#Trainee class extends Person class
class Trainee(Person):
    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications):
        super().__init__(name, age, email)#call parent class constructor
        self.batch_id = batch_id
        self.marks = marks
        self.num_projects = num_projects
        self.num_publications = num_publications

    def display_info(self):
        super().display_info()
        print(f"Batch: {self.batch_id}")
        print(f"Marks: {self.marks}")
        print(f"Avg: {sum(self.marks)//len(self.marks)}")
        print(f"Projects: {self.num_projects} | Publications: {self.num_publications}")


class SDETTrainee(Trainee):
    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications, tool_proficiency):
        #call parent(Person) class constructor 
        super().__init__(name, age, email, batch_id, marks, num_projects, num_publications)
        self.tool_proficiency = tool_proficiency

    def compute_aggregate(self):
        avg_marks = sum(self.marks)/len(self.marks)
        aggregate = (avg_marks * 0.6) + (self.num_projects * 5) + (self.num_publications * 3)
        return aggregate
    
    def display_info(self):
        super().display_info()
        print("Tool: ",self.tool_proficiency)

SDET = SDETTrainee("Myl", 21, "mugan@example.com", "B21", [85, 90, 88], 3, 2, "Selenium")
SDET.display_info()
print("Aggregate:", SDET.compute_aggregate())
