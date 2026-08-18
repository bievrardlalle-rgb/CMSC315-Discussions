# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

* Create parent and child classes
* Use inheritance to extend functionality
* Understand class and instance namespaces
* Demonstrate shallow and deep copying
* Apply object-oriented design principles

## Requirements

All TODO sections in the source code were completed:

1. Created a parent class.
2. Created a child class using inheritance.
3. Demonstrated class and instance namespaces.
4. Demonstrated shallow and deep copying.
5. Created and tested objects in `main()`.
6. Added a student-created extension.

## Implementation Documentation

I created a `ParentClass` that represented a basic employee and included a class variable, instance variables for the employee's name and ID, a constructor, and a method for displaying employee information.

I created a `ChildClass` that inherited from `ParentClass`. The child class represented an employee working in Information Technology and added a job title and a list of skills. I used `super()` to call the parent constructor and reused the name and employee ID attributes. I also overrode the `display_info()` method and created a `display_skills()` method.

I demonstrated class and instance namespaces by creating multiple child objects, accessing class variables through both the class and an object, adding an attribute to only one object, and displaying the namespaces with `__dict__`.

I demonstrated shallow and deep copying using Python's `copy()` and `deepcopy()` functions. After modifying the nested skills list in the original object, the shallow copy reflected the modification because it shared the nested list. The deep copy remained unchanged because it contained an independent copy of the nested data.

As my student-created extension, I added an `add_skill()` method. The method allowed a new skill to be added to an employee's skills list while preventing duplicate skills from being added.

## Discussion Board Reflection

After completing the programming assignment, add the reflection to the initial discussion post in LEO.

The reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this to managing overhead, practical application development, and future use.

Completing this assignment helped me better understand object-oriented programming concepts such as classes, objects, inheritance, namespaces, and shallow and deep copying. I learned how a child class can inherit attributes and methods from a parent class while also adding or overriding functionality. One challenge I encountered was understanding the difference between shallow and deep copying, especially when working with a nested list. Testing the program and comparing the results helped me understand that a shallow copy can share nested data with the original object, while a deep copy creates independent data.

Compared with procedural programming, OOP organizes a program around objects that combine data and related behaviors, while procedural programming focuses more on functions and a sequence of steps. I can see how OOP can make larger applications easier to organize and modify. Reusable classes also reduce the need to duplicate code, which can lower development and maintenance overhead. In practical application development, this can make programs easier to expand, troubleshoot, and update. These concepts will be useful in future projects because I can reuse existing classes and extend them as application requirements change.
