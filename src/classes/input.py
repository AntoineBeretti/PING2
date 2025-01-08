from abc import ABC, abstractmethodclass 
class Input:
    def __init__(self, PlayerInput, OtherInput):
        self.PlayerInput=PlayerInput
        self.OtherInput=OtherInput
    pass

class PlayerInput:
    def __init__(self, BeamSwitch, LinearActuator, Manette):
        self.BeamSwitch=BeamSwitch
        self.LinearActuator=LinearActuator
        self.Manette=Manette
    pass

class Manette(ABC):
    @abstractmethod
    def __init__(self, action):
        pass

class Manette3bouton(Manette):
    def __init__(self, action):
        self.action=action
    pass

class OtherInput:
    def __init__(self, ballPose, playerPose):
        self.ballPose=ballPose
        self.playerPose=playerPose
    pass


