using System.Collections.Generic;
using System;
using System.Linq;

string c = "test";
int length = c.Length;

char[] charArray = c.ToCharArray();
// var newArray = new List<char>();
var result = string.Empty;

for (int i = length - 1; i >= 0; i--)
{
    //    newArray.Add(charArray[i]) ;
    result += charArray[i];
}

// var result = String.Join("", newArray);
var test = new string[] { "test", "test1" };
var result2 = string.Concat(test);

var test2 = "testonetwo";
var test3 = test2.Substring(3, 3);
Console.WriteLine(test3);

Console.WriteLine(result);
Console.WriteLine(result2);
Console.WriteLine("====================================");

Func<int, int, int> addition = AddNumber;
int result = AddNumber(1, 2);


//Delegates 
// int result = 0;
// Action<int, int> add = AddNumber;
// Predicate<int> isTrue = IsTrue;
// add(1, 5);

// bool IsTrue(int a)
// {
//     return true;
// }

// var test = isTrue(1);
// Console.WriteLine(test);

// void AddNumber(int a, int b)
// {
//     result = a + b;
// }

// Console.WriteLine(result);

// var result = GetEmployee().Where(GetPredicate());
// Console.WriteLine(result);


// static Func<Employee, bool> GetPredicate()
// {
//     Func<Employee, bool> predicate = (employee) => employee.Id == 2;
//     return predicate;
// }



// static IQueryable<Employee> GetEmployee()
// {

//     return new List<Employee>(){
//         new Employee() {
//                 Id = 1,
//                 Name = "test"
//             }
//     }.AsQueryable();
// }

// class Employee
// {
//     public int Id { get; set; }
//     public string Name { get; set; }
// }