# Algorithms  

Here I am going to post Python implementation of some algorithms that are being discussed in the on-line Stanford course called "Algorithms: Design and Analysis, Part 1". I should point out that **this is not a repo with solutions**, since posting solutions is a violation of [Coursera Honor Code](https://learner.coursera.help/hc/en-us/articles/209818863). Instead, this is a repository that contains Python implementation of some very well-known algorithms that are also available elsewhere in the internet. 

## Week 1

Week 1 discusses the basics of the divide-and-conquer approach, as well as how to apply O ("big-oh") notation to make a crude estimation of algorithms performance. Two examples the are implemented here are the Merge Sort algorithm and its extension that calculates the number of inversions required to perform a sorting procedure. 

Following the lecture notes I have implemented two algorithms: 
  1. Merge-sort (1- and n-dimensional) 
  2. Finding the closest pair of points (brute force and divide-and-conquer approaches).

## Week 2

Week 2 continues the introduction to divide-and-conquer paradigm and introduces a new sorting algorithm, quick sort. We saw how performance of this algorithm can vary based on the selection of a pivot element - the element that is used as a separation point for left and right parts of the input unsorted array. Following the lecture notes I have implemented a quick sort algorithm with a possibility to select a pivot element as one from the three available options: 
  1. The first element of the input array
  2. The last element  
  3. The median element

The median element is selected as follows. First we pick three elements from the input array: the very first, the very last and the middle element. Then we sort them in the ascending order and select a median from this sorted array. This element is then used as the pivot element to sort the original input array around. Such procedure, even though requires a bit of extra work, allows for a significant speed improvements on input arrays that are nearly sorted or reverse sorted.
