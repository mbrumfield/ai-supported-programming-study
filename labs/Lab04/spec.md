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

* The available courses are in a Select component.
* Each score has its own InputNumber component. They are arranged vertically and
  labeled "Score 1", "Score 2", etc.
* The average is placed below the last score, as "Average: \<numeric grade>".
* The letter grade is placed below the average, as "Letter grade: \<letter>".

Test cases
----------

| Score 1 | Score 2 | Score 3 | Score 4 | Score 5 | Course                              | Average | Letter Grade | Note |
| ------- | ------- | ------- | ------- | ------- | ----------------------------------- | ------- | ------------ | ---- |
| 95      | 88      | 92      | 85      | 90      | MAT 131 - College Algebra           | 90      | A            |      |
| 75      | 70      | 80      | 72      | 78      | CSC 221 - Fundamental Programming I | 75      | C            |      |
| 80      | 90      | 105     | 87      | 92      | BIO 111 - General Biology           | 89.8    | B            | 1    |
| (blank) | (blank) | (blank) | (blank) | (blank) | CSC 221 - Fundamental Programming I | (blank) | (blank)      |      |
| 85      | (blank) | 90      | (blank) | 78      | MAT 131 - College Algebra           | 84.3    | B            | 2    |
| (blank) | (blank) | (blank) | (blank) | 64      | BIO 111 - General Biology           | 64      | D            | 2    |
| 70      | -50     | 80      | 75      | 85      | CSC 221 - Fundamental Programming I | 72      | C            | 3    |
| 88      | abc     | 92      | 79      | 85      | MAT 131 - College Algebra           | 86      | B            | 4    |
| 8x5     | 90      | 78      | 82      | 88      | BIO 111 - General Biology           | 84.6    | B            | 5    |
| 55      | 62      | 48      | 70      | 51      | CSC 221 - Fundamental Programming I | 57.2    | F            |      |

"(blank)" means the score is left empty or, in the Average and Letter Grade
columns, that nothing is displayed.

Notes:

1. The InputNumber component changes the 105 to 100, making the average lower
   than what the values suggest.
2. Blank scores are excluded from the average.
3. The InputNumber component rejects the minus sign when its minimum is 0, so
   typing -50 produces 50.
4. The InputNumber component ignores non-numeric keystrokes, so typing abc
   leaves the score empty; it is then excluded from the average.
5. The InputNumber component ignores non-numeric keystrokes, so typing 8x5
   produces 85.

Implementation
--------------

* TypeScript
* Vue.js using the Composition API.
* PrimeVue v4 for controls
