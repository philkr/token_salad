# 2025 Admission problem set

For those curious, there are a few interesting solutions to the problem

- **Greedy Algorithm**: maintain two lists, and assign the next word based on likelihood
- **Sampling**: Reformulate the problem into a sequence generation problem, where we generate a sequence of 0 or 1 for each mixed word. Essentially constrain the next word that can be predicted. If we repeat this sufficiently, we should obtain a good solution. All tricks from LLM sampling can apply here (i.e. nucleus etc)
- **Beam Search**: Same as above, just apply beam search
- **Tree Search**: Explicitly search over all possible assignments
- **Simulated annealing**: Start with a random or greedy solution and find local moves to improve the solution

- **Training based**: Generate a large dataset of jumbled poems and learn to separate them
- **Prompt engineering**: It turns out ChatGPT can unscramble this with the right prompt
