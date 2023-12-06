using Microsoft.AspNetCore.Mvc;
using app_csharp.Services;


namespace app_csharp.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TimeController : ControllerBase
    {
        private readonly ITimeService _timeService;
        private int visits;
        private FileStream st;

        public TimeController(ITimeService timeService)
        {
            _timeService = timeService;
            visits = 0;
        }

        [HttpGet("moscow-time")]
        public IActionResult GetMoscowTime()
        {
            st = new FileStream("visits.txt", FileMode.Create, FileAccess.Write);
            StreamWriter writer = new StreamWriter(st);
            writer.WriteLine(visits.ToString());
            writer.Close();
            visits++;
            return Ok(_timeService.GetMoscowTime());
        }
        [HttpGet("visits")]
        public IActionResult getVisits()
        {
            return Ok(visits);
        }
    }
}
