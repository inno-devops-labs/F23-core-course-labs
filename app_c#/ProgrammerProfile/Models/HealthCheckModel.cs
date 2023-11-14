using Microsoft.Extensions.Diagnostics.HealthChecks;

namespace ProgrammerProfile.Models
{
    public sealed class HealthCheckModel : IHealthCheck
    {
        public Task<HealthCheckResult> CheckHealthAsync(HealthCheckContext context,
            CancellationToken cancellationToken = default)
        {
            return Task.FromResult(HealthCheckResult.Healthy());
        }
    }
}