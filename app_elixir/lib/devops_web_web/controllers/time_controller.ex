defmodule DevopsWebWeb.TimeController do
  use DevopsWebWeb, :controller

  @counter_file_path "/app/visits/visits"

  def time(conn, _params) do
    increment_and_save_counter()
    datetime = "Etc/UTC" |> DateTime.now!() |> DateTime.add(3 * 3600, :second)

    conn
    |> json(%{time: DateTime.to_string(datetime)})
  end

  def visits(conn, _params) do
    conn
    |> json(%{counter: read_counter()})
  end

  defp read_counter do
    with {:ok, content} <- File.read(@counter_file_path),
    {int, ""} <- String.trim(content) |> Integer.parse() do
      int
    else
      _ ->
        0
    end
  end

  defp increment_and_save_counter do
    with current_count <- read_counter(),
         new_count <- current_count + 1,
         :ok <- File.write(@counter_file_path, Integer.to_string(new_count)) do
      new_count
    else
      _ -> :error
    end
  end
end
