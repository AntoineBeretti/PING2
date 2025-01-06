from abc import ABC, abstractmethod
from gameController import 



class Input:
    def __init__(self, gameController=false, ballPose=0, playerPose):
        self.gameController=gameController
        self.ballPose=ballPose
        self.playerPose=playerPose

class Output:
    def __init__(self, led=0, sound=0, playerMove=False):
        self.led=led
        self.sound=sound
        self.playerMove=playerMove

class GameMode(ABC):
    """
    Mother class to all game mode that Should be inherited.
    Every game mode describe the behavior of outputs (LEDs, sound, and player moves) 
    based on the inputs (game controller, ball pose, and player pose). additional, it take UI panel as settings.
    """
    @abstractmethod
    def run(self,Input):
        pass

    @abstractmethod
    def stop(self,Input):
        pass

    pass

class RedLightGreenLight(GameMode):
    """
    Game mode of Red Light Green Light. 1 2 3 soleil in french.
    """
    
    pass

class AtYourCommand(GameMode):
    """
    Game mode of At Your Command. A vos ordres in french.
    """
    
    pass

class LightTracker(GameMode):
    """
    Game mode of Light Tracker. Traque-lumière in french.
    """
    
    self.

    pass

class MemoChain(GameMode):
    """
    Game mode of Memo Chain. Mémo-chaîne in french.
    """
    
    pass

class SandBox(GameMode):
    """
    Game mode of Sand Box. Bac à sable in french.
    """
    
    pass

class PING(GameMode):
    """
    Game mode of PING.
    """
    
    pass

class BattleRoyale(GameMode):
    """
    Game mode of Battle Royale.
    """
    
    pass