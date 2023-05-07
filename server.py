import uvicorn

from pytholine.asgi import get_asgi_application


if __name__ == '__main__':
    uvicorn.run(get_asgi_application())