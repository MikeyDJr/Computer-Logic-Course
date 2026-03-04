class Program
{
    // Method to calculate payroll
    (double regularHours, double overtimeHours, double regularPay, double overtimePay,
        double grossPay, double stateTax, double federalTax, double totalTax, double postTaxAmount)
    CalculatePayroll(double rate, double hoursWorked)
    {
        double regularHours = 0;
        double overtimeHours = 0;
        double regularPay = 0;
        double overtimePay = 0;

        // Determine regular vs overtime hours
        if (hoursWorked <= 40)
        {
            regularHours = hoursWorked;
            overtimeHours = 0;
        }
        else
        {
            regularHours = 40;
            overtimeHours = hoursWorked - 40;
        }

        regularPay = regularHours * rate;
        overtimePay = overtimeHours * rate * 1.5;
        double grossPay = regularPay + overtimePay;

        double stateTax = grossPay * 0.05;      // 5% state tax
        double federalTax = grossPay * 0.15;    // 15% federal tax
        double totalTax = stateTax + federalTax;
        double postTaxAmount = grossPay - totalTax;
        return (regularHours, overtimeHours, regularPay, overtimePay,
                grossPay, stateTax, federalTax, totalTax, postTaxAmount);
    }

    // Main entry point
    static void Main(string[] args)
    {
        Program program = new Program();

        Console.WriteLine("Payroll Processing System");
        Console.WriteLine("-------------------------");

        Console.Write("Enter number of employees: ");
        int numEmployees = int.Parse(Console.ReadLine());

        for (int i = 0; i < numEmployees; i++)
        {
            Console.WriteLine("\nEnter Employee ID:");
            string id = Console.ReadLine();

            Console.WriteLine("Enter Employee Name:");
            string name = Console.ReadLine();

            Console.WriteLine("Enter Number of Dependents:");
            int dependents = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter Hourly Rate:");
            double rate = double.Parse(Console.ReadLine());

            Console.WriteLine("Enter Hours Worked:");
            double hoursWorked = double.Parse(Console.ReadLine());

            var (regularHours, overtimeHours, regularPay, overtimePay,
                 grossPay, stateTax, federalTax, totalTax,
                 postTaxAmount) = program.CalculatePayroll(rate, hoursWorked);

            Console.WriteLine("\n----- Payroll Summary -----");
            Console.WriteLine("Employee ID: " + id);
            Console.WriteLine("Name: " + name);
            Console.WriteLine("Regular Hours: " + regularHours);
            Console.WriteLine("Overtime Hours: " + overtimeHours);
            Console.WriteLine("Regular Pay: $ " + Math.Round(regularPay, 2));
            Console.WriteLine("Overtime Pay: $ " + Math.Round(overtimePay, 2));
            Console.WriteLine("Gross Pay: $ " + Math.Round(grossPay, 2));
            Console.WriteLine("State Tax: $ " + Math.Round(stateTax, 2));
            Console.WriteLine("Federal Tax: $ " + Math.Round(federalTax, 2));
            Console.WriteLine("Total Tax: $ " + Math.Round(totalTax, 2));
            Console.WriteLine("Post-Tax Pay: $ " + Math.Round(postTaxAmount, 2));
        }
    }
}
