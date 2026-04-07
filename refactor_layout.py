import re

# 1. Update index.html
with open(r'd:\jwoo\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_main = """<main class="flex-grow flex flex-col md:flex-row items-center justify-center p-2 md:p-8 gap-4 md:gap-8 overflow-hidden w-full max-w-4xl mx-auto">
<div class="flex flex-row items-start justify-center gap-4 w-full md:w-auto">
<aside class="flex flex-col gap-6 w-20 md:w-32 py-2">
<div class="space-y-1">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">SCORE</p>
<p id="score" class="text-2xl md:text-4xl font-headline font-black tracking-tighter text-primary">0</p>
</div>
<div class="space-y-1">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">LEVEL</p>
<p id="level" class="text-2xl md:text-4xl font-headline font-black tracking-tighter text-primary">1</p>
</div>
<div class="space-y-1">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">LINES</p>
<p id="lines" class="text-2xl md:text-4xl font-headline font-black tracking-tighter text-primary">0</p>
</div>
<div class="space-y-2 pt-4">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">NEXT</p>
<div class="w-16 h-16 md:w-24 md:h-24 bg-surface-container flex items-center justify-center relative border border-outline-variant">
    <canvas id="next-piece" width="96" height="96"></canvas>
</div>
</div>
</aside>
<section class="relative">
    <canvas id="game-board" width="300" height="600" class="bg-surface-container-low border-[4px] border-primary tetris-grid"></canvas>
    
    <div id="game-over" class="absolute inset-0 bg-[#f2ffcf] bg-opacity-90 flex flex-col items-center justify-center hidden">
        <h1 class="text-3xl font-black font-headline text-primary uppercase mb-2">GAME OVER</h1>
        <p class="text-xl font-bold mb-4 font-headline text-[#002104] uppercase">Score: <span id="final-score">0</span></p>
        <button id="restart-btn" class="bg-primary text-white font-headline px-4 py-2 font-bold border-4 border-primary hover:bg-[#CDF14B] hover:text-[#002104] transition-none uppercase">RESTART</button>
    </div>
</section>
</div>
<aside class="flex flex-col items-center gap-6 w-full max-w-xs md:mt-0 mt-2">
<div class="grid grid-cols-3 gap-2">
<div></div>
<button id="btn-up" class="w-14 h-14 md:w-16 md:h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">expand_less</span>
</button>
<div></div>
<button id="btn-left" class="w-14 h-14 md:w-16 md:h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button id="btn-down" class="w-14 h-14 md:w-16 md:h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">expand_more</span>
</button>
<button id="btn-right" class="w-14 h-14 md:w-16 md:h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
<div class="flex gap-4 w-full px-4">
<button id="btn-rotate" class="flex-1 py-3 bg-secondary text-white font-headline font-bold uppercase tracking-widest text-sm hover:opacity-90 active:bg-primary">
    ROT
</button>
<button id="btn-harddrop" class="flex-1 py-3 bg-surface-container-highest text-primary font-headline font-bold uppercase tracking-widest text-sm hover:opacity-90 active:bg-primary active:text-white">
    DROP
</button>
</div>
</aside>
</main>"""

html = re.sub(r'<main.*?</main>', new_main, html, flags=re.DOTALL)

with open(r'd:\jwoo\index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update script.js for better responsiveness
with open(r'd:\jwoo\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_sizing = """// Game Constants
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
nextCanvas.height = 4 * BLOCK_SIZE;"""

js = re.sub(r'// Game Constants.*?nextCanvas\.height = 4 \* BLOCK_SIZE;', new_sizing, js, flags=re.DOTALL)

with open(r'd:\jwoo\script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Layout refactored successfully.")
