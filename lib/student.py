from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initialize empty knowledge list
        
    def learn(self, information):
        """Adds information to student's knowledge"""
        self.knowledge.append(information)