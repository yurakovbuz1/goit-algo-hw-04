Merge sort test results:
Random array: 0.09694591700099409s
Sorted array: 0.07507787505164742s
Reversed array: 0.07600124995224178s

Insertion sort test results:
Random array: 10.34121199999936s
Sorted array: 0.004963249899446964s
Reversed array: 19.97019854094833s

Timsort sort test results:
Random array: 0.004935959121212363s
Sorted array: 0.0004530001897364855s
Reversed array: 0.00043612485751509666s

Conclusion:
Based on the results, Timsort (which is used in Python by default) is most efficient in all three cases.
At the same time the results show that Merge sort is a number of times more efficient compared to Insertion sort, except for the case with an already sorted array, as it still needs to divide the subsets and merge them back.