"""
Tests for the app_python module.
"""
__author__ = "Artem Bulgakov"

import asyncio
import aiohttp
import subprocess
import random
import time


def get_free_port() -> int:
    """
    An utility function to get a free port.
    A port is considered free if no process is listening for TCP on it.
    """
    import socket
    retries = 10
    for i in range(retries):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tentative_port = random.randint(1024, 65535)
        try:
            s.connect(('localhost', tentative_port))
        except Exception:
            return tentative_port


async def connectivity_check(port: int):
    """
    A simple connectivity check.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:{port}/time') as resp:
            assert resp.status == 200
            assert 'Current time in Moscow' in await resp.text()


# unit tests
def test_get_time():
    from zoneinfo import ZoneInfo
    import datetime
    import timeutils

    time = datetime.datetime.now(tz=ZoneInfo(
        "Europe/Moscow")).strftime("%H:%M:%S")
    assert timeutils.get_time() == "Current time in Moscow: " + time


# component tests
def test_start_server():
    import server
    port = get_free_port()

    async def async_test():
        await server.run_server(port)
        await connectivity_check(port)
    asyncio.run(async_test())


# system tests
def test_app_no_port():
    subproc = subprocess.Popen(['python3', 'app_main.py'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    assert subproc.wait(5) != 0


def test_app_port():
    port = get_free_port()
    subproc = subprocess.Popen(['python3', 'app_main.py', f'{port}'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # subprocess must be running
    assert subproc.poll() is None
    time.sleep(1)
    asyncio.run(connectivity_check(port))
    subproc.terminate()
