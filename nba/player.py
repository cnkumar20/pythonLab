class Player:
    def __init__(self,player_dict):
        self.id = player_dict["id"]
        self.height_inches = player_dict["height_inches"]
        self.position = player_dict["position"]
        self.first_name = player_dict["first_name"]
        self.last_name = player_dict["last_name"]
        self.weight_pounds = player_dict["weight_pounds"]
        self.team = player_dict["team"]
