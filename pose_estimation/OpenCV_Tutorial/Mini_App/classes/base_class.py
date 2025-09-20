import uuid
from datetime import datetime as dt

"""creating a basic importable class that will be used for timestamping
CRUD operations and IDs for each object"""
class BaseClass():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()
    
    def save(self):
        return self.updated_at
    
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self.save()

    def to_dict(self):
        return {
            'id': self.id,
            'created at': self.created_at.isoformat(),
            'updated at': self.updated_at.isoformat()
        }