import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    # Database configuration (Azure SQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mssql+pyodbc://@articlecmsserver12345.database.windows.net/articlecmsdb?driver=ODBC+Driver+17+for+SQL+Server&authentication=ActiveDirectoryPassword"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Azure Storage (for images/files if used)
    AZURE_STORAGE_ACCOUNT = os.environ.get("AZURE_STORAGE_ACCOUNT")
    AZURE_STORAGE_KEY = os.environ.get("AZURE_STORAGE_KEY")
    AZURE_STORAGE_CONTAINER = os.environ.get("AZURE_STORAGE_CONTAINER")

    # Microsoft Login (Azure AD)
    AZURE_CLIENT_ID = os.environ.get("AZURE_CLIENT_ID")
    AZURE_CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET")
    AZURE_TENANT_ID = os.environ.get("AZURE_TENANT_ID")

    AUTHORITY = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"