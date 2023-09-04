using System.ComponentModel.DataAnnotations;

namespace PetApp.Models;

public class Dog
{
    [Required(ErrorMessage = "The dog's name is required.")]
    public string? DogName { get; set; }
    public string? Owner { get; set; }
    public string? Address { get; set; }
    public string? OwnerPhoneNumber { get; set; }
    public DateTime DateOfBirth { get; set; } = new DateTime(2000, 1, 1);
    public int ConvertedAgeInDays { get; set; }
    public int ConvertedAgeInYears { get; set; }
}