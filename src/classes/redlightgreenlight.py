from classes.gameMode import GameMode
from classes.output import Output
import time
from logFile import*   
from classes.config import GREEN, ORANGE, YELLOW, RED

log = LogFile()

class RedLightGreenLight(GameMode):
    """
    Game mode of Red Light Green Light. 1 2 3 soleil in French.
    """
    def __init__(self):
        self.is_light_green = False
        self.time_init = time.time()
        self.duration_green_light = 3  # Temps du feu vert
        self.reaction_time = 0.5      # Temps de réaction
        self.output_data = Output([])  # Initialisation des données de sortie

    def can_move(self, current_time):
        """
        Vérifie si le joueur peut se déplacer (lumière verte).
        """
        elapsed_time = current_time - self.time_init
        if elapsed_time<0:
            log.write_in_log("ERROR", "gameMode", "can_move", "elaspsed time has a negative value")
        return elapsed_time < self.duration_green_light

    def check_action(self, player_input, current_time):
        """
        Vérifie l'action du joueur selon l'état actuel de la lumière.
        """
        if player_input.GameController.newAction:
            player_output = self.output_data.ListPlayerOutput[player_input.id_player]
            
            if self.can_move(current_time):
                # Lumière verte : déplacement autorisé
                player_output.LinearActuatorOutput.move_to_right = True
                player_output.LinearActuatorOutput.move_to_leftLimit = False
                player_output.PlayerLedStrip.onPlayer(GREEN)
            else:
                # Lumière rouge : déplacement interdit
                player_output.LinearActuatorOutput.move_to_leftLimit = True
                player_output.PlayerLedStrip.onPlayer(ORANGE)
        else:
            player_output = self.output_data.ListPlayerOutput[player_input.id_player]
            player_output.LinearActuatorOutput.move_to_right = False
            player_output.LinearActuatorOutput.move_to_leftLimit = False

    def check_victory(self, player_input):
        """
        Vérifie si un joueur a gagné.
        """
        if player_input.LinearActuatorInput.currentPose >= player_input.LinearActuatorInput.rightLimit-20:
            self.output_data.ListPlayerOutput[player_input.id_player].PlayerLedStrip.onPlayer(YELLOW)
            return True
        return False

    def cycle(self, current_time):
        """
        Gère l'alternance entre les feux vert et rouge.
        """
        elapsed_time = current_time - self.time_init
        if elapsed_time<0:
            log.write_in_log("ERROR", "gameMode", "cycle", "elaspsed time has a negative value")
        self.is_light_green = elapsed_time < self.duration_green_light

        self.output_data.ledStrip.onLedStrip(GREEN) if self.is_light_green else self.output_data.ledStrip.onLedStrip(GREEN)

    def run(self, input_data):
        """
        Exécute une itération du mode de jeu.
        """
        if not input_data.ListPlayerInput:
            log.write_in_log("ERROR", "gameMode", "run", "no player was connected")
        for player_input in input_data.ListPlayerInput:
            if self.check_victory(player_input):
                self.stop(input_data)
                return self.output_data

            # Vérifie les actions des joueurs
            self.check_action(player_input, time.time())

        # Cycle du feu rouge / vert
        self.cycle(time.time())
        return self.output_data

    def stop(self, input_data):
        """
        Arrête le jeu et réinitialise les sorties.
        """
        for player_input in input_data.ListPlayerInput:
            player_output = self.output_data.ListPlayerOutput[player_input.id_player]
            player_output.PlayerLedStrip.clearPlayer()
            player_output.LinearActuatorOutput.move_to_right = False
            player_output.LinearActuatorOutput.move_to_leftLimit = True
