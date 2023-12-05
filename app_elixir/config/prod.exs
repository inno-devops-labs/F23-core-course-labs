import Config

# Do not print debug messages in production
config :logger, level: :info

config :watch, WatchWeb.Endpoint,
  # Binding to loopback ipv4 address prevents access from other machines.
  # Change to `ip: {0, 0, 0, 0}` to allow access from other machines.
  http: [ip: {0, 0, 0, 0}, port: 4000],
  check_origin: false,
  code_reloader: true,
  debug_errors: true,
  secret_key_base: "5Ms9YbqJi6VZzMIuKPXZVbwEGC8VM0DVDHsz6BTHQTR2wXikxC8gJiwNCHlTkGBW",
  watchers: []

# Runtime production configuration, including reading
# of environment variables, is done on config/runtime.exs.
