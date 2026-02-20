#!/usr/bin/env python3
"""
Student Society Event Planner
ECM1414 - Algorithms and Data Structures Coursework

This program helps plan a student society event by selecting activities
that maximize enjoyment while staying within time and budget constraints.

Usage:
    python event_planner.py <input_file>
"""

import time
from itertools import combinations
#T = 0


def read_input(filename):
    """
    Read input file and parse activity data.
    
    Args:
        filename: Path to input file
    
    Returns:
        tuple: (num_activities, max_time, max_budget, activities)
               activities is a list of dicts with keys: name, time, cost, enjoyment
    """
    activities = []
    #open the file and assign test to variable lines
    with open(filename, "r") as f:
        lines = [ln for ln in f]

    #assign n, T and B

    n = int(lines[0])
    line2 = lines[1].split()
    T = int(line2[0])
    B = int(line2[1])

    #iterate through each activity and assign parts to dictionary
    for i in range(n):
        name, time, cost, enjoyment = lines[i+2].split()
        activities.append({
            "name" : name,
            "time" : int(time),
            "cost" : int(cost),
            "enjoyment" : int(enjoyment),
        })
    #tests to see if code runs correctly:
#    print(n, T, B)
#   print(activities[0]["names"])
    return n, T, B, activities



def brute_force_solver(acts, T):
    """
    Brute force algorithm to find optimal activity selection.
    Generates all possible subsets and evaluates each.
    
    Args:
        activities: List of activity dictionaries
        max_constraint: Maximum time or budget available
        constraint_type: 'time' or 'budget'
    
    Returns:
        tuple: (selected_activities, total_enjoyment, execution_time)
    """
    start = time.perf_counter()

    best_enjoyment = -1
    best_acts = []
    best_time = 999
    best_cost = 0
    for i in range(len(acts)+1):
        for combs in combinations(acts, i):
            sum_time = sum(j["time"] for j in combs)
            if sum_time > int(T):
                continue
            sum_enjoyment = sum(k["enjoyment"] for k in combs)
            if (sum_enjoyment > best_enjoyment or
                (sum_enjoyment == best_enjoyment and sum_time < best_time)):
                best_enjoyment = sum_enjoyment
                best_time = sum_time
                best_acts = list(combs)
                best_cost = sum(j["cost"] for j in combs)
    #print(best_enjoyment)
    #print(best_acts)

    end = time.perf_counter()
    exec_time = end - start
    return best_acts, best_enjoyment, best_time, best_cost, exec_time



def dp_solver(activities, max_constraint, constraint_type='time'):
    """
    Dynamic programming algorithm to find optimal activity selection.
    Uses memoization to avoid redundant calculations.
    
    Args:
        activities: List of activity dictionaries
        max_constraint: Maximum time or budget available
        constraint_type: 'time' or 'budget'
    
    Returns:
        tuple: (selected_activities, total_enjoyment, execution_time)
    """
    # TODO: Implement dynamic programming algorithm
    pass


def print_results(input_file, selected_activities_BF, total_enjoyment_BF, 
                 total_time_BF, total_cost_BF, max_time, max_budget, exec_time_BF,
                 selected_activites_DP, total_enjoyment_DP, total_time_DP,
                 total_cost_DP, exec_time_DP):
    """
    Print results in the required format.
    
    Args:
        algorithm_name: Name of the algorithm used
        selected_activities: List of selected activity dicts
        total_enjoyment: Sum of enjoyment values
        total_time: Sum of time used
        total_cost: Sum of cost
        max_time: Available time
        max_budget: Available budget
        exec_time: Execution time in seconds
    """
    print("========================================")
    print("EVENT PLANNER - RESULTS")
    print("========================================")
    print()
    print("Input File: ", input_file)
    print("Available Time: ", max_time)
    print("Available Budget: ", max_budget)
    print()
    print("--- BRUTE FORCE ALGORITHM ---")
    print("Selected Activities:")
    for act in selected_activities_BF:
        name = act.get("name")
        t = act.get("time")
        c = act.get("cost")
        e = act.get("enjoyment")
        print(f"   - {name} ({t} hours, £{c}, enjoyment {e})")
    print()
    print("Total Enjoyment:", total_enjoyment_BF)
    print("Total Time Used:", total_time_BF, "hours")
    print(f"Total cost: £{total_cost_BF}")
    print()
    print("Execution Time:", round(exec_time_BF, 7), "seconds")
    print()
    print("--- DYNAMIC PROGRAMMING ALGORITHM ---")
    print("Selected Activities:")
    for act in selected_activities_DP:
        name = act.get("name")
        t = act.get("time")
        c = act.get("cost")
        e = act.get("enjoyment")
        print(f"   - {name} ({t} hours, £{c}, enjoyment {e})")
    print()
    print("Total Enjoyment:", total_enjoyment_DP)
    print("Total Time Used:", total_time_DP, "hours")
    print(f"Total cost: £{total_cost_DP}")
    print()
    print("Execution Time:", round(exec_time_DP, 7), "seconds")
    print()
    print("========================================")

def main():
    """
    Main function to run the event planner.
    """

    input_file = "Input_Files/Sample Input Files-20260121/input_10.txt"
    n, T, B, activities = read_input(input_file)
    best_acts_BF, best_enjoyment_BF, best_time_BF, best_cost_BF, exec_time_BF = brute_force_solver(activities, T)
    best_acts_DP, best_enjoyment_DP, best_time_DP, best_cost_DP, exec_time_DP = dp_solver()
    print_results(input_file, best_acts_BF, best_enjoyment_BF, best_time_BF,
                  best_cost_BF, T, B, exec_time_BF, best_acts_DP, best_enjoyment_DP,
                  best_time_DP, best_cost_DP, exec_time_DP)


if __name__ == "__main__":
    main()
