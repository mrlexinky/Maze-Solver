function generateMaze(){
  fetch("/maze.json")
    .then(response => response.json()) // Convert the response to JSON
    .then(mazeData => {
      const canvas = document.getElementById("maze-canvas");
      const ctx = canvas.getContext("2d");

      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const rows = mazeData.maze.length;
      const cols = mazeData[0].length;

      const cellSize = Math.min(
        canvas.width / cols,
        canvas.height / rows
      );


      // Set line style for drawing walls
      ctx.lineWidth = 2;
      ctx.strokeStyle = "black";

      // Loop through each cell in the maze
      for (let y = 0; y < rows; y++) {
        for (let x = 0; x < cols; x++) {
          const cell = mazeData[y][x];

          // Calculate the top-left corner of this cell
          const px = x * cellSize;
          const py = y * cellSize;

          // Draw each wall if it exists
          if (cell.walls.N) {
            ctx.beginPath();
            ctx.moveTo(px, py);
            ctx.lineTo(px + cellSize, py);
            ctx.stroke();
          }

          if (cell.walls.E) {
            ctx.beginPath();
            ctx.moveTo(px + cellSize, py);
            ctx.lineTo(px + cellSize, py + cellSize);
            ctx.stroke();
          }

          if (cell.walls.S) {
            ctx.beginPath();
            ctx.moveTo(px, py + cellSize);
            ctx.lineTo(px + cellSize, py + cellSize);
            ctx.stroke();
          }

          if (cell.walls.W) {
            ctx.beginPath();
            ctx.moveTo(px, py);
            ctx.lineTo(px, py + cellSize);
            ctx.stroke();
          }
        }
      }
    })
}

const generateButton = document.getElementById("generate-btn")

generateButton.addEventListener("click", generateMaze)

  // Fill in visited cells with light blue (optional)
  if (cell.visited) {
    ctx.fillStyle = "#bfdbfe"; // light blue
    ctx.fillRect(
      px + 1,
      py + 1,
      cellSize - 2,
      cellSize - 2
    );
  }