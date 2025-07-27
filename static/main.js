const rawData = document.getElementById("maze-data").textContent;
const mazeData = JSON.parse(rawData);

const container = document.getElementById("maze-container");

const height = mazeData.length;
const width = mazeData[0].length;

container.style.display = 'grid';
container.style.gridTemplateColumns = `repeat(${width}, 40px)`;
container.style.gridTemplateRows = `repeat(${height}, 40px)`;

for (let y = 0; y < height; y++) {
  for (let x = 0; x < width; x++) {
    const cell = mazeData[y][x];
    const walls = cell.walls;

    const cellDiv = document.createElement('div');
    cellDiv.classList.add('w-10', 'h-10');

    if (walls.N) cellDiv.classList.add('border-t', 'border-black', 'color');
    if (walls.E) cellDiv.classList.add('border-r', 'border-black');
    if (walls.S) cellDiv.classList.add('border-b', 'border-black');
    if (walls.W) cellDiv.classList.add('border-l', 'border-black');

    cellDiv.classList.add(cell.visited ? 'bg-blue-200' : 'bg-white');

    container.appendChild(cellDiv);
  }
}