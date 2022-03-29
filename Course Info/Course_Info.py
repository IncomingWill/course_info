# Title: Course Info
# Program created by William Schaeffer
# CPS 313
# P. 517, Exercise 1, Course Info Program
# 03.01.22

# This program will create a dictionary containing course numbers, room numbers, instructor name, and meeting times.

# imports for functions

import sys                                          # For Command-Line Args

# Main Function

def main():
    
    # initialize dictionaries, course number will be dictionary key
        # room number, instructor name, and meeting times will be dictionary value
    room_number_dict = {"CS101":3004, "CS102":4501, "CS103":6755, "NT110":1244, "CM241":1411}
    instructor_name_dict = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}
    meeting_time_dict = {"CS101":"8:00 AM", "CS102":"9:00 AM", "CS103":"10:00 AM", "NT110":"11:00 AM", "CM241":"1:00 PM"}
    
    course_number = ""                              # initialize user input for course number for dictionary searches

    course_number = sys.argv[1]                    # intialize user input for course number via command line

    #course_number = input('Please enter the course number with appropriate case for aplhabetical characters: ')

    while course_number not in room_number_dict:    # test for course_number in dictionary
        course_number = input('Entered course number not found. Please re-enter course number with appropriate case: ')
    
    # grab appropriate dictionary values to display from each dictionary
    room_number = room_number_dict.get(course_number)
    instructor_name = instructor_name_dict.get(course_number)
    meeting_time = meeting_time_dict.get(course_number)

    print(f'Course {course_number} is in room number {room_number} with instructor {instructor_name} at {meeting_time}')

main()                                              # call main function

