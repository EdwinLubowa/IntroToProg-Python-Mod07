# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
# Edwin Kintu-Lubowa,11/23/2024,Created Script
# Edwin Kintu-Lubowa,11/24/2024,Updated FileProcessor methods to handle file objects
# ------------------------------------------------------------------------------------------- #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Data --------------------------------------------------------------------------------------- #

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class Person:
    """
    A class representing person data

    Properties:
    - first_name (str): The student's first name
    - last_name (str): The student's last name

    ChangeLog: (Who, When, What)
    Edwin Kintu-Lubowa,11/23/2024,Created the class.
    """

    # Create a constructor with private attributes for the first_name and last_name data
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    # Create property getter and setter for first name using the same code as in the Student class
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()   # formatting code

    @first_name.setter  # (use this decorator for the setter or mutator)
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("First name should not contain numbers!")

    # Create property getter and setter for last name using the same code as in the Student class
    @property  # (Use this decorator for the getter or accessor)
    def last_name(self):
        return self.__last_name.title()   # formatting code

    @last_name.setter  # (use this decorator for the setter or mutator)
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("Last name should not contain numbers!")

    # Add code to inherit code from the person class
    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Student(Person):
    """
       A class representing student data

       Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): course name student's enrolled in

       ChangeLog: (Who, When, What)
       Edwin Kintu-Lubowa,11/23/2024,Created Class
       Edwin Kintu-Lubowa,11/23/2024,Added properties and private attributes
       Edwin Kintu-Lubowa,11/23/2024,Moved first_name and last_name into parent class
       """

    # Create a constructor with private attributes for the first_name, last_name ,and course name data
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    @property  # (Use this decorator for the getter or accessor)
    def course_name(self):
        return self.__course_name.title()   # formatting code

    @course_name.setter  # (use this decorator for the setter or mutator)
    def course_name(self, value: str):
        self.__course_name = value

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course_name}"



# Processing ---------------------------------------------------------------------------------- #
class FileProcessor:
    """
        A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created Class
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries
        """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
                 This function reads data from a json file and loads it into a list of dictionary rows

                ChangeLog: (Who, When, What)
                Edwin Kintu-Lubowa,11/23/2024,Created function
                Edwin Kintu-Lubowa,11/24/2024,Converted list of dictionaries to list of student objects

                :param file_name: string data with name of file to read from
                :param student_data: list of dictionary rows to be filled with file data

                :return: list
                """
        try:
            file = open(file_name, "r")

            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)

            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

        # I will not be using the code below; it does not handle student objects
        # try:
        #     file = open(file_name, "r")
        #     student_data = json.load(file)
        #     file.close()
        # except Exception as e:
        #     IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        #
        # finally:
        #     if file.closed == False:
        #         file.close()
        # return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
                This function writes data to a json file with data from a list of dictionary rows

                ChangeLog: (Who, When, What)
                Edwin Kintu-Lubowa,11/23/2024,Created function
                Edwin Kintu-Lubowa,11/24/2024,Converted code to use student objects instead of dictionaries

                :param file_name: string data with name of file to write to
                :param student_data: list of dictionary rows to be writen to the file

                :return: None
                """
        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()

        # I will not be using the code below; it does not handle student objects
        # try:
        #     file = open(file_name, "w")
        #     json.dump(student_data, file)
        #     file.close()
        #     IO.output_student_and_course_names(student_data=student_data)
        # except Exception as e:
        #     message = "Error: There was a problem with writing to the file.\n"
        #     message += "Please check that the file is not open by another program."
        #     IO.output_error_messages(message=message,error=e)
        # finally:
        #     if file.closed == False:
        #         file.close()


# Presentation -------------------------------------------------------------------------------- #
class IO:
    """
        A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created Class
        RRoot,1.2.2030,Added menu output and input functions
        RRoot,1.3.2030,Added a function to display the data
        RRoot,1.4.2030,Added a function to display custom error messages
        Edwin Kintu-Lubowa,11/24/2024,Converted methods to use student objects instead of dictionaries
        """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
                This function gets the first name, last name, and GPA from the user

                ChangeLog: (Who, When, What)
                Edwin Kintu-Lubowa,11/23/2024,Created function
                Edwin Kintu-Lubowa,11/23/2024,Converted code to use student objects instead of dictionaries

                :param student_data: list of dictionary rows to be filled with input data

                :return: list
                """
        try:
            # Input the data
            student = Student()
            student.first_name = input("What is the student's first name? ")
            student.last_name = input("What is the student's last name? ")
            student.course_name = input("Please enter the name of the course: ")
            student_data.append(student)
            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

        # I will not be using this it of code; validation and error handling performed in the Data layer
        # try:
        #     student_first_name = input("Enter the student's first name: ")
        #     if not student_first_name.isalpha():
        #         raise ValueError("The last name should not contain numbers.")
        #     student_last_name = input("Enter the student's last name: ")
        #     if not student_last_name.isalpha():
        #         raise ValueError("The last name should not contain numbers.")
        #     course_name = input("Please enter the name of the course: ")
        #     student = {"FirstName": student_first_name,
        #                     "LastName": student_last_name,
        #                     "CourseName": course_name}
        #     student_data.append(student)
        #     print()
        #     print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        # except ValueError as e:
        #     IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        # except Exception as e:
        #     IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        # return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":  # End the program
        break  # out of the while loop

    # I will not be using the code below, processing performed by input_menu_choice() function
    # elif menu_choice == "4":
    #     break  # out of the loop
    # else:
    #     print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")

#Exiting the program gracefully
input("\nPausing until you use the Enter key...\n")
