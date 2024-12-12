import bpy
import os
import numpy as np

def make_scans(name='Empty', samples = 180, animation = False, slices_number = 1):
    scans_path = './scans'
    id = len(os.listdir(scans_path))
    os.makedirs(os.path.join(scans_path, f"test{id}"), if_exists = True)
    step = 180 / samples
    
    # Defining scanner
    tomograph = bpy.data.objects[name]
    for slice in range(slices_number):
        for i in range(samples):
            angle = i * step
            tomograph.rotation_euler.y = np.radians(angle)
            bpy.context.scene.render.filepath = os.path.join(scans_path,f"test{id}" , f"{i}.jpg")
            bpy.ops.render.render(write_still = True)
    
    tomograph.rotation_euler.y = 0  
    
make_scans(samples=10)