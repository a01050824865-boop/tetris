// DOM Elements
const canvas = document.getElementById('game-board');
const ctx = canvas.getContext('2d');
const nextCanvas = document.getElementById('next-piece');
const nextCtx = nextCanvas.getContext('2d');

const scoreElement = document.getElementById('score');
const levelElement = document.getElementById('level');
const linesElement = document.getElementById('lines');

// Game Constants
const ROWS = 20;
const COLS = 10;
// Dynamically calculate block size responsive to screen height & width
const availableHeight = window.innerHeight - 280; // controls + navbar
const availableWidth = window.innerWidth - 120; // safe area for left sidebar
let BLOCK_SIZE = Math.max(15, Math.min(30, 
    Math.min(
        Math.floor(availableHeight / ROWS),
        Math.floor(availableWidth / COLS)
    )
));

// Resize canvases appropriately
canvas.width = COLS * BLOCK_SIZE;
canvas.height = ROWS * BLOCK_SIZE;
canvas.style.backgroundSize = `${BLOCK_SIZE}px ${BLOCK_SIZE}px`;

nextCanvas.width = 4 * BLOCK_SIZE;
nextCanvas.height = 4 * BLOCK_SIZE;
// Initialize board
let board = Array.from({ length: ROWS }, () => Array(COLS).fill(0));

// Tetromino Definitions
const SHAPES = [
    [], // 0
    [ [0,0,0,0], [1,1,1,1], [0,0,0,0], [0,0,0,0] ], // I - 1
    [ [2,0,0], [2,2,2], [0,0,0] ],                 // J - 2
    [ [0,0,3], [3,3,3], [0,0,0] ],                 // L - 3
    [ [4,4], [4,4] ],                              // O - 4
    [ [0,5,5], [5,5,0], [0,0,0] ],                 // S - 5
    [ [0,6,0], [6,6,6], [0,0,0] ],                 // T - 6
    [ [7,7,0], [0,7,7], [0,0,0] ]                  // Z - 7
];

const COLORS = [
    '#000',      // 0: Empty
    '#00ffff',   // 1: I (Cyan)
    '#0000ff',   // 2: J (Blue)
    '#ff7f00',   // 3: L (Orange)
    '#ffff00',   // 4: O (Yellow)
    '#00ff00',   // 5: S (Green)
    '#800080',   // 6: T (Purple)
    '#ff0000'    // 7: Z (Red)
];

let dropCounter = 0;
let dropInterval = 1000;
let lastTime = 0;
let animationId;

let score = 0;
let lines = 0;
let level = 1;
let isGameOver = false;

let currentPiece = null;
let nextPieceObj = null;

class Piece {
    constructor(shape, colorId) {
        this.shape = shape;
        this.colorId = colorId;
        this.x = Math.floor(COLS / 2) - Math.floor(shape[0].length / 2);
        this.y = 0;
    }

    draw(context = ctx, xOffset = 0, yOffset = 0) {
        for (let r = 0; r < this.shape.length; r++) {
            for (let c = 0; c < this.shape[r].length; c++) {
                if (this.shape[r][c] !== 0) {
                    drawBlock(context, this.x + c + xOffset, this.y + r + yOffset, COLORS[this.colorId]);
                }
            }
        }
    }

    moveDown() {
        if (isValid(0, 1)) {
            this.y++;
        } else {
            lockPiece();
            currentPiece = randomPiece();
        }
    }

    moveLeft() {
        if (isValid(-1, 0)) {
            this.x--;
        }
    }

    moveRight() {
        if (isValid(1, 0)) {
            this.x++;
        }
    }

    rotate() {
        const rotated = this.shape[0].map((val, index) => 
            this.shape.map(row => row[index]).reverse()
        );
        if (isValid(0, 0, rotated)) {
            this.shape = rotated;
        } else if (isValid(1, 0, rotated)) {
            this.x++;
            this.shape = rotated;
        } else if (isValid(-1, 0, rotated)) {
            this.x--;
            this.shape = rotated;
        }
    }

    hardDrop() {
        while (isValid(0, 1)) {
            this.y++;
        }
        this.moveDown();
    }
}

function randomPiece() {
    const id = Math.floor(Math.random() * 7) + 1;
    return new Piece(SHAPES[id], id);
}

function spawnPiece() {
    if (!nextPieceObj) {
        nextPieceObj = randomPiece();
    }
    currentPiece = nextPieceObj;
    nextPieceObj = randomPiece();
    drawNextPiece();
    
    if (!isValid(0, 0)) {
        gameOver();
    }
}

function drawNextPiece() {
    nextCtx.clearRect(0, 0, nextCanvas.width, nextCanvas.height);
    
    if (nextPieceObj) {
        const rows = nextPieceObj.shape.length;
        const cols = nextPieceObj.shape[0].length;
        const xOffset = (4 - cols) / 2;
        const yOffset = (4 - rows) / 2;
        
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (nextPieceObj.shape[r][c] !== 0) {
                    drawBlock(nextCtx, c + xOffset, r + yOffset, COLORS[nextPieceObj.colorId]);
                }
            }
        }
    }
}

function isValid(offsetX, offsetY, newShape) {
    offsetX = offsetX || 0;
    offsetY = offsetY || 0;
    newShape = newShape || currentPiece.shape;

    for (let r = 0; r < newShape.length; r++) {
        for (let c = 0; c < newShape[r].length; c++) {
            if (newShape[r][c] !== 0) {
                let newX = currentPiece.x + c + offsetX;
                let newY = currentPiece.y + r + offsetY;

                if (newX < 0 || newX >= COLS || newY >= ROWS) {
                    return false;
                }
                if (newY >= 0 && board[newY][newX] !== 0) {
                    return false;
                }
            }
        }
    }
    return true;
}

