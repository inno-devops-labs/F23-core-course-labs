defmodule DevopsWeb.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # Start the Telemetry supervisor
      DevopsWebWeb.Telemetry,
      # Start the Ecto repository
      # DevopsWeb.Repo,
      # Start the PubSub system
      {Phoenix.PubSub, name: DevopsWeb.PubSub},
      # Start Finch
      {Finch, name: DevopsWeb.Finch},
      # Start the Endpoint (http/https)
      DevopsWebWeb.Endpoint
      # Start a worker by calling: DevopsWeb.Worker.start_link(arg)
      # {DevopsWeb.Worker, arg}
    ]

    require Prometheus.Registry
    DevopsWeb.PhoenixInstrumenter.setup()
    DevopsWeb.PipelineInstrumenter.setup()

    if :os.type() == {:unix, :linux} do
      Prometheus.Registry.register_collector(:prometheus_process_collector)
    end

    DevopsWeb.Exporter.setup()
    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: DevopsWeb.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    DevopsWebWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
