Grade calculator
================

Create a program that asks the user to select a course and enables the user to
enter five test scores for that course. Allow only scores between 0 and 100. The
program displays the average score and the resulting letter grade. Include a
reset button which clears all selections.

Available courses:

* CSC 221 - Fundamental Programming I
* MAT 131 - College Algebra
* BIO 111 - General Biology

Grading scale is as follows:

* 90 - 100 = A
* 80 - 89 = B
* 70 - 79 = C
* 60 - 69 = D
* Below 60 = F

Implementation
--------------

* TypeScript.
* Vue.js using the Composition API.
* [PrimeVue v4 components](https://primevue.dev/components/).
* Use the
  [PrimeVue Playground v4 on StackBlitz](https://stackblitz.com/edit/primevue-4-ts-vite-issue-template-sqfbbp).
  Upload the LLM-generated `src/main.ts` and `src/App.vue` there.

Assignment
----------
> "The model's job is to produce something plausible. Your job is to make sure
> only one thing is plausible." -- Claude

Tighten this specification to produce one plausible result.

Learning objectives
-------------------

* Incorrect specifications: the grading scale doesn't specify grades between 89
  and 90, etc.
* User interface layout: grade entry, average, letter grade, reset button
  locations.
* Validation: select correct UI components for validation.
* Corner cases: if the average is 89.99, the UI rounds to 90, but the letter
  grade is B.
* Updates: should averages be updated as they're typed, as they're committed, or
  only after a button press?
* Test: students should develop additional test cases.
* Rounding: should the average be displayed as a whole number? If not, how many
  decimal places? How many decimal places for raw scores?
* No input: what should the program display when no scores are entered?
* Unstated: what is the role of the course selector? What should it do when
  changed?
* Accessibility:
  * Can everything be done with the keyboard alone?
  * Is each input tied to its label?
  * Do screen readers announce errors and changes to the result?
* Responsive design: how should the layout change with screen size?
