namespace ProgrammerProfile.Models;

public class Profile
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string GitHubProfileUrl { get; set; } = "";
    public string? ProfileImageUrl { get; set; }
    public List<GitHubRepository> Repositories { get; set; } = new List<GitHubRepository>();
}