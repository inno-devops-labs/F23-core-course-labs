defmodule DevopsTest do
  use ExUnit.Case
  doctest Devops

  test "greets the world" do
    assert Devops.hello() == :world
  end
end
