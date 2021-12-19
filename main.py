from copy import deepcopy
from collections import defaultdict
from matplotlib import pyplot as plt
import random
import timeit
from sorting_algos import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--fast', type=bool)
    parser.add_argument('--limit', type=int)
    args = parser.parse_args()
    if args.fast:
        algo_names = {"Merge":merge_sort, "Quick":quick_sort, "Heap":heap_sort,"Python Inbuilt(Tim)":sorted}
    else:
        algo_names = {"Bubble":bubble_sort, "Selection":selection_sort,"Insertion":insertion_sort, "Merge":merge_sort, "Quick":quick_sort, "Heap":heap_sort,"Python Inbuilt(Tim)":sorted}
    
    limits = [500,1000,5000,10000,25000,50000,75000,100000,300000,500000,1000000,2000000,5000000,10000000]
    if args.limit:
        limits=limits[:args.limit]
    
    print(limits)
    a = []
    algo_times = defaultdict(lambda:list())
    for n in limits:
        for i in range(n):
            a.append(random.randint(1,100000))
        original_value = tuple(a)

        print("\nTotal Elements",n,end="\n\n")

        for name,func in algo_names.items():
            start_selection = timeit.default_timer()
            res = func(list(original_value))
            end_selection = timeit.default_timer()
            total_time = round(end_selection-start_selection,5)
            print(f"\t{name} Sort : {total_time}")
            algo_times[name].append(total_time)
    
    new_ticks = range(len(limits))
    for algo, time in algo_times.items():
        plt.plot(new_ticks, time, label = algo+" Sort", marker = ".")
    
    plt.xticks(new_ticks, limits)
    plt.xlabel("Total elements")
    plt.ylabel("Time in Seconds")
    plt.legend()
    plt.show()
