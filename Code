import random

ROWS = 3
COLS = 3
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

symbols = { "A": 2, "B": 4 , "C": 6 , "D": 8}

payouts = {"A": 5, "B": 4, "C": 3, "D": 2}

def get_spin(rows, cols, symbols):
    pool = []
    for sym, count in symbols.items():
        pool.extend([sym] * count)
    spin = random.choices(pool, k=rows * cols)
    return [spin[i * cols:(i + 1) * cols] for i in range(rows)]

def print_spin(spin):
    for row in spin:
        print(" | ".join(row))

def check_win(spin, lines, bet):
    total = 0
    win_lines = []
    for i in range(lines):
        if all(s == spin[i][0] for s in spin[i]):
            total += payouts[spin[i][0]] * bet
            win_lines.append(i + 1)
    return total, win_lines

def get_number(msg, min_val, max_val):
    while True:
        val = input(msg)
        if val.isdigit():
            val = int(val)
            if min_val <= val <= max_val:
                return val
        print(f"Enter a number between {min_val} and {max_val}.")

def main():
    balance = get_number("Deposit amount: $", 1, 100000)
    
    while True:
        print(f"\nBalance: ${balance}")
        if input("Press Enter to spin (or 'q' to quit): ").lower() == "q":
            break

        lines = get_number(f"Lines to bet on (1-{MAX_LINES}): ", 1, MAX_LINES)
        bet = get_number(f"Bet per line (${MIN_BET}-${MAX_BET}): ", MIN_BET, MAX_BET)
        total_bet = bet * lines

        if total_bet > balance:
            print("Not enough balance.")
            continue

        balance -= total_bet
        spin = get_spin(ROWS, COLS, symbols)
        print("\nSlot Machine:")
        print_spin(spin)

        win, win_lines = check_win(spin, lines, bet)
        balance += win
        print(f"You won: ${win}")
        if win_lines:
            print("Winning lines:", ", ".join(map(str, win_lines)))
        else:
            print("No wins.")

    print(f"\nYou left with ${balance}")

main()
