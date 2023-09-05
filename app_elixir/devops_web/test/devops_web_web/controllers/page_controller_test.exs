defmodule DevopsWebWeb.PageControllerTest do
  use DevopsWebWeb.ConnCase

  test "GET /time", %{conn: conn} do
    conn = get(conn, "/time")
    assert time_json = json(conn, 200)
    assert Map.has_key(time_json, "time")
  end
end
