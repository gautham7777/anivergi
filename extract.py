# extract.py
from PIL import Image

# 1. Load the image you saved
img = Image.open('image.png').convert('RGBA')

# 2. Resize to prevent browser crash. Width 100 usually yields ~7,000-10,000 particles.
aspect = img.width / img.height
new_width = 100
new_height = int(new_width / aspect)
img = img.resize((new_width, new_height))

positions = []
colors = []

# 3. Scan pixels
for y in range(new_height):
    for x in range(new_width):
        r, g, b, a = img.getpixel((x, y))
        # Only grab non-transparent pixels
        if a > 128:
            # Map 2D coordinates to 3D space
            px = round((x - new_width / 2) * 0.15, 3)
            py = round(-(y - new_height / 2) * 0.15, 3) # Invert Y for Three.js
            pz = 0 
            
            positions.extend([px, py, pz])
            colors.extend([round(r/255.0, 3), round(g/255.0, 3), round(b/255.0, 3)])

# 4. Write directly to a JS file
with open('data.js', 'w') as f:
    f.write(f"const imagePositions = {positions};\n")
    f.write(f"const imageColors = {colors};\n")

print(f"SUCCESS: data.js created with {len(positions)//3} particles.")