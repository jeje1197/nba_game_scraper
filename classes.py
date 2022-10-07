class Game:
    def __init__(self, type:str, teams:list, is_live:bool, status:str, score=None):
        self.type = type
        self.teams = teams
        self.is_live = is_live
        self.status = status
        self.score = score