#cython: language_level=3

import numpy as np
cimport cython

def _mandelbrot_cy(centre, view_side, int n_max_iter = 255, int view_side_pixels = 500):
  image = np.zeros((view_side_pixels, view_side_pixels), dtype=np.intc)
  return image
