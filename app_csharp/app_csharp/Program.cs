using app_csharp.Services;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Register services
builder.Services.AddSingleton<ITimeService, MoscowTimeService>();

// Add controllers
app.MapControllers();

app.Run();