function lockPiece() {
    for (let r = 0; r < currentPiece.shape.length; r++) {
        for (let c = 0; c < currentPiece.shape[r].length; c++) {
            if (currentPiece.shape[r][c] !== 0) {
                if (currentPiece.y + r < 0) {
                    gameOver();
                    return; 
                }
                board[currentPiece.y + r][currentPiece.x + c] = currentPiece.colorId;
            }
        }
    }
    
    if (isGameOver) return;
    clearLines();
    spawnPiece();
}

function clearLines() {
    let linesCleared = 0;
    
    outer: for (let r = ROWS - 1; r >= 0; r--) {
        for (let c = 0; c < COLS; c++) {
            if (board[r][c] === 0) continue outer;
        }
        
        const row = board.splice(r, 1)[0].fill(0);
        board.unshift(row);
        r++;
        linesCleared++;
    }
    
    if (linesCleared > 0) {
        updateScore(linesCleared);
    }
}

function updateScore(linesCleared) {
    const lineScores = [0, 40, 100, 300, 1200];
    score += lineScores[linesCleared] * level;
    lines += linesCleared;
    level = Math.floor(lines / 10) + 1;
    dropInterval = Math.max(100, 1000 - (level - 1) * 100);
    
    scoreElement.innerText = score;
    levelElement.innerText = level;
    linesElement.innerText = lines;
}

function gameOver() {
    isGameOver = true;
    cancelAnimationFrame(animationId);
    document.getElementById('final-score').innerText = score;
    document.getElementById('game-over').classList.remove('hidden');
}

function resetGame() {
    board = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
    score = 0;
    lines = 0;
    level = 1;
    dropInterval = 1000;
    isGameOver = false;
    
    scoreElement.innerText = score;
    levelElement.innerText = level;
    linesElement.innerText = lines;
    
    document.getElementById('game-over').classList.add('hidden');
    
    nextPieceObj = null;
    spawnPiece();
    lastTime = performance.now();
    update(lastTime);
}

document.getElementById('restart-btn').addEventListener('click', resetGame);

document.addEventListener('keydown', event => {
    if (!currentPiece || isGameOver) return;
    
    if ([32, 37, 38, 39, 40].includes(event.keyCode)) {
        event.preventDefault();
    }
    
    switch (event.keyCode) {
        case 37:
            currentPiece.moveLeft();
            draw();
            break;
        case 38:
            currentPiece.rotate();
            draw();
            break;
        case 39:
            currentPiece.moveRight();
            draw();
            break;
        case 40:
            currentPiece.moveDown();
            draw();
            break;
        case 32:
            currentPiece.hardDrop();
            draw();
            break;
    }
});

function drawGrid() {
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    for (let r = 0; r <= ROWS; r++) {
        ctx.beginPath();
        ctx.moveTo(0, r * BLOCK_SIZE);
        ctx.lineTo(canvas.width, r * BLOCK_SIZE);
        ctx.stroke();
    }
    for (let c = 0; c <= COLS; c++) {
        ctx.beginPath();
        ctx.moveTo(c * BLOCK_SIZE, 0);
        ctx.lineTo(c * BLOCK_SIZE, canvas.height);
        ctx.stroke();
    }
}

function drawBlock(context, x, y, color) {
    context.fillStyle = color;
    context.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
    
    // pseudo-3D effect
    context.fillStyle = 'rgba(255, 255, 255, 0.2)';
    context.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, 3);
    context.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, 3, BLOCK_SIZE);
    
    context.fillStyle = 'rgba(0, 0, 0, 0.4)';
    context.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE + BLOCK_SIZE - 3, BLOCK_SIZE, 3);
    context.fillRect(x * BLOCK_SIZE + BLOCK_SIZE - 3, y * BLOCK_SIZE, 3, BLOCK_SIZE);
}

function drawBoard() {
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (board[r][c] !== 0) {
                drawBlock(ctx, c, r, COLORS[board[r][c]]);
            }
        }
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    drawBoard();
    // Grid rendering is handled natively via the tetris-grid CSS class 
    if (currentPiece) currentPiece.draw();
}

function update(time = 0) {
    if (isGameOver) return;

    const deltaTime = time - lastTime;
    lastTime = time;
    
    dropCounter += deltaTime;
    if (dropCounter > dropInterval) {
        if (currentPiece) currentPiece.moveDown();
        dropCounter = 0;
    }
    
    draw();
    animationId = requestAnimationFrame(update);
}

function init() {
    board = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
    spawnPiece();
    lastTime = performance.now();
    update(lastTime);
}

init();

/* Mobile Controls Binding */
function setupMobileControls() {
    const handleControl = (action) => {
        if (!currentPiece || isGameOver) return;
        action();
        draw();
    };

    const bindButton = (id, action) => {
        const btn = document.getElementById(id);
        if (!btn) return;
        
        btn.addEventListener('touchstart', (e) => { 
            e.preventDefault(); 
            handleControl(action); 
        }, {passive: false});
        
        btn.addEventListener('click', (e) => { 
            e.preventDefault(); 
            handleControl(action); 
        });
    };

    bindButton('btn-left', () => currentPiece.moveLeft());
    bindButton('btn-right', () => currentPiece.moveRight());
    bindButton('btn-down', () => currentPiece.moveDown());
    bindButton('btn-up', () => currentPiece.rotate());
    bindButton('btn-rotate', () => currentPiece.rotate());
    bindButton('btn-harddrop', () => currentPiece.hardDrop());
}

setupMobileControls();
