def solution(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))



import functools
@functools.total_ordering
class CodeSignalUser:
    def __init__(self, *args):
        self.user_name = args[0]
        self.user_id = int(args[1])
        self.user_xp = int(args[2])
    def __lt__(self, other):
        if self.user_xp < other.user_xp:
            return self.user_xp < other.user_xp
        elif self.user_xp == other.user_xp:
            return self.user_id>other.user_id
        return False
    
    def __str__(self):
        return self.user_name