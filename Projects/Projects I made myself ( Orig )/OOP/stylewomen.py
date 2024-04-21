class Style:

    breasts = 2

    def __init__(self, eyes, body, nationality, skincolor):
        self.eyes = eyes
        self.body = body
        self.nationality = nationality 
        self.skincolor = skincolor

    def gfmat(self):
        print(f"She is {self.body} enough!")

    def notgfmat(self):
        print(f"She is not {self.body} enough!")