/****************************************************************/
/*** Title:  Weighted Average Calculator                      ***/
/*** Course: Computational Problem Solving 1  (CPET 121)      ***/
/*** Developer: Hector Garcia (Computer Engineering Tech)     ***/
/*** Date: 9/13/2022                                          ***/
/*** Description: Program that calculates a student’s         ***/
/***    final course average based on grades from homeworks   ***/
/***    labs, term papers, midterm, final and class           ***/
/***    participation.                                        ***/
/****************************************************************/

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    float homework, lab, midTerm, final;
    char termPaper;
    /* boolean because its either a one or zero */
    bool participation;
    float hw1, hw2, hw3, hw4, lab1, lab2, lab3, lab4;

    /*   User inputs grades accordingly */
    cin >> hw1>>hw2>>hw3>>hw4;
    cin >> lab1>>lab2>>lab3>>lab4;
    cin >> midTerm;
    cin >> final;
    cin >> termPaper;
    cin >> participation;
    
    /* calculating averages for homework and lab scores */
    homework = (hw1 + hw2 + hw3 + hw4)/4;
    lab = (lab1 + lab2 + lab3 + lab4)/4;

    /* int for the score of the term paper so it's easier to output later on */
    int termPaperGrade;

    switch(termPaper){

    case 'A'  :
    case 'a'  : termPaperGrade = 95;
                break;
    case 'B'  :
    case 'b'  : termPaperGrade = 85;
                break;
    case 'C'  :
    case 'c'  : termPaperGrade = 75;
                break;
    case 'D'  :
    case 'd'  : termPaperGrade = 65;
                break;
    case 'F'  :
    case 'f'  : termPaperGrade = 55;
                break;
    default   : termPaperGrade = 0;

    }

    if (participation == true){
        participation = 1;
    }
    else{
        participation = 0;
    }

    /*Numeric Constants for percentages(weighting factors)*/
    const double HOMEWORK_PERC = 0.1;
    const double LAB_PERC = 0.2;
    const double MIDTERM_PERC = 0.25;
    const double FINAL_PERC = 0.25;
    const double TERMPAPER_PERC = 0.15;
    const double PARTICIPATION_PERC = 0.05;

    float ParticipationGrade;

    homework *= HOMEWORK_PERC;
    lab *= LAB_PERC;
    midTerm *= MIDTERM_PERC;
    final *= FINAL_PERC;
    termPaperGrade *= TERMPAPER_PERC;
    ParticipationGrade = participation * PARTICIPATION_PERC;

    float finalAverage = homework + lab + midTerm + final + termPaperGrade + participation;

    /* char to store final course lettee grade */
    char finalLetterGrade;
 
    if (finalAverage >= 93.0){
        finalLetterGrade = 'A';
    }
    else if (finalAverage >= 90.0 && finalAverage < 93.0 ){
        finalLetterGrade = 'A-';
    }
    else if (finalAverage >= 87.0 && finalAverage < 90.0 ){
        finalLetterGrade = 'B+';
    }
    else if (finalAverage >= 83.0 && finalAverage < 87.0){
        finalLetterGrade = 'B';
    }
    else if (finalAverage >= 80.0 && finalAverage < 83.0){
        finalLetterGrade = "B-";
    }
    else if (finalAverage >= 77.0 && finalAverage < 80.0){
        finalLetterGrade = 'C+';
    }
    else if (finalAverage >= 73.0 && finalAverage < 77.0){
        finalLetterGrade = "C";
    }
    else if (finalAverage >=70.0 && finalAverage < 73.0){
        finalLetterGrade = 'C-';
    }
    else if (finalAverage >= 60.0 && finalAverage < 70.0 ){
        finalLetterGrade = "D";
    }
    else if (finalAverage < 60.0){
        finalLetterGrade = 'F';
    }
    else {
        finalLetterGrade = 'F';
    }

    cout << "Homework Average" << setfill('.') << setw(6) << "  :" << "   " << homework << setprecision(2) << endl;
    cout << "Laboratory Average" << setfill('.') << setw(4) << "  :" << "   " << lab << setprecision(2) << endl;
    cout << "Midterm Exam" << setfill('.') << setw(10) << "  :" << "      " << midTerm << endl;
    cout << "Final Exam" << setfill('.') << setw(12) << "  :" << "      " << final << endl;
    cout << "Term Paper" << setfill('.') << setw(12) << "  :" << "      " << termPaperGrade << " [" << termPaper << "]" << endl;
    cout << "Class Participation" << setfill('.') << setw(3) << "  :" << "      " << participation <<  endl;
    cout << endl;
    cout << "Final Average" << setfill('.') << setw(9) << "  :" << "   " << finalAverage << setprecision(2) << endl;
    cout << "Course Letter Grade" << setfill('.') << setw(3) << "  :" << "      " << finalLetterGrade << endl;

   return(0);
}