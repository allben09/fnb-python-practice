"""
FNB App Academy – Phase 2
Module 3: Digital Entrepreneurship & Online Tools

A digital presence audit tool for small businesses and NPOs.
Checks whether key online assets are in place and scores readiness.

Author: Allben Rakgoale
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class DigitalPresence:
    """Represents an organisation's digital footprint."""
    name: str
    has_website: bool = False
    has_ssl: bool = False
    has_mobile_responsive: bool = False
    has_online_payment: bool = False
    has_social_media: bool = False
    has_email_list: bool = False
    has_analytics: bool = False
    has_contact_form: bool = False


CHECKLIST = [
    ("has_website",            "Website",              "🌐"),
    ("has_ssl",                "SSL Certificate",      "🔒"),
    ("has_mobile_responsive",  "Mobile Responsive",    "📱"),
    ("has_online_payment",     "Online Payments",      "💳"),
    ("has_social_media",       "Social Media Presence", "📣"),
    ("has_email_list",         "Email List",           "✉️"),
    ("has_analytics",          "Analytics Setup",      "📊"),
    ("has_contact_form",       "Contact Form",         "📩"),
]


def audit(presence: DigitalPresence) -> dict:
    """Return a readiness score and breakdown."""
    passed = []
    missing = []

    for attr, label, icon in CHECKLIST:
        if getattr(presence, attr):
            passed.append((label, icon))
        else:
            missing.append((label, icon))

    score = round((len(passed) / len(CHECKLIST)) * 100, 2)

    return {"score": score, "passed": passed, "missing": missing}


def readiness_level(score: float) -> str:
    """Map score to a business maturity level."""
    if score >= 90:   return "🏆 Digital Leader"
    if score >= 70:   return "🚀 Digital Ready"
    if score >= 50:   return "⚙️ Developing"
    if score >= 25:   return "🌱 Early Stage"
    return "❌ Not Started"


def report(presence: DigitalPresence) -> None:
    """Print a full digital readiness report."""
    result = audit(presence)

    print("=" * 55)
    print(f"  DIGITAL PRESENCE AUDIT: {presence.name.upper()}")
    print("=" * 55)
    print(f"\nReadiness Score: {result['score']}%")
    print(f"Level: {readiness_level(result['score'])}")

    print(f"\n✅ In Place ({len(result['passed'])})")
    for label, icon in result["passed"]:
        print(f"   {icon}  {label}")

    print(f"\n❌ Missing ({len(result['missing'])})")
    for label, icon in result["missing"]:
        print(f"   {icon}  {label}")

    print("\n" + "=" * 55)
    if result["missing"]:
        print("Priority Actions:")
        for i, (label, _) in enumerate(result["missing"][:3], start=1):
            print(f"   {i}. Implement {label}")
    print("=" * 55)


if __name__ == "__main__":
    # Example: Hypothetical member organisation
    member_org = DigitalPresence(
        name="Communi-Connect Umbrella",
        has_website=True,
        has_ssl=True,
        has_mobile_responsive=True,
        has_online_payment=False,   # ← Still to build
        has_social_media=True,
        has_email_list=False,
        has_analytics=False,
        has_contact_form=True,
    )

    report(member_org)
