# wordle-ai
An information-theoretic Wordle agent that maintains a posterior over possible answers and selects entropy-minimising guesses.

This project studies optimal and approximate decision-making strategies for the game Wordle.

The core idea is to first implement an exact, information-theoretic solution that is optimal under a clear probabilistic model, and then analyse how well various approximations, including learning-based methods, can replicate this behaviour under computational constraints.

---

## Problem formulation

Wordle is modelled as a sequential decision-making problem under uncertainty.

- **Hidden state:** the target word \( w \), drawn uniformly from a fixed answer set  
- **Action:** selecting a guess word \( g \) from a dictionary  
- **Observation:** feedback (green, yellow, grey) for each letter according to its accuracy 
- **Belief state:** the set of words consistent with all observed feedback  
- **Objective:** minimise the expected number of guesses required to identify the target word

At each step, the agent updates its belief state based on observed feedback and selects a new guess according to a chosen policy.

---

## Exact entropy-minimising policy

An exact entropy-minimising policy is implemented as a reference method.

Given a belief state, this method evaluates all candidate guesses, computes the expected posterior entropy induced by each possible feedback pattern, and selects the guess that minimises this expected entropy. The entropy of a guess is computed as:

H = −∑ p_i log₂(p_i)

where p_i is the probability of observing feedback pattern i.

While this policy is optimal under the modelling assumptions, it is computationally expensive, motivating the study of faster approximation methods.

Empirical experiments confirmed that even with caching and pruning heuristics,
entropy-based strategies scale poorly as the search space grows.


---

## Project goals

1. Implement an exact entropy-minimising Wordle solver
2. Measure its computational cost and performance
3. Develop faster approximation methods, including learning-based approaches
4. Analyse the tradeoff between decision quality and computational efficiency

