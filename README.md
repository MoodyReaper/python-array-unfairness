![CI Status](https://github.com/MoodyReaper/python-array-unfairness/actions/workflows/ci_poetry.yml/badge.svg)
![Test Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/MoodyReaper/9d078240555ff416181fdec9cfb370cf/raw/python-array-unfairness-test-coverage.json)

# Test task

My solving of the following task:

> You will be given a list of integers `arr` and a single integer `k`.  
> You must create an array of length `k` from elements of `arr` such that it's unfairness is minimized.  
> Call that array `sub_arr`.  
> Unfairness of an array is calculated as: `max(sub_arr) - min(sub_arr)`
>
> Example:  
> `arr = [1, 4, 7, 2]`  
> `k = 2`
>
> Pick any two elements, for example, `sub_arr = [4, 7]`  
> `Unfairness = max(4,7) - min(4,7) = 7 - 4 = 3`
>
> Testing for all pairs, the solution provides the minimum unfairness.

`Basically, it is a so-called "Min-Max optimization problem"`
