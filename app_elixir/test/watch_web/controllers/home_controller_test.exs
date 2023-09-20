defmodule WatchWeb.WatchControllerTest do
  use WatchWeb.ConnCase

  test "GET / returns 200", %{conn: conn} do
    conn = get(conn, "/")
    assert conn.status == 200
  end

  test "time updates", %{conn: conn} do
    conn_a = get(conn, "/")
    1 |> :timer.seconds() |> :timer.sleep()
    conn_b = get(conn, "/")

    assert conn_a.resp_body != conn_b.resp_body
  end
end
