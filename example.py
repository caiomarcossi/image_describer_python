import sys
from pathlib import Path
from image_describer import ImageDescriber
import pyperclip as pc

describer=ImageDescriber()
image_path=Path(input("Path of the image:"))
if not image_path.exists() or not image_path.is_file():
	print("File not found")
	sys.exit(0)
description=describer.describe(image_path)
pc.copy(description)
