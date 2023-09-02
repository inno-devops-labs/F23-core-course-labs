"""
A simple app that returns current time in Moscow.
"""
__author__ = "Artem Bulgakov"

import asyncio
import server


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, help="port to listen on")
    args = parser.parse_args()
    return args


async def main():
    async def server_loop():
        try:
            while True:
                await asyncio.sleep(3600)
        except asyncio.CancelledError:
            pass
        except KeyboardInterrupt:
            print("Stopping server...")
    args = parse_args()
    await server.run_server(args.port)
    await server_loop()

if __name__ == '__main__':
    asyncio.run(main())
