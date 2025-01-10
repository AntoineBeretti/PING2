class PlayerInput:
    def __init__(self, BeamSwitch, LinearActuatorInput, GameController, id_player, PointCounter, LifePointCounter):
        self.BeamSwitch=BeamSwitch
        self.LinearActuatorInput=LinearActuatorInput
        self.GameController=GameController
        self.id_player=id_player
        self.PointCounter=PointCounter
        self.LifePointCounter=LifePointCounter
    pass