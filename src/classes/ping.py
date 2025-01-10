from classes.communication import Communication
from classes.gameMode import RedLightGreenLight, AtYourCommand, LightTracker, MemoChain, SandBox, PING, BattleRoyale

class Ping:
    def __init__(self):
        self.communication = Communication()

    def choice_ping_mode(self, Parameter):
        if Parameter.mode == 1:
            currentGame = RedLightGreenLight()
        elif Parameter.mode == 2:
            currentGame = AtYourCommand()
        elif Parameter.mode == 3:
            currentGame = LightTracker()
        elif Parameter.mode == 4:
            currentGame = MemoChain()
        elif Parameter.mode == 5:
            currentGame = SandBox()
        elif Parameter.mode == 6:
            currentGame = PING()
        elif Parameter.mode == 7:
            currentGame = BattleRoyale()
        else:
            print("Error")
        return currentGame
        
    def run(self):
        
        
        pass
        
    def __str__(self):
        return "Ping :\n" + self.communication.__str__()
    
p = Ping()

print(p)
    