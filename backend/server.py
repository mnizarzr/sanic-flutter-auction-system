from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

if __name__ == '__main__':
    app.run(dev=True, debug=True, host="0.0.0.0")
