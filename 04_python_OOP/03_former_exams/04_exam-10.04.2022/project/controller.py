class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def _find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    @staticmethod
    def _check_if_player_cannot_duel(first_player, second_player):
        result = []
        if first_player.stamina == 0:
            result.append(f"Player {first_player.name} does not have enough stamina.")
        if second_player.stamina == 0:
            result.append(f"Player {second_player.name} does not have enough stamina.")
        return '\n'.join(result)

    def add_player(self, *players):
        players_to_add = []
        for player in players:
            if player not in self.players:
                players_to_add.append(player)
                self.players.append(player)
        return f"Successfully added: {', '.join([p.name for p in players_to_add])}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player(player_name)

        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        for supply in reversed(self.supplies):
            if type(supply).__name__ == sustenance_type:
                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy
                self.supplies.remove(supply)
                return f"{player.name} sustained successfully with {supply.name}."

        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self._find_player(first_player_name)
        second_player = self._find_player(second_player_name)

        result = self._check_if_player_cannot_duel(first_player, second_player)

        if result:
            return result

        first_attacker = first_player if first_player.stamina < second_player.stamina else second_player
        second_attacker = first_player if first_attacker == second_player else second_player

        if second_attacker.stamina - (first_attacker.stamina / 2) < 0:
            second_attacker.stamina = 0
        else:
            second_attacker.stamina -= (first_attacker.stamina / 2)

        if first_attacker.stamina - (second_attacker.stamina / 2) < 0:
            first_attacker.stamina = 0
        else:
            first_attacker.stamina -= (second_attacker.stamina / 2)

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for pl in self.players:
            result.append(f"{pl.__str__()}")

        for spl in self.supplies:
            result.append(f"{spl.details()}")

        return '\n'.join(result)
