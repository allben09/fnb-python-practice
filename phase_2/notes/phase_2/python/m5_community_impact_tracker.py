"""
FNB App Academy – Phase 2
Module 5: Community Impact & Inclusive Growth

An impact measurement tool for NPOs, NGOs, and NPCs.
Calculates Social Return on Investment (SROI) and tracks
outcomes against targets.

Author: Allben Rakgoale
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ImpactMetric:
    """A single measurable impact indicator."""
    name: str
    unit: str
    target: float
    achieved: float
    monetary_value_per_unit: float = 0.0   # ZAR value of social benefit


@dataclass
class CommunityProgramme:
    """A programme run by an organisation."""
    name: str
    organisation: str
    province: str
    total_investment: float              # ZAR spent
    beneficiaries: int
    metrics: List[ImpactMetric]


def completion_rate(metric: ImpactMetric) -> float:
    """Percentage of target achieved."""
    if metric.target == 0:
        return 0.0
    return round((metric.achieved / metric.target) * 100, 2)


def total_social_value(programme: CommunityProgramme) -> float:
    """Total monetary value of social outcomes produced."""
    return sum(
        m.achieved * m.monetary_value_per_unit
        for m in programme.metrics
    )


def sroi(programme: CommunityProgramme) -> float:
    """
    Social Return on Investment.
    SROI of 3.0 means every R1 invested created R3 of social value.
    """
    if programme.total_investment == 0:
        return 0.0
    return round(total_social_value(programme) / programme.total_investment, 2)


def cost_per_beneficiary(programme: CommunityProgramme) -> float:
    """Average cost to serve one beneficiary."""
    if programme.beneficiaries == 0:
        return 0.0
    return round(programme.total_investment / programme.beneficiaries, 2)


def report(programme: CommunityProgramme) -> None:
    """Print a full impact report."""
    print("=" * 70)
    print(f"  COMMUNITY IMPACT REPORT")
    print(f"  Programme: {programme.name}")
    print(f"  Organisation: {programme.organisation}")
    print(f"  Province: {programme.province}")
    print("=" * 70)

    print(f"\n📊 Programme Overview")
    print(f"  Investment:            R{programme.total_investment:,.2f}")
    print(f"  Beneficiaries:         {programme.beneficiaries:,}")
    print(f"  Cost per Beneficiary:  R{cost_per_beneficiary(programme):,.2f}")

    print(f"\n🎯 Impact Metrics")
    print(f"{'Metric':<30}{'Target':<12}{'Achieved':<12}{'%':<8}")
    print("-" * 70)

    for m in programme.metrics:
        pct = completion_rate(m)
        print(
            f"{m.name:<30}"
            f"{m.achieved:>6.0f}/{m.target:<5.0f}"
            f"{pct:>9.1f}%"
        )

    print("\n" + "-" * 70)
    print(f"  Total Social Value: R{total_social_value(programme):,.2f}")
    print(f"  SROI Ratio:         {sroi(programme)}:1")

    rating = (
        "🏆 Excellent" if sroi(programme) >= 4 else
        "✅ Strong"    if sroi(programme) >= 2 else
        "🟡 Moderate"  if sroi(programme) >= 1 else
        "🔴 Needs Review"
    )
    print(f"  Impact Rating:      {rating}")
    print("=" * 70)


if __name__ == "__main__":
    # Example: A rural youth skills programme in Limpopo
    youth_programme = CommunityProgramme(
        name="Rural Youth Digital Skills Initiative",
        organisation="Communi-Connect Umbrella",
        province="Limpopo",
        total_investment=250_000.00,
        beneficiaries=180,
        metrics=[
            ImpactMetric(
                name="Youth trained in digital skills",
                unit="people",
                target=200, achieved=180,
                monetary_value_per_unit=1500.0,
            ),
            ImpactMetric(
                name="Youth employed after training",
                unit="people",
                target=60, achieved=42,
                monetary_value_per_unit=12000.0,
            ),
            ImpactMetric(
                name="Small businesses supported",
                unit="businesses",
                target=40, achieved=35,
                monetary_value_per_unit=8000.0,
            ),
            ImpactMetric(
                name="Community workshops held",
                unit="workshops",
                target=25, achieved=25,
                monetary_value_per_unit=2000.0,
            ),
        ],
    )

    report(youth_programme)
