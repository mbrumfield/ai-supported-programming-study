Name: Marcus Brumfield

Date: 10/14/2026

Lab 4 Design Specification
==========================

**Purpose**

This purpose of this program is to calculate the average of a specified course
based on the assignment scores the user enters. The user will select a course
from a given list and enter any number of assignment scores that will be used
for the calculation of the average. The course name, average rounded to two
decimal places, and the letter grade will be displayed on the screen to the
user.

**Inputs**

The program will take the course name and test scores as the inputs. Below are
the details for each input.

| Input          | Data Type | Valid Values                                                                                          | Validation Behavior                                                                                            |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| course\_choice | int       | 1 = CSC 221 - Fundamental Programming I, 2 = MAT 131 - College Algebra, 3 = BIO 111 - General Biology | Display an error message if the user enters a number other than 1-3                                            |
| score1         | double    | 0-100                                                                                                 | Display an error message if a number is out or range or a value other than a number (e.g., char, string, etc.) |
| score2         | double    | 0-100                                                                                                 | Display an error message if a number is out or range or a value other than a number (e.g., char, string, etc.) |
| score3         | double    | 0-100                                                                                                 | Display an error message if a number is out or range or a value other than a number (e.g., char, string, etc.) |
| score4         | double    | 0-100                                                                                                 | Display an error message if a number is out or range or a value other than a number (e.g., char, string, etc.) |
| score5         | double    | 0-100                                                                                                 | Display an error message if a number is out or range or a value other than a number (e.g., char, string, etc.) |

**Processing**

The average will be calculated by adding the four valid test scores and then
divide the total by five (5). Below is the formula to calculate the average.

$average = (score1 + score2 + score3 + score4 + score5) / 5$

Based on the average, the program will check the letter grade with the following
grading scale:

| Average                  | Letter Grade |
| ------------------------ | ------------ |
| average >= 90 and <= 100 | A            |
| average >= 80 and < 90   | B            |
| average >= 70 and < 80   | C            |
| average >= 60 and < 70   | D            |
| average < 60             | F            |

### Problem Statement

In this program, the user will choose a course and enter five valid assignment
scores, where the average will be calculated and display the letter grade.

### Requirements

The user shoud only be able to enter a valid course and each assignment score
has to be within the range of 0-100. Any invalid input should display an error
message and safely end the program.

The user will first display a menu with the courses and corresponding number
choices. If the user enters an input ouside of the choices or a non-numeric
number, an error message will be displayed and the program will end. If the
input is valid, the user will be asked to enter the assignment scores. If any of
the assignment scores are outside of the range of 0-100 or a non-numeric number
is entered, an error message will be displayed and the program will end.

Given the user enters valid input for the course and each of the scores, the
program will then calculate the average. The output will be the course details,
the average rounded by two decimal places, and the letter grade.

### Program Design

**Pseudocode**

* Display the menu for the courses and ask the user to enter a choice using a
  switch statement
  * If the user enters 1, the course variable is set equal to "CSC 221 -
    Fundamental Programming I"
  * If the user enters 2, the course variable is set equal to "MAT 131 - College
    Algebra"
  * If the user enters 3, the course variable is set equal to "BIO 111 - General
    Biology"
  * Any other input, display a meddage stating that the input is invalid and end
    the program
* Ask the user for five scores
  * If any of the scores are non-numeric, display a message that the scores must
    be numeric and end the program
  * If any of the scores are outside the range of 0-100, display a message that
    the scores must be between the range and end the program
  * Otherwise
    * Calcualate the average
      * average = (score1 + score2 + score3 + score4 + score5) / 5
    * Use if-else statements to determine the letter grade specified in the Processing section
    * Display the course, average formatted in two decimal places, and the letter grade

### Language and Enviroment

* C++ 26

### Acceptance Criteria

**Test Cases**

| Test Case | Menu Choice | Score 1 | Score 2 | Score 3 | Score 4 | Score 5 | Course Display | Average | Letter Grade | Test Passed? (Y/N) |
| --------- | ----------- | ------- | ------- | ------- | ------- | ------- | -------------- | ------- | ------------ | ------------------ |
| 1 | 2 | 95 | 88 | 92 | 85 | 90 | MAT 131 - College Algebra | 90 | A | Y |
| 2 | 1	| 75 | 70 | 80 | 72 | 78 | CSC 221 - Fundamental Programming I | 75 | C | Y |
| 3	| 3	| 85 | 90 | 105 | 88 | 92 | BIO 111 - General Biology | N/A | N/A | Y| 
