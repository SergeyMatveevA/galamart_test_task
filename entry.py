import argparse
import asyncio
import aiohttp
from demo import create_app
from demo.settings import load_config

from aiohttp.web import Application, run_app
from aiohttp_json_rpc import JsonRpc
import asyncio


try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("Uvloop has not been installed")

parser = argparse.ArgumentParser(description="Demo project")
parser.add_argument("--host", help="Host to listen", default="0.0.0.0")
parser.add_argument("--port", help="Port to accept connections", default=5000)
parser.add_argument("--reload", action="store_true")
parser.add_argument("-с", "--config", type=argparse.FileType("r"))

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    print("Start with code reload")
    import aioreloader

    aioreloader.start()


if __name__ == "__main__":
    aiohttp.web.run_app(app, host=args.host, port=args.port)
