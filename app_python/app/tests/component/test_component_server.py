
"""
Tests for the app_python module.
"""
__author__ = "Artem Bulgakov"

import asyncio

from testutils.testutils import TestUtility
from server import server


# component tests
def test_start_server():
    port = TestUtility.get_free_port()
    host = '127.0.0.1'

    async def async_test():
        await server.run_server(host, port)
        await TestUtility.connectivity_check(port)
    asyncio.run(async_test())
