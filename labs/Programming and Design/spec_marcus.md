Lab 4 Design Specification
==========================

Name: Marcus Brumfield Date: 11/16/2026

Purpose
-------

The purpose of this program is to calculate the average of a specified course
based on the assignment scores the user enters. The user will select a course
from a given list and enter up to five assignment scores to calculate the
average. The course name, average rounded to two decimal places, and letter
grade will be displayed on the screen.

Inputs
------

| Input            | Data Type          | Valid Values                                                                              | Validation Behavior                                                                                      |
| ---------------- | ------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Course Selection | Dropdown Selection | CSC 221 - Fundamental Programming I, MAT 131 - College Algebra, BIO 111 - General Biology | Display an error message if no course is selected. Prevent calculation until a valid course is selected. |
| score1 - score5  | Number             | 0-100                                                                                     | Catch cases where a number is out of range or is not a number (e.g., char, string, etc.)                 |

Processing
----------

### Average Calculation

The average is calculated by adding the valid test scores, then dividing the
total by the number of scores entered. Below is an example formula to calculate
the average.

<strong>Formula:</strong>

```text
average = (sum of all scores)/(number of scores)
```

Based on the average, the program will check the letter grade with the following
grading scale:

| Average  | Letter Grade |
| -------- | ------------ |
| 90-100   | A            |
| 80-89.99 | B            |
| 70-79.99 | C            |
| 60-69.99 | D            |
| Below 60 | F            |

### Business Rules

1. At least one valid score must be entered before calculating an average.
2. Blank score fields are ignored and are not included in the average
   calculation.
3. The average must be displayed with exactly two decimal places.
4. Only valid scores are included in calculations.
5. The letter grade is determined from the calculated average.

Outputs
-------

The application will display:

* Selected course name
* Assignment scores entered
* Average rounded to two decimal places
* Letter grade
* Validation messages (when applicable)

Requirements
------------

### User Interface Requirements

* Provide a dropdown list containing the available courses.
* Provide five score input fields.
* Provide a Calculate Average button.
* Provide a Reset button that clears all fields and results.
* Provide a Save to CSV button.
  * The file name should be YYYY-MM-DD\_CourseSelection.csv

### Validation Requirements

* A course must be selected from the dropdown before the average can be
  calculated. If no course is selected, display a validation message and prevent
  calculation.
  * Initial state: "Select a Course" (this should not be treated as a valid
    option)
* Score values must be numeric.
* Score values must be between 0 and 100 inclusive.
* Invalid fields must display a visual indicator and an explanatory message.
* The application must prevent calculation when invalid data exists.

### Functional Requirements

When the user selects a valid course and enters one or more valid scores:

1. Calculate the average when the user selects the Calculate Average button
2. Round the average to two decimal places.
   * Display the average rounded to two decimal places using standard rounding.
3. Determine the letter grade.
4. Display the course name, average, and letter grade.
5. Allow the results to be exported to a CSV file containing the following
   columns:
   * Course Name
   * Score 1
   * Score 2
   * Score 3
   * Score 4
   * Score 5
   * Average
   * Letter Grade
6. Any input left blank by the user should have a blank value in the CSV.

Technology Stack
----------------

* Language: JavaScript
* Markup: HTML5
* Styling: CSS3

Folder Structure
----------------

```text
Lab4Project/
│
├── index.html
├── style.css
└── main.js
```

Review rounds table
-------------------

| Round | Number of findings | Main changes made                                                                                                                                                                                                                                                                                                                                                                       | Suggestions rejected with explanation                                                                                                                                                                                                                                                                                   |
| ----- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 10                 | Fixed Markdown formatting; reorganized sections; added Outputs section; clarified average calculation; added minimum-score requirement; clarified handling of blank score fields; made grade ranges explicit; expanded validation requirements; added UI requirements; clarified rounding behavior; added business rules and functional workflow; improved folder structure formatting. | None. All identified findings were incorporated into the revised specification.                                                                                                                                                                                                                                         |
| 2     | 8                  | Specified the functional requirements to add a Calculate Average button; Added the specification of using Math.round() for calculating the average; Updated the course selection text to refelct the dropdown functionality; Added the CSV file name structure                                                                                                                          | 4: Average formula formatting is broken; Missing output format examples; Technology Stack section is incomplete; Folder structure formatting is not Markdown-friendly. These suggestions were rejected because The format does not appear to be broken and the suggestions are more superficial than implemtaton-based. |
| 3     | 4                  | Updated rounding requirement; Added bullet point for UI for the dropdown list; Updated Technology Stack section; Specified the CSV format                                                                                                                                                                                                                                               | None. All identified findings were incorporated into the revised specification.                                                                                                                                                                                                                                         |
