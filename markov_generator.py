import random
import re
import argparse
from collections import defaultdict

def load_jokes(filename):
    jokes = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = re.sub(r'https?://\S+', '', line)
            line = re.sub(r'Анекдоты про.*', '', line).strip()
            if line:
                jokes.append(line)
    return jokes

def build_markov_chain(texts, n=2):
    chain = defaultdict(list)
    starts = []  # запомним фразы, с которых начинаются анекдоты

    for text in texts:
        words = text.split()
        if len(words) < n:
            continue
        starts.append(tuple(words[:n]))  # первые n слов — возможное начало
        for i in range(len(words) - n):
            key = tuple(words[i:i+n])
            next_word = words[i+n]
            chain[key].append(next_word)

    return chain, starts

def generate_joke(chain, starts, n=2, max_words=50):
    if not chain or not starts:
        return ""
    key = random.choice(starts)  # начинаем с реального начала
    result = list(key)
    for _ in range(max_words - n):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        key = tuple(result[-n:])
        if result[-1].endswith(('.', '!', '?')) and len(result) > 10:
            break
    return " ".join(result)

def main():
    parser = argparse.ArgumentParser(description="Markov Joke Generator")
    parser.add_argument("file", help="Файл с анекдотами (txt)")
    parser.add_argument("--jokes", type=int, default=5, help="Количество анекдотов для генерации")
    args = parser.parse_args()

    jokes = load_jokes(args.file)
    chain, starts = build_markov_chain(jokes, n=2)

    for i in range(args.jokes):
        print(f"{i+1}. {generate_joke(chain, starts)}\n")

if __name__ == "__main__":
    main()
