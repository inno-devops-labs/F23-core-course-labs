using FluentAssertions;
using PetApp.Converters;

namespace UnitTests;

public class AgeConverterTests
{
    [Fact]
    public void AgeInDaysTest()
    {
        var date = DateTime.Today.Subtract(TimeSpan.FromDays(4));
        var converted = AgeConverter.FromDateInDays(date);

        converted.Should().Be(28);
    }

    [Fact]
    public void AgeInYearsTest()
    {
        var date = DateTime.Today.Subtract(TimeSpan.FromDays(365));
        var converted = AgeConverter.FromDateInDays(date);
        var years = AgeConverter.DaysToYears(converted);

        years.Should().Be(7);
    }
}