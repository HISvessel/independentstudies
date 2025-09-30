"""adding the data persistence memory for image storing"""
from abc import ABC, abstractmethod

class repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass
    
    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

class InMemoryRepository(repository):
    def __init__(self):
        self._storage = {}
