import os

# Fix IDs in index.html to match what script.js expects
with open(r'd:\jwoo\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('score-display', 'score')
c = c.replace('level-display', 'level')
c = c.replace('lines-display', 'lines')
c = c.replace('game-over-overlay', 'game-over')

if 'final-score' not in c:
    c = c.replace('GAME OVER</h1>', 'GAME OVER</h1>\n        <p class="text-2xl font-bold mb-4 font-headline text-[#002104] uppercase">Final Score: <span id="final-score">0</span></p>')

with open(r'd:\jwoo\index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Restore style.css to the brutalist configuration just in case
original_css = """@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: #f2ffcf;
    color: #141f00;
}

.game-container {
    display: flex;
    gap: 30px;
}

#game-board {
    background-color: #000;
    border: 2px solid #444;
}

#next-piece {
    background-color: #000;
}
"""
with open(r'd:\jwoo\style.css', 'w', encoding='utf-8') as f:
    f.write(original_css)

print("IDs fixed and CSS cleaned.")
