from pymongo import MongoClient # type: ignore
from pymongo.database import Database # type: ignore

# Configurar MongoDB
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "rpadb"

client = MongoClient(MONGO_URI)
db: Database = client[DATABASE_NAME]

# Coleções específicas
queue_collection = db["queue"]
tasks_collection = db["tasks"]
triggers_collection = db["triggers"]
