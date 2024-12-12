# blender_tomo
Repository with codes to simmulate a CT Scan aquisition with Blender and then reconstructing the image from the obtained projections

This repository will contain generic Blender scenarios with automated render codes that will simulate the acquisition of CT scans. This is done by controling that Alpha of the created structures, changing their oppacities, allowing some light to penetrate through them.

With this, it becomes possible to use simples light to simulate the effects of x-rays, by using a mesh in the opposite side of light to identify how much light passed through each section of the volume.

To run the current stage of this repository, you can simply run the following code in your cmd:

blender ./scenario/base.blend --background --python generate_scans.py

The background flag is optional, but useful, since it will make Blender run entirely in the background, instead of opening the GUI.
The generated projections will be stored in the scans folder, under the name "test" with a number to differentiate between multiple simulations done.

To reconstruct the generated projections, the notebook "ct_reconstruct.ipynb" contains some codes and functions that will make it easy to visualize the process.
This repository is still under development, so it's still simple and the reconstruction algorithms are still under development, so be aware of that when trying to run the codes here made available.