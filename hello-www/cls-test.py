import modal

image = modal.Image.debian_slim().pip_install("fastapi[standard]")
app = modal.App(name="example-cls", image=image)

@app.cls()
class WebApp:
    @modal.enter()
    def startup(self):
        from datetime import datetime, timezone

        print("🏁 Starting up!")
        self.start_time = datetime.now(timezone.utc)

    @modal.web_endpoint(docs=True)
    def web(self):
        from datetime import datetime, timezone

        current_time = datetime.now(timezone.utc)
        return {"start_time": self.start_time, "current_time": current_time}

