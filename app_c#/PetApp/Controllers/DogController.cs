using Microsoft.AspNetCore.Mvc;
using PetApp.Converters;
using PetApp.Models;
using Prometheus;
using static System.Int32;

namespace PetApp.Controllers;

public class DogController : Controller
{
    private readonly Counter _convertAgeCalls
        = Metrics.CreateCounter("convert_age_calls", "Number of calls of ConvertAge route");

    private readonly string _visitsPath = $"{Directory.GetCurrentDirectory()}/volume/visits";

    public IActionResult Index()
    {
        UpdateVisits();
        return View();
    }

    [HttpPost]
    public IActionResult ConvertAge(Dog model)
    {
        _convertAgeCalls.Inc();

        if (!ModelState.IsValid)
        {
            return View("Index", model);
        }

        model.ConvertedAgeInDays = AgeConverter.FromDateInDays(model.DateOfBirth);
        model.ConvertedAgeInYears = AgeConverter.DaysToYears(model.ConvertedAgeInDays);

        return View("Profile", model);
    }

    [Route("visits")]
    [HttpGet]
    public async Task<IActionResult> Visits()
    {
        var value = await ReadVisits();
        return new ObjectResult(value);
    }

    private async Task<string> ReadVisits()
    {
        return await System.IO.File.ReadAllTextAsync(_visitsPath);
    }

    private void UpdateVisits()
    {
        Console.WriteLine(_visitsPath);

        var value = System.IO.File.ReadAllText(_visitsPath);
        TryParse(value, out var number);
        System.IO.File.WriteAllTextAsync(_visitsPath, (number + 1).ToString());
    }
}