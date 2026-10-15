import cadquery as cq

# Load the STEP model
step_file = "AQ64-DOT-4-approximate.stp"
model = cq.importers.importStep(step_file)
shape = model.val()

# Get the model's overall dimensions
bbox = shape.BoundingBox()

model_dimensions = {
    "Z": bbox.zlen
}

# Spec-sheet dimensions converted from inches to millimeters
spec_dimensions = {
    "A": 0.94 * 25.4,
    "B": 1.17 * 25.4,
    "Tube OD": 0.25 * 25.4,
    "C HEX": 0.375 * 25.4
}

# Team's acceptable error bound
tolerance = 1.5  # mm

print("STEP Model Dimensions")
for axis, value in model_dimensions.items():
    print(f"{axis}: {value:.3f} mm")

print("\nSpec-Sheet Reference Dimensions")
for name, value in spec_dimensions.items():
    print(f"{name}: {value:.3f} mm")

print(f"\nAcceptable error: {tolerance} mm")

def validate_dimension(spec_value, model_value):
    error = abs(model_value - spec_value)
    status = "PASS" if error <= tolerance else "REVIEW"
    return error, status

# Example test of the validation logic.
# Replace these example values with actual, matching measurements.
example_error, example_status = validate_dimension(
    spec_dimensions["B"],
    model_dimensions["Z"]
)

print("\nCompare dimension B with model Z")
print(f"Error: {example_error:.3f} mm")
print(f"Result: {example_status}")

