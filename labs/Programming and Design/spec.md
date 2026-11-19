Review this specification.

Grade calculator
================

This program calculates a student's average and letter grade from five test
scores in a selected course.

Inputs
------

* Course: selected from the following list:
  * CSC 221 - Fundamental Programming I
  * MAT 131 - College Algebra
  * BIO 111 - General Biology
* Five test scores, each a number from 0 to 100.
* A "Reset" button.

Invalid inputs: a score outside 0-100 is clamped to the nearest limit (0 or
100) when its field loses focus.

Processing
----------

* When a score is committed, compute the average of the entered scores, rounded
  to one decimal place.
* Determine the letter grade from the average using this scale:
  * 90 – 100 = A
  * 80 – <90 = B
  * 70 – <80 = C
  * 60 – <70 = D
  * Below 60 = F
* When no scores are entered, no average or letter grade is computed.
* Out-of-range scores are clamped (see Inputs) before being used in the
  calculation.
* The "Reset" button clears all input.

Outputs
-------

* The average, rounded to one decimal place.
* The letter grade.
* When no scores are entered, display nothing for either output.

User interface
--------------

* The available courses are in a dropdown selector.
* Each score has its own numeric input component. They are arranged vertically
  and labeled "Score 1", "Score 2", etc.
* The average is placed below the last score, as "Average: \<numeric grade>".
* The letter grade is placed below the average, as "Letter grade: \<letter>".

Implementation
--------------

Implement this program in JavaScript, HTML5, and CSS3.
