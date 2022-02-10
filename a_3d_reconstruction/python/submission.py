"""
Homework 5
Submission Functions
"""

# import packages here
import numpy as np
import helper as hlp

"""
Q3.1.1 Eight Point Algorithm
       [I] pts1, points in image 1 (Nx2 matrix)
           pts2, points in image 2 (Nx2 matrix)
           M, scalar value computed as max(H1,W1)
       [O] F, the fundamental matrix (3x3 matrix)
"""
def eight_point(pts1, pts2, M):
    N = pts1.shape[0]

    # normalize pints coords in image
    T = 1.0/M * np.eye(3);  T[2,2] = 1.0
    Temp = 1.0/M * np.eye(N)
    pts1 = Temp@pts1
    pts2 = Temp@pts2
    print(pts1)
    A = np.zeros([N,9]) # we have overdeterminstic system
    for i in range(N):
        x_i = pts1[i][0]; y_i = pts1[i][1]
        x_i_p = pts2[i][0]; y_i_p = pts2[i][1]
        A[i,0] = x_i_p * x_i
        A[i,1] = x_i_p * y_i
        A[i,2] = x_i_p 
        A[i,3] = y_i_p * x_i
        A[i,4] = y_i_p * y_i
        A[i,5] = y_i_p 
        A[i,6] = x_i
        A[i,7] = y_i
        A[i,8] = 1

    # print(A)
    U, D, V = np.linalg.svd(A)
    F_hat = V.T[:,8].reshape((3,3))
    U, D, V = np.linalg.svd(F_hat)
    D[2] = 0.0
    F = U @ np.diag(D) @ V.T
    F = T.T @ F @ T
    print("F:", F.shape)
    return F

"""
Q3.1.2 Epipolar Correspondences
       [I] im1, image 1 (H1xW1 matrix)
           im2, image 2 (H2xW2 matrix)
           F, fundamental matrix from image 1 to image 2 (3x3 matrix)
           pts1, points in image 1 (Nx2 matrix)
       [O] pts2, points in image 2 (Nx2 matrix)
"""

def _similarity(im1, im2, xi,yi,xi_prime, yi_prime):
    a,b,c = im1.shape
    for _c in range(c):
        cost = abs(im1[xi,yi, _c] - im2[xi_prime, yi_prime,_c])
    + abs(im1[xi-1,yi, _c] - im2[xi_prime, yi_prime, _c])
    + abs(im1[xi+1,yi, _c] - im2[xi_prime+1, yi_prime, _c])
    return cost

def epipolar_correspondences(im1, im2, F, pts1):
    # replace pass by your implementation
    MX, MY, _ = im1.shape
    N = pts1.shape[0]
    pts2 = np.zeros([N,2])
    for i in range(N):
        xi = pts1[i,0]; yi = pts1[i,1]
        e = np.array([xi,yi,1]).reshape((3,1))
        epi_line = F @ e # [a b c].T
        # print(epi_line)
        a = epi_line[0,0]; b = epi_line[1,0]; c = epi_line[2,0]

        final_x = 0; final_y = 0; _cost = 1e8
        for xi_prime in range(0, MX):
            yi_prime = (-c -a*xi_prime ) / b

            cur_cost = _similarity(im1, im2, xi,yi,xi_prime, yi_prime)
            if cur_cost < _cost:
                _cost = cur_cost; final_x = xi_prime; final_y = yi_prime
        pts2[i,:] = [final_x,final_y]
    return pts2




"""
Q3.1.3 Essential Matrix
       [I] F, the fundamental matrix (3x3 matrix)
           K1, camera matrix 1 (3x3 matrix)
           K2, camera matrix 2 (3x3 matrix)
       [O] E, the essential matrix (3x3 matrix)
"""
def essential_matrix(F, K1, K2):
    # replace pass by your implementation
    E = K2.T @ F @ K1
    return E

"""
Q3.1.4 Triangulation
       [I] P1, camera projection matrix 1 (3x4 matrix)
           pts1, points in image 1 (Nx2 matrix)
           P2, camera projection matrix 2 (3x4 matrix)
           pts2, points in image 2 (Nx2 matrix)
       [O] pts3d, 3D points in space (Nx3 matrix)
"""
def triangulate(P1, pts1, P2, pts2):
    # replace pass by your implementation
    pass


"""
Q3.2.1 Image Rectification
       [I] K1 K2, camera matrices (3x3 matrix)
           R1 R2, rotation matrices (3x3 matrix)
           t1 t2, translation vectors (3x1 matrix)
       [O] M1 M2, rectification matrices (3x3 matrix)
           K1p K2p, rectified camera matrices (3x3 matrix)
           R1p R2p, rectified rotation matrices (3x3 matrix)
           t1p t2p, rectified translation vectors (3x1 matrix)
"""
def rectify_pair(K1, K2, R1, R2, t1, t2):
    # replace pass by your implementation
    pass


"""
Q3.2.2 Disparity Map
       [I] im1, image 1 (H1xW1 matrix)
           im2, image 2 (H2xW2 matrix)
           max_disp, scalar maximum disparity value
           win_size, scalar window size value
       [O] dispM, disparity map (H1xW1 matrix)
"""
def get_disparity(im1, im2, max_disp, win_size):
    # replace pass by your implementation
    pass


"""
Q3.2.3 Depth Map
       [I] dispM, disparity map (H1xW1 matrix)
           K1 K2, camera matrices (3x3 matrix)
           R1 R2, rotation matrices (3x3 matrix)
           t1 t2, translation vectors (3x1 matrix)
       [O] depthM, depth map (H1xW1 matrix)
"""
def get_depth(dispM, K1, K2, R1, R2, t1, t2):
    # replace pass by your implementation
    pass


"""
Q3.3.1 Camera Matrix Estimation
       [I] x, 2D points (Nx2 matrix)
           X, 3D points (Nx3 matrix)
       [O] P, camera matrix (3x4 matrix)
"""
def estimate_pose(x, X):
    # replace pass by your implementation
    pass


"""
Q3.3.2 Camera Parameter Estimation
       [I] P, camera matrix (3x4 matrix)
       [O] K, camera intrinsics (3x3 matrix)
           R, camera extrinsics rotation (3x3 matrix)
           t, camera extrinsics translation (3x1 matrix)
"""
def estimate_params(P):
    # replace pass by your implementation
    pass
