from database import tasks_collection

def get_all():
    return list(tasks_collection.find({}, {"_id": 0}))

def create(data: dict):
    return tasks_collection.insert_one(data)