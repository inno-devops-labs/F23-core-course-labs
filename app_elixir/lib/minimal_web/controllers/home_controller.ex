defmodule MinimalWeb.HomeController do
  use Phoenix.Controller, namespace: MinimalWeb

  plug(:fetch_query_params)
  plug(:fetch_cookies, keys: [:timezone])

  def index(conn, %{"tz" => tz}) do
    case DateTime.now(tz) do
      {:ok, time} -> Phoenix.Controller.html(conn, """
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

  def index(conn, params) do
    case DateTime.now(conn.cookies["timezone"]) do
      {:ok, time} -> Phoenix.Controller.html(conn, """
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
end
