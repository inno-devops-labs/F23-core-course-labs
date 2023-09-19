using ProgrammerProfile.DTO;
using ProgrammerProfile.Models;

namespace ProgrammerProfile.Mappers;

public static class ProfileMapper
{
    public static Profile MapProfile(ProfileDto dto, List<GitHubRepository> repos)
    {
        return new Profile()
        {
            Description = dto.Bio,
            GitHubProfileUrl = dto.HtmlUrl,
            Name = dto.Login,
            ProfileImageUrl = dto.AvatarUrl,
            Repositories = repos
        };
    }
}