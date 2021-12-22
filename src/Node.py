import json
import matplotlib.pyplot as plt
import numpy as np


class Node:
    # count=0
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
        selfId = i

    def setPos(self, i: int):
        selfPos = i











