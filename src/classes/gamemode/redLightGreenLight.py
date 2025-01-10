from classes.gameMode import GameMode
from classes.output.output import Output
import time
from logFile import*   
from classes.config import GREEN, ORANGE, YELLOW, RED

log = LogFile()

class RedLightGreenLight(GameMode):
    """
    Game mode of Red Light Green Light. 1 2 3 soleil in French.
    """
    def __init__(self):
        self.isLightGreen = False
        self.timeInit = time.time()
        self.durationGreenLight = 3  # Temps du feu vert
        self.reactionTime = 0.5      # Temps de réaction
        self.outputData = Output([])  # Initialisation des données de sortie

    def can_move(self, currentTime):
        """
        Vérifie si le joueur peut se déplacer (lumière verte).
        """
        elapsedTime = currentTime - self.timeInit
        if elapsedTime<0:
            log.write_in_log("ERROR", "gameMode", "can_move", "elaspsed time has a negative value")
        return elapsedTime < self.durationGreenLight

    def check_action(self, playerInput, currentTime):
        """
        Vérifie l'action du joueur selon l'état actuel de la lumière.
        """
        if playerInput.GameController.newAction:
            playerOutput = self.outputData.ListPlayerOutput[playerInput.idPlayer]
            
            if self.can_move(currentTime):
                # Lumière verte : déplacement autorisé
                playerOutput.LinearActuatorOutput.move_to_right = True
                playerOutput.LinearActuatorOutput.move_to_leftLimit = False
                playerOutput.PlayerLedStrip.onPlayer(GREEN)
            else:
                # Lumière rouge : déplacement interdit
                playerOutput.LinearActuatorOutput.move_to_leftLimit = True
                playerOutput.PlayerLedStrip.onPlayer(ORANGE)
        else:
            playerOutput = self.outputData.ListPlayerOutput[playerInput.idPlayer]
            playerOutput.LinearActuatorOutput.move_to_right = False
            playerOutput.LinearActuatorOutput.move_to_leftLimit = False

    def check_victory(self, playerInput):
        """
        Vérifie si un joueur a gagné.
        """
        if playerInput.LinearActuatorInput.currentPose >= playerInput.LinearActuatorInput.rightLimit-20:
            self.outputData.ListPlayerOutput[playerInput.idPlayer].PlayerLedStrip.onPlayer(YELLOW)
            return True
        return False

    def cycle(self, currentTime):
        """
        Gère l'alternance entre les feux vert et rouge.
        """
        elapsedTime = currentTime - self.timeInit
        if elapsedTime<0:
            log.write_in_log("ERROR", "gameMode", "cycle", "elaspsed time has a negative value")
        self.isLightGreen = elapsedTime < self.durationGreenLight

        self.outputData.ledStrip.onLedStrip(GREEN) if self.isLightGreen else self.outputData.ledStrip.onLedStrip(GREEN)

    def run(self, input_data):
        """
        Exécute une itération du mode de jeu.
        """
        if not input_data.ListPlayerInput:
            log.write_in_log("ERROR", "gameMode", "run", "no player was connected")
        for playerInput in input_data.ListPlayerInput:
            if self.check_victory(playerInput):
                self.stop(input_data)
                return self.outputData

            # Vérifie les actions des joueurs
            self.check_action(playerInput, time.time())

        # Cycle du feu rouge / vert
        self.cycle(time.time())
        return self.outputData

    def stop(self, input_data):
        """
        Arrête le jeu et réinitialise les sorties.
        """
        for playerInput in input_data.ListPlayerInput:
            playerOutput = self.outputData.ListPlayerOutput[playerInput.idPlayer]
            playerOutput.PlayerLedStrip.clearPlayer()
            playerOutput.LinearActuatorOutput.move_to_right = False
            playerOutput.LinearActuatorOutput.move_to_leftLimit = True
