import bpy
import os
import numpy as np

C = bpy.context
D = bpy.data

def make_scans(name='Empty', samples = 180, animation = False, slices_number = 1):
    scans_path = os.path.join(os.getcwd(), 'scans')
    id = len(os.listdir(scans_path))
    scans_folder = os.path.join(scans_path, f"test{id}")
    os.makedirs(scans_folder, exist_ok = True)

    step = 180 / samples
    
    # Defining scanner
    tomograph = D.objects[name]
    for slice in range(slices_number):
        for i in range(samples):
            angle = i * step
            tomograph.rotation_euler.y = np.radians(angle)
            C.scene.render.filepath = os.path.join(scans_folder, f"{i}.jpg")
            bpy.ops.render.render(write_still = True)
    
    tomograph.rotation_euler.y = 0  
    
make_scans(samples=10)