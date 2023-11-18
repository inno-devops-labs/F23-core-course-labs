defmodule WatchWeb.Router do
  use WatchWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api", WatchWeb do
    pipe_through :api
  end

  get("/", WatchWeb.WatchController, :index)
  get("/visits", WatchWeb.WatchController, :visits)
end
