import os

structure = {
    "app": ["api", "core", "db", "models", "services", "utils"],
    "migrations": [],
    "tests": []
}

files = [
    "app/main.py",
    "app/api/routes.py",
    "app/api/webhooks.py",
    "app/core/config.py",
    "app/core/security.py",
    "app/db/session.py",
    "app/db/models.py",
    "app/db/repositories.py",
    "app/models/schemas.py",
    "app/services/bsale_service.py",
    "app/services/odoo_service.py",
    "app/services/sync_service.py",
    "app/utils/logger.py",
    "app/utils/helpers.py",
    "README.md",
    "requirements.txt",
    ".env",
    ".gitignore"
]

root = "integrador_odoo_bsale"

os.makedirs(root, exist_ok=True)

for folder, subs in structure.items():
    for sub in subs:
        os.makedirs(os.path.join(root, folder, sub), exist_ok=True)
    os.makedirs(os.path.join(root, folder), exist_ok=True)

for file in files:
    path = os.path.join(root, file)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").close()

print("✅ Proyecto creado correctamente")
