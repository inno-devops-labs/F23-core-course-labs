### Implemented best practices and followed code standards:

- Proper naming of endpoints

  `/time` - noun. And GET HTTP method stands for action name. No any verbs in endpoint name

- Using proper umbrella project structure
- `mix.lock` file with all dependencies hashes
- `.formatter.txs` mix format config to ensure the same formatted code on each workstation
- `.tool-versions` locked erlang & elixir versions

### Ensured quality

- via unit tests (`mix test`)
- via manual testing
- via `mix credo` (static analysis tool)
- via `mix dialyzer` (also static analysis tool)
- via `mix format` (formatting tool)
- via cspell
