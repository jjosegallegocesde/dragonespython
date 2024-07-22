from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

user="root" 
password = "admin123"
port ="3306"
dbName="dragonespythondos"

conectionDB=f"mysql+mysqlconnector://{user}:{password}@localhost:{port}/{dbName}"
engine = create_engine(conectionDB, echo=True)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

@event.listens_for(Engine, "connect")
def set_sql_mode(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    cursor.close()
