import random

def solution(seed, n):
    class Die(object):
        __new__ = lambda _, s, n: int(random.Random(s).random()*n)+1

    class Game(object):
        die = Die(seed, n)

    return Game.die
