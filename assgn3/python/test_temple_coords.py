import numpy as np
import helper as hlp
import skimage.io as io
import submission as sub
import matplotlib.pyplot as plt

from submission import *

DATA_PATH = "../data/"

# 1. Load the two temple images and the points from data/some_corresp.npz
img1 = io.imread(DATA_PATH+"im1.png")
img2 = io.imread(DATA_PATH+"im2.png")
some_cor = np.load(DATA_PATH+"some_corresp.npz")
# print(some_cor.files)
pts1 = some_cor['pts1']; pts2 = some_cor['pts2']


# 2. Run eight_point to compute F
M = max(img1.shape)
F = eight_point(pts1, pts2, M)
# hlp.displayEpipolarF(img1, img2, F)

# 3. Load points in image 1 from data/temple_coords.npz
tem_pts1 = np.load(DATA_PATH+"temple_coords.npz")
tem_pts1 = tem_pts1['pts1']
# print(tem_pts1.max())
# print(tem_pts1.min())
# print(img1.shape)

# 4. Run epipolar_correspondences to get points in image 2
tem_pts2 = epipolar_correspondences(img1, img2, F, tem_pts1)
# epipolarMatchGUI(img1, img2, F)

# 5. Compute the camera projection matrix P1


# 6. Use camera2 to get 4 camera projection matrices P2

# 7. Run triangulate using the projection matrices

# 8. Figure out the correct P2

# 9. Scatter plot the correct 3D points

# 10. Save the computed extrinsic parameters (R1,R2,t1,t2) to data/extrinsics.npz
