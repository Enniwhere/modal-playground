

import modal

image = modal.Image.debian_slim().pip_install("fastapi[standard]")
app = modal.App(name="example-lifecycle-web", image=image)


@app.function()
@modal.web_endpoint(
    docs=True  # adds interactive documentation in the browser
)
def hello():
    return "Hello to all!"


@app.function()
@modal.web_endpoint(docs=True)
def greet(user: str) -> str:
    return f"Hello {user}!"


@app.function()
@modal.web_endpoint(method="POST", docs=True)
def goodbye(data: dict) -> str:
    name = data.get("name") or "world"
    return f"Goodbye {name}!"