from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.81968, -76.86868,  45.88631,
                       
     VERTEX,    9.83349, -73.54475,  46.79787,
     VERTEX,   10.46079, -73.30827,  47.48502,
     VERTEX,   10.82313, -73.57800,  48.33212,
     VERTEX,   10.78211, -74.25090,  49.01558,
     VERTEX,   10.35341, -75.06995,  49.27435,
     VERTEX,    9.70077, -75.72231,  49.00961,
     VERTEX,    9.07348, -75.95879,  48.32245,
     VERTEX,    8.71114, -75.68906,  47.47536,
     VERTEX,    8.75215, -75.01617,  46.79190,
     VERTEX,    9.18085, -74.19711,  46.53312,
     VERTEX,    9.83349, -73.54475,  46.79787,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.76713, -74.63353,  47.90374,
                       
     VERTEX,    9.83349, -73.54475,  46.79787,
     VERTEX,   10.46079, -73.30827,  47.48502,
     VERTEX,   10.82313, -73.57800,  48.33212,
     VERTEX,   10.78211, -74.25090,  49.01558,
     VERTEX,   10.35341, -75.06995,  49.27435,
     VERTEX,    9.70077, -75.72231,  49.00961,
     VERTEX,    9.07348, -75.95879,  48.32245,
     VERTEX,    8.71114, -75.68906,  47.47536,
     VERTEX,    8.75215, -75.01617,  46.79190,
     VERTEX,    9.18085, -74.19711,  46.53312,
     VERTEX,    9.83349, -73.54475,  46.79787,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,   9.76713, -74.63353,  47.90374,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.86997, -76.48645,  40.75016,
                       
     VERTEX,   24.48994, -75.97855,  41.15118,
     VERTEX,   24.72655, -75.11118,  41.48777,
     VERTEX,   25.12359, -74.64738,  42.22861,
     VERTEX,   25.52941, -74.76429,  43.09072,
     VERTEX,   25.78901, -75.41727,  43.74481,
     VERTEX,   25.80322, -76.35690,  43.94103,
     VERTEX,   25.56661, -77.22427,  43.60443,
     VERTEX,   25.16957, -77.68806,  42.86359,
     VERTEX,   24.76375, -77.57114,  42.00148,
     VERTEX,   24.50415, -76.91817,  41.34740,
     VERTEX,   24.48994, -75.97855,  41.15118,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.14658, -76.16772,  42.54610,
                       
     VERTEX,   24.48994, -75.97855,  41.15118,
     VERTEX,   24.72655, -75.11118,  41.48777,
     VERTEX,   25.12359, -74.64738,  42.22861,
     VERTEX,   25.52941, -74.76429,  43.09072,
     VERTEX,   25.78901, -75.41727,  43.74481,
     VERTEX,   25.80322, -76.35690,  43.94103,
     VERTEX,   25.56661, -77.22427,  43.60443,
     VERTEX,   25.16957, -77.68806,  42.86359,
     VERTEX,   24.76375, -77.57114,  42.00148,
     VERTEX,   24.50415, -76.91817,  41.34740,
     VERTEX,   24.48994, -75.97855,  41.15118,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.14658, -76.16772,  42.54610,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.78924, -73.23392,  36.35913,
                       
     VERTEX,   26.52921, -73.46824,  36.59360,
     VERTEX,   26.59936, -72.54044,  36.82997,
     VERTEX,   26.88689, -71.93327,  37.51573,
     VERTEX,   27.28199, -71.87865,  38.38895,
     VERTEX,   27.63374, -72.39745,  39.11609,
     VERTEX,   27.80777, -73.29149,  39.41940,
     VERTEX,   27.73763, -74.21928,  39.18304,
     VERTEX,   27.45009, -74.82645,  38.49727,
     VERTEX,   27.05499, -74.88107,  37.62405,
     VERTEX,   26.70325, -74.36228,  36.89692,
     VERTEX,   26.52921, -73.46824,  36.59360,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.16849, -73.37986,  38.00650,
                       
     VERTEX,   26.52921, -73.46824,  36.59360,
     VERTEX,   26.59936, -72.54044,  36.82997,
     VERTEX,   26.88689, -71.93327,  37.51573,
     VERTEX,   27.28199, -71.87865,  38.38895,
     VERTEX,   27.63374, -72.39745,  39.11609,
     VERTEX,   27.80777, -73.29149,  39.41940,
     VERTEX,   27.73763, -74.21928,  39.18304,
     VERTEX,   27.45009, -74.82645,  38.49727,
     VERTEX,   27.05499, -74.88107,  37.62405,
     VERTEX,   26.70325, -74.36228,  36.89692,
     VERTEX,   26.52921, -73.46824,  36.59360,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  27.16849, -73.37986,  38.00650,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.55732, -18.89428,  92.09277,
                       
     VERTEX,   36.45636, -19.26874,  91.89655,
     VERTEX,   36.41504, -18.38430,  91.52552,
     VERTEX,   36.17603, -17.88020,  90.74427,
     VERTEX,   35.83063, -17.94899,  89.85120,
     VERTEX,   35.51075, -18.56438,  89.18745,
     VERTEX,   35.33860, -19.49133,  89.00654,
     VERTEX,   35.37992, -20.37577,  89.37757,
     VERTEX,   35.61893, -20.87987,  90.15883,
     VERTEX,   35.96433, -20.81108,  91.05189,
     VERTEX,   36.28421, -20.19569,  91.71564,
     VERTEX,   36.45636, -19.26874,  91.89655,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.89748, -19.38004,  90.45155,
                       
     VERTEX,   36.45636, -19.26874,  91.89655,
     VERTEX,   36.41504, -18.38430,  91.52552,
     VERTEX,   36.17603, -17.88020,  90.74427,
     VERTEX,   35.83063, -17.94899,  89.85120,
     VERTEX,   35.51075, -18.56438,  89.18745,
     VERTEX,   35.33860, -19.49133,  89.00654,
     VERTEX,   35.37992, -20.37577,  89.37757,
     VERTEX,   35.61893, -20.87987,  90.15883,
     VERTEX,   35.96433, -20.81108,  91.05189,
     VERTEX,   36.28421, -20.19569,  91.71564,
     VERTEX,   36.45636, -19.26874,  91.89655,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  35.89748, -19.38004,  90.45155,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.40716, -17.99049,  84.74892,
                       
     VERTEX,   32.02357, -18.10414,  84.74737,
     VERTEX,   31.94592, -17.19925,  84.43633,
     VERTEX,   31.69775, -16.65458,  83.68576,
     VERTEX,   31.37385, -16.67818,  82.78236,
     VERTEX,   31.09793, -17.26104,  82.07120,
     VERTEX,   30.97540, -18.18051,  81.82391,
     VERTEX,   31.05304, -19.08540,  82.13496,
     VERTEX,   31.30121, -19.63006,  82.88552,
     VERTEX,   31.62512, -19.60646,  83.78892,
     VERTEX,   31.90103, -19.02361,  84.50008,
     VERTEX,   32.02357, -18.10414,  84.74737,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.49948, -18.14232,  83.28564,
                       
     VERTEX,   32.02357, -18.10414,  84.74737,
     VERTEX,   31.94592, -17.19925,  84.43633,
     VERTEX,   31.69775, -16.65458,  83.68576,
     VERTEX,   31.37385, -16.67818,  82.78236,
     VERTEX,   31.09793, -17.26104,  82.07120,
     VERTEX,   30.97540, -18.18051,  81.82391,
     VERTEX,   31.05304, -19.08540,  82.13496,
     VERTEX,   31.30121, -19.63006,  82.88552,
     VERTEX,   31.62512, -19.60646,  83.78892,
     VERTEX,   31.90103, -19.02361,  84.50008,
     VERTEX,   32.02357, -18.10414,  84.74737,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  31.49948, -18.14232,  83.28564,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   86.54025, -60.43397,  92.68842,
                       
     VERTEX,   83.30532, -67.28553,  92.77398,
     VERTEX,   82.63408, -66.90851,  92.20049,
     VERTEX,   81.84601, -66.36057,  92.18301,
     VERTEX,   81.24213, -65.85100,  92.72823,
     VERTEX,   81.05309, -65.57444,  93.62788,
     VERTEX,   81.35111, -65.63652,  94.53835,
     VERTEX,   82.02235, -66.01353,  95.11183,
     VERTEX,   82.81042, -66.56148,  95.12931,
     VERTEX,   83.41431, -67.07105,  94.58409,
     VERTEX,   83.60334, -67.34761,  93.68444,
     VERTEX,   83.30532, -67.28553,  92.77398,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   82.32822, -66.46102,  93.65616,
                       
     VERTEX,   83.30532, -67.28553,  92.77398,
     VERTEX,   82.63408, -66.90851,  92.20049,
     VERTEX,   81.84601, -66.36057,  92.18301,
     VERTEX,   81.24213, -65.85100,  92.72823,
     VERTEX,   81.05309, -65.57444,  93.62788,
     VERTEX,   81.35111, -65.63652,  94.53835,
     VERTEX,   82.02235, -66.01353,  95.11183,
     VERTEX,   82.81042, -66.56148,  95.12931,
     VERTEX,   83.41431, -67.07105,  94.58409,
     VERTEX,   83.60334, -67.34761,  93.68444,
     VERTEX,   83.30532, -67.28553,  92.77398,
                       
     END,              
                       
     CYLINDER,   75.51300, -76.21300,  95.22200,  82.32822, -66.46102,  93.65616,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   79.98777, -55.20199,  88.33964,
                       
     VERTEX,   77.97029, -61.58364,  88.23674,
     VERTEX,   77.32344, -61.29648,  87.58810,
     VERTEX,   76.48598, -60.84087,  87.47549,
     VERTEX,   75.77779, -60.39084,  87.94189,
     VERTEX,   75.46938, -60.11828,  88.80919,
     VERTEX,   75.67854, -60.12730,  89.74608,
     VERTEX,   76.32539, -60.41446,  90.39471,
     VERTEX,   77.16285, -60.87007,  90.50734,
     VERTEX,   77.87104, -61.32011,  90.04092,
     VERTEX,   78.17945, -61.59266,  89.17364,
     VERTEX,   77.97029, -61.58364,  88.23674,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.82442, -60.85547,  88.99141,
                       
     VERTEX,   77.97029, -61.58364,  88.23674,
     VERTEX,   77.32344, -61.29648,  87.58810,
     VERTEX,   76.48598, -60.84087,  87.47549,
     VERTEX,   75.77779, -60.39084,  87.94189,
     VERTEX,   75.46938, -60.11828,  88.80919,
     VERTEX,   75.67854, -60.12730,  89.74608,
     VERTEX,   76.32539, -60.41446,  90.39471,
     VERTEX,   77.16285, -60.87007,  90.50734,
     VERTEX,   77.87104, -61.32011,  90.04092,
     VERTEX,   78.17945, -61.59266,  89.17364,
     VERTEX,   77.97029, -61.58364,  88.23674,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.82442, -60.85547,  88.99141,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.91869, -74.17678,  88.08057,
                       
     VERTEX,   73.33930, -79.03951,  88.63483,
     VERTEX,   72.76514, -78.31568,  88.37403,
     VERTEX,   72.32236, -77.52379,  88.68780,
     VERTEX,   72.18008, -76.96630,  89.45628,
     VERTEX,   72.39267, -76.85616,  90.38595,
     VERTEX,   72.87891, -77.23544,  91.12170,
     VERTEX,   73.45308, -77.95926,  91.38249,
     VERTEX,   73.89586, -78.75115,  91.06873,
     VERTEX,   74.03813, -79.30864,  90.30024,
     VERTEX,   73.82555, -79.41878,  89.37057,
     VERTEX,   73.33930, -79.03951,  88.63483,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   73.10911, -78.13747,  89.87827,
                       
     VERTEX,   73.33930, -79.03951,  88.63483,
     VERTEX,   72.76514, -78.31568,  88.37403,
     VERTEX,   72.32236, -77.52379,  88.68780,
     VERTEX,   72.18008, -76.96630,  89.45628,
     VERTEX,   72.39267, -76.85616,  90.38595,
     VERTEX,   72.87891, -77.23544,  91.12170,
     VERTEX,   73.45308, -77.95926,  91.38249,
     VERTEX,   73.89586, -78.75115,  91.06873,
     VERTEX,   74.03813, -79.30864,  90.30024,
     VERTEX,   73.82555, -79.41878,  89.37057,
     VERTEX,   73.33930, -79.03951,  88.63483,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  73.10911, -78.13747,  89.87827,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   77.14320, -77.92091,  92.43362,
                       
     VERTEX,   71.15694, -81.97524,  93.11109,
     VERTEX,   70.66726, -81.16602,  92.94684,
     VERTEX,   70.36069, -80.34896,  93.34688,
     VERTEX,   70.35432, -79.83615,  94.15841,
     VERTEX,   70.65059, -79.82347,  95.07146,
     VERTEX,   71.13634, -80.31576,  95.73727,
     VERTEX,   71.62601, -81.12498,  95.90154,
     VERTEX,   71.93258, -81.94204,  95.50150,
     VERTEX,   71.93895, -82.45484,  94.68996,
     VERTEX,   71.64268, -82.46753,  93.77691,
     VERTEX,   71.15694, -81.97524,  93.11109,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   71.14664, -81.14550,  94.42419,
                       
     VERTEX,   71.15694, -81.97524,  93.11109,
     VERTEX,   70.66726, -81.16602,  92.94684,
     VERTEX,   70.36069, -80.34896,  93.34688,
     VERTEX,   70.35432, -79.83615,  94.15841,
     VERTEX,   70.65059, -79.82347,  95.07146,
     VERTEX,   71.13634, -80.31576,  95.73727,
     VERTEX,   71.62601, -81.12498,  95.90154,
     VERTEX,   71.93258, -81.94204,  95.50150,
     VERTEX,   71.93895, -82.45484,  94.68996,
     VERTEX,   71.64268, -82.46753,  93.77691,
     VERTEX,   71.15694, -81.97524,  93.11109,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  71.14664, -81.14550,  94.42419,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   74.56277, -81.74161,  98.53464,
                       
     VERTEX,   68.26025, -84.71220,  99.31223,
     VERTEX,   67.90767, -83.82033,  99.26910,
     VERTEX,   67.77927, -83.01093,  99.76908,
     VERTEX,   67.92409, -82.59315, 100.62119,
     VERTEX,   68.28681, -82.72658, 101.49995,
     VERTEX,   68.72889, -83.36025, 102.06972,
     VERTEX,   69.08147, -84.25212, 102.11285,
     VERTEX,   69.20987, -85.06152, 101.61287,
     VERTEX,   69.06505, -85.47930, 100.76076,
     VERTEX,   68.70232, -85.34587,  99.88199,
     VERTEX,   68.26025, -84.71220,  99.31223,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   68.49457, -84.03622, 100.69097,
                       
     VERTEX,   68.26025, -84.71220,  99.31223,
     VERTEX,   67.90767, -83.82033,  99.26910,
     VERTEX,   67.77927, -83.01093,  99.76908,
     VERTEX,   67.92409, -82.59315, 100.62119,
     VERTEX,   68.28681, -82.72658, 101.49995,
     VERTEX,   68.72889, -83.36025, 102.06972,
     VERTEX,   69.08147, -84.25212, 102.11285,
     VERTEX,   69.20987, -85.06152, 101.61287,
     VERTEX,   69.06505, -85.47930, 100.76076,
     VERTEX,   68.70232, -85.34587,  99.88199,
     VERTEX,   68.26025, -84.71220,  99.31223,
                       
     END,              
                       
     CYLINDER,   58.67600, -87.74900, 104.18000,  68.49457, -84.03622, 100.69097,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -29.09928,  38.90023,  95.01006,
                       
     VERTEX,  -30.53755,  32.93029,  94.02086,
     VERTEX,  -31.12540,  33.26220,  93.33832,
     VERTEX,  -31.96876,  33.69336,  93.18197,
     VERTEX,  -32.74549,  34.05910,  93.61154,
     VERTEX,  -33.15891,  34.21970,  94.46295,
     VERTEX,  -33.05110,  34.11382,  95.41099,
     VERTEX,  -32.46325,  33.78192,  96.09353,
     VERTEX,  -31.61989,  33.35075,  96.24987,
     VERTEX,  -30.84316,  32.98502,  95.82030,
     VERTEX,  -30.42974,  32.82442,  94.96889,
     VERTEX,  -30.53755,  32.93029,  94.02086,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.79432,  33.52206,  94.71592,
                       
     VERTEX,  -30.53755,  32.93029,  94.02086,
     VERTEX,  -31.12540,  33.26220,  93.33832,
     VERTEX,  -31.96876,  33.69336,  93.18197,
     VERTEX,  -32.74549,  34.05910,  93.61154,
     VERTEX,  -33.15891,  34.21970,  94.46295,
     VERTEX,  -33.05110,  34.11382,  95.41099,
     VERTEX,  -32.46325,  33.78192,  96.09353,
     VERTEX,  -31.61989,  33.35075,  96.24987,
     VERTEX,  -30.84316,  32.98502,  95.82030,
     VERTEX,  -30.42974,  32.82442,  94.96889,
     VERTEX,  -30.53755,  32.93029,  94.02086,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.79432,  33.52206,  94.71592,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.76345,  33.94002,  87.66311,
                       
     VERTEX,  -27.61041,  28.64219,  86.71301,
     VERTEX,  -28.18237,  28.94757,  86.00505,
     VERTEX,  -29.03412,  29.34609,  85.81193,
     VERTEX,  -29.84034,  29.68553,  86.20741,
     VERTEX,  -30.29306,  29.83623,  87.04043,
     VERTEX,  -30.21937,  29.74063,  87.99281,
     VERTEX,  -29.64742,  29.43525,  88.70078,
     VERTEX,  -28.79566,  29.03673,  88.89390,
     VERTEX,  -27.98945,  28.69729,  88.49841,
     VERTEX,  -27.53672,  28.54659,  87.66539,
     VERTEX,  -27.61041,  28.64219,  86.71301,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.91489,  29.19141,  87.35291,
                       
     VERTEX,  -27.61041,  28.64219,  86.71301,
     VERTEX,  -28.18237,  28.94757,  86.00505,
     VERTEX,  -29.03412,  29.34609,  85.81193,
     VERTEX,  -29.84034,  29.68553,  86.20741,
     VERTEX,  -30.29306,  29.83623,  87.04043,
     VERTEX,  -30.21937,  29.74063,  87.99281,
     VERTEX,  -29.64742,  29.43525,  88.70078,
     VERTEX,  -28.79566,  29.03673,  88.89390,
     VERTEX,  -27.98945,  28.69729,  88.49841,
     VERTEX,  -27.53672,  28.54659,  87.66539,
     VERTEX,  -27.61041,  28.64219,  86.71301,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.91489,  29.19141,  87.35291,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.61025,  35.32935,  86.37102,
                       
     VERTEX,  -22.11275,  30.63577,  85.28999,
     VERTEX,  -22.72248,  31.06792,  84.68743,
     VERTEX,  -23.52463,  31.59303,  84.63836,
     VERTEX,  -24.21281,  32.01054,  85.16152,
     VERTEX,  -24.52415,  32.16097,  86.05709,
     VERTEX,  -24.33973,  31.98686,  86.98298,
     VERTEX,  -23.73000,  31.55471,  87.58554,
     VERTEX,  -22.92785,  31.02960,  87.63461,
     VERTEX,  -22.23967,  30.61209,  87.11144,
     VERTEX,  -21.92833,  30.46166,  86.21588,
     VERTEX,  -22.11275,  30.63577,  85.28999,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -23.22624,  31.31132,  86.13648,
                       
     VERTEX,  -22.11275,  30.63577,  85.28999,
     VERTEX,  -22.72248,  31.06792,  84.68743,
     VERTEX,  -23.52463,  31.59303,  84.63836,
     VERTEX,  -24.21281,  32.01054,  85.16152,
     VERTEX,  -24.52415,  32.16097,  86.05709,
     VERTEX,  -24.33973,  31.98686,  86.98298,
     VERTEX,  -23.73000,  31.55471,  87.58554,
     VERTEX,  -22.92785,  31.02960,  87.63461,
     VERTEX,  -22.23967,  30.61209,  87.11144,
     VERTEX,  -21.92833,  30.46166,  86.21588,
     VERTEX,  -22.11275,  30.63577,  85.28999,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -23.22624,  31.31132,  86.13648,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -14.06833,  42.96599,  95.97582,
                       
     VERTEX,  -17.23670,  38.52709,  94.73515,
     VERTEX,  -17.82546,  39.16550,  94.32601,
     VERTEX,  -18.47409,  39.85013,  94.50533,
     VERTEX,  -18.93484,  40.31948,  95.20464,
     VERTEX,  -19.03171,  40.39427,  96.15680,
     VERTEX,  -18.72771,  40.04594,  96.99814,
     VERTEX,  -18.13895,  39.40754,  97.40729,
     VERTEX,  -17.49032,  38.72290,  97.22796,
     VERTEX,  -17.02958,  38.25356,  96.52866,
     VERTEX,  -16.93270,  38.17876,  95.57649,
     VERTEX,  -17.23670,  38.52709,  94.73515,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.98221,  39.28651,  95.86665,
                       
     VERTEX,  -17.23670,  38.52709,  94.73515,
     VERTEX,  -17.82546,  39.16550,  94.32601,
     VERTEX,  -18.47409,  39.85013,  94.50533,
     VERTEX,  -18.93484,  40.31948,  95.20464,
     VERTEX,  -19.03171,  40.39427,  96.15680,
     VERTEX,  -18.72771,  40.04594,  96.99814,
     VERTEX,  -18.13895,  39.40754,  97.40729,
     VERTEX,  -17.49032,  38.72290,  97.22796,
     VERTEX,  -17.02958,  38.25356,  96.52866,
     VERTEX,  -16.93270,  38.17876,  95.57649,
     VERTEX,  -17.23670,  38.52709,  94.73515,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -17.98221,  39.28651,  95.86665,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -15.94669,  41.13187, 101.50009,
                       
     VERTEX,  -18.69374,  36.49604, 100.29855,
     VERTEX,  -19.29968,  37.07566,  99.83111,
     VERTEX,  -20.00060,  37.72157,  99.94557,
     VERTEX,  -20.52879,  38.18707, 100.59821,
     VERTEX,  -20.68249,  38.29435, 101.53973,
     VERTEX,  -20.40299,  38.00243, 102.41051,
     VERTEX,  -19.79706,  37.42282, 102.87794,
     VERTEX,  -19.09613,  36.77691, 102.76349,
     VERTEX,  -18.56795,  36.31141, 102.11086,
     VERTEX,  -18.41425,  36.20413, 101.16933,
     VERTEX,  -18.69374,  36.49604, 100.29855,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.54837,  37.24924, 101.35453,
                       
     VERTEX,  -18.69374,  36.49604, 100.29855,
     VERTEX,  -19.29968,  37.07566,  99.83111,
     VERTEX,  -20.00060,  37.72157,  99.94557,
     VERTEX,  -20.52879,  38.18707, 100.59821,
     VERTEX,  -20.68249,  38.29435, 101.53973,
     VERTEX,  -20.40299,  38.00243, 102.41051,
     VERTEX,  -19.79706,  37.42282, 102.87794,
     VERTEX,  -19.09613,  36.77691, 102.76349,
     VERTEX,  -18.56795,  36.31141, 102.11086,
     VERTEX,  -18.41425,  36.20413, 101.16933,
     VERTEX,  -18.69374,  36.49604, 100.29855,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.54837,  37.24924, 101.35453,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   44.72703,  29.94070,  47.49664,
                       
     VERTEX,   41.47031,  35.01344,  46.95325,
     VERTEX,   41.82308,  35.24155,  47.81644,
     VERTEX,   41.75372,  35.05991,  48.75655,
     VERTEX,   41.28870,  34.53788,  49.41447,
     VERTEX,   40.60566,  33.87488,  49.53889,
     VERTEX,   39.96549,  33.32414,  49.08231,
     VERTEX,   39.61272,  33.09603,  48.21911,
     VERTEX,   39.68208,  33.27768,  47.27901,
     VERTEX,   40.14709,  33.79970,  46.62109,
     VERTEX,   40.83014,  34.46270,  46.49666,
     VERTEX,   41.47031,  35.01344,  46.95325,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.71790,  34.16879,  48.01778,
                       
     VERTEX,   41.47031,  35.01344,  46.95325,
     VERTEX,   41.82308,  35.24155,  47.81644,
     VERTEX,   41.75372,  35.05991,  48.75655,
     VERTEX,   41.28870,  34.53788,  49.41447,
     VERTEX,   40.60566,  33.87488,  49.53889,
     VERTEX,   39.96549,  33.32414,  49.08231,
     VERTEX,   39.61272,  33.09603,  48.21911,
     VERTEX,   39.68208,  33.27768,  47.27901,
     VERTEX,   40.14709,  33.79970,  46.62109,
     VERTEX,   40.83014,  34.46270,  46.49666,
     VERTEX,   41.47031,  35.01344,  46.95325,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  40.71790,  34.16879,  48.01778,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.35623,  24.99714,  53.89653,
                       
     VERTEX,   37.88404,  29.65881,  53.29855,
     VERTEX,   38.21288,  29.84749,  54.18052,
     VERTEX,   38.09689,  29.64668,  55.11209,
     VERTEX,   37.58038,  29.13310,  55.73743,
     VERTEX,   36.86064,  28.50292,  55.81769,
     VERTEX,   36.21259,  27.99683,  55.32220,
     VERTEX,   35.88375,  27.80816,  54.44024,
     VERTEX,   35.99974,  28.00896,  53.50866,
     VERTEX,   36.51625,  28.52254,  52.88332,
     VERTEX,   37.23599,  29.15273,  52.80306,
     VERTEX,   37.88404,  29.65881,  53.29855,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.04832,  28.82782,  54.31038,
                       
     VERTEX,   37.88404,  29.65881,  53.29855,
     VERTEX,   38.21288,  29.84749,  54.18052,
     VERTEX,   38.09689,  29.64668,  55.11209,
     VERTEX,   37.58038,  29.13310,  55.73743,
     VERTEX,   36.86064,  28.50292,  55.81769,
     VERTEX,   36.21259,  27.99683,  55.32220,
     VERTEX,   35.88375,  27.80816,  54.44024,
     VERTEX,   35.99974,  28.00896,  53.50866,
     VERTEX,   36.51625,  28.52254,  52.88332,
     VERTEX,   37.23599,  29.15273,  52.80306,
     VERTEX,   37.88404,  29.65881,  53.29855,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  37.04832,  28.82782,  54.31038,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.28308,  28.40991,  55.67225,
                       
     VERTEX,   32.37928,  32.31486,  54.86163,
     VERTEX,   32.74995,  32.64322,  55.68405,
     VERTEX,   32.74679,  32.52982,  56.63733,
     VERTEX,   32.37101,  32.01798,  57.35733,
     VERTEX,   31.76614,  31.30320,  57.56905,
     VERTEX,   31.16323,  30.65850,  57.19160,
     VERTEX,   30.79256,  30.33014,  56.36918,
     VERTEX,   30.79572,  30.44354,  55.41590,
     VERTEX,   31.17150,  30.95539,  54.69590,
     VERTEX,   31.77637,  31.67017,  54.48418,
     VERTEX,   32.37928,  32.31486,  54.86163,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.77126,  31.48668,  56.02662,
                       
     VERTEX,   32.37928,  32.31486,  54.86163,
     VERTEX,   32.74995,  32.64322,  55.68405,
     VERTEX,   32.74679,  32.52982,  56.63733,
     VERTEX,   32.37101,  32.01798,  57.35733,
     VERTEX,   31.76614,  31.30320,  57.56905,
     VERTEX,   31.16323,  30.65850,  57.19160,
     VERTEX,   30.79256,  30.33014,  56.36918,
     VERTEX,   30.79572,  30.44354,  55.41590,
     VERTEX,   31.17150,  30.95539,  54.69590,
     VERTEX,   31.77637,  31.67017,  54.48418,
     VERTEX,   32.37928,  32.31486,  54.86163,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  31.77126,  31.48668,  56.02662,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.67136,  39.65636,  47.99659,
                       
     VERTEX,   28.27436,  42.78884,  47.01525,
     VERTEX,   28.63136,  43.35774,  47.70118,
     VERTEX,   28.75763,  43.44668,  48.64867,
     VERTEX,   28.60492,  43.02169,  49.49583,
     VERTEX,   28.23158,  42.24509,  49.91905,
     VERTEX,   27.78020,  41.41353,  49.75668,
     VERTEX,   27.42319,  40.84463,  49.07076,
     VERTEX,   27.29693,  40.75569,  48.12326,
     VERTEX,   27.44963,  41.18068,  47.27611,
     VERTEX,   27.82298,  41.95728,  46.85289,
     VERTEX,   28.27436,  42.78884,  47.01525,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.02728,  42.10118,  48.38597,
                       
     VERTEX,   28.27436,  42.78884,  47.01525,
     VERTEX,   28.63136,  43.35774,  47.70118,
     VERTEX,   28.75763,  43.44668,  48.64867,
     VERTEX,   28.60492,  43.02169,  49.49583,
     VERTEX,   28.23158,  42.24509,  49.91905,
     VERTEX,   27.78020,  41.41353,  49.75668,
     VERTEX,   27.42319,  40.84463,  49.07076,
     VERTEX,   27.29693,  40.75569,  48.12326,
     VERTEX,   27.44963,  41.18068,  47.27611,
     VERTEX,   27.82298,  41.95728,  46.85289,
     VERTEX,   28.27436,  42.78884,  47.01525,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  28.02728,  42.10118,  48.38597,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.81569,  38.47670,  42.18068,
                       
     VERTEX,   29.65548,  41.92188,  41.25477,
     VERTEX,   30.02745,  42.43172,  41.97816,
     VERTEX,   30.13229,  42.46446,  42.93186,
     VERTEX,   29.92995,  42.00760,  43.75158,
     VERTEX,   29.49772,  41.23564,  44.12421,
     VERTEX,   29.00070,  40.44345,  43.90743,
     VERTEX,   28.62873,  39.93361,  43.18404,
     VERTEX,   28.52388,  39.90087,  42.23034,
     VERTEX,   28.72622,  40.35773,  41.41063,
     VERTEX,   29.15845,  41.12968,  41.03799,
     VERTEX,   29.65548,  41.92188,  41.25477,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.32809,  41.18266,  42.58110,
                       
     VERTEX,   29.65548,  41.92188,  41.25477,
     VERTEX,   30.02745,  42.43172,  41.97816,
     VERTEX,   30.13229,  42.46446,  42.93186,
     VERTEX,   29.92995,  42.00760,  43.75158,
     VERTEX,   29.49772,  41.23564,  44.12421,
     VERTEX,   29.00070,  40.44345,  43.90743,
     VERTEX,   28.62873,  39.93361,  43.18404,
     VERTEX,   28.52388,  39.90087,  42.23034,
     VERTEX,   28.72622,  40.35773,  41.41063,
     VERTEX,   29.15845,  41.12968,  41.03799,
     VERTEX,   29.65548,  41.92188,  41.25477,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  29.32809,  41.18266,  42.58110,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00002_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    4.82800, -71.01700,  51.16800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   19.12200, -75.65200,  45.45200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   21.31000, -73.61600,  40.67200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   42.92000, -20.16600,  87.79600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   38.12100, -18.38800,  80.91800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   75.51300, -76.21300,  95.22200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   71.70600, -70.00300,  90.04600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   63.70900, -84.54600,  92.78700,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   61.44400, -86.36300,  97.64500,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   58.67600, -87.74900, 104.18000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -36.15500,  24.82000,  94.24000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -32.39600,  21.50800,  86.85100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -27.45900,  24.81000,  85.75700,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -24.31500,  33.33300,  95.69000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -25.37600,  30.96700, 101.11900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   34.23100,  41.01000,  48.86100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   31.69600,  35.02600,  54.98000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   26.08900,  36.46500,  56.60000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   20.51300,  46.05700,  49.01600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   22.06700,  45.56100,  43.22900,   0.80000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00002_arror_pos') 
