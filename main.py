import os
from dotenv import load_dotenv

from Core.server import Server

load_dotenv()
PORT = int(os.getenv("APP_PORT", 8000))
ENV = os.getenv("APP_ENV", "development")

#start server
server = Server(PORT,ENV)
server.run()