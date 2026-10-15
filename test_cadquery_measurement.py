
import cadquery as cq

# Create a test box with known dimensions (in millimeters)
model = cq.Workplane("XY").box(100, 60, 40)

# Get the actual bounding box from the CAD geometry
shape = model.val()
bbox = shape.BoundingBox()

print("CAD Model Measurements")
print("----------------------")
print(f"Length (X): {bbox.xlen:.2f} mm")
print(f"Width  (Y): {bbox.ylen:.2f} mm")
print(f"Height (Z): {bbox.zlen:.2f} mm")