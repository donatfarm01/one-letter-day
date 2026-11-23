import os

# The letter that stands for the day: U, for "ugh" — the groan that is the
# most universal sound of a bad day. A single letter has to carry the whole
# mood, and "ugh" paints it sharper than any vague mood word could.
LETTER = "U"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
