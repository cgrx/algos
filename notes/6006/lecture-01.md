# Algorithms and Computation

## Course Objectives
1. Solve the computational problem
2. Prove the correctness
3. Argue the efficiency

## Algorithm

### Introduction
1. A computational problem is a map (binary relationship) from the space of inputs to the space of outputs. 
	1. Given the number of combinations, we don't often enumerate every possible input-output combination. 
	2. A predicate (a property) is often used to verify the correctness of the output.
2. An algorithm is a (deterministic) procedure to solve a computational problem of arbitrary sized input (i.e.) maps every input in the space to the correct output.

### Correctness
1. For an arbitrarily large inputs, an algorithm must be recursive in some way. 
2. Idea : Due to presence of recurrence, we can use induction to prove the correctness. 
3. Principle of mathematical induction : 
	1. Let $P: \mathbb{N} \to [0,1]$ (predicate) be a map such that $P(n)$ is either true or false $\forall~n~\in \mathbb{N}$.
	2. Base case : $P(1)$ is true. 
	3. Hypothesis : For an arbitrary $n \in \mathbb{N}$, let us assume that $P(n)$ is true.
	4. Induction : $P(n) \implies P(n+1)$

### Efficiency
1. The trivial idea is to measure the time taken to produce a correct output. However, the time is dependent on the machine, and size of the input.
2. Idea : Count the number of fixed-time operations an algorithm takes to run. 
	1. Operations performed by an algorithm on a machine, can be represented in terms of fixed-time operations.
	2. The count of fixed-time operations is dependent on the size of input.
3. Idea : Represent different algorithms in terms of asymptotic notation to identify the bounds.
	1. Ignore constant factors, and lower order terms
	2. Derive the upper bound ($O$), lower bound ($\Omega$), and tight bound ($\Theta$)

### Word-RAM Model
1. A model of computations is specification for what operations on the machine can be performed in $O(1)$ time.
2. Model :
	1. Machine word : Block of $w$ bits. $w$ is called word-size.
	2. Memory : Addressable sequence of machine words.
	3. Fixed-time operations :
		1. Integer : $(+, -, *, /, \%)$
		2. Logical : $(\&\&, ||, !, ==, <, >, <=, >=)$
		3. Bitwise : $(\&, |, <<, >>)$
		4. Read a word ($w$ bits) from an address
		5. Write a word ($w$ bits) to an address
3. Memory size : 
		1. Word size ($w$) $\geq$ No. of bits used to represent largest memory ($n$)
		2. Max memory is approx. $2^{w}$ bits

## Data Structure
1. Data structure : A way to store non-constant data, and support a set of operations on the data.
2. Interface : A collection of operations
	1. Sequence : Extrinsic order to items
	2. Set : Intrinsic order to items
3. We can maintain the interface of a data structure while updating the operations to improve its performance.
4. Example : Static array - Fixed width slots, fixed length, and static sequence interface
	1. $StaticArray(n)$ : Allocate static array of size $n$ initialized to 0 in $\Theta(n)$ time
	2. $StaticArray.get\_{at}(i)$ : Return word stored at an array index $i$ in $\Theta(1)$ time 
	3. $StaticArray.set\_{at}(i, x)$ : Write a word $x$ to an array index $i$ in $\Theta(1)$ time

## Resources
1. [Lecture Page](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-1-algorithms-and-computation/)
