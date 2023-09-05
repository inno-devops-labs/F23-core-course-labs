defmodule DevopsWebWeb.TimeController do
  use DevopsWebWeb, :controller

  def time(conn, _params) do
    datetime = "Etc/UTC" |> DateTime.now!() |> DateTime.add(3 * 3600, :second)

    conn
    |> json(%{time: DateTime.to_string(datetime)})
  end
end
