import random
import numpy

class maze:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = hash
        for y in range(h):
            row = []
            for x in range(w):
                row.append({
                    "x":x,
                    "y":y,
                    "visited": False,
                    "walls": {"N": True, "E": True, "S": True, "W": True}})
            self.maze.append(row)
    def is_valid(self, x: int, y: int) -> bool:
        if x < 0 or x > self.w-1:
            return False
        if y < 0 or y > self.y-1:
            return False
        if maze[x][y]{"visited"}:
            return False
    def dfs(self, start_pos:list[int]) -> list[list[dict]]:
        solved = False
        stack = []
        stack.append(start_pos[0])
        while not solved:
            