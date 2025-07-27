import random
import numpy

class maze:
    def __init__(self):
        self.maze = []
    def generate_maze(self, w: int, h: int) -> list[list[dict]]:
        for y in range(h):
            row = []
            for x in range(w):
                row.append({
                    "x":x,
                    "y":y,
                    "visited": False,
                    "walls": {"N": True, "E": True, "S": True, "W": True}})
            self.maze.append(row)
        return self.maze
    def dfs(self, start_pos:list[int], end_pos:list[int]) -> list[list[dict]]:
        solved = False
        while not solved:
        
