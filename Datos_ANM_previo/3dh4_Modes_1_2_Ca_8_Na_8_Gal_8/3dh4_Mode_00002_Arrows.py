from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.21056, -76.83457,  45.43423,
                       
     VERTEX,   10.00007, -73.52845,  46.51185,
     VERTEX,   10.63888, -73.26466,  47.17813,
     VERTEX,   11.03699, -73.51569,  48.01485,
     VERTEX,   11.04233, -74.18564,  48.70240,
     VERTEX,   10.65286, -75.01862,  48.97817,
     VERTEX,   10.01735, -75.69647,  48.73682,
     VERTEX,    9.37853, -75.96026,  48.07054,
     VERTEX,    8.98042, -75.70923,  47.23382,
     VERTEX,    8.97508, -75.03928,  46.54627,
     VERTEX,    9.36455, -74.20629,  46.27050,
     VERTEX,   10.00007, -73.52845,  46.51185,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.00871, -74.61246,  47.62434,
                       
     VERTEX,   10.00007, -73.52845,  46.51185,
     VERTEX,   10.63888, -73.26466,  47.17813,
     VERTEX,   11.03699, -73.51569,  48.01485,
     VERTEX,   11.04233, -74.18564,  48.70240,
     VERTEX,   10.65286, -75.01862,  48.97817,
     VERTEX,   10.01735, -75.69647,  48.73682,
     VERTEX,    9.37853, -75.96026,  48.07054,
     VERTEX,    8.98042, -75.70923,  47.23382,
     VERTEX,    8.97508, -75.03928,  46.54627,
     VERTEX,    9.36455, -74.20629,  46.27050,
     VERTEX,   10.00007, -73.52845,  46.51185,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,  10.00871, -74.61246,  47.62434,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.35299, -76.14339,  40.32775,
                       
     VERTEX,   24.75530, -75.84796,  40.89747,
     VERTEX,   24.95037, -74.95856,  41.20164,
     VERTEX,   25.33440, -74.45004,  41.91964,
     VERTEX,   25.76072, -74.51662,  42.77721,
     VERTEX,   26.06648, -75.13288,  43.44678,
     VERTEX,   26.13490, -76.06343,  43.67261,
     VERTEX,   25.93983, -76.95283,  43.36844,
     VERTEX,   25.55580, -77.46136,  42.65044,
     VERTEX,   25.12948, -77.39477,  41.79288,
     VERTEX,   24.82372, -76.77851,  41.12330,
     VERTEX,   24.75530, -75.84796,  40.89747,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.44510, -75.95570,  42.28504,
                       
     VERTEX,   24.75530, -75.84796,  40.89747,
     VERTEX,   24.95037, -74.95856,  41.20164,
     VERTEX,   25.33440, -74.45004,  41.91964,
     VERTEX,   25.76072, -74.51662,  42.77721,
     VERTEX,   26.06648, -75.13288,  43.44678,
     VERTEX,   26.13490, -76.06343,  43.67261,
     VERTEX,   25.93983, -76.95283,  43.36844,
     VERTEX,   25.55580, -77.46136,  42.65044,
     VERTEX,   25.12948, -77.39477,  41.79288,
     VERTEX,   24.82372, -76.77851,  41.12330,
     VERTEX,   24.75530, -75.84796,  40.89747,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.44510, -75.95570,  42.28504,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.26702, -72.81093,  35.98630,
                       
     VERTEX,   26.81852, -73.29620,  36.37436,
     VERTEX,   26.83726, -72.35768,  36.57545,
     VERTEX,   27.09532, -71.70975,  37.23514,
     VERTEX,   27.49411, -71.59988,  38.10145,
     VERTEX,   27.88132, -72.07005,  38.84348,
     VERTEX,   28.10905, -72.94067,  39.17780,
     VERTEX,   28.09030, -73.87919,  38.97671,
     VERTEX,   27.83224, -74.52712,  38.31702,
     VERTEX,   27.43345, -74.63699,  37.45071,
     VERTEX,   27.04624, -74.16682,  36.70868,
     VERTEX,   26.81852, -73.29620,  36.37436,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.46378, -73.11844,  37.77608,
                       
     VERTEX,   26.81852, -73.29620,  36.37436,
     VERTEX,   26.83726, -72.35768,  36.57545,
     VERTEX,   27.09532, -71.70975,  37.23514,
     VERTEX,   27.49411, -71.59988,  38.10145,
     VERTEX,   27.88132, -72.07005,  38.84348,
     VERTEX,   28.10905, -72.94067,  39.17780,
     VERTEX,   28.09030, -73.87919,  38.97671,
     VERTEX,   27.83224, -74.52712,  38.31702,
     VERTEX,   27.43345, -74.63699,  37.45071,
     VERTEX,   27.04624, -74.16682,  36.70868,
     VERTEX,   26.81852, -73.29620,  36.37436,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  27.46378, -73.11844,  37.77608,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.33264, -18.97960,  92.60084,
                       
     VERTEX,   36.36092, -19.33539,  92.19402,
     VERTEX,   36.30312, -18.44683,  91.83524,
     VERTEX,   36.03735, -17.93487,  91.06788,
     VERTEX,   35.66510, -17.99505,  90.18504,
     VERTEX,   35.32858, -18.60439,  89.52393,
     VERTEX,   35.15631, -19.53014,  89.33708,
     VERTEX,   35.21411, -20.41869,  89.69586,
     VERTEX,   35.47989, -20.93066,  90.46323,
     VERTEX,   35.85213, -20.87048,  91.34608,
     VERTEX,   36.18866, -20.26114,  92.00718,
     VERTEX,   36.36092, -19.33539,  92.19402,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.75862, -19.43276,  90.76556,
                       
     VERTEX,   36.36092, -19.33539,  92.19402,
     VERTEX,   36.30312, -18.44683,  91.83524,
     VERTEX,   36.03735, -17.93487,  91.06788,
     VERTEX,   35.66510, -17.99505,  90.18504,
     VERTEX,   35.32858, -18.60439,  89.52393,
     VERTEX,   35.15631, -19.53014,  89.33708,
     VERTEX,   35.21411, -20.41869,  89.69586,
     VERTEX,   35.47989, -20.93066,  90.46323,
     VERTEX,   35.85213, -20.87048,  91.34608,
     VERTEX,   36.18866, -20.26114,  92.00718,
     VERTEX,   36.36092, -19.33539,  92.19402,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  35.75862, -19.43276,  90.76556,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.05330, -17.95652,  85.26276,
                       
     VERTEX,   31.84951, -18.08295,  85.04815,
     VERTEX,   31.76345, -17.17814,  84.73907,
     VERTEX,   31.49304, -16.63360,  83.99614,
     VERTEX,   31.14154, -16.65733,  83.10312,
     VERTEX,   30.84324, -17.24025,  82.40111,
     VERTEX,   30.71206, -18.15972,  82.15826,
     VERTEX,   30.79811, -19.06452,  82.46733,
     VERTEX,   31.06853, -19.60906,  83.21027,
     VERTEX,   31.42002, -19.58533,  84.10329,
     VERTEX,   31.71833, -19.00241,  84.80530,
     VERTEX,   31.84951, -18.08295,  85.04815,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.28078, -18.12133,  83.60320,
                       
     VERTEX,   31.84951, -18.08295,  85.04815,
     VERTEX,   31.76345, -17.17814,  84.73907,
     VERTEX,   31.49304, -16.63360,  83.99614,
     VERTEX,   31.14154, -16.65733,  83.10312,
     VERTEX,   30.84324, -17.24025,  82.40111,
     VERTEX,   30.71206, -18.15972,  82.15826,
     VERTEX,   30.79811, -19.06452,  82.46733,
     VERTEX,   31.06853, -19.60906,  83.21027,
     VERTEX,   31.42002, -19.58533,  84.10329,
     VERTEX,   31.71833, -19.00241,  84.80530,
     VERTEX,   31.84951, -18.08295,  85.04815,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  31.28078, -18.12133,  83.60320,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   85.82083, -57.42597,  89.79052,
                       
     VERTEX,   83.01408, -64.46325,  89.91226,
     VERTEX,   82.34985, -64.14349,  89.29730,
     VERTEX,   81.53133, -63.64680,  89.22724,
     VERTEX,   80.87112, -63.16292,  89.72883,
     VERTEX,   80.62144, -62.87665,  90.61048,
     VERTEX,   80.87763, -62.89735,  91.53543,
     VERTEX,   81.54185, -63.21711,  92.15038,
     VERTEX,   82.36038, -63.71379,  92.22045,
     VERTEX,   83.02058, -64.19768,  91.71886,
     VERTEX,   83.27027, -64.48395,  90.83721,
     VERTEX,   83.01408, -64.46325,  89.91226,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   81.94585, -63.68030,  90.72385,
                       
     VERTEX,   83.01408, -64.46325,  89.91226,
     VERTEX,   82.34985, -64.14349,  89.29730,
     VERTEX,   81.53133, -63.64680,  89.22724,
     VERTEX,   80.87112, -63.16292,  89.72883,
     VERTEX,   80.62144, -62.87665,  90.61048,
     VERTEX,   80.87763, -62.89735,  91.53543,
     VERTEX,   81.54185, -63.21711,  92.15038,
     VERTEX,   82.36038, -63.71379,  92.22045,
     VERTEX,   83.02058, -64.19768,  91.71886,
     VERTEX,   83.27027, -64.48395,  90.83721,
     VERTEX,   83.01408, -64.46325,  89.91226,
                       
     END,              
                       
     CYLINDER,   75.67600, -73.80000,  92.23400,  81.94585, -63.68030,  90.72385,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   80.05659, -55.26133,  88.05654,
                       
     VERTEX,   77.99891, -61.63597,  88.05608,
     VERTEX,   77.34551, -61.35273,  87.41231,
     VERTEX,   76.50932, -60.89355,  87.30486,
     VERTEX,   75.80973, -60.43385,  87.77480,
     VERTEX,   75.51396, -60.14919,  88.64261,
     VERTEX,   75.73499, -60.14832,  89.57682,
     VERTEX,   76.38838, -60.43156,  90.22059,
     VERTEX,   77.22457, -60.89073,  90.32803,
     VERTEX,   77.92416, -61.35044,  89.85810,
     VERTEX,   78.21993, -61.63510,  88.99029,
     VERTEX,   77.99891, -61.63597,  88.05608,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.86694, -60.89214,  88.81645,
                       
     VERTEX,   77.99891, -61.63597,  88.05608,
     VERTEX,   77.34551, -61.35273,  87.41231,
     VERTEX,   76.50932, -60.89355,  87.30486,
     VERTEX,   75.80973, -60.43385,  87.77480,
     VERTEX,   75.51396, -60.14919,  88.64261,
     VERTEX,   75.73499, -60.14832,  89.57682,
     VERTEX,   76.38838, -60.43156,  90.22059,
     VERTEX,   77.22457, -60.89073,  90.32803,
     VERTEX,   77.92416, -61.35044,  89.85810,
     VERTEX,   78.21993, -61.63510,  88.99029,
     VERTEX,   77.99891, -61.63597,  88.05608,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.86694, -60.89214,  88.81645,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.99860, -74.29684,  87.50423,
                       
     VERTEX,   73.34443, -79.12827,  88.28189,
     VERTEX,   72.77015, -78.40135,  88.03010,
     VERTEX,   72.34421, -77.60198,  88.34818,
     VERTEX,   72.22929, -77.03549,  89.11466,
     VERTEX,   72.46931, -76.91826,  90.03675,
     VERTEX,   72.97256, -77.29506,  90.76225,
     VERTEX,   73.54684, -78.02198,  91.01405,
     VERTEX,   73.97278, -78.82135,  90.69595,
     VERTEX,   74.08769, -79.38784,  89.92948,
     VERTEX,   73.84769, -79.50507,  89.00739,
     VERTEX,   73.34443, -79.12827,  88.28189,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   73.15849, -78.21167,  89.52207,
                       
     VERTEX,   73.34443, -79.12827,  88.28189,
     VERTEX,   72.77015, -78.40135,  88.03010,
     VERTEX,   72.34421, -77.60198,  88.34818,
     VERTEX,   72.22929, -77.03549,  89.11466,
     VERTEX,   72.46931, -76.91826,  90.03675,
     VERTEX,   72.97256, -77.29506,  90.76225,
     VERTEX,   73.54684, -78.02198,  91.01405,
     VERTEX,   73.97278, -78.82135,  90.69595,
     VERTEX,   74.08769, -79.38784,  89.92948,
     VERTEX,   73.84769, -79.50507,  89.00739,
     VERTEX,   73.34443, -79.12827,  88.28189,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  73.15849, -78.21167,  89.52207,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   77.19605, -78.10463,  91.86343,
                       
     VERTEX,   71.13753, -82.09531,  92.76347,
     VERTEX,   70.65397, -81.28028,  92.61017,
     VERTEX,   70.37106, -80.45715,  93.01515,
     VERTEX,   70.39688, -79.94031,  93.82375,
     VERTEX,   70.72156, -79.92719,  94.72707,
     VERTEX,   71.22108, -80.42279,  95.38012,
     VERTEX,   71.70464, -81.23782,  95.53342,
     VERTEX,   71.98754, -82.06095,  95.12843,
     VERTEX,   71.96172, -82.57778,  94.31985,
     VERTEX,   71.63705, -82.59091,  93.41651,
     VERTEX,   71.13753, -82.09531,  92.76347,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   71.17931, -81.25905,  94.07179,
                       
     VERTEX,   71.13753, -82.09531,  92.76347,
     VERTEX,   70.65397, -81.28028,  92.61017,
     VERTEX,   70.37106, -80.45715,  93.01515,
     VERTEX,   70.39688, -79.94031,  93.82375,
     VERTEX,   70.72156, -79.92719,  94.72707,
     VERTEX,   71.22108, -80.42279,  95.38012,
     VERTEX,   71.70464, -81.23782,  95.53342,
     VERTEX,   71.98754, -82.06095,  95.12843,
     VERTEX,   71.96172, -82.57778,  94.31985,
     VERTEX,   71.63705, -82.59091,  93.41651,
     VERTEX,   71.13753, -82.09531,  92.76347,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  71.17931, -81.25905,  94.07179,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   74.59297, -82.05326,  97.91849,
                       
     VERTEX,   68.21129, -84.89273,  98.93873,
     VERTEX,   67.87873, -83.99256,  98.91219,
     VERTEX,   67.78853, -83.18264,  99.41963,
     VERTEX,   67.97514, -82.77234, 100.26723,
     VERTEX,   68.36728, -82.91837, 101.13124,
     VERTEX,   68.81517, -83.56496, 101.68163,
     VERTEX,   69.14773, -84.46513, 101.70816,
     VERTEX,   69.23792, -85.27504, 101.20071,
     VERTEX,   69.05132, -85.68534, 100.35311,
     VERTEX,   68.65917, -85.53931,  99.48911,
     VERTEX,   68.21129, -84.89273,  98.93873,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   68.51323, -84.22884, 100.31017,
                       
     VERTEX,   68.21129, -84.89273,  98.93873,
     VERTEX,   67.87873, -83.99256,  98.91219,
     VERTEX,   67.78853, -83.18264,  99.41963,
     VERTEX,   67.97514, -82.77234, 100.26723,
     VERTEX,   68.36728, -82.91837, 101.13124,
     VERTEX,   68.81517, -83.56496, 101.68163,
     VERTEX,   69.14773, -84.46513, 101.70816,
     VERTEX,   69.23792, -85.27504, 101.20071,
     VERTEX,   69.05132, -85.68534, 100.35311,
     VERTEX,   68.65917, -85.53931,  99.48911,
     VERTEX,   68.21129, -84.89273,  98.93873,
                       
     END,              
                       
     CYLINDER,   58.67600, -87.74900, 104.18000,  68.51323, -84.22884, 100.31017,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -29.17222,  39.01206,  94.80745,
                       
     VERTEX,  -30.57798,  32.99793,  93.90540,
     VERTEX,  -31.16759,  33.31553,  93.21758,
     VERTEX,  -32.01381,  33.73842,  93.05425,
     VERTEX,  -32.79342,  34.10506,  93.47780,
     VERTEX,  -33.20862,  34.27542,  94.32643,
     VERTEX,  -33.10083,  34.18442,  95.27602,
     VERTEX,  -32.51122,  33.86682,  95.96383,
     VERTEX,  -31.66500,  33.44393,  96.12715,
     VERTEX,  -30.88540,  33.07729,  95.70361,
     VERTEX,  -30.47019,  32.90693,  94.85497,
     VERTEX,  -30.57798,  32.99793,  93.90540,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.83941,  33.59118,  94.59071,
                       
     VERTEX,  -30.57798,  32.99793,  93.90540,
     VERTEX,  -31.16759,  33.31553,  93.21758,
     VERTEX,  -32.01381,  33.73842,  93.05425,
     VERTEX,  -32.79342,  34.10506,  93.47780,
     VERTEX,  -33.20862,  34.27542,  94.32643,
     VERTEX,  -33.10083,  34.18442,  95.27602,
     VERTEX,  -32.51122,  33.86682,  95.96383,
     VERTEX,  -31.66500,  33.44393,  96.12715,
     VERTEX,  -30.88540,  33.07729,  95.70361,
     VERTEX,  -30.47019,  32.90693,  94.85497,
     VERTEX,  -30.57798,  32.99793,  93.90540,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.83941,  33.59118,  94.59071,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.84465,  34.01823,  87.47634,
                       
     VERTEX,  -27.65564,  28.69015,  86.60811,
     VERTEX,  -28.22877,  28.98014,  85.89464,
     VERTEX,  -29.08313,  29.36928,  85.69409,
     VERTEX,  -29.89241,  29.70895,  86.08306,
     VERTEX,  -30.34747,  29.86940,  86.91299,
     VERTEX,  -30.27451,  29.78934,  87.86686,
     VERTEX,  -29.70139,  29.49936,  88.58032,
     VERTEX,  -28.84702,  29.11021,  88.78088,
     VERTEX,  -28.03774,  28.77054,  88.39190,
     VERTEX,  -27.58268,  28.61009,  87.56197,
     VERTEX,  -27.65564,  28.69015,  86.60811,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.96508,  29.23975,  87.23748,
                       
     VERTEX,  -27.65564,  28.69015,  86.60811,
     VERTEX,  -28.22877,  28.98014,  85.89464,
     VERTEX,  -29.08313,  29.36928,  85.69409,
     VERTEX,  -29.89241,  29.70895,  86.08306,
     VERTEX,  -30.34747,  29.86940,  86.91299,
     VERTEX,  -30.27451,  29.78934,  87.86686,
     VERTEX,  -29.70139,  29.49936,  88.58032,
     VERTEX,  -28.84702,  29.11021,  88.78088,
     VERTEX,  -28.03774,  28.77054,  88.39190,
     VERTEX,  -27.58268,  28.61009,  87.56197,
     VERTEX,  -27.65564,  28.69015,  86.60811,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.96508,  29.23975,  87.23748,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.70711,  35.40448,  86.14170,
                       
     VERTEX,  -22.16772,  30.67530,  85.16034,
     VERTEX,  -22.78244,  31.08923,  84.55011,
     VERTEX,  -23.58955,  31.60572,  84.49169,
     VERTEX,  -24.28075,  32.02750,  85.00739,
     VERTEX,  -24.59203,  32.19345,  85.90023,
     VERTEX,  -24.40449,  32.04020,  86.82918,
     VERTEX,  -23.78976,  31.62628,  87.43941,
     VERTEX,  -22.98265,  31.10978,  87.49783,
     VERTEX,  -22.29145,  30.68801,  86.98212,
     VERTEX,  -21.98018,  30.52205,  86.08929,
     VERTEX,  -22.16772,  30.67530,  85.16034,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -23.28610,  31.35775,  85.99476,
                       
     VERTEX,  -22.16772,  30.67530,  85.16034,
     VERTEX,  -22.78244,  31.08923,  84.55011,
     VERTEX,  -23.58955,  31.60572,  84.49169,
     VERTEX,  -24.28075,  32.02750,  85.00739,
     VERTEX,  -24.59203,  32.19345,  85.90023,
     VERTEX,  -24.40449,  32.04020,  86.82918,
     VERTEX,  -23.78976,  31.62628,  87.43941,
     VERTEX,  -22.98265,  31.10978,  87.49783,
     VERTEX,  -22.29145,  30.68801,  86.98212,
     VERTEX,  -21.98018,  30.52205,  86.08929,
     VERTEX,  -22.16772,  30.67530,  85.16034,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -23.28610,  31.35775,  85.99476,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -14.18633,  43.15742,  95.64625,
                       
     VERTEX,  -17.30464,  38.62612,  94.54799,
     VERTEX,  -17.90568,  39.24389,  94.12525,
     VERTEX,  -18.56381,  39.92314,  94.28987,
     VERTEX,  -19.02764,  40.40440,  94.97896,
     VERTEX,  -19.12001,  40.50386,  95.92931,
     VERTEX,  -18.80563,  40.18353,  96.77793,
     VERTEX,  -18.20459,  39.56575,  97.20067,
     VERTEX,  -17.54646,  38.88651,  97.03606,
     VERTEX,  -17.08263,  38.40525,  96.34696,
     VERTEX,  -16.99026,  38.30579,  95.39661,
     VERTEX,  -17.30464,  38.62612,  94.54799,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -18.05514,  39.40482,  95.66296,
                       
     VERTEX,  -17.30464,  38.62612,  94.54799,
     VERTEX,  -17.90568,  39.24389,  94.12525,
     VERTEX,  -18.56381,  39.92314,  94.28987,
     VERTEX,  -19.02764,  40.40440,  94.97896,
     VERTEX,  -19.12001,  40.50386,  95.92931,
     VERTEX,  -18.80563,  40.18353,  96.77793,
     VERTEX,  -18.20459,  39.56575,  97.20067,
     VERTEX,  -17.54646,  38.88651,  97.03606,
     VERTEX,  -17.08263,  38.40525,  96.34696,
     VERTEX,  -16.99026,  38.30579,  95.39661,
     VERTEX,  -17.30464,  38.62612,  94.54799,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -18.05514,  39.40482,  95.66296,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -16.06148,  41.39488, 101.17487,
                       
     VERTEX,  -18.75258,  36.64314, 100.11877,
     VERTEX,  -19.36991,  37.19714,  99.63548,
     VERTEX,  -20.08250,  37.83314,  99.73203,
     VERTEX,  -20.61818,  38.30819, 100.37154,
     VERTEX,  -20.77231,  38.44085, 101.30975,
     VERTEX,  -20.48604,  38.18043, 102.18830,
     VERTEX,  -19.86871,  37.62642, 102.67159,
     VERTEX,  -19.15612,  36.99043, 102.57504,
     VERTEX,  -18.62045,  36.51538, 101.93552,
     VERTEX,  -18.46631,  36.38272, 100.99731,
     VERTEX,  -18.75258,  36.64314, 100.11877,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.61931,  37.41179, 101.15353,
                       
     VERTEX,  -18.75258,  36.64314, 100.11877,
     VERTEX,  -19.36991,  37.19714,  99.63548,
     VERTEX,  -20.08250,  37.83314,  99.73203,
     VERTEX,  -20.61818,  38.30819, 100.37154,
     VERTEX,  -20.77231,  38.44085, 101.30975,
     VERTEX,  -20.48604,  38.18043, 102.18830,
     VERTEX,  -19.86871,  37.62642, 102.67159,
     VERTEX,  -19.15612,  36.99043, 102.57504,
     VERTEX,  -18.62045,  36.51538, 101.93552,
     VERTEX,  -18.46631,  36.38272, 100.99731,
     VERTEX,  -18.75258,  36.64314, 100.11877,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.61931,  37.41179, 101.15353,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   44.60436,  29.85345,  47.16402,
                       
     VERTEX,   41.39544,  34.97523,  46.76101,
     VERTEX,   41.75727,  35.18004,  47.62630,
     VERTEX,   41.69314,  34.97800,  48.56261,
     VERTEX,   41.22754,  34.44627,  49.21228,
     VERTEX,   40.53832,  33.78795,  49.32718,
     VERTEX,   39.88874,  33.25451,  48.86341,
     VERTEX,   39.52691,  33.04970,  47.99812,
     VERTEX,   39.59104,  33.25174,  47.06182,
     VERTEX,   40.05664,  33.78348,  46.41214,
     VERTEX,   40.74585,  34.44179,  46.29724,
     VERTEX,   41.39544,  34.97523,  46.76101,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.64209,  34.11487,  47.81221,
                       
     VERTEX,   41.39544,  34.97523,  46.76101,
     VERTEX,   41.75727,  35.18004,  47.62630,
     VERTEX,   41.69314,  34.97800,  48.56261,
     VERTEX,   41.22754,  34.44627,  49.21228,
     VERTEX,   40.53832,  33.78795,  49.32718,
     VERTEX,   39.88874,  33.25451,  48.86341,
     VERTEX,   39.52691,  33.04970,  47.99812,
     VERTEX,   39.59104,  33.25174,  47.06182,
     VERTEX,   40.05664,  33.78348,  46.41214,
     VERTEX,   40.74585,  34.44179,  46.29724,
     VERTEX,   41.39544,  34.97523,  46.76101,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  40.64209,  34.11487,  47.81221,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.22328,  24.95219,  53.60815,
                       
     VERTEX,   37.80403,  29.64523,  53.13395,
     VERTEX,   38.14080,  29.80994,  54.01773,
     VERTEX,   38.02889,  29.58891,  54.94521,
     VERTEX,   37.51105,  29.06655,  55.56213,
     VERTEX,   36.78508,  28.44240,  55.63284,
     VERTEX,   36.12827,  27.95486,  55.13035,
     VERTEX,   35.79150,  27.79015,  54.24657,
     VERTEX,   35.90341,  28.01118,  53.31909,
     VERTEX,   36.42125,  28.53353,  52.70217,
     VERTEX,   37.14722,  29.15768,  52.63145,
     VERTEX,   37.80403,  29.64523,  53.13395,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.96615,  28.80004,  54.13215,
                       
     VERTEX,   37.80403,  29.64523,  53.13395,
     VERTEX,   38.14080,  29.80994,  54.01773,
     VERTEX,   38.02889,  29.58891,  54.94521,
     VERTEX,   37.51105,  29.06655,  55.56213,
     VERTEX,   36.78508,  28.44240,  55.63284,
     VERTEX,   36.12827,  27.95486,  55.13035,
     VERTEX,   35.79150,  27.79015,  54.24657,
     VERTEX,   35.90341,  28.01118,  53.31909,
     VERTEX,   36.42125,  28.53353,  52.70217,
     VERTEX,   37.14722,  29.15768,  52.63145,
     VERTEX,   37.80403,  29.64523,  53.13395,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  36.96615,  28.80004,  54.13215,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.13157,  28.36920,  55.34325,
                       
     VERTEX,   32.27992,  32.31295,  54.67217,
     VERTEX,   32.66535,  32.61530,  55.49778,
     VERTEX,   32.67350,  32.47693,  56.44772,
     VERTEX,   32.30125,  31.95072,  57.15915,
     VERTEX,   31.69080,  31.23764,  57.36032,
     VERTEX,   31.07531,  30.61008,  56.97440,
     VERTEX,   30.68988,  30.30774,  56.14879,
     VERTEX,   30.68173,  30.44610,  55.19885,
     VERTEX,   31.05398,  30.97232,  54.48742,
     VERTEX,   31.66443,  31.68539,  54.28625,
     VERTEX,   32.27992,  32.31295,  54.67217,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.67762,  31.46152,  55.82329,
                       
     VERTEX,   32.27992,  32.31295,  54.67217,
     VERTEX,   32.66535,  32.61530,  55.49778,
     VERTEX,   32.67350,  32.47693,  56.44772,
     VERTEX,   32.30125,  31.95072,  57.15915,
     VERTEX,   31.69080,  31.23764,  57.36032,
     VERTEX,   31.07531,  30.61008,  56.97440,
     VERTEX,   30.68988,  30.30774,  56.14879,
     VERTEX,   30.68173,  30.44610,  55.19885,
     VERTEX,   31.05398,  30.97232,  54.48742,
     VERTEX,   31.66443,  31.68539,  54.28625,
     VERTEX,   32.27992,  32.31295,  54.67217,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  31.67762,  31.46152,  55.82329,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.51736,  39.50268,  47.52097,
                       
     VERTEX,   28.15880,  42.73053,  46.73675,
     VERTEX,   28.54125,  43.27275,  47.43053,
     VERTEX,   28.69103,  43.33120,  48.37697,
     VERTEX,   28.55093,  42.88354,  49.21457,
     VERTEX,   28.17446,  42.10077,  49.62339,
     VERTEX,   27.70541,  41.28188,  49.44728,
     VERTEX,   27.32296,  40.73965,  48.75351,
     VERTEX,   27.17318,  40.68121,  47.80706,
     VERTEX,   27.31328,  41.12887,  46.96947,
     VERTEX,   27.68976,  41.91164,  46.56064,
     VERTEX,   28.15880,  42.73053,  46.73675,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.93211,  42.00621,  48.09202,
                       
     VERTEX,   28.15880,  42.73053,  46.73675,
     VERTEX,   28.54125,  43.27275,  47.43053,
     VERTEX,   28.69103,  43.33120,  48.37697,
     VERTEX,   28.55093,  42.88354,  49.21457,
     VERTEX,   28.17446,  42.10077,  49.62339,
     VERTEX,   27.70541,  41.28188,  49.44728,
     VERTEX,   27.32296,  40.73965,  48.75351,
     VERTEX,   27.17318,  40.68121,  47.80706,
     VERTEX,   27.31328,  41.12887,  46.96947,
     VERTEX,   27.68976,  41.91164,  46.56064,
     VERTEX,   28.15880,  42.73053,  46.73675,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.93211,  42.00621,  48.09202,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.68431,  38.24738,  41.69492,
                       
     VERTEX,   29.56423,  41.81903,  40.97451,
     VERTEX,   29.96098,  42.29552,  41.70741,
     VERTEX,   30.08497,  42.29280,  42.65937,
     VERTEX,   29.88885,  41.81190,  43.46676,
     VERTEX,   29.44752,  41.03653,  43.82119,
     VERTEX,   28.92955,  40.26284,  43.58727,
     VERTEX,   28.53280,  39.78635,  42.85436,
     VERTEX,   28.40881,  39.78907,  41.90241,
     VERTEX,   28.60494,  40.26997,  41.09502,
     VERTEX,   29.04627,  41.04534,  40.74059,
     VERTEX,   29.56423,  41.81903,  40.97451,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.24689,  41.04094,  42.28089,
                       
     VERTEX,   29.56423,  41.81903,  40.97451,
     VERTEX,   29.96098,  42.29552,  41.70741,
     VERTEX,   30.08497,  42.29280,  42.65937,
     VERTEX,   29.88885,  41.81190,  43.46676,
     VERTEX,   29.44752,  41.03653,  43.82119,
     VERTEX,   28.92955,  40.26284,  43.58727,
     VERTEX,   28.53280,  39.78635,  42.85436,
     VERTEX,   28.40881,  39.78907,  41.90241,
     VERTEX,   28.60494,  40.26997,  41.09502,
     VERTEX,   29.04627,  41.04534,  40.74059,
     VERTEX,   29.56423,  41.81903,  40.97451,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  29.24689,  41.04094,  42.28089,   0.80000,
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
                       
     SPHERE,   75.67600, -73.80000,  92.23400,   0.80000,
                       
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
