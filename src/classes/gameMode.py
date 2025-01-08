from abc import ABC, abstractmethod
from classes.input import Input
from classes.output import Output
import time

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
    def __init__(self):
        self.is_light_green=False
        self.light_duration=3 # in seconds
        self.last_light_switch_time = time.time()
        pass


    def _switch_light(self):
        """Change la couleur de la lumière (rouge ↔ vert)."""
        current_time = time.time()
        if current_time - self.last_light_switch_time >= self.light_duration:
            self.is_light_green = not self.is_light_green  # Alterne entre rouge et vert
            self.last_light_switch_time = current_time

    def run(self,Input):
        self._switch_light()  # Vérifie si on doit changer l'état de la lumière
        for player in Input.PlayerInput.Manette:
            if player in self.players_eliminated:
                continue

            if not self.is_light_green and player.action == "move":
                # Si la lumière est rouge et que le joueur bouge, il est éliminé
                self.players_eliminated.append(player)
                Output.led = self.is_light_green
                Output.sound = "Player {} eliminated".format(player)
                
            elif self.is_light_green:
                # Si la lumière est verte, les joueurs peuvent bouger librement
                Output.led = self.is_light_green
                Output.sound = "La lumière est verte"
                
            else:
                # Si la lumière est rouge et que le joueur ne bouge pas
                Output.led = self.is_light_green
                Output.sound = "La lumière est rouge"
                

        return outputs
            
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
    
    def LightTracker(speed):
        playersAlive=[]
        for i in connectedGamepads:
            if i == 1 :
                playersAlive.append("joueur {i}")
        if not playersAlive:
            print("No player is connected")
            endgame=1
            return endgame





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