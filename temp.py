import sys
import datetime

def generate_patterns(day, month, year, company, initials, word, pet):
    patterns = [
        f"{month}{year}",
        f"{month}{year}.",
        f"{month}{day}_{year}",
        f"{month[:3]}{year}",
        f"{month[:3]}{year}.",
        f"{company}{month}{year}",
        f"{initials}_{month}{year}",
        f"{word}{month}{year}",
        f"{pet}{month}{year}",
        f"{month}{day}{initials}",
        f"{initials}_{month}{day}_{year}",
        f"{month}{year}!",
        f"{year}{month}!",
        f"{company}{year}{month}",
        f"{word}{day}{month}{year}",
        f"{month[:3]}{day}_{year}",
        f"{month[:3]}{day}_{year}!",
        f"{day}{month}{year}",
        f"{day}{month[:3]}{year}",
        f"{day}{company}{month}{year}",
        f"{month}{year}!!",
        f"{word}{day}{month[:3]}{year}",
        f"{pet}{day}{month}{year}",
        f"{initials}_{day}{month}{year}",
        f"{month}{day}_{year}!",
    ]
    return patterns

def save_patterns_to_file(patterns, filename):
    with open(filename, 'w') as f:
        for pattern in patterns:
            f.write(f"{pattern}\n")

def main():
    today = datetime.datetime.now()
    day = str(today.day) if len(sys.argv) < 2 else sys.argv[1]
    month = today.strftime("%B") if len(sys.argv) < 3 else sys.argv[2]
    year = str(today.year) if len(sys.argv) < 4 else sys.argv[3]
    company = "Empresa" if len(sys.argv) < 5 else sys.argv[4]
    initials = "JD" if len(sys.argv) < 6 else sys.argv[5]
    word = "Contraseña" if len(sys.argv) < 7 else sys.argv[6]
    pet = "Firulais" if len(sys.argv) < 8 else sys.argv[7]

    patterns = generate_patterns(day, month, year, company, initials, word, pet)
    save_patterns_to_file(patterns, 'generated_patterns.txt')
    print("Patrones generados y guardados en 'generated_patterns.txt'")

if __name__ == "__main__":
    main()