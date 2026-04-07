import os

file1 = """<!DOCTYPE html>
<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "tertiary-fixed": "#cdf14b",
                        "surface-container-high": "#ddf0b1",
                        "inverse-surface": "#283508",
                        "surface-dim": "#cfe1a4",
                        "secondary-container": "#ccf157",
                        "secondary": "#516600",
                        "on-tertiary-fixed": "#171e00",
                        "on-secondary-container": "#566c00",
                        "surface-container-low": "#e9fbbc",
                        "error-container": "#ffdad6",
                        "inverse-primary": "#9dd496",
                        "on-tertiary-container": "#85a300",
                        "tertiary-container": "#293400",
                        "on-surface": "#141f00",
                        "surface-bright": "#f2ffcf",
                        "surface-container-highest": "#d8eaac",
                        "tertiary-fixed-dim": "#b2d42f",
                        "on-tertiary": "#ffffff",
                        "surface": "#f2ffcf",
                        "on-secondary": "#ffffff",
                        "surface-tint": "#376936",
                        "on-tertiary-fixed-variant": "#3d4c00",
                        "on-error": "#ffffff",
                        "primary-fixed-dim": "#9dd496",
                        "background": "#f2ffcf",
                        "on-primary-fixed-variant": "#1f5121",
                        "on-primary": "#ffffff",
                        "surface-container-lowest": "#ffffff",
                        "surface-container": "#e3f5b6",
                        "on-error-container": "#93000a",
                        "on-surface-variant": "#42493f",
                        "on-primary-fixed": "#002204",
                        "secondary-fixed-dim": "#b1d43d",
                        "on-secondary-fixed-variant": "#3c4d00",
                        "outline-variant": "#c2c9bc",
                        "primary": "#002104",
                        "outline": "#72796e",
                        "surface-variant": "#d8eaac",
                        "tertiary": "#171e00",
                        "primary-fixed": "#b8f1b1",
                        "on-secondary-fixed": "#161e00",
                        "on-background": "#141f00",
                        "primary-container": "#03390c",
                        "inverse-on-surface": "#e6f8b9",
                        "on-primary-container": "#70a56b",
                        "error": "#ba1a1a",
                        "secondary-fixed": "#ccf157"
                    },
                    "borderRadius": {
                        "DEFAULT": "0px",
                        "lg": "0px",
                        "xl": "0px",
                        "full": "0px"
                    },
                    "fontFamily": {
                        "headline": ["Space Grotesk"],
                        "body": ["Inter"],
                        "label": ["Space Grotesk"]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f2ffcf;
        }
        .pixel-text {
            font-family: 'Space Grotesk', sans-serif;
            text-transform: uppercase;
        }
        body {
          min-height: max(884px, 100dvh);
        }
    </style>
  </head>
<body class="bg-background text-on-surface min-h-screen flex flex-col items-center">
<header class="bg-[#f2ffcf] dark:bg-[#002104] text-[#002104] dark:text-[#f2ffcf] flex justify-between items-center w-full px-6 py-4 fixed top-0 z-50">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-[#002104] dark:text-[#f2ffcf]" data-icon="grid_view">grid_view</span>
<span class="text-2xl font-black tracking-tighter text-[#002104] dark:text-[#f2ffcf] font-['Space_Grotesk'] uppercase">TETRIS</span>
</div>
<div class="flex items-center">
<span class="font-['Space_Grotesk'] uppercase tracking-tighter font-bold text-[#002104] dark:text-[#f2ffcf]">LVL 01</span>
</div>
</header>
<main class="flex-grow w-full max-w-4xl flex flex-col justify-center items-center px-6 pt-24 pb-32">
<div class="w-full flex flex-col items-center mb-16">
<h1 class="text-7xl md:text-9xl font-black font-headline tracking-tighter text-primary text-center leading-none">
                TETRIS
            </h1>
<div class="mt-4 flex gap-2">
<div class="w-8 h-8 bg-primary"></div>
<div class="w-8 h-8 bg-secondary"></div>
<div class="w-8 h-8 bg-tertiary"></div>
<div class="w-8 h-8 bg-on-primary-container"></div>
</div>
</div>
<div class="w-full max-w-md space-y-4">
<button class="w-full h-20 bg-primary text-surface font-headline font-extrabold text-2xl flex items-center justify-center border-4 border-primary transition-none active:bg-surface active:text-primary">
                START GAME
            </button>
<div class="grid grid-cols-2 gap-4">
<button class="h-20 bg-surface-container-high border-4 border-primary text-primary font-headline font-bold text-xl flex items-center justify-center transition-none hover:bg-surface-container-highest active:bg-primary active:text-surface">
                    SCORES
                </button>
<button class="h-20 bg-surface-container-high border-4 border-primary text-primary font-headline font-bold text-xl flex items-center justify-center transition-none hover:bg-surface-container-highest active:bg-primary active:text-surface">
                    SETTINGS
                </button>
</div>
</div>
<div class="mt-16 w-full max-w-md">
<div class="bg-surface-container p-6 border-l-8 border-primary flex justify-between items-center">
<div class="flex flex-col">
<span class="font-label text-xs font-bold opacity-70">HIGH SCORE</span>
<span class="font-headline text-3xl font-black text-primary">000000</span>
</div>
<div class="flex flex-col items-end">
<span class="font-label text-xs font-bold opacity-70">VERSION</span>
<span class="font-headline text-lg font-bold text-primary">V1.0</span>
</div>
</div>
</div>
<div class="mt-12 flex items-center gap-4 opacity-30 select-none pointer-events-none">
<div class="w-4 h-4 rounded-full bg-primary"></div>
<div class="h-[1px] w-32 bg-primary"></div>
<span class="font-label text-[10px] font-bold tracking-widest">LICENSED TO TETRIS GMBH</span>
<div class="h-[1px] w-32 bg-primary"></div>
<div class="w-4 h-4 rounded-full bg-primary"></div>
</div>
</main>
<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-stretch h-16 bg-[#f2ffcf] dark:bg-[#002104]">
<div class="flex flex-col items-center justify-center bg-[#002104] dark:bg-[#f2ffcf] text-[#f2ffcf] dark:text-[#002104] p-4 flex-1">
<span class="material-symbols-outlined" data-icon="videogame_asset" style="font-variation-settings: 'FILL' 1;">videogame_asset</span>
</div>
<div class="flex flex-col items-center justify-center text-[#002104] dark:text-[#f2ffcf] opacity-50 p-4 flex-1 hover:bg-[#d8eaac] dark:hover:bg-[#171e00]">
<span class="material-symbols-outlined" data-icon="trophy">trophy</span>
</div>
<div class="flex flex-col items-center justify-center text-[#002104] dark:text-[#f2ffcf] opacity-50 p-4 flex-1 hover:bg-[#d8eaac] dark:hover:bg-[#171e00]">
<span class="material-symbols-outlined" data-icon="settings">settings</span>
</div>
</nav>
</body></html>"""

