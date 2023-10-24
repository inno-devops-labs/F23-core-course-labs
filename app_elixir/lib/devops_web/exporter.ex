defmodule DevopsWeb.Exporter do
  @moduledoc """
  Exports `Prometheus` metrics at `/metrics`
  """

  @dialyzer :no_match

  use Prometheus.PlugExporter
end
