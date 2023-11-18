using Newtonsoft.Json;
using ProgrammerProfile.DTO;
using ProgrammerProfile.Models;

namespace ProgrammerProfile.Clients;

public interface IGitHubApiClient
{
    public Task<ProfileDto?> GetProfile(string userName);
    public Task<List<GitHubRepository>> GetRepositories(string userName);
}

public class GitHubApiClient : IGitHubApiClient
{
    private const string Url = "https://api.github.com/users";
    private readonly HttpClient _client;

    public GitHubApiClient(IServiceProvider serviceProvider)
    {
        _client = serviceProvider
            .GetService<IHttpClientFactory>()!
            .CreateClient();

        _client.DefaultRequestHeaders.UserAgent
            .TryParseAdd("request");
    }

    public async Task<ProfileDto?> GetProfile(string userName)
    {
        try
        {
            var response = await GetResponse($"{Url}/{userName}");
            return JsonConvert.DeserializeObject<ProfileDto>(response);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
            return null;
        }
    }

    public async Task<List<GitHubRepository>> GetRepositories(string userName)
    {
        try
        {
            var response = await GetResponse($"{Url}/{userName}/repos");
            var deserializeObject = JsonConvert.DeserializeObject<GitHubRepository[]>(response);

            return deserializeObject == null
                ? new List<GitHubRepository>()
                : deserializeObject.ToList();
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
            return new List<GitHubRepository>();
        }
    }

    private async Task<string> GetResponse(string uri)
    {
        return await _client.GetStringAsync(uri);
    }
}