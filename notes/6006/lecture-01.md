from typing import List

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
3. A computer program that implements an algorithm will have a finite size, but works for an arbitrarily sized input.

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
4. Asymptotic notations 
	1. Upper bound ($O$) : Non-negative function $g(n) \in O(f(n))~\iff~\exists~c \in \mathbb{R}^{+},~n_{0} \in \mathbb{Z}^{+}~:~g(n) \leq c \cdot f(n),~ \forall n \geq n_{0}$ 
	2. Lower bound ($\Omega$) : Non-negative function $g(n) \in \Omega(f(n))~\iff~\exists~c \in \mathbb{R}^{+},~n_{0} \in \mathbb{Z}^{+}~:~c \cdot f(n) \leq g(n) ,~ \forall n \geq n_{0}$
	3. Tight bound ($\Theta$) : Non-negative function $g(n) \in \Theta(f(n))~\iff~g(n) \in O(f(n)) \cap \Omega(f(n))$ 
5. $f(n)$ of interest : $1,~log(n),~n,~n^{c} : c \in \mathbb{R}^{+},~...$ 

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
		2. Max memory is approx. $2^{w}$ bits representing an integer sequence $\{0,...,2^{w}-1\}$ of addresses

## Data Structure
1. Data structure : A way to store non-constant data, and support a set of operations on the data.
2. Interface : A collection of operations
	1. Sequence : Extrinsic order to items
	2. Set : Intrinsic order to items
3. Data Structure vs Interface :
	1. Interface is a specification (i.e.) what operations are supported. {Problem}
	2. Data structure is a representations (i.e.) how the operations are supported. {Solution}
4. We can maintain the interface while updating the operations to improve its performance. 
5. Example : Static array - Fixed width slots, fixed length, and static sequence interface

```python
from typing import List, Any

class StaticArray:
	""" Static array implementation
	Note: Technically, a static array is a fixed-length array of fixed-width slots. Therefore, usage should be restricted to those cases.
	"""
	def __init__(self, size: int) -> None:
		"""Allocate static array of size n initialized to None in linear time
		:param size: size of the array
		:return: None
		"""
		self._size: int = size
		self._data: List[Any] = [None] * size

	def __len__(self) -> int:
		"""Return length of the array in constant time
		:return: length of the array
		"""
		return self._size

	def __getitem__(self, item: int) -> Any:
		"""Return word stored at an array index item in constant time
		:param item: index of the array
		:return: word stored at index item
		"""
		if not (0 <= item < self._size):
			raise IndexError("Index out of bounds")
		return self._data[item]

	def __setitem__(self, key, value):
		"""Write a word value to an array index key in constant time
		:param key: index of the array
		:param value: word to be written
		:return: None
		"""
		if not (0 <= key < self._size):
			raise IndexError("Index out of bounds")
		self._data[key] = value

```

## Resources
1. [Lecture Page](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-1-algorithms-and-computation/)
