# medical-3d-visualization
[Liver Visualization from CT slices](/docs/csm_001_ct_slices.gif)
## 1. Setup

### a. Install Blender:
Blender is a powerful open-source tool for 3D graphics, is used in this project to display .obj files
- **Option 1:** Download and install Blender 2.8 or higher using the official [installer](https://www.blender.org/download/).
- **Option 2:** Install Blender via [Steam](https://store.steampowered.com/app/365670/Blender/).

### b. Install Required Python Libraries:

You'll need two Python libraries: [pynrrd](https://github.com/mhe/pynrrd) for reading NRRD files and [PyMCubes](https://github.com/pmneila/PyMCubes) for 3D reconstruction using a [marching cubes algorithm](https://en.wikipedia.org/wiki/Marching_cubes).

```bash
conda install pynrrd
pip install --upgrade PyMCubes
```

## 2. How to run it
### a. Convert NRRD image-label pair to Mesh
convert your NRRD files to a mesh format `.obj`.
*Note:* argparse for paths is pending. the scripts requires manual path specification.

```bash
python src\nrrd2mesh_multilabel.py
```

### b. Visualize in Blender

Once you have your `.obj` files, you can visualize them in Blender, The visualization assigns a unique transparent color to each segmented object using the default [plotly color pallete](https://plotly.com/python/discrete-color/#color-sequences-in-plotly-express)

```bash
python src\run_blender_visualizer.py
```
