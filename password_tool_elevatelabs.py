from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)

    print("\nPassword Analysis")
    print("-----------------")
    print("Strength Score (0-4):", result["score"])
    print("Estimated Crack Time:",
          result["crack_times_display"]["offline_fast_hashing_1e10_per_second"])


def generate_wordlist(name, pet, year):
    words = set()

    inputs = [name, pet]
    suffixes = ["123", "1234", "@123", "!", "_"]
    leet_map = str.maketrans({"a": "@", "i": "1", "o": "0", "e": "3"})

    short_year = year[-2:] if len(year) == 4 else year

    for word in inputs:
        if not word:
            continue

        base = word.lower()

        words.add(base)
        words.add(base.capitalize())
        words.add(base.upper())
        words.add(base.translate(leet_map))

        for s in suffixes:
            words.add(base + s)
            words.add(base.capitalize() + s)

        if year:
            words.add(base + year)
            words.add(base + short_year)

    # name + pet combinations
    if name and pet:
        words.add(name + pet)
        words.add(name.capitalize() + pet)
        words.add(name + pet.capitalize())

    with open("wordlist.txt", "w") as f:
        for w in sorted(words):
            f.write(w + "\n")

    print("\nWordlist generated: wordlist.txt")
    print("Total entries:", len(words))


# -------- MAIN --------

print("Password Strength Analyzer")

password = input("\nEnter password to analyze: ")
analyze_password(password)

print("\nEnter details for wordlist generation")
name = input("Name: ").strip()
pet = input("Pet name: ").strip()
year = input("Important year: ").strip()

generate_wordlist(name, pet, year)
