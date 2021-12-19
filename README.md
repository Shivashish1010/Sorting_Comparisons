# Sorting_Comparisons

This represents the visual comparison between the most common sorting algorithms using python and matplotlib.

## Sorting Algorithms

1. Insertion Sort
2. Bubble Sort
3. Selection Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Python's inbuilt sort (Tim Sort)

## How to run

    python main.py --limit int --fast bool

## Optional arguments

For large values of n, the algorithms with running time of O(n^2) takes a lot of time, in order to have a quick look at the comparisons, 2 optional arguments are provided.

1. --fast bool : If fast is set to True, only the algorithms with O(nlogn) running time are implemented.
2. --limit int : There are total 14 different values of n that are provided, starting from 500 to 10000000, you can change how many different values you want to try with the limit argument.
