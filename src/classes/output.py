from classes.ledStrip import LedStrip, PlayerLedStrip

class Output:
    def __init__(self, ListPlayerOutput, ledStrip):
        self.Speaker=Speaker
        self.ListPlayerOutput=ListPlayerOutput
        self.ledStrip=ledStrip
    pass

class PlayerOutput:
    def __init__(self, PlayerLedStrip, LinearActuatorOutput):
        self.PlayerLedStrip=PlayerLedStrip
        self.LinearActuatorOutput=LinearActuatorOutput
    pass

class Speaker:
    def __init__(self, sound):
        self.sound=sound
    pass

class LinearActuatorOutput:
    def __init__(self, move_to_right, move_to_leftLimit):
        self.move_to_right=move_to_right
        self.move_to_leftLimit=move_to_leftLimit
    pass

