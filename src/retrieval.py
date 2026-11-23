"""Find the most relevant nonempty lines in a UTF-8 knowledge base."""
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STOP_WORDS = set("a an the of to for in is are was it its what how do does can and or about me tell on by with which".split())


def terms(text):
    words = re.findall(r"[^\W_]+", text.casefold())
    return {word.removesuffix("s") for word in words if word not in STOP_WORDS}


def retrieve(question, path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    passages = [line.strip() for line in lines if line.strip()]
    vocabulary = [terms(passage) for passage in passages]
    query = terms(question)
    weights = {}
    for term in query:
        frequency = sum(term in words for words in vocabulary)
        weights[term] = 1 + math.log((1 + len(passages)) / (1 + frequency))

    matches = []
    for passage, words in zip(passages, vocabulary):
        overlap = query & words
        if overlap:
            score = sum(weights[t] for t in overlap) / math.sqrt(len(words))
            matches.append((score, passage))
    matches.sort(key=lambda match: match[0], reverse=True)
    return [passage for _, passage in matches[:3]]
