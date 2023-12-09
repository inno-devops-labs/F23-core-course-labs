import subprocess
import time
import asyncio
from testutils.testutils import TestUtility


def test_app_no_port():
    subproc = subprocess.Popen(['python3', 'main.py'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    assert subproc.wait(5) != 0


def test_app_port():
    port = TestUtility.get_free_port()
    host = '127.0.0.1'
    import os
    os.system("ls")
    subproc = subprocess.Popen(['python3', 'main.py', host, f'{port}'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # subprocess must be running
    assert subproc.poll() is None
    time.sleep(1)
    asyncio.run(TestUtility.connectivity_check(port))
    subproc.terminate()
