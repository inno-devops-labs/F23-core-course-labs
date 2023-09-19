using Microsoft.AspNetCore.Mvc;
using PetApp.Converters;
using PetApp.Models;

namespace PetApp.Controllers;

public class DogController : Controller
{
    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public IActionResult ConvertAge(Dog model)
    {
        if (!ModelState.IsValid)
        {
            return View("Index", model);
        }

        model.ConvertedAgeInDays = AgeConverter.FromDateInDays(model.DateOfBirth);
        model.ConvertedAgeInYears = AgeConverter.DaysToYears(model.ConvertedAgeInDays);

        return View("Profile", model);
    }
}