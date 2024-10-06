from fastapi import FastAPI

app = FastAPI()


def hello():
    print("Hello world CLI entrypoint")


@app.get("/")
async def root():
    return "Hello world, John Doe!"
