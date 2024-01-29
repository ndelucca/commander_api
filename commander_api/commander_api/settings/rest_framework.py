REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Commander API",
    "DESCRIPTION": "ndelucca base of operations",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
