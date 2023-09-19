using Microsoft.AspNetCore.Mvc;
using ProgrammerProfile.Clients;
using ProgrammerProfile.Mappers;
using ProgrammerProfile.Models;

namespace ProgrammerProfile.Controllers;

public class ProfileController : Controller
{
    private const string MainUser = "DamirNabiull";
    private readonly IGitHubApiClient _client;

    public ProfileController(IGitHubApiClient client)
    {
        _client = client;
    }

    public async Task<ActionResult> Index()
    {
        return await GetPageInfo(MainUser);
    }

    [HttpGet]
    public async Task<IActionResult> Get(string? userName)
    {
        if (userName is null)
        {
            return View("Error", new ErrorViewModel());
        }

        return await GetPageInfo(userName);
    }

    private async Task<ActionResult> GetPageInfo(string userName)
    {
        var profileDto = await _client.GetProfile(userName);
        var repositories = await _client.GetRepositories(userName);

        return profileDto == null
            ? View("Error", new ErrorViewModel())
            : View("Index", ProfileMapper.MapProfile(profileDto, repositories));
    }
}