import re

files = [r'd:\jwoo\1.md', r'd:\jwoo\2.md', r'd:\jwoo\3.md', r'd:\jwoo\4.md']

tailwind_config_pattern = re.compile(r'<script id="tailwind-config">.*?</script>', re.DOTALL)
style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)

new_config_and_styles = """<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        primary: "#0ea5e9",
                        secondary: "#f43f5e",
                        tertiary: "#8b5cf6",
                        background: "#0f172a",
                        surface: "#1e293b",
                        surfaceLight: "#334155",
                        onPrimary: "#ffffff",
                        onBackground: "#f8fafc",
                        onSurface: "#f8fafc",
                    },
                    fontFamily: {
                        headline: ["Space Grotesk", "sans-serif"],
                        body: ["Inter", "sans-serif"]
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; }
        .glass-panel {
            background: rgba(30, 41, 59, 0.5) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }
        .neon-text {
            color: #fff;
            text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #0ea5e9, 0 0 40px #0ea5e9, 0 0 80px #0ea5e9;
        }
        .neon-text-secondary {
            color: #fff;
            text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #f43f5e, 0 0 40px #f43f5e;
        }
        .neon-border {
            box-shadow: 0 0 10px rgba(14, 165, 233, 0.5), inset 0 0 10px rgba(14, 165, 233, 0.5);
        }
        .material-symbols-outlined { font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        .tetris-grid {
            background-size: 30px 30px;
            background-image: linear-gradient(to right, rgba(14, 165, 233, 0.15) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(14, 165, 233, 0.15) 1px, transparent 1px);
        }
        /* Make all buttons look modern neon */
        button { border-radius: 8px !important; transition: all 0.3s ease !important; }
        button.bg-primary { background: linear-gradient(135deg, #0ea5e9, #3b82f6) !important; color: white !important; border: none !important; box-shadow: 0 4px 15px rgba(14, 165, 233, 0.5); }
        button.bg-primary:hover { transform: scale(1.05); box-shadow: 0 6px 20px rgba(14, 165, 233, 0.7); }
        button.bg-surface-container-high { background: rgba(30, 41, 59, 0.7) !important; backdrop-filter: blur(10px); color: #0ea5e9 !important; border: 1px solid rgba(14, 165, 233, 0.5) !important; }
        button.bg-surface-container-high:hover { background: rgba(30, 41, 59, 0.9) !important; transform: scale(1.05); box-shadow: 0 0 15px rgba(14, 165, 233, 0.3); }
        button.bg-secondary-container { background: linear-gradient(135deg, #f43f5e, #e11d48) !important; color: white !important; border: none !important; box-shadow: 0 4px 15px rgba(244, 63, 94, 0.5); }
        button.bg-secondary-container:hover { transform: scale(1.05); box-shadow: 0 6px 20px rgba(244, 63, 94, 0.7); }
        
        .bg-surface-container, .bg-surface-container-low, .bg-surface-variant {
            background: rgba(30, 41, 59, 0.6) !important; backdrop-filter: blur(12px); border-radius: 16px !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }
        nav { background: rgba(15, 23, 42, 0.8) !important; backdrop-filter: blur(16px); border-top: 1px solid rgba(255,255,255,0.1); }
        header { background: rgba(15, 23, 42, 0.8) !important; backdrop-filter: blur(16px); border-bottom: 1px solid rgba(255,255,255,0.1); }
        
        .text-primary { color: #38bdf8 !important; text-shadow: 0 0 10px rgba(56, 189, 248, 0.4); }
        .text-secondary { color: #f472b6 !important; text-shadow: 0 0 10px rgba(244, 114, 182, 0.4); }
        .border-primary { border-color: #0ea5e9 !important; border-radius: 12px; }
    </style>"""

replacements = {
    'bg-[#f2ffcf]': 'bg-transparent',
    'dark:bg-[#002104]': 'dark:bg-transparent',
    'text-[#002104]': 'text-onBackground',
    'dark:text-[#f2ffcf]': 'dark:text-onBackground',
    'bg-[#002104]': 'bg-surfaceLight/50',
    'dark:bg-[#f2ffcf]': 'dark:bg-surfaceLight/50',
    'text-[#f2ffcf]': 'text-onSurface',
    'dark:text-[#002104]': 'dark:text-onSurface',
    'bg-[#d8eaac]': 'bg-surfaceLight',
    'dark:hover:bg-[#171e00]': 'dark:hover:bg-surfaceLight',
    'text-7xl md:text-9xl font-black font-headline tracking-tighter text-primary text-center leading-none': 'text-7xl md:text-9xl font-black font-headline tracking-tighter neon-text text-center leading-none',
    'text-6xl font-black font-headline tracking-tighter text-primary mb-12 uppercase': 'text-6xl font-black font-headline tracking-tighter neon-text-secondary mb-12 uppercase',
    'transition-none': 'transition-all duration-300 ease-in-out',
    'brutalist-grid': 'cyber-grid'
}

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = style_pattern.sub('', content)
    content = tailwind_config_pattern.sub(new_config_and_styles, content)
    
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Redesign updated successfully.")
