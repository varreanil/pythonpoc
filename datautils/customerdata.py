import re

import psycopg2

class customer :

    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

    def tostring(self):
        print("%s \'%s\' \'%s\'" % (self.id,self.name,self.email))

    def validate(self):
        if not isinstance(self.id, (int, float, complex)) :
            return False
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email) :
            return False
        else :
            return True






gm = customer(100,"General Motors", "info@gm.com")

gm.tostring()

print(gm.validate())

