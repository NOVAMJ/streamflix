
import sqlalchemy
from app.db.database import DATABASE_URL

engine = sqlalchemy.create_engine(DATABASE_URL)
inspector = sqlalchemy.inspect(engine)
print(inspector.get_table_names())
