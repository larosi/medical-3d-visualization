# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:04:01 2023

@author: Mico
"""

import os
import numpy as np
import nrrd #pynrrd # conda install pynrrd
import mcubes

if __name__ == '__main__' :
    dataset_path = r'C:\Users\Mico\Desktop\github\medical-3d-visualization\data\Ejemplo Multilabel-20230923T135530Z-001\Ejemplo Multilabel'
    filename = 'liver_image.nrrd'
    mask_filename = 'vascular_segmentation.nrrd'
    image_fn = os.path.join(dataset_path, filename)
    segmentation_fn = os.path.join(dataset_path, mask_filename) 

    output_filename = os.path.join(dataset_path,'..', mask_filename.replace('.nrrd', '.obj'))
    
    data, header = nrrd.read(image_fn)
    data_mask, header_mask = nrrd.read(segmentation_fn)
    
    res_x, res_y, res_z = np.diag(header['space directions'])
    labels = np.unique(data_mask)
    labels = labels[labels>0]
    
    for label in labels:
        output_filename = os.path.join(dataset_path,'..', mask_filename.replace('.nrrd', f'_{label}.obj'))
        vertices, triangles = mcubes.marching_cubes(data_mask==label, 0.5)
        vertices = vertices * np.array([res_x, res_y, res_z])
        mcubes.export_obj(vertices, triangles, output_filename)
