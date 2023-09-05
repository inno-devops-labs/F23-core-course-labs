use Mix.Config

config :minimal, MinimalWeb.Endpoint, []

config :phoenix, :json_library, Jason

config :elixir, :time_zone_database, Tz.TimeZoneDatabase

import_config "#{Mix.env()}.exs"
