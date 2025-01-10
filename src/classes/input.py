from abc import ABC, abstractmethod
class Input:
    def __init__(self, ListPlayerInput, OtherInput):
        self.ListPlayerInput=ListPlayerInput
        self.OtherInput=OtherInput
    pass

class PlayerInput:
    def __init__(self, BeamSwitch, LinearActuatorInput, GameController, id_player):
        self.BeamSwitch=BeamSwitch
        self.LinearActuatorInput=LinearActuatorInput
        self.GameController=GameController
        self.id_player=id_player
    pass

class BeamSwitch():
    def __init__(self, isBeamSwitchOn):
        self.isBeamSwitchOn=isBeamSwitchOn

class LinearActuatorInput():
    def __init__(self, leftLimit, rightLimit, currentPose):
        self.leftLimit=leftLimit
        self.rightLimit=rightLimit
        self.currentPose=currentPose

class GameController(ABC):
    @abstractmethod
    def __init__(self, newAction, newActionleft, newActionright, newActionShoot):
        pass

class GameController3button(GameController):
    def __init__(self, newAction, newActionleft, newActionright, newActionShoot):
        self.newAction=newAction
        self.newActionleft=newActionleft
        self.newActionright=newActionright
        self.newActionShoot=newActionShoot
    pass


class OtherInput:
    def __init__(self, ballPose):
        self.ballPose=ballPose
    pass


