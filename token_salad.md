# Interview - UT Austin

In this interview, I want to see how we can solve a small problem together.
While the backstory behind the problem is completely artificial, it is grounded in two research problems we encountered in the past year.

There is no need to prepare slides or a solution, but I'd like you to think about the problem and potential solutions before the interview.

For the interview, have your favorite coding editor ready, we might do some pair coding if time permits.

## Token salad

Bevo, UT Austin's mascot, made a mess.
He wrote two poems, both in English, and both absolutely marvelous.
Unfortunately, he mixed them up at a word level.

He remembers poem 1 started with

```md
In heart of Texas, where the wild things play,
```

and Poem 2 started with

```md
Under Texas skies, where the sun dips low,
```

However, what he wrote down was a mix of the two

```md
Under In heart Texas of Texas, where skies, where the wild the sun things dips low, play,
```

As you can see above the order words in the two poems did not change, but they are interleaved.

> Under **In heart Texas of** Texas, **where** skies, **where the wild** the sun **things** dips low, **play,**

> **Under** In heart Texas of **Texas,** where **skies,** where the wild **the sun** things **dips low,** play,

Can you help Bevo unscramble the two Poems?

Assume that you have access to an auto-regressive Language Model $\pi$ of your choice (trained on infinite relevant data, but not instruction tuned).
For simplicity, we will use a word-level model.
Let $w_1, \ldots, w_K$ be a sequence of words.
The language model $\pi$ predicts the likelihood $\pi(w_k|w_1\ldots w_{k-1})$ of the the next word $w_k$, given all words that came before it $w_1\ldots w_{k-1}$.
