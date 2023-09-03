using Microsoft.AspNetCore.SignalR;

namespace app_csharp.Hubs;

public class ClockHub : Hub
{
    public async Task GetTime()
    {
        while (true)
        {
            await Clients.All.SendAsync("ReceiveTime", DateTime.Now.ToString("HH:mm:ss"));
            await Task.Delay(1000);
        }
    }
}