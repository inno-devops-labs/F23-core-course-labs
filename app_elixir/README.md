# Watch.ex

Watch.ex is a [phoenix](https://www.phoenixframework.org/) web application that displays the current time in arbitrary timezone.

## Installation

I recommend to install Elixir stack using [asdf](https://asdf-vm.com/).

Then just run:
```bash
mix local.hex --force
mix local.rebar --force
```

## Usage

```bash
mix phx.server
```

You should see output like this:

```bash
07:44:21.944 [info] Running MinimalWeb.Endpoint with cowboy 2.10.0 at 0.0.0.0:4000 (http)

07:44:21.946 [info] Access MinimalWeb.Endpoint at http://localhost:4000
```

And open http://localhost:4000 in your browser.

## Docker

### Build image

```bash
docker build -t sl1depengwyn/elixir_devops .
```

### Or pull

```bash
docker pull sl1depengwyn/elixir_devops
```

### Run image

```bash
docker run -p 80:80 sl1depengwyn/elixir_devops
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

To run the tests:

```bash
pytest
```
