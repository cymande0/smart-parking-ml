import sqlalchemy as sa
from dotenv import load_dotenv
import os

# Load credentials from .env file
load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")

# Build PostgreSQL connection string
engine = sa.create_engine(
    f"postgresql://{user}:{password}@localhost:5432/{db}"
)

# Try to connect and run a simple query
with engine.connect() as conn:
    result = conn.execute(sa.text("SELECT version()"))
    print("Connected! PostgreSQL version:")
    print(result.fetchone()[0])