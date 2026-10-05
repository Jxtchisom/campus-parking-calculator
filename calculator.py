# ==========================================
# Campus Parking Fee Calculator
# Demonstrating defensive input validation and conditional logic
# ==========================================

print("=== CAMPUS PARKING FEE CALCULATOR ===")
print("Vehicle Types: [C]ar ($3.00/hr) | [M]otorcycle ($1.50/hr) | [B]us ($7.00/hr)")
print("======================================\n")

# 1. Capture and sanitize vehicle type
vehicle_type = input("Enter vehicle type (C, M, B): ").strip().upper()

# Validate vehicle selection before proceeding
if vehicle_type == "C":
    rate = 3.00
    vehicle_name = "Car"
elif vehicle_type == "M":
    rate = 1.50
    vehicle_name = "Motorcycle"
elif vehicle_type == "B":
    rate = 7.00
    vehicle_name = "Bus"
else:
    print(f"Error: '{vehicle_type}' is an unrecognized vehicle type.")
    exit()

# 2. Capture and validate duration
duration_input = input("Enter hours parked: ").strip()

# Guard against non-numeric entries or negative durations
try:
    hours = float(duration_input)
    if hours < 0:
        print("Error: Duration cannot be negative.")
        exit()
except ValueError:
    print(f"Error: '{duration_input}' is not a valid number.")
    exit()

# Quick exit if zero hours
if hours == 0:
    print("\nDuration was 0 hours. Total fee: $0.00")
    exit()

# 3. Capture pass status
has_pass = input("Do you hold an active Student/Staff pass? (Y/N): ").strip().upper()
is_pass_holder = has_pass == "Y" or has_pass == "YES"

# 4. Calculate base fee
subtotal = hours * rate

# 5. Apply overtime surcharge if parked longer than 8 hours (+15%)
surcharge = 0.0
if hours > 8:
    surcharge = subtotal * 0.15

# 6. Apply discount if student/staff pass holder (-20%)
discount = 0.0
if is_pass_holder:
    discount = (subtotal + surcharge) * 0.20

# 7. Final total calculation with minimum fee enforcement ($1.00)
final_total = (subtotal + surcharge) - discount
if final_total < 1.00:
    final_total = 1.00

# 8. Print receipt summary
print("\n" + "=" * 32)
print("       PARKING RECEIPT")
print("=" * 32)
print(f"Vehicle:           {vehicle_name}")
print(f"Hours Parked:      {hours:.2f} hrs")
print(f"Base Subtotal:     ${subtotal:.2f}")

if surcharge > 0:
    print(f"Overtime (+15%):   +${surcharge:.2f}")

if discount > 0:
    print(f"Pass Discount:     -${discount:.2f}")

print("-" * 32)
print(f"FINAL TOTAL:       ${final_total:.2f}")
print("=" * 32)