text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world.
Many tourists visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

def word_frequency(text):
    # removes punctuation and converts to lowercase
    clean = text.lower().replace(".", "").replace(",", "")

    # split into individual words
    words = clean.split()

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1   # word seen before — add 1
        else:
            counts[word] = 1    # word seen first time — start at 1

    # sort by count (highest first) and take top 3
    top3 = sorted(counts, key=lambda w: counts[w], reverse=True)[:3]

    # print results
    print("Top 3 words:")
    for word in top3:
        print(f"  {word} — {counts[word]} times")

word_frequency(text)