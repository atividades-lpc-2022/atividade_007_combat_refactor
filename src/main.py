from config import Config
from game import Game


class Main:
    def init(self):
        game = Game(Config())
        game.play()


main = Main()
main.init()
