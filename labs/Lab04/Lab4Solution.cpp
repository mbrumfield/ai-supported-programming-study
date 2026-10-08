/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std; 
#include <iomanip>

int main()
{
    double score1, score2, score3, score4, score5, average; 
    char lettergrade;
    int course_choice; 
    string course; 
    
    // Display the menu and ask the user to select the course
    cout << "Average and Letter Grade Calculator\n" << endl; 
    cout << "Course Selection" << endl; 
    cout << "1.) CSC 221" << endl; 
    cout << "2.) MAT 131" << endl; 
    cout << "3.) BIO 111\n" << endl; 
    
    cout << "Enter the course to calcuate the average: "; 
    cin >> course_choice; 
    
    // Store the full name of the course based on the user's input
    switch (course_choice)
    {
        case 1: 
            course = "CSC 221 - Fundamental Programming I"; 
            break; 
        case 2:
            course = "MAT 131 - College Algebra"; 
            break;
        case 3:
            course = "BIO 111 - General Biology"; 
            break;
        default: 
            cout << "\nInvalid selection. Exiting the program.";
            return 0;
            break; 
    }
    
    // Ask the user to enter five scores
    cout << "Enter Assignment Score 1: "; 
    cin >> score1;
    
    cout << "Enter Assignment Score 2: "; 
    cin >> score2; 
    
    cout << "Enter Assignment Score 3: "; 
    cin >> score3; 
    
    cout << "Enter Assignment Score 4: "; 
    cin >> score4;
    
    cout << "Enter Assignment Score 5: "; 
    cin >> score5; 
    
    // Validate the scores in the range
    if ((score1 < 0 || score1 > 100) || 
        (score2 < 0 || score2 > 100) ||
        (score3 < 0 || score3 > 100) ||
        (score4 < 0 || score4 > 100) ||
        (score5 < 0 || score5 > 100)) {
            cout << "\nInvalid test scores: must be between 0 and 100.";
        }
    else {
        // Calculate the average
        average = (score1 + score2 + score3 + score4 + score5) / 5.0;
        
        // Get the letter letter grade 
        if (average >= 90)
            lettergrade = 'A'; 
        else if (average >= 80)
            lettergrade = 'B'; 
        else if (average >= 70)
            lettergrade = 'C';
        else if (average >= 60)
            lettergrade = 'D';
        else
            lettergrade = 'F';
            
        //
        cout << fixed << setprecision(2); 
        
        // Display the course name, average,  and letter grade
        cout << "\nCourse: " << course << endl; 
        cout << "Average: " << average << endl; 
        cout << "Letter Grade: " << lettergrade << endl; 
    }

    return 0;
}