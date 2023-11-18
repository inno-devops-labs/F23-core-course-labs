defmodule WatchWeb.WatchController do
  use Phoenix.Controller, namespace: MinimalWeb

  plug(:fetch_query_params)
  plug(:fetch_cookies, keys: [:timezone])

  @counter_name "counter.txt"

  def index(conn, %{"tz" => tz}) do
    log_visit()
    case DateTime.now(tz) do
      {:ok, time} ->
        Phoenix.Controller.html(conn, """
          <p>Time in #{tz} is #{time}</p>
          <script>document.cookie = "timezone="+Intl.DateTimeFormat().resolvedOptions().timeZone;</script>
        """)

      _ ->
        utc_time = DateTime.utc_now()

        Phoenix.Controller.html(conn, """
          <p>TimeZone from "tz" query param is unknown :(. Here is at least Ect/UTC time: #{utc_time}</p>
          <script>document.cookie = "timezone="+Intl.DateTimeFormat().resolvedOptions().timeZone;</script>
        """)
    end
  end

  def index(conn, _params) do
    log_visit()
    case DateTime.now(conn.cookies["timezone"]) do
      {:ok, time} ->
        Phoenix.Controller.html(conn, """
          <p>Your time is #{time}</p>
          <p>To know the time of your friend send his/her timezone in tz query param</p>
          <script>document.cookie = "timezone="+Intl.DateTimeFormat().resolvedOptions().timeZone;</script>
        """)

      _ ->
        utc_time = DateTime.utc_now()

        Phoenix.Controller.html(conn, """
          <p>Ect/UTC time is #{utc_time}</p>
          <p>To know your time reload the page</p>
          <script>document.cookie = "timezone="+Intl.DateTimeFormat().resolvedOptions().timeZone;</script>
        """)
    end
  end

  def visits(conn, _params) do
    count = File.stream!(@counter_name)
    |> Enum.count()

    Phoenix.Controller.html(conn, "#{count}")
  end

  defp log_visit() do
    {:ok, file} = File.open(@counter_name, [:append])
    IO.binwrite(file, "x\n")
    File.close(file)
  end
end
