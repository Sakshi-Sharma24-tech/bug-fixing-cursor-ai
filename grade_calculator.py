"""
Grade Calculator Module (Assignment 8)
Fixed using Cursor AI and Test-Driven Debugging (Red -> Fix -> Green).
"""

def calculate_average(scores):
    """Calculates and returns the exact arithmetic mean of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def is_passing(score, passing_threshold=40):
    """Determines if a student score meets the inclusive passing boundary."""
    return score >= passing_threshold

def assign_grade(score):
    """Assigns the correct academic grade based on descending threshold ordering."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
