# Supposedly before 1st day of class

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:16:22 2017

@author: mead
"""

import torch  # This imports the torch library.
import matplotlib.pyplot as plt  # This is python's popular plotting library.
# This is to ensure matplotlib plots inline and does not try to open a new window.
%matplotlib inline


myTensor = torch.FloatTensor(7, 7)
myTensor[:, :] = 0   # Assign zeros everywhere in the matrix.
myTensor[3, 3] = 1   # Assign one in position 3, 3
myTensor[:2, :] = 1   # Assign ones on the top 2 rows.
myTensor[-2:, :] = 1    # Assign ones on the bottom 2 rows.

# Show the tensor.
def showTensor(aTensor):
    plt.figure()
    plt.imshow(aTensor.numpy())
    plt.colorbar()
    plt.show()
    
showTensor(myTensor);


