import shutil  
from colorama import Fore, Style, init

init(autoreset=True) 

SIZE = 7  
GAP = 2
COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def is_on(char, i, j):
    mid, last = SIZE // 2, SIZE - 1
    p = {
        "A": (i == 0 and 0 < j < last) or (i > 0 and (j == 0 or j == last)) or (i == mid),
        "B": (j == 0) or (i in [0, mid, last] and j < last) or (j == last and i != 0 and i != mid and i != last),
        "C": (i == 0 and j > 0) or (i == last and j > 0) or (j == 0 and 0 < i < last),
        "D": (j == 0) or (i in [0, last] and j < last) or (j == last and 0 < i < last),
        "E": i in [0, mid, last] or j == 0,
        "F": i in [0, mid] or j == 0,
        "G": (i == 0 and j > 0) or (i == last and j > 0 and j < mid+1) or (j == 0 and 0 < i < last) or (i >= mid and j == mid+1) or (i == mid and j > mid),
        "H": j == 0 or j == last or i == mid,
        "I": i == 0 or i == last or j == mid,
        "J": (i == 0) or (j == last and i < last) or (i == last and 0 < j < last) or (i >= last-2 and j == 0),
        "K": j == 0 or j == abs(mid - i) + 1,
        "L": j == 0 or i == last,
        "M": j == 0 or j == last or (i <= mid and (i == j or i + j == last)),
        "N": j == 0 or j == last or i == j,
        "O": (0 < i < last and (j == 0 or j == last)) or (0 < j < last and (i == 0 or i == last)),
        "P": j == 0 or (i in [0, mid] and j < last) or (j == last and 0 < i < mid),
        "Q": ((0 < i < last-1 and (j == 0 or j == last-1)) or (0 < j < last-1 and (i == 0 or i == last-1))) or (i == j and i > mid),
        "R": j == 0 or (i in [0, mid] and j < last) or (j == last and 0 < i < mid) or (i > mid and j == i),
        "S": (i in [0, mid, last]) or (j == 0 and i < mid) or (j == last and i > mid),
        "T": i == 0 or j == mid,
        "U": (j == 0 and i < last) or (j == last and i < last) or (i == last and 0 < j < last),
        "V": (j == i//2 and i < last-1) or (j == last - i//2 and i < last-1) or (i == last and j == mid),
        "W": j == 0 or j == last or (i >= mid and (i == j or i + j == last)),
        "X": i == j or i + j == last,
        "Y": (i <= mid and (i == j or i + j == last)) or (i > mid and j == mid),
        "Z": i == 0 or i == last or i + j == last,
    }
    return p.get(char.upper(), False)

def print_word_wrapped(text):
    # 1. Détecter la largeur du terminal
    terminal_width = shutil.get_terminal_size().columns
    char_full_width = SIZE + GAP
    
    # 2. Calculer combien de caractères max par ligne
    chars_per_line = max(1, terminal_width // char_full_width)
    
    # 3. Découper le mot en segments
    words_segments = [text[i:i+chars_per_line] for i in range(0, len(text), chars_per_line)]
    
    # 4. Afficher chaque segment
    for segment in words_segments:
        for i in range(SIZE):
            line = ""
            for idx_in_seg, ch in enumerate(segment):
                # Pour garder la couleur cohérente avec la position globale dans le mot original
                global_idx = text.find(ch) 
                color = COLORS[global_idx % len(COLORS)]
                
                if ch == " ":
                    line += " " * char_full_width
                    continue
                
                for j in range(SIZE):
                    if is_on(ch, i, j):
                        line += color + "█"
                    else:
                        line += " "
                line += " " * GAP
            print(line)
        print("\n") # Espace entre les blocs de lignes

# --- EXECUTION ---
user_input = input("Entrez votre mot : ").strip()
word = user_input.upper() if user_input else "DRAW LETTER"

print("\n" + "="*shutil.get_terminal_size().columns + "\n")
print_word_wrapped(word)