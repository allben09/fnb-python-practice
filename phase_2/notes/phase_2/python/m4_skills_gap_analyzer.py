"""
FNB App Academy – Phase 2
Module 4: 21st Century Work Readiness

A skills gap analyzer that compares current skills against
target job requirements and produces a prioritised action plan.

Author: Allben Rakgoale
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class JobProfile:
    """Target job with required skills (0–5 scale)."""
    title: str
    required: Dict[str, int]


@dataclass
class Candidate:
    """Candidate with current skill levels (0–5 scale)."""
    name: str
    skills: Dict[str, int]


def gap_analysis(candidate: Candidate, job: JobProfile) -> Dict[str, dict]:
    """Compare candidate skills against job requirements."""
    results = {}

    for skill, required_level in job.required.items():
        current_level = candidate.skills.get(skill, 0)
        gap = required_level - current_level

        if gap <= 0:
            status = "✅ Strong"
        elif gap == 1:
            status = "🟡 Minor Gap"
        elif gap == 2:
            status = "🟠 Moderate Gap"
        else:
            status = "🔴 Critical Gap"

        results[skill] = {
            "required": required_level,
            "current": current_level,
            "gap": gap,
            "status": status,
        }

    return results


def readiness_score(results: Dict[str, dict]) -> float:
    """Overall readiness as a percentage."""
    total_required = sum(r["required"] for r in results.values())
    total_current = sum(min(r["current"], r["required"]) for r in results.values())

    if total_required == 0:
        return 0.0

    return round((total_current / total_required) * 100, 2)


def report(candidate: Candidate, job: JobProfile) -> None:
    """Print full gap analysis and action plan."""
    results = gap_analysis(candidate, job)
    score = readiness_score(results)

    print("=" * 65)
    print(f"  SKILLS GAP ANALYSIS")
    print(f"  Candidate: {candidate.name}")
    print(f"  Target Role: {job.title}")
    print("=" * 65)
    print(f"\nOverall Readiness: {score}%\n")

    print(f"{'Skill':<22}{'Need':<8}{'Have':<8}{'Status'}")
    print("-" * 65)

    for skill, data in results.items():
        print(
            f"{skill:<22}"
            f"{data['required']:<8}"
            f"{data['current']:<8}"
            f"{data['status']}"
        )

    # Prioritised action plan
    gaps = [
        (skill, data) for skill, data in results.items()
        if data["gap"] > 0
    ]
    gaps.sort(key=lambda x: x[1]["gap"], reverse=True)

    print("\n" + "=" * 65)
    print("  PRIORITISED ACTION PLAN")
    print("=" * 65)

    if not gaps:
        print("  🎉 No gaps – you are fully ready for this role!")
    else:
        for i, (skill, data) in enumerate(gaps, start=1):
            print(f"  {i}. {skill} — close {data['gap']} level(s)")

    print("=" * 65)


if __name__ == "__main__":
    me = Candidate(
        name="Allben Rakgoale",
        skills={
            "Python": 5,
            "SQL": 4,
            "Machine Learning": 4,
            "Cloud (AWS)": 4,
            "Docker": 4,
            "Communication": 4,
            "System Design": 3,
            "Kubernetes": 1,
            "Terraform": 1,
        },
    )

    target = JobProfile(
        title="Junior Data Engineer – FNB",
        required={
            "Python": 4,
            "SQL": 5,
            "Machine Learning": 3,
            "Cloud (AWS)": 4,
            "Docker": 3,
            "Communication": 4,
            "System Design": 4,
            "Kubernetes": 3,
            "Terraform": 3,
        },
    )

    report(me, target)
