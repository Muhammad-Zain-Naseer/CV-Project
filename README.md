# CV-Project – Quick Start

1) Open VS Code in this folder.
2) Install a simple server globally (only once):
```
npm install -g http-server
```
3) Serve the Three.js app:
```
npx http-server . -p 8000
```
3) Visit in the browser:
```
http://localhost:8000/virtual_tour_advanced.html
```

### Python libraries used elsewhere in this repo
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from itertools import product
from PIL import Image
from PIL.ExifTags import TAGS
import open3d as o3d
from scipy.optimize import least_squares
from collections import defaultdict
import pickle
import os

plt.rcParams['figure.figsize'] = (12, 10)
```

Note: `open3d` currently supports Python 3.10 or lower; use 3.10 or earlier if you need it.*** End Patch"
