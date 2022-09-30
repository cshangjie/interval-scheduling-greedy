# Greedy Algorithm for Interval Scheduling of jobs with equal weight
Takes input in the following format:

```
Number_Instances
Number_Jobs
start_time end_time
...
start_time end_time
```

i.e.
```
2
1
1 2
3
1 2
3 4
2 6
```
## Handled Edge Cases
start_time > end_time    
```
1
1
5 0
```
negative times
```
1
1
-1 2
```
