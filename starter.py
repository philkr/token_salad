from pathlib import Path
import numpy as np

class LM:
    """
        A dummy language model
    """
    def __call__(self, words: list[str]) -> float:
        """
            Returns the likelihood under the model of the word sequence.
            Returns a value from 0...1.
        """
        return np.random.rand()

# Load
mixed_poem = (Path(__file__).parent / "mix.md").read_text()
mixed_words = mixed_poem.split()
...