file2 = """<!DOCTYPE html>
<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-fixed": "#cdf14b",
                    "surface-container-high": "#ddf0b1",
                    "inverse-surface": "#283508",
                    "surface-dim": "#cfe1a4",
                    "secondary-container": "#ccf157",
                    "secondary": "#516600",
                    "on-tertiary-fixed": "#171e00",
                    "on-secondary-container": "#566c00",
                    "surface-container-low": "#e9fbbc",
                    "error-container": "#ffdad6",
                    "inverse-primary": "#9dd496",
                    "on-tertiary-container": "#85a300",
                    "tertiary-container": "#293400",
                    "on-surface": "#141f00",
                    "surface-bright": "#f2ffcf",
                    "surface-container-highest": "#d8eaac",
                    "tertiary-fixed-dim": "#b2d42f",
                    "on-tertiary": "#ffffff",
                    "surface": "#f2ffcf",
                    "on-secondary": "#ffffff",
                    "surface-tint": "#376936",
                    "on-tertiary-fixed-variant": "#3d4c00",
                    "on-error": "#ffffff",
                    "primary-fixed-dim": "#9dd496",
                    "background": "#f2ffcf",
                    "on-primary-fixed-variant": "#1f5121",
                    "on-primary": "#ffffff",
                    "surface-container-lowest": "#ffffff",
                    "surface-container": "#e3f5b6",
                    "on-error-container": "#93000a",
                    "on-surface-variant": "#42493f",
                    "on-primary-fixed": "#002204",
                    "secondary-fixed-dim": "#b1d43d",
                    "on-secondary-fixed-variant": "#3c4d00",
                    "outline-variant": "#c2c9bc",
                    "primary": "#002104",
                    "outline": "#72796e",
                    "surface-variant": "#d8eaac",
                    "tertiary": "#171e00",
                    "primary-fixed": "#b8f1b1",
                    "on-secondary-fixed": "#161e00",
                    "on-background": "#141f00",
                    "primary-container": "#03390c",
                    "inverse-on-surface": "#e6f8b9",
                    "on-primary-container": "#70a56b",
                    "error": "#ba1a1a",
                    "secondary-fixed": "#ccf157"
            },
            "borderRadius": {
                    "DEFAULT": "0px",
                    "lg": "0px",
                    "xl": "0px",
                    "full": "0px"
            },
            "fontFamily": {
                    "headline": ["Space Grotesk"],
                    "body": ["Inter"],
                    "label": ["Space Grotesk"]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        body { font-family: 'Inter', sans-serif; background-color: #f2ffcf; min-height: max(884px, 100dvh); }
        .digital-brutalist-bg {
            background-image: linear-gradient(rgba(20, 31, 0, 0.03) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(20, 31, 0, 0.03) 1px, transparent 1px);
            background-size: 20px 20px;
        }
    </style>
  </head>
<body class="bg-background text-on-background min-h-screen flex flex-col digital-brutalist-bg">
<header class="bg-[#f2ffcf] dark:bg-[#002104] flex justify-between items-center w-full px-6 py-4 fixed top-0 z-50">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-[#002104] dark:text-[#f2ffcf]">grid_view</span>
<span class="text-2xl font-black tracking-tighter text-[#002104] dark:text-[#f2ffcf] font-['Space_Grotesk'] uppercase">TETRIS</span>
</div>
<div class="font-['Space_Grotesk'] uppercase tracking-tighter font-bold text-[#002104] dark:text-[#f2ffcf]">LVL 01</div>
</header>
<main class="flex-grow flex flex-col items-center justify-center pt-24 pb-32 px-4 max-w-2xl mx-auto w-full">
<div class="w-full text-center mb-12">
<h1 class="font-headline text-5xl md:text-7xl font-black tracking-tighter text-primary uppercase mb-2">HALL OF FAME</h1>
<div class="h-1 w-full bg-primary mb-1"></div>
<div class="h-0.5 w-full bg-primary-container opacity-20"></div>
</div>
<div class="w-full bg-surface-container-low p-1 mb-8">
<div class="bg-surface-container border-2 border-primary p-6">
<div class="flex flex-col gap-1">
<div class="flex justify-between items-center py-3 px-4 bg-primary text-surface font-headline font-bold text-xl tracking-widest"><span class="w-12">01</span><span class="flex-grow text-left ml-4">CYBER_KING</span><span class="text-right">482,000</span></div>
<div class="flex justify-between items-center py-3 px-4 font-headline font-bold text-xl tracking-widest border-b border-outline-variant"><span class="w-12 text-secondary">02</span><span class="flex-grow text-left ml-4">NEO_PIXEL</span><span class="text-right">395,500</span></div>
<div class="flex justify-between items-center py-3 px-4 font-headline font-bold text-xl tracking-widest"><span class="w-12 text-secondary">03</span><span class="flex-grow text-left ml-4">GLITCH_BIT</span><span class="text-right">312,000</span></div>
</div>
</div>
</div>
<div class="w-full">
<button class="w-full bg-primary text-on-primary font-headline font-black text-2xl py-6 tracking-widest hover:bg-primary-container transition-none active:bg-secondary-container active:text-on-secondary-container uppercase">BACK</button>
</div>
</main>
<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-stretch h-16 bg-[#f2ffcf] dark:bg-[#002104]">
<a class="flex flex-col items-center justify-center text-[#002104] dark:text-[#f2ffcf] opacity-50 p-4 transition-none hover:bg-[#d8eaac] dark:hover:bg-[#171e00]" href="#"><span class="material-symbols-outlined">videogame_asset</span></a>
<a class="flex flex-col items-center justify-center bg-[#002104] dark:bg-[#f2ffcf] text-[#f2ffcf] dark:text-[#002104] p-4 transition-none" href="#"><span class="material-symbols-outlined">trophy</span></a>
<a class="flex flex-col items-center justify-center text-[#002104] dark:text-[#f2ffcf] opacity-50 p-4 transition-none hover:bg-[#d8eaac] dark:hover:bg-[#171e00]" href="#"><span class="material-symbols-outlined">settings</span></a>
</nav>
</body></html>"""

