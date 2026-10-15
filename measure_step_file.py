
import cadquery as cq

# Replace this with your actual STEP filename
step_file = "AQ64-DOT-4-approximate.stp"

# Import the STEP model
model = cq.importers.importStep(step_file)

# Get the model's bounding box
shape = model.val()
bbox = shape.BoundingBox()

print("Imported STEP Model Measurements")
print("-" * 40)
print(f"Length (X): {bbox.xlen:.4f}")
print(f"Width  (Y): {bbox.ylen:.4f}")
print(f"Height (Z): {bbox.zlen:.4f}")