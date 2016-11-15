# multiset-partitioning
Simple multiset partitionin in Python

Reference: https://en.wikipedia.org/wiki/Partition_problem

Try running with --help for arguments.

Examples:

```
~/github/multiset-partitioning$ ./multiset_partition.py -s 3
----------------------------------------
Partitioning [84, 46, 8, 58, 10, 65, 74, 79, 56, 120, 43, 0, 62, 25, 0] into 3 sets.
----------------------------------------
Summary
A: [120, 62, 46, 10, 0, 0] (238)
B: [84, 65, 58, 43] (250)
C: [79, 74, 56, 25, 8] (242)
----------------------------------------

~/github/multiset-partitioning$ ./multiset_partition.py -s 4 -i ./input_data.txt
----------------------------------------
Partitioning [0, 0, 100, 200, 300, 400, 900, 800, 700, 600, 500, 1000, 0, 0] into 4 sets.
----------------------------------------
Summary
A: [1000, 300, 200] (1500)
B: [900, 400, 0, 0, 0, 0] (1300)
C: [800, 500, 100] (1400)
D: [700, 600] (1300)
----------------------------------------
```

--November 15, 2016