file3 = """<!DOCTYPE html>
<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "secondary": "#516600",
                        "primary": "#002104",
                        "surface-variant": "#d8eaac",
                        "primary-container": "#03390c",
                        "secondary-container": "#ccf157",
                        "background": "#f2ffcf"
                    },
                    "borderRadius": {
                        "DEFAULT": "0px",
                        "lg": "0px",
                        "xl": "0px",
                        "full": "0px"
                    },
                    "fontFamily": {
                        "headline": ["Space Grotesk"],
                        "body": ["Inter"],
                        "label": ["Space Grotesk"]
                    }
                },
            },
        }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; background-color: #f2ffcf; color: #141f00; margin: 0; min-height: max(884px, 100dvh); }
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        .brutalist-grid { background-image: radial-gradient(#c2c9bc 1px, transparent 1px); background-size: 24px 24px; }
    </style>
  </head>
<body class="bg-background text-on-background min-h-screen flex flex-col items-center">
<header class="bg-[#f2ffcf] dark:bg-[#002104] flex justify-between items-center w-full px-6 py-4 z-50">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-[#002104] dark:text-[#f2ffcf]">grid_view</span>
<h1 class="text-2xl font-black tracking-tighter text-[#002104] dark:text-[#f2ffcf] font-['Space_Grotesk'] uppercase">TETRIS</h1>
</div>
</header>
<main class="flex-grow w-full max-w-4xl flex flex-col justify-center items-center p-6 brutalist-grid">
<div class="w-full max-w-md bg-surface-variant bg-opacity-85 backdrop-blur-md p-1 items-center justify-center flex flex-col shadow-[0px_32px_32px_rgba(20,31,0,0.05)] border-0">
<div class="bg-surface border-0 w-full p-8 flex flex-col items-center text-center">
<h2 class="text-6xl font-black font-headline tracking-tighter text-primary mb-12 uppercase">GAME OVER</h2>
<div class="grid grid-cols-1 gap-4 w-full">
<button class="bg-primary text-on-primary py-4 px-8 font-label font-bold text-lg transition-none active:bg-primary uppercase">RETRY</button>
<button class="bg-secondary-container text-on-secondary-container py-4 px-8 font-label font-bold text-lg transition-none active:bg-secondary uppercase">QUIT</button>
</div>
</div>
</div>
</main>
</body></html>"""

