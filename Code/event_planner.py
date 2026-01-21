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


def read_input(filename):
    """
    Read input file and parse activity data.
    
    Args:
        filename: Path to input file
    
    Returns:
        tuple: (num_activities, max_time, max_budget, activities)
               activities is a list of dicts with keys: name, time, cost, enjoyment
    """
    #open the file and assign test to variable lines
    with open(filename, "r") as f:
        lines = [ln for ln in f]

    activities = []
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
#    print(n, T, B)
    print(activities)

    f.close()
    return n, T, B, activities
    # TODO: Implement input file parsing



def brute_force_solver(activities, max_constraint, constraint_type='time'):
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
    # TODO: Implement brute force algorithm
    pass


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


def print_results(algorithm_name, selected_activities, total_enjoyment, 
                 total_time, total_cost, max_time, max_budget, exec_time):
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
    # TODO: Implement output formatting
    pass


def main():
    """
    Main function to run the event planner.
    """

    input_file = "Input_Files/Sample Input Files-20260121/input_10.txt"
    read_input(input_file)

    # TODO: Implement main logic and run brute force and dp algorithms 
    print(f"Input file: {input_file}")


if __name__ == "__main__":
    main()
