using FluentAssertions;
using ProgrammerProfile.DTO;
using ProgrammerProfile.Mappers;
using ProgrammerProfile.Models;

namespace UnitTests.Mappers;

public class ProfileMapperTest
{
    private static readonly GitHubRepository Repository = new GitHubRepository()
    {
        Description = "abc",
        Name = "repo",
        Url = "url"
    };
        
    [Fact]
    public void DtoMappingTest()
    {
        var profileDto = new ProfileDto()
        {
            Login = "DamirNabiull",
            AvatarUrl = "avatar",
            Bio = "bio",
            HtmlUrl = "html"
        };
        
        var repos = new List<GitHubRepository>()
        {
            Repository
        };

        var profile = ProfileMapper.MapProfile(profileDto, repos);

        profile.Name.Should().Be(profileDto.Login);
        profile.Description.Should().Be(profileDto.Bio);
        profile.ProfileImageUrl.Should().Be(profileDto.AvatarUrl);
        profile.GitHubProfileUrl.Should().Be(profileDto.HtmlUrl);
        profile.Repositories.Should().Contain(Repository);
    }
}