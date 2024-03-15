# -*- coding: utf-8 -*-
"""data_loader

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgQfgVgXPAe7n28ByyVviFnKKSqrcc9u
"""

import os
from glob import glob
import numpy as np
import skimage.transform as st
from tensorflow.keras.utils import load_img, img_to_array

class DataLoader():
  def __init__(self, dataset_path:str):
    self.base_path = dataset_path
    self.data_path = {
        'train': os.path.join(self.base_path,'train'),
        'valid': os.path.join(self.base_path,'valid'),
        'test': os.path.join(self.base_path,'test')
    }
    label_base = os.path.join(self.base_path,'labels')
    self.label_path = {
        'train':os.path.join(label_base,'train'),
        'valid':os.path.join(label_base,'valid'),
        'test':os.path.join(label_base,'test')
    }

  def load(self, image_shape:tuple, purpose:str):
    image_list = []
    mask_list = []

    img_path = glob(self.data_path[purpose]+'/*')
    mask_path = glob(self.label_path[purpose]+'/*')

    for path in img_path:
      img = load_img(path,color_mode='rgb',target_size=image_shape)
      img = img_to_array(img)
      image_list.append(img)

    for path in mask_path:
      mask = np.load(path)
      mask = st.resize(mask, image_shape,order=0, preserve_range=True, anti_aliasing=False)
      mask_list.append(mask)

    return np.array(image_list), np.array(mask_list)

