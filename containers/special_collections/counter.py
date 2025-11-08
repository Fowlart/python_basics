from collections import Counter

if __name__ == "__main__":
    # Counter
    counts = Counter("Mississipi")
    print(counts.most_common(2))
    # Accepts list
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counts = Counter(fruits)
    print(counts.most_common(2))