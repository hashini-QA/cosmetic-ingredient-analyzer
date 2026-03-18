from sqlalchemy import create_engine
# to safely encode the special characters like @, %, # in passwords etc.,
from urllib.parse import quote_plus 

DB_NAME = "beauty_ai_db"
DB_USER = "root"
DB_PASSWORD = quote_plus("Hemuhasi@26")
DB_HOST = "localhost"
DB_PORT = "3306"

# syntax "mysql+pymysql://user:pass@host:port/db", host whom wea are calling 
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=False
)
