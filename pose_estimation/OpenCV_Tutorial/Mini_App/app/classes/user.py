from app.classes.base_class import BaseClass

"""this script contains a user class. While no attempt to login
or logout will be added, the goal is to use this user class to create
a video and append it to the user on the database schema"""

class User(BaseClass):
    def __init__(self, first_name='', last_name='', height=0.0, weight=0):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.videos = []

    def validate_method(self):
        status = []
        
        if not self.first_name or len() == 0:
            status.append('Please write your surname.')
        
        if not self.last_name or len() == 0:
            status.append('Please write your last name.')
        
        if not self.height or self.height < 0:
            status.append('Please provide a measurable height.')
        
        if not self.weight or self.weight < 0:
            status.append('Please provide a measurable weight.')

        return status

    def to_dict(self):
        return {
            "first name": self.first_name,
            "last name": self.last_name,
            "height": self.height,
            "weight": self.weight,
            'videos': self.videos
        }
