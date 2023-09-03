using Microsoft.AspNetCore.Mvc.RazorPages;

public class IndexModel : PageModel
{
    public string MoscowTime { get; set; }

    public void OnGet()
    {
        TimeZoneInfo moscowTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Russian Standard Time");
        DateTime moscowTime = TimeZoneInfo.ConvertTime(DateTime.Now, moscowTimeZone);
        MoscowTime = moscowTime.ToString("HH:mm:ss");
    }
}