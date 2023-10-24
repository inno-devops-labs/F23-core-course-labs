using Microsoft.AspNetCore.Mvc;
using PetApp.Converters;
using PetApp.Models;
using Prometheus;

namespace PetApp.Controllers;

public class DogController : Controller
{
    private readonly Counter _convertAgeCalls
        = Metrics.CreateCounter("convert_age_calls", "Number of calls of ConvertAge route");

    public IActionResult Index()
    {
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
}