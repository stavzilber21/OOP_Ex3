
class Node:
    def __init__(self, id, pos: dict) -> None:
        self.pos = pos
        self.id = id

    def __repr__(self) -> str:
        return f"id:{self.id} pos:{self.pos}"

    def getId(self):
        return self.id

    def getPos(self):
        return self.Pos

    def setId(self, i: int):
        self.Id = i

    def setPos(self,pos: tuple):
        self.Pos = pos

    def __repr__(self) -> str:
        return f"id:{self.id} pos:{self.pos}"












