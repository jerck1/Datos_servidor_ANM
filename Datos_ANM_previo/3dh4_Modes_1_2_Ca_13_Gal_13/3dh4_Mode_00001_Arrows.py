from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.49643, -62.94771,  35.64816,
                       
     VERTEX,   21.74062, -60.37149,  35.91078,
     VERTEX,   21.25519, -59.59024,  36.18574,
     VERTEX,   20.69068, -58.87789,  35.87674,
     VERTEX,   20.26271, -58.50653,  35.10179,
     VERTEX,   20.13475, -58.61802,  34.15691,
     VERTEX,   20.35568, -59.16976,  33.40301,
     VERTEX,   20.84111, -59.95101,  33.12805,
     VERTEX,   21.40562, -60.66336,  33.43705,
     VERTEX,   21.83359, -61.03472,  34.21200,
     VERTEX,   21.96155, -60.92323,  35.15688,
     VERTEX,   21.74062, -60.37149,  35.91078,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.04815, -59.77063,  34.65689,
                       
     VERTEX,   21.74062, -60.37149,  35.91078,
     VERTEX,   21.25519, -59.59024,  36.18574,
     VERTEX,   20.69068, -58.87789,  35.87674,
     VERTEX,   20.26271, -58.50653,  35.10179,
     VERTEX,   20.13475, -58.61802,  34.15691,
     VERTEX,   20.35568, -59.16976,  33.40301,
     VERTEX,   20.84111, -59.95101,  33.12805,
     VERTEX,   21.40562, -60.66336,  33.43705,
     VERTEX,   21.83359, -61.03472,  34.21200,
     VERTEX,   21.96155, -60.92323,  35.15688,
     VERTEX,   21.74062, -60.37149,  35.91078,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  21.04815, -59.77063,  34.65689,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -4.27475, -75.69580,  58.58569,
                       
     VERTEX,    0.61105, -74.09512,  55.26646,
     VERTEX,    0.28256, -73.19739,  55.35470,
     VERTEX,   -0.38068, -72.57864,  55.04028,
     VERTEX,   -1.12534, -72.47520,  54.44330,
     VERTEX,   -1.66698, -72.92660,  53.79179,
     VERTEX,   -1.79872, -73.76040,  53.33460,
     VERTEX,   -1.47024, -74.65813,  53.24636,
     VERTEX,   -0.80700, -75.27688,  53.56078,
     VERTEX,   -0.06234, -75.38031,  54.15776,
     VERTEX,    0.47931, -74.92892,  54.80927,
     VERTEX,    0.61105, -74.09512,  55.26646,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.59384, -73.92776,  54.30053,
                       
     VERTEX,    0.61105, -74.09512,  55.26646,
     VERTEX,    0.28256, -73.19739,  55.35470,
     VERTEX,   -0.38068, -72.57864,  55.04028,
     VERTEX,   -1.12534, -72.47520,  54.44330,
     VERTEX,   -1.66698, -72.92660,  53.79179,
     VERTEX,   -1.79872, -73.76040,  53.33460,
     VERTEX,   -1.47024, -74.65813,  53.24636,
     VERTEX,   -0.80700, -75.27688,  53.56078,
     VERTEX,   -0.06234, -75.38031,  54.15776,
     VERTEX,    0.47931, -74.92892,  54.80927,
     VERTEX,    0.61105, -74.09512,  55.26646,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  -0.59384, -73.92776,  54.30053,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.79116, -81.35974,  54.09985,
                       
     VERTEX,   13.80381, -79.44847,  51.89339,
     VERTEX,   13.44205, -78.57143,  52.04009,
     VERTEX,   12.81106, -77.92667,  51.71185,
     VERTEX,   12.15185, -77.76049,  51.03403,
     VERTEX,   11.71622, -78.13634,  50.26556,
     VERTEX,   11.67057, -78.91068,  49.69994,
     VERTEX,   12.03233, -79.78773,  49.55324,
     VERTEX,   12.66332, -80.43248,  49.88148,
     VERTEX,   13.32253, -80.59866,  50.55929,
     VERTEX,   13.75816, -80.22281,  51.32777,
     VERTEX,   13.80381, -79.44847,  51.89339,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.73719, -79.17957,  50.79666,
                       
     VERTEX,   13.80381, -79.44847,  51.89339,
     VERTEX,   13.44205, -78.57143,  52.04009,
     VERTEX,   12.81106, -77.92667,  51.71185,
     VERTEX,   12.15185, -77.76049,  51.03403,
     VERTEX,   11.71622, -78.13634,  50.26556,
     VERTEX,   11.67057, -78.91068,  49.69994,
     VERTEX,   12.03233, -79.78773,  49.55324,
     VERTEX,   12.66332, -80.43248,  49.88148,
     VERTEX,   13.32253, -80.59866,  50.55929,
     VERTEX,   13.75816, -80.22281,  51.32777,
     VERTEX,   13.80381, -79.44847,  51.89339,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  12.73719, -79.17957,  50.79666,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.19489, -78.00805,  41.36844,
                       
     VERTEX,   16.87465, -75.40838,  40.07050,
     VERTEX,   16.45915, -74.57023,  40.28608,
     VERTEX,   15.86218, -73.89276,  39.96012,
     VERTEX,   15.31174, -73.63473,  39.21712,
     VERTEX,   15.01810, -73.89471,  38.34089,
     VERTEX,   15.09340, -74.57339,  37.66611,
     VERTEX,   15.50889, -75.41153,  37.45053,
     VERTEX,   16.10587, -76.08900,  37.77649,
     VERTEX,   16.65631, -76.34703,  38.51949,
     VERTEX,   16.94995, -76.08706,  39.39572,
     VERTEX,   16.87465, -75.40838,  40.07050,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.98402, -74.99088,  38.86830,
                       
     VERTEX,   16.87465, -75.40838,  40.07050,
     VERTEX,   16.45915, -74.57023,  40.28608,
     VERTEX,   15.86218, -73.89276,  39.96012,
     VERTEX,   15.31174, -73.63473,  39.21712,
     VERTEX,   15.01810, -73.89471,  38.34089,
     VERTEX,   15.09340, -74.57339,  37.66611,
     VERTEX,   15.50889, -75.41153,  37.45053,
     VERTEX,   16.10587, -76.08900,  37.77649,
     VERTEX,   16.65631, -76.34703,  38.51949,
     VERTEX,   16.94995, -76.08706,  39.39572,
     VERTEX,   16.87465, -75.40838,  40.07050,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  15.98402, -74.99088,  38.86830,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.03074, -61.49548,  41.17347,
                       
     VERTEX,    5.31991, -59.12022,  39.92501,
     VERTEX,    4.90933, -58.27847,  40.13590,
     VERTEX,    4.30856, -57.60417,  39.81031,
     VERTEX,    3.74708, -57.35489,  39.07261,
     VERTEX,    3.43936, -57.62585,  38.20457,
     VERTEX,    3.50293, -58.31354,  37.53776,
     VERTEX,    3.91352, -59.15529,  37.32687,
     VERTEX,    4.51428, -59.82958,  37.65245,
     VERTEX,    5.07576, -60.07886,  38.39016,
     VERTEX,    5.38348, -59.80791,  39.25819,
     VERTEX,    5.31991, -59.12022,  39.92501,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    4.41142, -58.71688,  38.73138,
                       
     VERTEX,    5.31991, -59.12022,  39.92501,
     VERTEX,    4.90933, -58.27847,  40.13590,
     VERTEX,    4.30856, -57.60417,  39.81031,
     VERTEX,    3.74708, -57.35489,  39.07261,
     VERTEX,    3.43936, -57.62585,  38.20457,
     VERTEX,    3.50293, -58.31354,  37.53776,
     VERTEX,    3.91352, -59.15529,  37.32687,
     VERTEX,    4.51428, -59.82958,  37.65245,
     VERTEX,    5.07576, -60.07886,  38.39016,
     VERTEX,    5.38348, -59.80791,  39.25819,
     VERTEX,    5.31991, -59.12022,  39.92501,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,   4.41142, -58.71688,  38.73138,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   53.02995, -49.93094, 124.02410,
                       
     VERTEX,   49.03954, -53.95966, 122.59128,
     VERTEX,   48.51035, -53.21563, 122.29466,
     VERTEX,   47.96606, -52.48249, 122.59107,
     VERTEX,   47.61458, -52.04027, 123.36728,
     VERTEX,   47.59015, -52.05789, 124.32681,
     VERTEX,   47.90211, -52.52861, 125.10315,
     VERTEX,   48.43130, -53.27264, 125.39977,
     VERTEX,   48.97559, -54.00578, 125.10336,
     VERTEX,   49.32707, -54.44800, 124.32715,
     VERTEX,   49.35150, -54.43038, 123.36761,
     VERTEX,   49.03954, -53.95966, 122.59128,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.47083, -53.24414, 123.84721,
                       
     VERTEX,   49.03954, -53.95966, 122.59128,
     VERTEX,   48.51035, -53.21563, 122.29466,
     VERTEX,   47.96606, -52.48249, 122.59107,
     VERTEX,   47.61458, -52.04027, 123.36728,
     VERTEX,   47.59015, -52.05789, 124.32681,
     VERTEX,   47.90211, -52.52861, 125.10315,
     VERTEX,   48.43130, -53.27264, 125.39977,
     VERTEX,   48.97559, -54.00578, 125.10336,
     VERTEX,   49.32707, -54.44800, 124.32715,
     VERTEX,   49.35150, -54.43038, 123.36761,
     VERTEX,   49.03954, -53.95966, 122.59128,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  48.47083, -53.24414, 123.84721,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   51.07035, -45.22787, 124.74836,
                       
     VERTEX,   47.09174, -49.30306, 123.46860,
     VERTEX,   46.55266, -48.56863, 123.16593,
     VERTEX,   46.00878, -47.83287, 123.45656,
     VERTEX,   45.66785, -47.37683, 124.22947,
     VERTEX,   45.66009, -47.37468, 125.18943,
     VERTEX,   45.98846, -47.82726, 125.96978,
     VERTEX,   46.52754, -48.56169, 126.27245,
     VERTEX,   47.07142, -49.29744, 125.98183,
     VERTEX,   47.41235, -49.75349, 125.20892,
     VERTEX,   47.42011, -49.75563, 124.24895,
     VERTEX,   47.09174, -49.30306, 123.46860,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.54010, -48.56516, 124.71919,
                       
     VERTEX,   47.09174, -49.30306, 123.46860,
     VERTEX,   46.55266, -48.56863, 123.16593,
     VERTEX,   46.00878, -47.83287, 123.45656,
     VERTEX,   45.66785, -47.37683, 124.22947,
     VERTEX,   45.66009, -47.37468, 125.18943,
     VERTEX,   45.98846, -47.82726, 125.96978,
     VERTEX,   46.52754, -48.56169, 126.27245,
     VERTEX,   47.07142, -49.29744, 125.98183,
     VERTEX,   47.41235, -49.75349, 125.20892,
     VERTEX,   47.42011, -49.75563, 124.24895,
     VERTEX,   47.09174, -49.30306, 123.46860,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  46.54010, -48.56516, 124.71919,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   75.14723, -60.38103, 112.74466,
                       
     VERTEX,   71.32389, -64.92200, 113.08681,
     VERTEX,   70.67851, -64.30351, 112.73674,
     VERTEX,   70.12242, -63.55296, 112.95816,
     VERTEX,   69.86803, -62.95701, 113.66650,
     VERTEX,   70.01251, -62.74332, 114.59119,
     VERTEX,   70.50068, -62.99350, 115.37904,
     VERTEX,   71.14606, -63.61198, 115.72912,
     VERTEX,   71.70215, -64.36255, 115.50770,
     VERTEX,   71.95654, -64.95849, 114.79936,
     VERTEX,   71.81206, -65.17218, 113.87466,
     VERTEX,   71.32389, -64.92200, 113.08681,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   70.91228, -63.95775, 114.23293,
                       
     VERTEX,   71.32389, -64.92200, 113.08681,
     VERTEX,   70.67851, -64.30351, 112.73674,
     VERTEX,   70.12242, -63.55296, 112.95816,
     VERTEX,   69.86803, -62.95701, 113.66650,
     VERTEX,   70.01251, -62.74332, 114.59119,
     VERTEX,   70.50068, -62.99350, 115.37904,
     VERTEX,   71.14606, -63.61198, 115.72912,
     VERTEX,   71.70215, -64.36255, 115.50770,
     VERTEX,   71.95654, -64.95849, 114.79936,
     VERTEX,   71.81206, -65.17218, 113.87466,
     VERTEX,   71.32389, -64.92200, 113.08681,
                       
     END,              
                       
     CYLINDER,   64.06000, -69.74500, 116.64100,  70.91228, -63.95775, 114.23293,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.96305, -35.40564, 127.81990,
                       
     VERTEX,   36.99545, -39.37553, 126.22381,
     VERTEX,   36.47581, -38.62286, 125.93216,
     VERTEX,   35.92899, -37.89332, 126.23276,
     VERTEX,   35.56385, -37.46558, 127.01077,
     VERTEX,   35.51987, -37.50301, 127.96904,
     VERTEX,   35.81385, -37.99132, 128.74152,
     VERTEX,   36.33349, -38.74399, 129.03316,
     VERTEX,   36.88031, -39.47353, 128.73257,
     VERTEX,   37.24545, -39.90128, 127.95455,
     VERTEX,   37.28943, -39.86384, 126.99629,
     VERTEX,   36.99545, -39.37553, 126.22381,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.40465, -38.68343, 127.48267,
                       
     VERTEX,   36.99545, -39.37553, 126.22381,
     VERTEX,   36.47581, -38.62286, 125.93216,
     VERTEX,   35.92899, -37.89332, 126.23276,
     VERTEX,   35.56385, -37.46558, 127.01077,
     VERTEX,   35.51987, -37.50301, 127.96904,
     VERTEX,   35.81385, -37.99132, 128.74152,
     VERTEX,   36.33349, -38.74399, 129.03316,
     VERTEX,   36.88031, -39.47353, 128.73257,
     VERTEX,   37.24545, -39.90128, 127.95455,
     VERTEX,   37.28943, -39.86384, 126.99629,
     VERTEX,   36.99545, -39.37553, 126.22381,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  36.40465, -38.68343, 127.48267,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.73331, -41.87840, 126.88662,
                       
     VERTEX,   36.91859, -45.56124, 124.79987,
     VERTEX,   36.43128, -44.77904, 124.53104,
     VERTEX,   35.87985, -44.06024, 124.84862,
     VERTEX,   35.47493, -43.67941, 125.63132,
     VERTEX,   35.37120, -43.78202, 126.58016,
     VERTEX,   35.60826, -44.32887, 127.33273,
     VERTEX,   36.09557, -45.11108, 127.60157,
     VERTEX,   36.64700, -45.82987, 127.28398,
     VERTEX,   37.05191, -46.21070, 126.50129,
     VERTEX,   37.15565, -46.10809, 125.55244,
     VERTEX,   36.91859, -45.56124, 124.79987,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.26342, -44.94506, 126.06630,
                       
     VERTEX,   36.91859, -45.56124, 124.79987,
     VERTEX,   36.43128, -44.77904, 124.53104,
     VERTEX,   35.87985, -44.06024, 124.84862,
     VERTEX,   35.47493, -43.67941, 125.63132,
     VERTEX,   35.37120, -43.78202, 126.58016,
     VERTEX,   35.60826, -44.32887, 127.33273,
     VERTEX,   36.09557, -45.11108, 127.60157,
     VERTEX,   36.64700, -45.82987, 127.28398,
     VERTEX,   37.05191, -46.21070, 126.50129,
     VERTEX,   37.15565, -46.10809, 125.55244,
     VERTEX,   36.91859, -45.56124, 124.79987,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  36.26342, -44.94506, 126.06630,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -24.91664, -23.80153,  86.95316,
                       
     VERTEX,  -22.38425, -23.52113,  91.19958,
     VERTEX,  -22.62672, -22.59260,  91.17435,
     VERTEX,  -22.45623, -21.75708,  90.73341,
     VERTEX,  -21.93788, -21.33370,  90.04517,
     VERTEX,  -21.26968, -21.48419,  89.37252,
     VERTEX,  -20.70685, -22.15106,  88.97239,
     VERTEX,  -20.46437, -23.07959,  88.99762,
     VERTEX,  -20.63487, -23.91512,  89.43856,
     VERTEX,  -21.15321, -24.33849,  90.12680,
     VERTEX,  -21.82141, -24.18800,  90.79945,
     VERTEX,  -22.38425, -23.52113,  91.19958,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -21.54555, -22.83610,  90.08598,
                       
     VERTEX,  -22.38425, -23.52113,  91.19958,
     VERTEX,  -22.62672, -22.59260,  91.17435,
     VERTEX,  -22.45623, -21.75708,  90.73341,
     VERTEX,  -21.93788, -21.33370,  90.04517,
     VERTEX,  -21.26968, -21.48419,  89.37252,
     VERTEX,  -20.70685, -22.15106,  88.97239,
     VERTEX,  -20.46437, -23.07959,  88.99762,
     VERTEX,  -20.63487, -23.91512,  89.43856,
     VERTEX,  -21.15321, -24.33849,  90.12680,
     VERTEX,  -21.82141, -24.18800,  90.79945,
     VERTEX,  -22.38425, -23.52113,  91.19958,
                       
     END,              
                       
     CYLINDER,  -16.09100, -21.27400,  95.15500, -21.54555, -22.83610,  90.08598,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -10.55471,  -4.08539, 110.85900,
                       
     VERTEX,   -6.14132,  -2.20937, 112.49830,
     VERTEX,   -6.66434,  -1.44484, 112.75037,
     VERTEX,   -7.13650,  -0.68084, 112.41130,
     VERTEX,   -7.37745,  -0.20919, 111.61062,
     VERTEX,   -7.29517,  -0.21006, 110.65415,
     VERTEX,   -6.92107,  -0.68310, 109.90724,
     VERTEX,   -6.39805,  -1.44764, 109.65517,
     VERTEX,   -5.92588,  -2.21164, 109.99424,
     VERTEX,   -5.68493,  -2.68328, 110.79492,
     VERTEX,   -5.76722,  -2.68242, 111.75139,
     VERTEX,   -6.14132,  -2.20937, 112.49830,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.53119,  -1.44624, 111.20277,
                       
     VERTEX,   -6.14132,  -2.20937, 112.49830,
     VERTEX,   -6.66434,  -1.44484, 112.75037,
     VERTEX,   -7.13650,  -0.68084, 112.41130,
     VERTEX,   -7.37745,  -0.20919, 111.61062,
     VERTEX,   -7.29517,  -0.21006, 110.65415,
     VERTEX,   -6.92107,  -0.68310, 109.90724,
     VERTEX,   -6.39805,  -1.44764, 109.65517,
     VERTEX,   -5.92588,  -2.21164, 109.99424,
     VERTEX,   -5.68493,  -2.68328, 110.79492,
     VERTEX,   -5.76722,  -2.68242, 111.75139,
     VERTEX,   -6.14132,  -2.20937, 112.49830,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,  -6.53119,  -1.44624, 111.20277,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -12.63919, -10.36889, 109.36829,
                       
     VERTEX,   -8.25457,  -8.59600, 111.59536,
     VERTEX,   -8.78576,  -7.82985, 111.82436,
     VERTEX,   -9.20144,  -7.03954, 111.47191,
     VERTEX,   -9.34282,  -6.52694, 110.67262,
     VERTEX,   -9.15591,  -6.48785, 109.73181,
     VERTEX,   -8.71209,  -6.93720, 109.00882,
     VERTEX,   -8.18089,  -7.70335, 108.77982,
     VERTEX,   -7.76521,  -8.49366, 109.13227,
     VERTEX,   -7.62383,  -9.00626, 109.93156,
     VERTEX,   -7.81075,  -9.04535, 110.87237,
     VERTEX,   -8.25457,  -8.59600, 111.59536,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -8.48333,  -7.76660, 110.30209,
                       
     VERTEX,   -8.25457,  -8.59600, 111.59536,
     VERTEX,   -8.78576,  -7.82985, 111.82436,
     VERTEX,   -9.20144,  -7.03954, 111.47191,
     VERTEX,   -9.34282,  -6.52694, 110.67262,
     VERTEX,   -9.15591,  -6.48785, 109.73181,
     VERTEX,   -8.71209,  -6.93720, 109.00882,
     VERTEX,   -8.18089,  -7.70335, 108.77982,
     VERTEX,   -7.76521,  -8.49366, 109.13227,
     VERTEX,   -7.62383,  -9.00626, 109.93156,
     VERTEX,   -7.81075,  -9.04535, 110.87237,
     VERTEX,   -8.25457,  -8.59600, 111.59536,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,  -8.48333,  -7.76660, 110.30209,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -10.60159, -15.07000, 107.86262,
                       
     VERTEX,   -6.30687, -13.31219, 110.24276,
     VERTEX,   -6.85360, -12.55952, 110.47979,
     VERTEX,   -7.27102, -11.76491, 110.13928,
     VERTEX,   -7.39971, -11.23186, 109.35131,
     VERTEX,   -7.19050, -11.16400, 108.41684,
     VERTEX,   -6.72331, -11.58723, 107.69282,
     VERTEX,   -6.17659, -12.33990, 107.45579,
     VERTEX,   -5.75917, -13.13452, 107.79630,
     VERTEX,   -5.63048, -13.66756, 108.58427,
     VERTEX,   -5.83969, -13.73543, 109.51874,
     VERTEX,   -6.30687, -13.31219, 110.24276,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.51509, -12.44971, 108.96779,
                       
     VERTEX,   -6.30687, -13.31219, 110.24276,
     VERTEX,   -6.85360, -12.55952, 110.47979,
     VERTEX,   -7.27102, -11.76491, 110.13928,
     VERTEX,   -7.39971, -11.23186, 109.35131,
     VERTEX,   -7.19050, -11.16400, 108.41684,
     VERTEX,   -6.72331, -11.58723, 107.69282,
     VERTEX,   -6.17659, -12.33990, 107.45579,
     VERTEX,   -5.75917, -13.13452, 107.79630,
     VERTEX,   -5.63048, -13.66756, 108.58427,
     VERTEX,   -5.83969, -13.73543, 109.51874,
     VERTEX,   -6.30687, -13.31219, 110.24276,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,  -6.51509, -12.44971, 108.96779,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.14085, -19.07141, 107.80081,
                       
     VERTEX,    4.23914, -17.13523, 109.53315,
     VERTEX,    3.69767, -16.38990, 109.80315,
     VERTEX,    3.21157, -15.62661, 109.48270,
     VERTEX,    2.96650, -15.13691, 108.69421,
     VERTEX,    3.05608, -15.10784, 107.73884,
     VERTEX,    3.44609, -15.55051, 106.98151,
     VERTEX,    3.98756, -16.29584, 106.71151,
     VERTEX,    4.47366, -17.05913, 107.03196,
     VERTEX,    4.71873, -17.54884, 107.82047,
     VERTEX,    4.62915, -17.57790, 108.77583,
     VERTEX,    4.23914, -17.13523, 109.53315,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.84261, -16.34287, 108.25733,
                       
     VERTEX,    4.23914, -17.13523, 109.53315,
     VERTEX,    3.69767, -16.38990, 109.80315,
     VERTEX,    3.21157, -15.62661, 109.48270,
     VERTEX,    2.96650, -15.13691, 108.69421,
     VERTEX,    3.05608, -15.10784, 107.73884,
     VERTEX,    3.44609, -15.55051, 106.98151,
     VERTEX,    3.98756, -16.29584, 106.71151,
     VERTEX,    4.47366, -17.05913, 107.03196,
     VERTEX,    4.71873, -17.54884, 107.82047,
     VERTEX,    4.62915, -17.57790, 108.77583,
     VERTEX,    4.23914, -17.13523, 109.53315,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,   3.84261, -16.34287, 108.25733,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.45188,  38.24814,  36.09442,
                       
     VERTEX,   20.85238,  35.76884,  31.95303,
     VERTEX,   20.52134,  36.66800,  31.89366,
     VERTEX,   20.00974,  37.33908,  32.35139,
     VERTEX,   19.51300,  37.52575,  33.15140,
     VERTEX,   19.22086,  37.15672,  33.98809,
     VERTEX,   19.24489,  36.37292,  34.54190,
     VERTEX,   19.57593,  35.47376,  34.60127,
     VERTEX,   20.08752,  34.80268,  34.14353,
     VERTEX,   20.58426,  34.61601,  33.34353,
     VERTEX,   20.87641,  34.98505,  32.50684,
     VERTEX,   20.85238,  35.76884,  31.95303,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.04863,  36.07088,  33.24747,
                       
     VERTEX,   20.85238,  35.76884,  31.95303,
     VERTEX,   20.52134,  36.66800,  31.89366,
     VERTEX,   20.00974,  37.33908,  32.35139,
     VERTEX,   19.51300,  37.52575,  33.15140,
     VERTEX,   19.22086,  37.15672,  33.98809,
     VERTEX,   19.24489,  36.37292,  34.54190,
     VERTEX,   19.57593,  35.47376,  34.60127,
     VERTEX,   20.08752,  34.80268,  34.14353,
     VERTEX,   20.58426,  34.61601,  33.34353,
     VERTEX,   20.87641,  34.98505,  32.50684,
     VERTEX,   20.85238,  35.76884,  31.95303,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,  20.04863,  36.07088,  33.24747,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.15403,  37.33895,  63.27167,
                       
     VERTEX,   42.80703,  38.84773,  56.79563,
     VERTEX,   42.63912,  39.72111,  57.15705,
     VERTEX,   42.07423,  40.22018,  57.75155,
     VERTEX,   41.32815,  40.15432,  58.35207,
     VERTEX,   40.68584,  39.54868,  58.72922,
     VERTEX,   40.39265,  38.63459,  58.73894,
     VERTEX,   40.56056,  37.76122,  58.37752,
     VERTEX,   41.12544,  37.26215,  57.78302,
     VERTEX,   41.87153,  37.32801,  57.18250,
     VERTEX,   42.51384,  37.93365,  56.80536,
     VERTEX,   42.80703,  38.84773,  56.79563,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.59984,  38.74117,  57.76728,
                       
     VERTEX,   42.80703,  38.84773,  56.79563,
     VERTEX,   42.63912,  39.72111,  57.15705,
     VERTEX,   42.07423,  40.22018,  57.75155,
     VERTEX,   41.32815,  40.15432,  58.35207,
     VERTEX,   40.68584,  39.54868,  58.72922,
     VERTEX,   40.39265,  38.63459,  58.73894,
     VERTEX,   40.56056,  37.76122,  58.37752,
     VERTEX,   41.12544,  37.26215,  57.78302,
     VERTEX,   41.87153,  37.32801,  57.18250,
     VERTEX,   42.51384,  37.93365,  56.80536,
     VERTEX,   42.80703,  38.84773,  56.79563,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  41.59984,  38.74117,  57.76728,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.51801,  45.58022,  61.31020,
                       
     VERTEX,   29.61789,  45.78015,  55.48586,
     VERTEX,   29.42452,  46.68937,  55.72568,
     VERTEX,   28.89732,  47.24450,  56.30489,
     VERTEX,   28.23766,  47.23349,  57.00227,
     VERTEX,   27.69751,  46.66055,  57.55142,
     VERTEX,   27.48319,  45.74451,  57.74261,
     VERTEX,   27.67656,  44.83529,  57.50279,
     VERTEX,   28.20377,  44.28016,  56.92358,
     VERTEX,   28.86343,  44.29117,  56.22620,
     VERTEX,   29.40358,  44.86411,  55.67705,
     VERTEX,   29.61789,  45.78015,  55.48586,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.55054,  45.76233,  56.61423,
                       
     VERTEX,   29.61789,  45.78015,  55.48586,
     VERTEX,   29.42452,  46.68937,  55.72568,
     VERTEX,   28.89732,  47.24450,  56.30489,
     VERTEX,   28.23766,  47.23349,  57.00227,
     VERTEX,   27.69751,  46.66055,  57.55142,
     VERTEX,   27.48319,  45.74451,  57.74261,
     VERTEX,   27.67656,  44.83529,  57.50279,
     VERTEX,   28.20377,  44.28016,  56.92358,
     VERTEX,   28.86343,  44.29117,  56.22620,
     VERTEX,   29.40358,  44.86411,  55.67705,
     VERTEX,   29.61789,  45.78015,  55.48586,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  28.55054,  45.76233,  56.61423,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.53872,  48.73875,  48.21586,
                       
     VERTEX,   26.52765,  47.45527,  42.67891,
     VERTEX,   26.27890,  48.37766,  42.77345,
     VERTEX,   25.77245,  48.99476,  43.30664,
     VERTEX,   25.20174,  49.07087,  44.07481,
     VERTEX,   24.78476,  48.57692,  44.78456,
     VERTEX,   24.68079,  47.70158,  45.16479,
     VERTEX,   24.92954,  46.77920,  45.07025,
     VERTEX,   25.43599,  46.16210,  44.53706,
     VERTEX,   26.00670,  46.08599,  43.76889,
     VERTEX,   26.42368,  46.57993,  43.05914,
     VERTEX,   26.52765,  47.45527,  42.67891,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.60422,  47.57843,  43.92185,
                       
     VERTEX,   26.52765,  47.45527,  42.67891,
     VERTEX,   26.27890,  48.37766,  42.77345,
     VERTEX,   25.77245,  48.99476,  43.30664,
     VERTEX,   25.20174,  49.07087,  44.07481,
     VERTEX,   24.78476,  48.57692,  44.78456,
     VERTEX,   24.68079,  47.70158,  45.16479,
     VERTEX,   24.92954,  46.77920,  45.07025,
     VERTEX,   25.43599,  46.16210,  44.53706,
     VERTEX,   26.00670,  46.08599,  43.76889,
     VERTEX,   26.42368,  46.57993,  43.05914,
     VERTEX,   26.52765,  47.45527,  42.67891,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,  25.60422,  47.57843,  43.92185,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.80452,  33.08961,  41.05413,
                       
     VERTEX,   37.54060,  32.33834,  35.69275,
     VERTEX,   37.31107,  33.26003,  35.83208,
     VERTEX,   36.79871,  33.85844,  36.38073,
     VERTEX,   36.19924,  33.90499,  37.12910,
     VERTEX,   35.74162,  33.38192,  37.79135,
     VERTEX,   35.60065,  32.48901,  38.11453,
     VERTEX,   35.83018,  31.56733,  37.97519,
     VERTEX,   36.34254,  30.96893,  37.42655,
     VERTEX,   36.94201,  30.92237,  36.67818,
     VERTEX,   37.39963,  31.44544,  36.01592,
     VERTEX,   37.54060,  32.33834,  35.69275,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.57063,  32.41368,  36.90364,
                       
     VERTEX,   37.54060,  32.33834,  35.69275,
     VERTEX,   37.31107,  33.26003,  35.83208,
     VERTEX,   36.79871,  33.85844,  36.38073,
     VERTEX,   36.19924,  33.90499,  37.12910,
     VERTEX,   35.74162,  33.38192,  37.79135,
     VERTEX,   35.60065,  32.48901,  38.11453,
     VERTEX,   35.83018,  31.56733,  37.97519,
     VERTEX,   36.34254,  30.96893,  37.42655,
     VERTEX,   36.94201,  30.92237,  36.67818,
     VERTEX,   37.39963,  31.44544,  36.01592,
     VERTEX,   37.54060,  32.33834,  35.69275,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  36.57063,  32.41368,  36.90364,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00001_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   28.41300, -54.63000,  33.05300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    5.36200, -71.06700,  47.36700,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   19.12200, -75.65200,  45.45200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   23.73300, -70.10900,  34.82300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   11.59900, -54.22100,  34.78000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   41.09400, -58.60500, 123.56100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   39.21000, -53.96500, 124.67200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   64.06000, -69.74500, 116.64100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   29.02900, -43.98700, 126.93700,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   29.03100, -49.90700, 124.73900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -16.09100, -21.27400,  95.15500,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   -0.02100,   2.82400, 111.75900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   -1.75900,  -3.55600, 111.81300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    0.09700,  -8.21000, 110.75600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.28800, -11.92800, 108.99600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   11.30600,  32.54800,  28.64100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   34.23100,  41.01000,  48.86100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   20.51300,  46.05700,  49.01600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   16.00200,  45.70100,  36.97400,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   28.10200,  31.32000,  30.18800,   0.80000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00001_arror_pos') 
