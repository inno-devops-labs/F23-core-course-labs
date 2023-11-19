using ProgrammerProfile.Clients;
using ProgrammerProfile.Models;
using Prometheus;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();
builder.Services.AddHttpClient();
builder.Services.AddScoped<IGitHubApiClient, GitHubApiClient>();
builder.Services.AddHealthChecks()
    .AddCheck<HealthCheckModel>(nameof(HealthCheckModel));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.UseMetricServer();
app.UseHttpMetrics();

app.MapControllerRoute(
    name: "single",
    pattern: "{controller=Profile}/{action=Index}/{userName?}");

app.MapHealthChecks("/healthz");

app.MapControllers();

app.Run();