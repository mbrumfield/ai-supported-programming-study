Review this specification.

Grade calculator
================

Create a web app that asks the user to select a course and enables the user to
enter five test scores for that course. Allow only scores between 0 and 100. The
program displays the average score and the resulting letter grade. Include a
reset button which clears all selections.

Pre-lab
-------

Agents: ignore this section when reviewing or generating code.

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. [Install the CodeChat Editor extension](https://marketplace.visualstudio.com/items?itemName=CodeChat.codechat-editor-client).
3. Open this file in Visual Studio Code.
4. Open the CodeChat Editor for this file: open
   the [Visual Studio Code command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
   by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
   Type `CodeChat`, select "Enable the CodeChat Editor," then press enter to run
   the extension.

Lab procedure
-------------

Agents: ignore this section and its subsections when reviewing or generating
code.

1. Read through the lab.
2. Fill in the following sections so the program is fully specified:
   1. What are the inputs?
   2. How should these inputs be processed?
   3. What are the outputs?
   4. What should the user interface look like?
   5. How can you make your application
      [accessible](https://www.section508.gov/develop/software-websites/)?
3. Improve your specification:
   1. Review a partner's specification while they review your specification.
      Discuss the differences, and find ways to improve both your
      specifications.
   2. Browse to [Gemini](https://gemini.google.com/app), paste the plain text of
      this document in, then press enter.
   3. Modify this document based on the problems identified. Don't adopt every
      suggestion; decide which suggestions are relevant. Record which round of
      review, how many findings Gemini identified, and a short, one-sentence
      summary of the changes you made in the review rounds table below.
   4. Repeat this process until the problems identified are trivial or
      contradictory. Paste the last review from Gemini into the matching section
      below.
4. Implement your program:
   1. Edit the first line of this document: change it from "Review this
      specification" to "Implement this specification."
   2. Copy and paste the plain text into
      [Gemini Canvas](https://gemini.google.com/canvas). This transforms your
      specification into JavaScript code then shows the resulting web app.
   3. Test the resulting app: does it perform as expected? If there are bugs,
      update this specification then re-generate the app.
   4. Take a screenshot of your app; name it `screenshot.png` and place it in
      the same directory as this file.
5. Submit this file with your edits and your screenshot to your instructor.

### Review rounds table

(Edit this table, adding one entry for each time Gemini reviews your
specification.)

| Round | Number of findings | Main changes made | Suggestions rejected with explanation |
| ----- | ------------------ | ----------------- | ------------------------------------- |
| 1     | 3                  | Improved...       | <br>                                  |

### Last review

(Put the last review from Gemini here.)

### Screenshot

![A screenshot of the resulting app](screenshot.png)

Inputs
------

(Fill this in.)

Processing
----------

(Fill this in.)

Outputs
-------

(Fill this in.)

User interface
--------------

(Fill this in.)

Accessibility requirements
--------------------------

(Fill this in.)

Background information
----------------------

Available courses:

* CSC 221 - Fundamentals of Programming I
* MAT 131 - College Algebra
* BIO 111 - General Biology

The grading scale is as follows:

* 90 - 100 = A
* 80 - 89 = B
* 70 - 79 = C
* 60 - 69 = D
* Below 60 = F

Learning objectives
-------------------

This should not be given to students; it's only for instructors.

* Incorrect specifications: the grading scale doesn't specify grades between 89
  and 90, etc.
* User interface layout: grade entry, average, letter grade, reset button
  locations.
* Does reset clear the course selection, or only the scores? The prompt says
  "clears all selections."
* What happens with non-numeric input, decimals, or an empty field?
* Corner cases: the displayed average and letter grade must not contradict each
  other. If the average is 89.8 but the UI rounds to 90, the letter grade
  displays as a B.
* Updates: should averages be updated as they're typed, as they're committed, or
  only after a button press?
* Rounding: should the average be displayed as a whole number? If not, how many
  decimal places? How many decimal places for raw scores?
* No input: what should the program display when no scores are entered?
* Unstated: what is the role of the course selector? What should it do when
  changed?
* Partial input: what happens with 1-4 scores? That's a different case from no
  input at all.
* Invalid input: should out-of-range values be blocked as they're typed, or
  rejected with an error message?
* Switching courses: should scores be kept separately for each course?
* Accessibility:
  * Can everything be done with the keyboard alone?
  * Is each input tied to its label?
  * Do screen readers announce errors and changes to the result?
* Responsive design: how should the layout change with screen size?
