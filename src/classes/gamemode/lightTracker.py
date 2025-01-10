from abc import ABC, abstractmethod
from classes.input.input import Input
from classes.output.output import Output
from datetime import datetime
from gameMode import GameMode
import time
from classes.logFile import LogFile
import random

#Creation du logfile
log = LogFile()


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