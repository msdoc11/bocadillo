from bocadillo import App


def test_startup_and_shutdown(app: App):
    message = None

    @app.on("startup")
    async def setup():
        nonlocal message
        message = "hi"

    @app.on("shutdown")
    async def cleanup():
        nonlocal message
        message = None

    @app.route("/")
    async def index(req, res):
        res.text = message

    # The Starlette TestClient calls startup and shutdown events when
    # used as a context manager.
    with app.client:
        assert message == "hi"
        response = app.client.get("/")
        assert response.text == "hi"
    assert message is None


def test_sync_handler(app: App):
    message = None

    @app.on("startup")
    def setup():
        nonlocal message
        message = "hi"

    with app.client:
        assert message == "hi"


def test_non_decorator_syntax(app: App):
    message = None

    async def setup():
        nonlocal message
        message = "hi"

    app.on("startup", setup)

    with app.client:
        assert message == "hi"
