using System.Globalization;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace src.Pages;

public class IndexModel : PageModel
{
    public string? Time { get; private set; }

    public void OnGet()
    {
        var timeZone = TimeZoneInfo.FindSystemTimeZoneById("Europe/Moscow");
        Time = TimeZoneInfo
            .ConvertTime(DateTime.Now, timeZone)
            .ToString(CultureInfo.CurrentCulture);
    }
}
