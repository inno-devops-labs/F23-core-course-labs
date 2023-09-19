using Newtonsoft.Json;

namespace ProgrammerProfile.DTO;

public class ProfileDto
{
    [JsonProperty("login")]
    public string Login { get; set; } = "";
    [JsonProperty("avatar_url")]
    public string AvatarUrl { get; set; } = "";
    [JsonProperty("html_url")]
    public string HtmlUrl { get; set; } = "";
    [JsonProperty("bio")]
    public string Bio { get; set; } = "";
}