from demo.views import frontend


def setup_routes(app):
    app.router.add_route("GET", "/", frontend.index)
    app.router.add_route("GET", "/post", frontend.post)
    app.router.add_route("GET", "/write_to_db", frontend.write_to_db)
    app.router.add_route("GET", "/delete_by_id", frontend.delete_by_id)
