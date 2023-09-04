namespace PetApp.Converters;

public static class AgeConverter
{
    public static int FromDateInDays(DateTime date)
    {
        var currentDate = DateTime.Today;
        var ageDifference = currentDate - date;
        var ageInDays = (int)ageDifference.TotalDays;

        return ageInDays * 7;
    }

    public static int DaysToYears(int days)
    {
        return days / 365;
    }
}