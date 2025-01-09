from pathlib import Path
import numpy as np

THIS_DIR = Path(__file__).parent

a = (THIS_DIR / "a.md").read_text()
b = (THIS_DIR / "b.md").read_text()

a_words = a.split()
b_words = b.split()

index = np.array([0] * len(a_words) + [1] * len(b_words))
np.random.shuffle(index)

mixed_words = list(reversed([a_words.pop() if i == 0 else b_words.pop() for i in index]))

(THIS_DIR / "mid.md").write_text(" ".join(mixed_words))
