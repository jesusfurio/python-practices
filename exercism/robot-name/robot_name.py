import random
import string

class Robot(object):

    names_used = set()
    
    def __init__(self):
        self.reset()

    def generate_new_name(self):
        while True:
            new_name = self.random_name()
            if new_name not in self.names_used:
                return new_name

    def random_name(self):
        return (random.choice(string.ascii_uppercase) * 2) + (str(random.randrange(0,9)) *3)

    def reset(self):
        self.name = self.generate_new_name()
        self.names_used.add(self.name)