file4 = """<!DOCTYPE html>
<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-fixed": "#cdf14b",
                    "surface-container-high": "#ddf0b1",
                    "inverse-surface": "#283508",
                    "surface-dim": "#cfe1a4",
                    "secondary-container": "#ccf157",
                    "secondary": "#516600",
                    "surface-container-low": "#e9fbbc",
                    "tertiary": "#171e00",
                    "background": "#f2ffcf",
                    "primary": "#002104"
            },
            "borderRadius": {
                    "DEFAULT": "0px",
                    "full": "9999px"
            },
            "fontFamily": {
                    "headline": ["Space Grotesk"],
                    "body": ["Inter"],
                    "label": ["Space Grotesk"]
            }
          },
        },
      }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; min-height: max(884px, 100dvh); }
        .font-headline { font-family: 'Space Grotesk', sans-serif; }
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        .tetris-grid {
            background-size: 30px 30px;
            background-image: 
                linear-gradient(to right, rgba(194, 201, 188, 0.2) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(194, 201, 188, 0.2) 1px, transparent 1px);
        }
    </style>
  </head>
<body class="bg-background text-on-surface min-h-screen flex flex-col">
<header class="bg-[#f2ffcf] dark:bg-[#002104] justify-between items-center flex w-full px-6 py-4 sticky top-0 z-50 text-[#002104] dark:text-[#f2ffcf]">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined">grid_view</span>
<h1 class="text-2xl font-black tracking-tighter font-headline uppercase">TETRIS</h1>
</div>
<div class="flex items-center">
<span class="font-headline uppercase tracking-tighter font-bold">LVL 01</span>
</div>
</header>
<main class="flex-grow flex flex-col md:flex-row items-center justify-center p-4 md:p-8 gap-8 overflow-hidden">
<aside class="flex flex-row md:flex-col gap-6 md:w-48 justify-between w-full max-w-md md:max-w-none">
<div class="space-y-1">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">SCORE</p>
<p id="score-display" class="text-4xl font-headline font-black tracking-tighter text-primary">0</p>
</div>
<div class="space-y-1">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">LEVEL</p>
<p id="level-display" class="text-4xl font-headline font-black tracking-tighter text-primary">1</p>
</div>
<div class="space-y-1">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">LINES</p>
<p id="lines-display" class="text-4xl font-headline font-black tracking-tighter text-primary">0</p>
</div>
<div class="hidden md:block space-y-4 pt-8">
<p class="text-[10px] font-headline font-bold uppercase text-secondary">NEXT</p>
<div class="w-24 h-24 bg-surface-container flex items-center justify-center relative">
    <canvas id="next-piece" width="96" height="96"></canvas>
</div>
</div>
</aside>
<section class="relative">
    <canvas id="game-board" width="300" height="600" class="bg-surface-container-low border-[4px] border-primary tetris-grid"></canvas>
    
    <div id="game-over-overlay" class="absolute inset-0 bg-[#f2ffcf] bg-opacity-90 flex flex-col items-center justify-center hidden">
        <h1 class="text-4xl font-black font-headline text-primary uppercase mb-4">GAME OVER</h1>
        <button id="restart-btn" class="bg-primary text-white font-headline px-6 py-3 font-bold border-4 border-primary hover:bg-[#CDF14B] hover:text-[#002104] transition-none uppercase">RESTART</button>
    </div>
</section>
<aside class="flex flex-col items-center gap-8 w-full max-w-xs">
<div class="grid grid-cols-3 gap-2">
<div></div>
<button id="btn-up" class="w-16 h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">expand_less</span>
</button>
<div></div>
<button id="btn-left" class="w-16 h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button id="btn-down" class="w-16 h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">expand_more</span>
</button>
<button id="btn-right" class="w-16 h-16 bg-primary text-white flex items-center justify-center hover:opacity-80 active:scale-95 transition-none">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
<div class="flex gap-4 w-full">
<button id="btn-rotate" class="flex-1 py-4 bg-secondary text-white font-headline font-bold uppercase tracking-widest text-sm hover:opacity-90 active:bg-primary">
                    ROTATE
                </button>
<button id="btn-harddrop" class="flex-1 py-4 bg-surface-container-highest text-primary font-headline font-bold uppercase tracking-widest text-sm hover:opacity-90 active:bg-primary active:text-white">
                    DROP
                </button>
</div>
</aside>
</main>
<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-stretch h-16 bg-[#f2ffcf] dark:bg-[#002104]">
<div class="flex flex-col items-center justify-center bg-[#002104] dark:bg-[#f2ffcf] text-[#f2ffcf] dark:text-[#002104] p-4 flex-1">
<span class="material-symbols-outlined">videogame_asset</span>
</div>
<div class="flex flex-col items-center justify-center text-[#002104] dark:text-[#f2ffcf] opacity-50 p-4 flex-1">
<span class="material-symbols-outlined">trophy</span>
</div>
<div class="flex flex-col items-center justify-center text-[#002104] dark:text-[#f2ffcf] opacity-50 p-4 flex-1">
<span class="material-symbols-outlined">settings</span>
</div>
</nav>
<div class="h-16"></div>
<script src="script.js"></script>
</body></html>"""

with open(r"d:\jwoo\1.md", "w", encoding="utf-8") as f: f.write(file1)
with open(r"d:\jwoo\2.md", "w", encoding="utf-8") as f: f.write(file2)
with open(r"d:\jwoo\3.md", "w", encoding="utf-8") as f: f.write(file3)
with open(r"d:\jwoo\4.md", "w", encoding="utf-8") as f: f.write(file4)
with open(r"d:\jwoo\index.html", "w", encoding="utf-8") as f: f.write(file4) # We apply 4.md to index.html
