using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Grade to Letter Grade Converter");
        Console.WriteLine("------------------------------");

        double gradePercentage;
        char letterGrade;

        while (true)
        {
            Console.Write("Enter your grade as a percentage (0-100): ");
            if (double.TryParse(Console.ReadLine(), out gradePercentage) && gradePercentage >= 0 && gradePercentage <= 100)
            {
                letterGrade = ConvertToLetterGrade(gradePercentage);
                break; // Exit the loop after validating the input
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid percentage between 0 and 100.");
            }
        }

        Console.WriteLine($"Letter Grade: {letterGrade}");

        // Revision History
        Console.WriteLine("\nRevision History:");
        Console.WriteLine("Version 1.0 (Date: 2023-10-17)");
        Console.WriteLine("- Initial version of the program.");

        Console.ReadLine(); // Keep the console window open
    }

    static char ConvertToLetterGrade(double percentage)
    {
        if (percentage >= 90)
            return 'A';
        else if (percentage >= 80)
            return 'B';
        else if (percentage >= 70)
            return 'C';
        else if (percentage >= 60)
            return 'D';
        else
            return 'F';
    }
}

