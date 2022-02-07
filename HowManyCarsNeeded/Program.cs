//P indicates people in each group and S means the number of seats for each group. Find the least number cards needed
var result2 = Solution(new int[] { 4, 4, 2, 4 }, new int[] { 5, 5, 2, 5 });
var result3 = Solution(new int[] { 2, 3, 4, 2 }, new int[] { 2, 5, 7, 2 });
var result = Solution(new int[] { 1, 4, 1 }, new int[] { 1, 5, 1 });

Console.WriteLine(result.ToString() == "2");
Console.WriteLine(result2.ToString() == "3");
Console.WriteLine(result3.ToString() == "2");

Console.ReadLine();


static int Solution(int[] P, int[] S)
{
    //people can be ordered from the lowest number to fill in the car
    var totalPeople = P.Sum(x => x);

    var orderedSeats = S.OrderByDescending(x => x).ToList();

    var numberOfCarsNeeded = 0;

    for (int i = 0; i < orderedSeats.Count(); i++)
    {
        var seats = orderedSeats[i];
        //14 = 7 + 3 + 12
        totalPeople = totalPeople - seats;

        if (totalPeople <= 0)
        {
            numberOfCarsNeeded = i + 1;
            break;
        }
    }

    return numberOfCarsNeeded;

}
