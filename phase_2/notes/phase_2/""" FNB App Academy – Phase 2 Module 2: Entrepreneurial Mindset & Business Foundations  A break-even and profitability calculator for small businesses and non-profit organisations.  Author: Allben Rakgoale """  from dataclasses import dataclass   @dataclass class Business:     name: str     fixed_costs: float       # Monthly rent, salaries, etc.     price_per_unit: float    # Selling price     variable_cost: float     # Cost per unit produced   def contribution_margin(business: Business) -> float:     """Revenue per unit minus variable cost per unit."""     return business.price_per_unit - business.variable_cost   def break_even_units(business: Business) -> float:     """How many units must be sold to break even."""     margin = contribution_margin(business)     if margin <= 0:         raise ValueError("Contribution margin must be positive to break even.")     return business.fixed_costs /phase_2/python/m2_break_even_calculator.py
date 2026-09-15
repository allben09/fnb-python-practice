"""
FNB App Academy – Phase 2
Module 2: Entrepreneurial Mindset & Business Foundations

A break-even and profitability calculator for small businesses
and non-profit organisations.

Author: Allben Rakgoale
"""

from dataclasses import dataclass


@dataclass
class Business:
    name: str
    fixed_costs: float       # Monthly rent, salaries, etc.
    price_per_unit: float    # Selling price
    variable_cost: float     # Cost per unit produced


def contribution_margin(business: Business) -> float:
    """Revenue per unit minus variable cost per unit."""
    return business.price_per_unit - business.variable_cost


def break_even_units(business: Business) -> float:
    """How many units must be sold to break even."""
    margin = contribution_margin(business)
    if margin <= 0:
        raise ValueError("Contribution margin must be positive to break even.")
    return business.fixed_costs / margin


def break_even_revenue(business: Business) -> float:
    """Revenue needed to break even."""
    return break_even_units(business) * business.price_per_unit


def profit_at_volume(business: Business, units: float) -> float:
    """Profit (or loss) at a given sales volume."""
    return (units * contribution_margin(business)) - business.fixed_costs


def report(business: Business, expected_units: float = 0) -> None:
    """Print a full financial report."""
    print("=" * 55)
    print(f"  FINANCIAL ANALYSIS: {business.name.upper()}")
    print("=" * 55)

    print(f"\n💰 Unit Economics")
    print(f"  Selling Price:        R{business.price_per_unit:.2f}")
    print(f"  Variable Cost:        R{business.variable_cost:.2f}")
    print(f"  Contribution Margin:  R{contribution_margin(business):.2f}")

    print(f"\n📊 Break-Even Analysis")
    print(f"  Fixed Costs:          R{business.fixed_costs:,.2f}")
    print(f"  Break-Even Units:     {break_even_units(business):,.0f} units")
    print(f"  Break-Even Revenue:   R{break_even_revenue(business):,.2f}")

    if expected_units > 0:
        profit = profit_at_volume(business, expected_units)
        status = "✅ PROFIT" if profit >= 0 else "❌ LOSS"
        print(f"\n📈 At {expected_units:,.0f} Units Sold")
        print(f"  Result: {status}")
        print(f"  Amount: R{profit:,.2f}")

    print("=" * 55)


if __name__ == "__main__":
    # Example: A small NGO selling handmade goods to fund programmes
    ngo = Business(
        name="Communi-Connect Social Enterprise",
        fixed_costs=8000.00,      # Monthly overheads
        price_per_unit=150.00,     # Price per item
        variable_cost=60.00,       # Materials + labour per item
    )

    report(ngo, expected_units=150)
