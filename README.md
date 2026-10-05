# Campus Parking Fee Calculator

A Python command-line utility that computes parking fees based on vehicle classifications, parking duration, and discount entitlements. Built to practice clean conditional control flow, boolean evaluation, and defensive user input handling.

## Features
- **Defensive Input Handling:** Sanitizes inputs with `.strip().upper()` to handle arbitrary whitespace and case-insensitive inputs (`c`, `CAR`, `  c  `).
- **Input Guardrails:** Validates numeric types and rejects negative durations gracefully without runtime crashes.
- **Dynamic Pricing Rules:**
  - Standard hourly tiers: Car ($3.00), Motorcycle ($1.50), Bus ($7.00).
  - Overtime congestion surcharge (15% for stays over 8 hours).
  - Student/Staff entitlement discount (20%).
  - Minimum floor enforcement ($1.00 minimum charge).

## Usage
Run the script using Python 3:
```bash
python calculator.py