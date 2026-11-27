import string
import sys


def read_file(filepath: str) -> str:
    """Read and return the full text content of a UTF-8 file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def count_words(text: str) -> dict[str, int]:
    """Normalize text, strip punctuation, and return a dictionary of word frequencies."""
    translator = str.maketrans("", "", string.punctuation)
    cleaned_words = text.lower().translate(translator).split()
    counts = {}
    for word in cleaned_words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def get_top_words(word_counts: dict[str, int], top_n: int = 10) -> list[tuple[str, int]]:
    """Return the top_n most frequent (word, count) pairs sorted descending."""
    sorted_items = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:top_n]


def main() -> None:
    """Entry point to count and display top 10 words from a given text file."""
    filepath = sys.argv[1] if len(sys.argv) > 1 else input("Enter path to text file: ").strip()
    try:
        text = read_file(filepath)
        counts = count_words(text)
        top_10 = get_top_words(counts, top_n=10)
        print(f"\nTop {len(top_10)} words in '{filepath}':")
        for rank, (word, count) in enumerate(top_10, start=1):
            print(f"{rank}. {word}: {count}")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")


if __name__ == "__main__":
    main()
