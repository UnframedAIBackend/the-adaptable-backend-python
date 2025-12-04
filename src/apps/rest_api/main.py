import asyncio
from src.core.configuration.configuration import config
from src.apps.rest_api.server import Server

async def main() -> None:
    server = Server()
    port = config.get("PORT")
    await server.run(port=port)

if __name__ == "__main__":
    asyncio.run(main())
