from word_bank import get_word_bank
from haiku_generator import generate_haiku

def main():
    theme = input("Enter a theme (e.g., nature, love, sadness): ")
    word_bank = get_word_bank(theme)
    haiku = generate_haiku(word_bank)
    print("\nYour Personalized Haiku:\n")
    print(haiku)

if __name__ == "__main__":
    main()
