from abc import ABC, abstractmethod
from classes.input import Input
from classes.output import Output
from datetime import datetime
import time
from classes.logFile import LogFile
import random

#Creation du logfile
log = LogFile()

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


class AtYourCommand(GameMode):
    """
    Game mode of At Your Command. A vos ordres in french.
    """
    
    pass

class LightTracker(GameMode):
    """
    Game mode of Light Tracker. Traque-lumière in french.
    """
    def __init__(self, position_led, distance_led):
        self.position_led=position_led
        self.distance_led=distance_led
        self.round_number=5 #5 rounds
        self.actual_round=0
        self.output_data = Output([])
    
    def run(self,PlayerInput):
        pass

    def stop(self,PlayerInput):
        pass

    def check_distance(self,PlayerInput):
        distance = abs(PlayerInput.LinearActuatorInput.currentPose - self.position_led)
        return distance
        pass 

    def move(self,PlayerInput):
        if PlayerInput.Manette.newAction:
            if PlayerInput.Manette.newActionleft:
                PlayerInput.LinearActuatorOutput.move_to_left = True
                PlayerInput.LinearActuatorOutput.move_to_right = False
            elif PlayerInput.Manette.newActionright:
                PlayerInput.LinearActuatorOutput.move_to_left = False
                PlayerInput.LinearActuatorOutput.move_to_right = True
        pass

    def check_move(self,PlayerInput,Input):
        for player_input in Input.ListPlayerInput:
            if PlayerInput.Manette.newAction == True:
                return False
            else:
                return True
        pass

    def check_hold_on(self,PlayerInput):
        """Cette fonction permet de vérifier si le joueur maintient le bouton de la manette enfoncé"""
        

        pass

    def new_round(self,PlayerInput):
        new_position_led = random.uniform(PlayerInput.LinearActuatorInput.rightLimit, PlayerInput.LinearActuatorInput.leftLimit)
        if new_position_led == self.position_led:
            new_position_led = random.uniform(PlayerInput.LinearActuatorInput.rightLimit, PlayerInput.LinearActuatorInput.leftLimit)
        else:
            self.position_led = new_position_led
            self.actual_round += 1
        pass

    def modif_score(self,PlayerInput):
        PlayerInput.PointCounter += 1
        pass


    def check_victory(self,PlayerInput):
        if PlayerInput.PointCounter == 5:
            self.output_data.ListPlayerOutput[PlayerInput.id_player].PlayerLedStrip.onPlayer(YELLOW)
            return True
        return False
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

class PingGame(GameMode):
    """
    Game mode of PING.
    """
    
    pass

class BattleRoyale(GameMode):
    """
    Game mode of Battle Royale.
    """
    
    pass