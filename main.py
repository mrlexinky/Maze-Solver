import random as rand
import numpy as np
import json

from flask import Flask, render_template

class maze:
    def __init__(self, w: int, h: int):
        self.maze = []
        self.w = w
        self.h = h

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
        if y < 0 or y > self.h-1:
            return False
        if self.maze[y][x]["visited"]:
            return False
        return True
    
    def remove_wall(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if dx == 1:
            self.maze[y1][x1]["walls"]["E"] = False
            self.maze[y2][x2]["walls"]["W"] = False
        elif dx == -1:
            self.maze[y1][x1]["walls"]["W"] = False
            self.maze[y2][x2]["walls"]["E"] = False
        elif dy == 1:
            self.maze[y1][x1]["walls"]["S"] = False
            self.maze[y2][x2]["walls"]["N"] = False
        elif dy == -1:
            self.maze[y1][x1]["walls"]["N"] = False
            self.maze[y2][x2]["walls"]["S"] = False
            
    def dfs(self, start_pos: list[int]) -> list[list[dict]]:
        stack = [start_pos]

        while stack:
            x, y = stack[-1]
            self.maze[y][x]["visited"] = True

            neighbors = []
            for dx, dy in [ (0, -1), (1, 0), (0, 1), (-1, 0) ]:
                sx, sy = x + dx, y + dy
                if self.is_valid(sx, sy):
                    neighbors.append((sx, sy))

            if neighbors:
                sx, sy = rand.choice(neighbors)
                self.remove_wall(x, y, sx, sy)
                stack.append((sx, sy))
            else:
                stack.pop()

        return self.maze
                
m = maze(10,10)

app = Flask(__name__)

@app.route("/")
def home():
    maze_data = m.dfs([0,0])
    maze_json = json.dumps(maze_data)
    return render_template("index.html", maze_json=maze_json)

if __name__ == "__main__":
    app.run(debug = True)