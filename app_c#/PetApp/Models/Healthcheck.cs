using Microsoft.Extensions.Diagnostics.HealthChecks;

namespace PetApp.Models;

public class Healthcheck : IHealthCheck
{
    public Task<HealthCheckResult> CheckHealthAsync(HealthCheckContext context,
        CancellationToken cancellationToken = default)
    {
        return Task.FromResult(HealthCheckResult.Healthy());
    }
}