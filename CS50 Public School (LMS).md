# CS50 Public School (LMS)


I have created a structure of Learning Management System (LMS) of a school as my Final Project.

### Features:
  - The project is based upon **Python**
  - It has **Object Oriented Programming (OOP)** concepts infused.
  - GUI is made through **Tkinter** module
  - Database is managed in SQL language using **sqlite3** module (*i didn't use cs50 training wheel*s ;) )

### How to start program?
In order to start RUN `GUI.py` file.

# Actors:
This software can be used by a School to manage Everything! There are several actors who can perform actions (Like Principal can rusticate you ). Written below are the actions which actors can perform in my program.

## Teacher
Teachers are heart-and-soul of a school. A teacher can;
  - View Attandance of any Student by providing roll no.
  - Assign Students Assignments.
  - Upload Lecture videos for students.
  - Change Password

## Coordinator
Coordinators are literally teachers, They can do everything a teacher can do except;
  - They can't upload a lecture. (obviously,because they don't teach)
  **BUT**;
  - They can watch lectures videos secretly. so that they can ensure the quality of content.


## Principal
Principal is most senior of School. It is somewhat like Co-Ordinator but have some additional methods - or powers so to speak. like;
  - Giving fee-concession to students.
  - Ability to hire new teachers.
  - Ability to fire teachers.
  - Ability to rusticate students from school.

Principal is the super-user thus,its password can not be changed.

## Student
Student is the least complex class in my project. A student can only;

  - Attend Lecture
  - Upload Assignment
  - Pay Fee

This was CS50 <3 
