class User:
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, attr):
        return "{} attribute is not defined".format(attr)
    

def solution(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)
