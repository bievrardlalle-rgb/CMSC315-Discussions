"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "Employee"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    department = "Information Technology"

    def __init__(self, name, employee_id, job_title, skills):
        super().__init__(name, employee_id)
        self.job_title = job_title
        self.skills = skills

    def display_info(self):
        return (
            f"Name: {self.name}, Employee ID: {self.employee_id}, "
            f"Job Title: {self.job_title}, Department: {self.department}"
        )

    def display_skills(self):
        return f"{self.name}'s skills: {', '.join(self.skills)}"

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            return f"{skill} added successfully."
        return f"{skill} is already listed."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    employee1 = ChildClass(
        "Alex", 101, "Software Developer", ["Python", "Java"]
    )

    employee2 = ChildClass(
        "Jordan", 102, "IT Specialist", ["Networking", "Security"]
    )

    # Access a class variable through the class.
    print("Class variable through class:", ChildClass.department)

    # Access the same class variable through an object.
    print("Class variable through object:", employee1.department)

    # Add an attribute to only one object.
    employee1.certification = "Security+"

    # Display each object's instance namespace.
    print("Employee 1 namespace:", employee1.__dict__)
    print("Employee 2 namespace:", employee2.__dict__)

    # Display information about the class namespace.
    print("Child class namespace:", ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Taylor", 103, "Systems Administrator",
        ["Python", "Linux", "Networking"]
    )

    # Create a shallow copy and a deep copy.
    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # Modify nested mutable data in the original object.
    original.skills.append("Cloud Computing")

    # A shallow copy shares the nested skills list with the original,
    # so the change appears in both objects.
    # A deep copy creates an independent copy of the nested list,
    # so the change does not appear in the deep copy.

    print("Original skills:", original.skills)
    print("Shallow copy skills:", shallow_copy.skills)
    print("Deep copy skills:", deep_copy.skills)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.

# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    parent = ParentClass("Chris", 100)
    print(parent.display_info())

    print("\nTODO: Create and test your child object")
    child = ChildClass(
        "Morgan", 200, "Cybersecurity Analyst",
        ["Python", "Networking", "Cybersecurity"]
    )

    # Demonstrate the overridden method inherited from the parent structure.
    print(child.display_info())

    # Demonstrate the new method created in the child class.
    print(child.display_skills())

    # Test the student-created extension.
    print(child.add_skill("Cloud Computing"))
    print(child.display_skills())

    # Test duplicate skill handling.
    print(child.add_skill("Cloud Computing"))


if __name__ == "__main__":
    main()