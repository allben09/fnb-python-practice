"""
FNB App Academy – Phase 2
Module 1: Digital Literacy & Productivity Tools

A practical tool that demonstrates:
- Task prioritisation
- Time blocking
- Productivity scoring

Author: Allben Rakgoale
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    """Represents a single task with priority and time estimate."""
    name: str
    priority: int      # 1 (highest) to 5 (lowest)
    hours: float
    completed: bool = False


def sort_by_priority(tasks: List[Task]) -> List[Task]:
    """Sort tasks by priority (1 = highest)."""
    return sorted(tasks, key=lambda t: t.priority)


def total_hours(tasks: List[Task]) -> float:
    """Calculate total estimated hours."""
    return sum(t.hours for t in tasks)


def productivity_score(tasks: List[Task]) -> float:
    """
    Calculate productivity score as a percentage.
    Completed high-priority tasks weigh more.
    """
    if not tasks:
        return 0.0

    weighted_done = sum(
        (6 - t.priority) for t in tasks if t.completed
    )
    weighted_total = sum((6 - t.priority) for t in tasks)

    return round((weighted_done / weighted_total) * 100, 2)


def print_schedule(tasks: List[Task]) -> None:
    """Print a clean daily schedule."""
    print("=" * 55)
    print("        DAILY PRODUCTIVITY SCHEDULE")
    print("=" * 55)

    for i, task in enumerate(sort_by_priority(tasks), start=1):
        status = "✅" if task.completed else "⏳"
        print(f"{i}. {status} {task.name}")
        print(f"   Priority: P{task.priority} | Est: {task.hours}h")

    print("-" * 55)
    print(f"Total Hours: {total_hours(tasks):.1f}h")
    print(f"Productivity Score: {productivity_score(tasks)}%")
    print("=" * 55)


if __name__ == "__main__":
    my_tasks = [
        Task("Complete Module 5 quiz", priority=1, hours=1.0),
        Task("Update GitHub README", priority=1, hours=0.5, completed=True),
        Task("Study for Statistics 600", priority=2, hours=3.0),
        Task("Work on Capstone idea", priority=2, hours=2.0, completed=True),
        Task("Watch productivity masterclass", priority=3, hours=1.5, completed=True),
        Task("Read entrepreneurship notes", priority=4, hours=1.0),
    ]

    print_schedule(my_tasks)
