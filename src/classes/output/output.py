from classes.ledStrip import LedStrip, PlayerLedStrip

class Output:
    def __init__(self, ListPlayerOutput, ledStrip):
        self.Speaker=Speaker
        self.ListPlayerOutput=ListPlayerOutput
        self.ledStrip=ledStrip
    pass




class LinearActuatorOutput:
    def __init__(self, move_to_right, move_to_leftLimit):
        self.move_to_right=move_to_right
        self.move_to_leftLimit=move_to_leftLimit
    pass

