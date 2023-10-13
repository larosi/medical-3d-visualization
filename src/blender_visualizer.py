# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:30:04 2023

@author: Mico
"""

import bpy
import os


def delete_default_objets(default_objets=['Cube', 'Light', 'Camera']):
    objects_exits = min([obj_name in bpy.data.objects for obj_name in default_objets])
    if objects_exits:
        bpy.ops.object.select_all(action='DESELECT')
        for obj_name in default_objets:
            bpy.data.objects[obj_name].select_set(True)
        bpy.ops.object.delete()


def import_objs(obj_folder):
    obj_filenames = os.listdir(obj_folder)
    
    for obj_fn in obj_filenames:
        obj_filepath = os.path.join(obj_folder, obj_fn)
        bpy.ops.wm.obj_import(filepath=obj_filepath,
                              directory=obj_folder,
                              files=[{"name": obj_fn, "name": obj_fn}],
                              forward_axis='X', up_axis='Z')


def create_transparent_material(color, material_name):
    material = bpy.data.materials.new(name=material_name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Specular'].default_value = 0.5
    bsdf.inputs['Roughness'].default_value = 0.2
    bsdf.inputs['Alpha'].default_value = 0.2
    material.blend_method = 'BLEND'
    return material

def set_viewport_shading():
    for area in bpy.context.screen.areas: 
            if area.type == 'VIEW_3D':
                space = area.spaces.active
                if space.type == 'VIEW_3D':
                    space.shading.type = 'MATERIAL'

def zoom_all_objects():
    # Select all objects and focus view on selection
    bpy.ops.object.select_all(action='SELECT')
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = bpy.context.copy()
                    override['area'] = area
                    override['region'] = region
                    bpy.ops.view3d.view_selected(override)
                    break


DEFAULT_COLORS = [(31, 119, 180),  # 0: Blue
                  (255, 127, 14),
                  (44, 160, 44),
                  (214, 39, 40),   # 3: Red
                  (148, 103, 189),
                  (140, 86, 75),
                  (227, 119, 194),
                  (127, 127, 127),
                  (188, 189, 34),
                  (23, 190, 207)]

bpy.context.preferences.view.show_splash = False
delete_default_objets()
obj_folder = r'C:\Users\Mico\Desktop\github\medical-3d-visualization\data\Ejemplo Multilabel-20230923T135530Z-001\obj'

# import all objects in a folder
import_objs(obj_folder)

# assing a transparent color to each object
color_i = 0
for obj in bpy.data.objects:
    rgb = DEFAULT_COLORS[color_i]
    color = (rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0, 1.0)
    color_i += 1
    material_name = obj.name 
    material = create_transparent_material(color, material_name)
    obj.data.materials.append(material)
    
    decimate_mod = obj.modifiers.new("Decimate", type='DECIMATE')
    decimate_mod.decimate_type = 'COLLAPSE'
    decimate_mod.ratio = 0.5
    #bpy.ops.object.modifier_apply(modifier="Decimate")
    smooth_mod = obj.modifiers.new("Smooth", type='SMOOTH')
    smooth_mod.factor = 0.5
    smooth_mod.iterations = 8
    #bpy.ops.object.modifier_apply(modifier="Smooth")
    
# zoom out to view all objects
set_viewport_shading()
zoom_all_objects()

