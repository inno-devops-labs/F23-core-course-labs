import aiohttp
import random


class TestUtility:
    @staticmethod
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
                s.connect(('127.0.0.1', tentative_port))
            except Exception:
                return tentative_port

    async def connectivity_check(port: int):
        """
        A simple connectivity check.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://127.0.0.1:{port}/time') as resp:
                assert resp.status == 200
                assert 'Current time in Moscow' in await resp.text()
