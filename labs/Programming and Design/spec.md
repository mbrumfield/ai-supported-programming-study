Specification
=============

Create a program that asks the user to select the course for which they want to
calculate the average and enables the user to enter 5 test scores.

* Scores outside 0-100 are clamped to the nearest limit when the field loses
  focus.
* The average and letter grade update when a score is committed; when no scores
  are entered, display nothing.
* The average is rounded to one decimal place.
* A "Reset" button clears all input.

Available courses:

* CSC 221 - Fundamental Programming I
* MAT 131 - College Algebra
* BIO 111 - General Biology

The grading scale is as follows:

* 90 – 100 = A
* 80 – <90 = B
* 70 – <80 = C
* 60 – <70 = D
* Below 60 = F

UI
--

* The available courses are in a dropdown selector.
* Each score has its own numeric input component. They are arranged vertically and
  labeled "Score 1", "Score 2", etc.
* The average is placed below the last score, as "Average: \<numeric grade>".
* The letter grade is placed below the average, as "Letter grade: \<letter>".
