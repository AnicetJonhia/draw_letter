import shutil  
from colorama import Fore, Style, init

init(autoreset=True) 

SIZE = 7  
GAP = 2
COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def is_on(char, i, j):
    mid, last = SIZE // 2, SIZE - 1
    
    # Prédicats pour arrondir les coins (
    is_top_left = (i == 0 and j == 0)
    is_top_right = (i == 0 and j == last)
    is_bot_left = (i == last and j == 0)
    is_bot_right = (i == last and j == last)
    is_corner = is_top_left or is_top_right or is_bot_left or is_bot_right

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
        "S": (i == 0 and j > 0) or (i == mid and 0 < j < last) or (i == last and j < last) or (j == 0 and 0 < i < mid) or (j == last and mid < i < last),
        "T": i == 0 or j == mid,
        "U": (j == 0 and i < last) or (j == last and i < last) or (i == last and 0 < j < last),
        "V": (j == i//2 and i < last-1) or (j == last - i//2 and i < last-1) or (i == last and j == mid),
        "W": j == 0 or j == last or (i >= mid and (i == j or i + j == last)),
        "X": i == j or i + j == last,
        "Y": (i <= mid and (i == j or i + j == last)) or (i > mid and j == mid),
        "Z": i == 0 or i == last or i + j == last,
        
      
        "0": ( (i == 0 or i == last) and (0 < j < last) ) or ( (j == 0 or j == last) and (0 < i < last) ),
        "1": (j == mid) or (i == 1 and j == mid - 1) or (i == last and 0 < j < last+1),
        "2": (i == 0 and 0 < j < last) or (i == mid and 0 < j < last) or (i == last) or (j == last and 0 < i < mid) or (j == 0 and mid < i < last),
        "3": (i in [0, mid, last] and j < last) or (j == last and not is_corner),
        "4": (j == last) or (i == mid) or (j == 0 and i < mid),
        "5": (i == 0) or (i == mid and 0 < j < last) or (i == last and j < last) or (j == 0 and 0 < i < mid) or (j == last and mid < i < last),
        "6": (i == 0 and j > 0) or (i == mid and 0 < j < last) or (i == last and 0 < j < last) or (j == 0 and 0 < i < last) or (j == last and mid < i < last),
        "7": (i == 0) or (j == last and i > 0) or (i == mid and j > mid),
        "8": ( (i in [0, mid, last]) and 0 < j < last ) or ( (j == 0 or j == last) and not is_corner and i != mid ),
        "9": ( (i in [0, mid, last]) and 0 < j < last ) or ( j == last and 0 < i < last ) or ( j == 0 and 0 < i < mid ),
        " ": False
    }
    return p.get(char.upper(), False)

def draw(text):
    terminal_width = shutil.get_terminal_size().columns
    char_full_width = SIZE + GAP
    
    chars_per_line = max(1, terminal_width // char_full_width)
    
    # On garde une trace de l'index global pour la couleur
    global_pos = 0
    
    # Découper le texte par segments pour le wrapping
    for start in range(0, len(text), chars_per_line):
        segment = text[start : start + chars_per_line]
        
        for i in range(SIZE):
            line = ""
            for local_idx, ch in enumerate(segment):
                # Calcul de la couleur basée sur la position réelle dans la chaîne
                current_char_pos = global_pos + local_idx
                color = COLORS[current_char_pos % len(COLORS)]
                
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
        
        global_pos += len(segment)
        print("\n") 

    
if __name__ == "__main__":
    user_input = input("Entrez votre texte (lettres et chiffres) : ").strip()
    word = user_input.upper() if user_input else "Draw letter"

    print("\n" + "="*shutil.get_terminal_size().columns + "\n")
    draw(word)