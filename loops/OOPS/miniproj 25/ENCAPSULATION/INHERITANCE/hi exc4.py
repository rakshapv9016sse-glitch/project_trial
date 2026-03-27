class sport:
    def start_game(self):
        print("game starts now!!")
class football(sport):
    def kick_ball(self):
        print("football should be kicked")
class cricket(sport):
    def bat(self):
        print("cricket needs bat")

a=cricket()
b=football()
a.start_game()
a.bat()
b.start_game()
b.kick_ball()
