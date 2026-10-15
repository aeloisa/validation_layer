
import cadquery as cq

# Reference dimensions from the spec sheet (in millimeters)
spec_dimensions = {
    "length": 100,
    "width": 60,
    "height": 40
}

# Create a test CAD model (in millimeters)
model = cq.Workplane("XY").box(98, 60, 40)

# Automatically measure the model
bbox = model.val().BoundingBox()

model_dimensions = {
    "length": bbox.xlen,
    "width": bbox.ylen,
    "height": bbox.zlen
}

# Example tolerance for testing only
tolerance = 1.0  # millimeters

print("Dimensional Validation")
print("-" * 35)

for name, spec_value in spec_dimensions.items():
    model_value = model_dimensions[name]
    difference = abs(spec_value - model_value)
    passed = difference <= tolerance

    status = "PASS" if passed else "REVIEW"

    print(f"\n{name.capitalize()}")
    print(f"  Spec:       {spec_value:.2f} mm")
    print(f"  Model:      {model_value:.2f} mm")
    print(f"  Difference: {difference:.2f} mm")
    print(f"  Status:     {status}")