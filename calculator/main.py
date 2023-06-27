# Import the typing module to use type hints
from typing import Optional

# Import the FastAPI and uvicorn modules
import fastapi
import uvicorn

# Create a new FastAPI instance. This will be the main point of entry for our application
api = fastapi.FastAPI()


# Define a new route for the root ("/") of our API. When a GET request is sent to "/", the function `index` will be called.
@api.get('/')
def index():
    # Create a simple HTML page that will be displayed when the root route is accessed
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    # Return the HTML page as a response to the request
    return fastapi.responses.HTMLResponse(content=body)


# Define a new route for the "/api/calculate" path. This function takes in two mandatory parameters `x` and `y`,
# and an optional parameter `z`.
@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    # Check if `z` is zero. If it is, return an error response, as we cannot divide by zero
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "ERROR: Z cannot be zero."},
            status_code=400)
    # Perform the addition of `x` and `y`
    value = x + y

    # If `z` is not None, divide the sum of `x` and `y` by `z`
    if z is not None:
        value /= z

    # Return the calculation results as a JSON response
    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }


# Use uvicorn to run our FastAPI application. This will start a web server that listens on port 8000 at localhost
uvicorn.run(api, port=8000, host="127.0.0.1")
