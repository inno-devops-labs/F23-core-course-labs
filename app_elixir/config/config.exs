# This file is responsible for configuring your application
# and its dependencies with the aid of the Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
import Config

# config :devops_web,
#   ecto_repos: [DevopsWeb.Repo]

# Configures the endpoint
config :devops_web, DevopsWebWeb.Endpoint,
  url: [host: "localhost"],
  render_errors: [
    formats: [html: DevopsWebWeb.ErrorHTML, json: DevopsWebWeb.ErrorJSON],
    layout: false
  ],
  pubsub_server: DevopsWeb.PubSub,
  live_view: [signing_salt: "wn550Slh"],
  instrumenters: [DevopsWeb.PhoenixInstrumenter]

config :prometheus, DevopsWeb.PhoenixInstrumenter,
  controller_call_labels: [:controller, :action],
  duration_buckets: [
    10,
    25,
    50,
    100,
    250,
    500,
    1000,
    2500,
    5000,
    10_000,
    25_000,
    50_000,
    100_000,
    250_000,
    500_000,
    1_000_000,
    2_500_000,
    5_000_000,
    10_000_000
  ],
  registry: :default,
  duration_unit: :microseconds

config :prometheus, DevopsWeb.PipelineInstrumenter,
  labels: [:status_class, :method, :host, :scheme, :request_path],
  duration_buckets: [
    10,
    100,
    1_000,
    10_000,
    100_000,
    300_000,
    500_000,
    750_000,
    1_000_000,
    1_500_000,
    2_000_000,
    3_000_000
  ],
  registry: :default,
  duration_unit: :microseconds

# Configures the mailer
#
# By default it uses the "Local" adapter which stores the emails
# locally. You can see the emails in your browser, at "/dev/mailbox".
#
# For production it's recommended to configure a different adapter
# at the `config/runtime.exs`.
config :devops_web, DevopsWeb.Mailer, adapter: Swoosh.Adapters.Local

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{config_env()}.exs"
