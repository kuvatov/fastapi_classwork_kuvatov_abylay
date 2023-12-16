TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:postgres@localhost:5432/kino"},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.db.models"],
            "default_connection": "default",
        },
    },
}
