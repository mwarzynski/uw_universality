# Universality of Finite-State Automata

Consider the following problem: does the given non-deterministic finite-state automaton A accept all words of given
length n? The automaton is presented as A = (Σ, Q, I, F, δ), where Σ = {a1, . . . , ak } is the alphabet,
Q = {q1, . . . , ql } is the set of states, I ⊆ Q is the set of initial states, F ⊆ Q is the set of final states,
and δ ⊆ Q × Σ × Q is the set of transitions. The automaton accepts a word w if there exists a run of A on w that begins
in a state from I and ends in a state from F. Write a program that reads the automaton and the number n from standard
input (in the format described below), translates the problem above to SAT, runs Z3 over it, and writes to standard
output either YES, or NO followed by some rejected word (in the format described below).

## Input

The first line of the input contains 5 numbers: k (the number of symbols in the alphabet), l (the number of states),
l1 (the number of initial states), lf (the number of final states), and m (the number of transitions). The second line
contains k distinct words a1, . . . , ak separated by single spaces, representing the symbols of the alphabet. The
third line contains l distinct words q1 , . . . , ql separated by single spaces, representing the states of the
automaton. The fourth line contains l1 distinct words separated by single spaces, representing the initial states;
each of these words occurs in the list of states (the third line). The fifth line contains lf distinct words separated
by single spaces, representing the final states; each of these words occurs in the list of states (the third line).
The next m lines represent the transitions. A transition is represented as p a q. Such a transition can be executed
if the current state of the automaton is p, and the current symbol is a. The automaton changes its state to q, and
moves to the next symbol. For each transition, the words p and q appear in the list of states (the third line),
and the word a appears in the list of symbols (the second line). The last line of the input contains a single number n,
representing the length of input words.

## Output

If all words of length n are accepting, the first and only line of the output should contain YES. Otherwise, the first
line should contain NO, the second line should be empty, and the third line should contain an input word of length n
rejected by the automaton. The rejected input word should be represented as a sequence of n symbols from the alphabet,
separated by single spaces.

## Example

For the input data:
```
2 4 1 1 6
a b
i a b f
i
f
i a i
i b i
i a a
i b b
a a f
b b f
3
```

a correct result is:
```
NO

a b a
```

## Allowed languages

We recommand that you write your solution in Python.
