from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.23363, -46.52939,  30.46421,
                       
     VERTEX,   36.02702, -50.47663,  30.19214,
     VERTEX,   35.46668, -49.74432,  29.92505,
     VERTEX,   35.00254, -48.96588,  30.24160,
     VERTEX,   34.81190, -48.43864,  31.02088,
     VERTEX,   34.96756, -48.36400,  31.96523,
     VERTEX,   35.41008, -48.77046,  32.71394,
     VERTEX,   35.97042, -49.50278,  32.98103,
     VERTEX,   36.43456, -50.28122,  32.66448,
     VERTEX,   36.62521, -50.80845,  31.88520,
     VERTEX,   36.46954, -50.88309,  30.94085,
     VERTEX,   36.02702, -50.47663,  30.19214,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.71855, -49.62355,  31.45304,
                       
     VERTEX,   36.02702, -50.47663,  30.19214,
     VERTEX,   35.46668, -49.74432,  29.92505,
     VERTEX,   35.00254, -48.96588,  30.24160,
     VERTEX,   34.81190, -48.43864,  31.02088,
     VERTEX,   34.96756, -48.36400,  31.96523,
     VERTEX,   35.41008, -48.77046,  32.71394,
     VERTEX,   35.97042, -49.50278,  32.98103,
     VERTEX,   36.43456, -50.28122,  32.66448,
     VERTEX,   36.62521, -50.80845,  31.88520,
     VERTEX,   36.46954, -50.88309,  30.94085,
     VERTEX,   36.02702, -50.47663,  30.19214,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  35.71855, -49.62355,  31.45304,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.94090, -66.56243,  36.28156,
                       
     VERTEX,   10.64341, -69.31383,  39.54508,
     VERTEX,   10.15950, -68.48887,  39.46215,
     VERTEX,   10.10437, -67.58529,  39.78169,
     VERTEX,   10.49909, -66.94822,  40.38164,
     VERTEX,   11.19289, -66.82100,  41.03284,
     VERTEX,   11.92075, -67.25223,  41.48656,
     VERTEX,   12.40467, -68.07718,  41.56949,
     VERTEX,   12.45979, -68.98076,  41.24995,
     VERTEX,   12.06507, -69.61783,  40.65000,
     VERTEX,   11.37128, -69.74505,  39.99880,
     VERTEX,   10.64341, -69.31383,  39.54508,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.28208, -68.28303,  40.51582,
                       
     VERTEX,   10.64341, -69.31383,  39.54508,
     VERTEX,   10.15950, -68.48887,  39.46215,
     VERTEX,   10.10437, -67.58529,  39.78169,
     VERTEX,   10.49909, -66.94822,  40.38164,
     VERTEX,   11.19289, -66.82100,  41.03284,
     VERTEX,   11.92075, -67.25223,  41.48656,
     VERTEX,   12.40467, -68.07718,  41.56949,
     VERTEX,   12.45979, -68.98076,  41.24995,
     VERTEX,   12.06507, -69.61783,  40.65000,
     VERTEX,   11.37128, -69.74505,  39.99880,
     VERTEX,   10.64341, -69.31383,  39.54508,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  11.28208, -68.28303,  40.51582,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.37579, -70.06821,  36.90975,
                       
     VERTEX,   25.10706, -73.23866,  39.07164,
     VERTEX,   24.56440, -72.45959,  38.92951,
     VERTEX,   24.36353, -71.58178,  39.26219,
     VERTEX,   24.58116, -70.94048,  39.94262,
     VERTEX,   25.13417, -70.78068,  40.71090,
     VERTEX,   25.81133, -71.16339,  41.27356,
     VERTEX,   26.35398, -71.94245,  41.41569,
     VERTEX,   26.55485, -72.82027,  41.08301,
     VERTEX,   26.33722, -73.46156,  40.40258,
     VERTEX,   25.78421, -73.62137,  39.63431,
     VERTEX,   25.10706, -73.23866,  39.07164,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.45919, -72.20103,  40.17260,
                       
     VERTEX,   25.10706, -73.23866,  39.07164,
     VERTEX,   24.56440, -72.45959,  38.92951,
     VERTEX,   24.36353, -71.58178,  39.26219,
     VERTEX,   24.58116, -70.94048,  39.94262,
     VERTEX,   25.13417, -70.78068,  40.71090,
     VERTEX,   25.81133, -71.16339,  41.27356,
     VERTEX,   26.35398, -71.94245,  41.41569,
     VERTEX,   26.55485, -72.82027,  41.08301,
     VERTEX,   26.33722, -73.46156,  40.40258,
     VERTEX,   25.78421, -73.62137,  39.63431,
     VERTEX,   25.10706, -73.23866,  39.07164,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.45919, -72.20103,  40.17260,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.17501, -62.38936,  28.38947,
                       
     VERTEX,   31.40318, -66.31380,  29.63846,
     VERTEX,   30.83333, -65.57028,  29.42855,
     VERTEX,   30.48855, -64.73804,  29.76039,
     VERTEX,   30.50055, -64.13497,  30.50722,
     VERTEX,   30.86473, -63.99141,  31.38378,
     VERTEX,   31.44200, -64.36221,  32.05526,
     VERTEX,   32.01185, -65.10571,  32.26516,
     VERTEX,   32.35662, -65.93795,  31.93333,
     VERTEX,   32.34463, -66.54102,  31.18650,
     VERTEX,   31.98044, -66.68459,  30.30993,
     VERTEX,   31.40318, -66.31380,  29.63846,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.42259, -65.33800,  30.84686,
                       
     VERTEX,   31.40318, -66.31380,  29.63846,
     VERTEX,   30.83333, -65.57028,  29.42855,
     VERTEX,   30.48855, -64.73804,  29.76039,
     VERTEX,   30.50055, -64.13497,  30.50722,
     VERTEX,   30.86473, -63.99141,  31.38378,
     VERTEX,   31.44200, -64.36221,  32.05526,
     VERTEX,   32.01185, -65.10571,  32.26516,
     VERTEX,   32.35662, -65.93795,  31.93333,
     VERTEX,   32.34463, -66.54102,  31.18650,
     VERTEX,   31.98044, -66.68459,  30.30993,
     VERTEX,   31.40318, -66.31380,  29.63846,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  31.42259, -65.33800,  30.84686,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.14794, -47.17211,  28.40675,
                       
     VERTEX,   18.67597, -50.84964,  29.64166,
     VERTEX,   18.10854, -50.10189,  29.44043,
     VERTEX,   17.78101, -49.26349,  29.77421,
     VERTEX,   17.81851, -48.65467,  30.51551,
     VERTEX,   18.20670, -48.50798,  31.38119,
     VERTEX,   18.79730, -48.87946,  32.04057,
     VERTEX,   19.36474, -49.62720,  32.24181,
     VERTEX,   19.69226, -50.46560,  31.90803,
     VERTEX,   19.65477, -51.07442,  31.16672,
     VERTEX,   19.26658, -51.22111,  30.30105,
     VERTEX,   18.67597, -50.84964,  29.64166,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.73664, -49.86454,  30.84112,
                       
     VERTEX,   18.67597, -50.84964,  29.64166,
     VERTEX,   18.10854, -50.10189,  29.44043,
     VERTEX,   17.78101, -49.26349,  29.77421,
     VERTEX,   17.81851, -48.65467,  30.51551,
     VERTEX,   18.20670, -48.50798,  31.38119,
     VERTEX,   18.79730, -48.87946,  32.04057,
     VERTEX,   19.36474, -49.62720,  32.24181,
     VERTEX,   19.69226, -50.46560,  31.90803,
     VERTEX,   19.65477, -51.07442,  31.16672,
     VERTEX,   19.26658, -51.22111,  30.30105,
     VERTEX,   18.67597, -50.84964,  29.64166,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,  18.73664, -49.86454,  30.84112,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.58240, -71.99719, 118.68833,
                       
     VERTEX,   32.39278, -69.87579, 120.74889,
     VERTEX,   31.85712, -69.11844, 120.99606,
     VERTEX,   31.40859, -68.34045, 120.65672,
     VERTEX,   31.21852, -67.83897, 119.86048,
     VERTEX,   31.35951, -67.80556, 118.91148,
     VERTEX,   31.77770, -68.25298, 118.17220,
     VERTEX,   32.31337, -69.01033, 117.92502,
     VERTEX,   32.76189, -69.78831, 118.26436,
     VERTEX,   32.95197, -70.28979, 119.06060,
     VERTEX,   32.81098, -70.32320, 120.00961,
     VERTEX,   32.39278, -69.87579, 120.74889,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.08524, -69.06438, 119.46054,
                       
     VERTEX,   32.39278, -69.87579, 120.74889,
     VERTEX,   31.85712, -69.11844, 120.99606,
     VERTEX,   31.40859, -68.34045, 120.65672,
     VERTEX,   31.21852, -67.83897, 119.86048,
     VERTEX,   31.35951, -67.80556, 118.91148,
     VERTEX,   31.77770, -68.25298, 118.17220,
     VERTEX,   32.31337, -69.01033, 117.92502,
     VERTEX,   32.76189, -69.78831, 118.26436,
     VERTEX,   32.95197, -70.28979, 119.06060,
     VERTEX,   32.81098, -70.32320, 120.00961,
     VERTEX,   32.39278, -69.87579, 120.74889,
                       
     END,              
                       
     CYLINDER,   39.37100, -64.31900, 120.71000,  32.08524, -69.06438, 119.46054,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.05933, -66.96675, 123.11974,
                       
     VERTEX,   34.13036, -64.52262, 124.56333,
     VERTEX,   33.59909, -63.77262, 124.84055,
     VERTEX,   33.08962, -63.02270, 124.52485,
     VERTEX,   32.79655, -62.55931, 123.73682,
     VERTEX,   32.83183, -62.55946, 122.77747,
     VERTEX,   33.18197, -63.02307, 122.01323,
     VERTEX,   33.71324, -63.77308, 121.73602,
     VERTEX,   34.22271, -64.52299, 122.05172,
     VERTEX,   34.51578, -64.98637, 122.83974,
     VERTEX,   34.48051, -64.98624, 123.79910,
     VERTEX,   34.13036, -64.52262, 124.56333,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.65617, -63.77285, 123.28828,
                       
     VERTEX,   34.13036, -64.52262, 124.56333,
     VERTEX,   33.59909, -63.77262, 124.84055,
     VERTEX,   33.08962, -63.02270, 124.52485,
     VERTEX,   32.79655, -62.55931, 123.73682,
     VERTEX,   32.83183, -62.55946, 122.77747,
     VERTEX,   33.18197, -63.02307, 122.01323,
     VERTEX,   33.71324, -63.77308, 121.73602,
     VERTEX,   34.22271, -64.52299, 122.05172,
     VERTEX,   34.51578, -64.98637, 122.83974,
     VERTEX,   34.48051, -64.98624, 123.79910,
     VERTEX,   34.13036, -64.52262, 124.56333,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  33.65617, -63.77285, 123.28828,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.32305, -62.33843, 124.57553,
                       
     VERTEX,   32.37172, -59.87622, 125.88223,
     VERTEX,   31.84195, -59.12742, 126.16549,
     VERTEX,   31.32039, -58.38345, 125.85551,
     VERTEX,   31.00627, -57.92848, 125.07070,
     VERTEX,   31.01957, -57.93629, 124.11082,
     VERTEX,   31.35520, -58.40391, 123.34252,
     VERTEX,   31.88497, -59.15271, 123.05927,
     VERTEX,   32.40652, -59.89668, 123.36924,
     VERTEX,   32.72065, -60.35165, 124.15405,
     VERTEX,   32.70735, -60.34384, 125.11393,
     VERTEX,   32.37172, -59.87622, 125.88223,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.86346, -59.14007, 124.61237,
                       
     VERTEX,   32.37172, -59.87622, 125.88223,
     VERTEX,   31.84195, -59.12742, 126.16549,
     VERTEX,   31.32039, -58.38345, 125.85551,
     VERTEX,   31.00627, -57.92848, 125.07070,
     VERTEX,   31.01957, -57.93629, 124.11082,
     VERTEX,   31.35520, -58.40391, 123.34252,
     VERTEX,   31.88497, -59.15271, 123.05927,
     VERTEX,   32.40652, -59.89668, 123.36924,
     VERTEX,   32.72065, -60.35165, 124.15405,
     VERTEX,   32.70735, -60.34384, 125.11393,
     VERTEX,   32.37172, -59.87622, 125.88223,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  31.86346, -59.14007, 124.61237,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   52.74883, -79.10534, 120.68584,
                       
     VERTEX,   57.94555, -76.09032, 120.29456,
     VERTEX,   57.44886, -75.34283, 120.63540,
     VERTEX,   56.80721, -74.66684, 120.40537,
     VERTEX,   56.26566, -74.32056, 119.69234,
     VERTEX,   56.03109, -74.43624, 118.76865,
     VERTEX,   56.19308, -74.96970, 117.98714,
     VERTEX,   56.68977, -75.71719, 117.64629,
     VERTEX,   57.33142, -76.39318, 117.87633,
     VERTEX,   57.87297, -76.73946, 118.58936,
     VERTEX,   58.10754, -76.62378, 119.51305,
     VERTEX,   57.94555, -76.09032, 120.29456,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   57.06931, -75.53001, 119.14085,
                       
     VERTEX,   57.94555, -76.09032, 120.29456,
     VERTEX,   57.44886, -75.34283, 120.63540,
     VERTEX,   56.80721, -74.66684, 120.40537,
     VERTEX,   56.26566, -74.32056, 119.69234,
     VERTEX,   56.03109, -74.43624, 118.76865,
     VERTEX,   56.19308, -74.96970, 117.98714,
     VERTEX,   56.68977, -75.71719, 117.64629,
     VERTEX,   57.33142, -76.39318, 117.87633,
     VERTEX,   57.87297, -76.73946, 118.58936,
     VERTEX,   58.10754, -76.62378, 119.51305,
     VERTEX,   57.94555, -76.09032, 120.29456,
                       
     END,              
                       
     CYLINDER,   64.06000, -69.74500, 116.64100,  57.06931, -75.53001, 119.14085,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.22683, -52.02204, 125.90261,
                       
     VERTEX,   22.15011, -49.72773, 127.57835,
     VERTEX,   21.61539, -48.97680, 127.84624,
     VERTEX,   21.12630, -48.21674, 127.52264,
     VERTEX,   20.86966, -47.73789, 126.73117,
     VERTEX,   20.94349, -47.72314, 125.77413,
     VERTEX,   21.31960, -48.17813, 125.01707,
     VERTEX,   21.85433, -48.92906, 124.74918,
     VERTEX,   22.34342, -49.68911, 125.07278,
     VERTEX,   22.60006, -50.16797, 125.86425,
     VERTEX,   22.52623, -50.18272, 126.82130,
     VERTEX,   22.15011, -49.72773, 127.57835,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.73486, -48.95293, 126.29771,
                       
     VERTEX,   22.15011, -49.72773, 127.57835,
     VERTEX,   21.61539, -48.97680, 127.84624,
     VERTEX,   21.12630, -48.21674, 127.52264,
     VERTEX,   20.86966, -47.73789, 126.73117,
     VERTEX,   20.94349, -47.72314, 125.77413,
     VERTEX,   21.31960, -48.17813, 125.01707,
     VERTEX,   21.85433, -48.92906, 124.74918,
     VERTEX,   22.34342, -49.68911, 125.07278,
     VERTEX,   22.60006, -50.16797, 125.86425,
     VERTEX,   22.52623, -50.18272, 126.82130,
     VERTEX,   22.15011, -49.72773, 127.57835,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  21.73486, -48.95293, 126.29771,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.27894, -18.87362, 103.29330,
                       
     VERTEX,   -9.57555, -19.92233,  99.06581,
     VERTEX,   -9.85727, -19.00525,  99.10036,
     VERTEX,  -10.43981, -18.38810,  99.54910,
     VERTEX,  -11.10067, -18.30661, 100.24063,
     VERTEX,  -11.58742, -18.79192, 100.91082,
     VERTEX,  -11.71414, -19.65864, 101.30367,
     VERTEX,  -11.43243, -20.57573, 101.26913,
     VERTEX,  -10.84989, -21.19287, 100.82039,
     VERTEX,  -10.18903, -21.27436, 100.12885,
     VERTEX,   -9.70228, -20.78905,  99.45866,
     VERTEX,   -9.57555, -19.92233,  99.06581,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -10.64485, -19.79049, 100.18474,
                       
     VERTEX,   -9.57555, -19.92233,  99.06581,
     VERTEX,   -9.85727, -19.00525,  99.10036,
     VERTEX,  -10.43981, -18.38810,  99.54910,
     VERTEX,  -11.10067, -18.30661, 100.24063,
     VERTEX,  -11.58742, -18.79192, 100.91082,
     VERTEX,  -11.71414, -19.65864, 101.30367,
     VERTEX,  -11.43243, -20.57573, 101.26913,
     VERTEX,  -10.84989, -21.19287, 100.82039,
     VERTEX,  -10.18903, -21.27436, 100.12885,
     VERTEX,   -9.70228, -20.78905,  99.45866,
     VERTEX,   -9.57555, -19.92233,  99.06581,
                       
     END,              
                       
     CYLINDER,  -16.09100, -21.27400,  95.15500, -10.64485, -19.79049, 100.18474,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.50335,   9.55711, 112.65472,
                       
     VERTEX,    7.01335,   6.33057, 111.00748,
     VERTEX,    6.52731,   7.12243, 110.76596,
     VERTEX,    6.02449,   7.86190, 111.11520,
     VERTEX,    5.69697,   8.26653, 111.92179,
     VERTEX,    5.66984,   8.18178, 112.87766,
     VERTEX,    5.95347,   7.64001, 113.61768,
     VERTEX,    6.43951,   6.84816, 113.85921,
     VERTEX,    6.94232,   6.10869, 113.50997,
     VERTEX,    7.26984,   5.70405, 112.70338,
     VERTEX,    7.29697,   5.78880, 111.74751,
     VERTEX,    7.01335,   6.33057, 111.00748,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.48341,   6.98529, 112.31258,
                       
     VERTEX,    7.01335,   6.33057, 111.00748,
     VERTEX,    6.52731,   7.12243, 110.76596,
     VERTEX,    6.02449,   7.86190, 111.11520,
     VERTEX,    5.69697,   8.26653, 111.92179,
     VERTEX,    5.66984,   8.18178, 112.87766,
     VERTEX,    5.95347,   7.64001, 113.61768,
     VERTEX,    6.43951,   6.84816, 113.85921,
     VERTEX,    6.94232,   6.10869, 113.50997,
     VERTEX,    7.26984,   5.70405, 112.70338,
     VERTEX,    7.29697,   5.78880, 111.74751,
     VERTEX,    7.01335,   6.33057, 111.00748,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,   6.48341,   6.98529, 112.31258,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.10336,   3.06369, 114.23222,
                       
     VERTEX,    5.58658,  -0.02610, 112.00510,
     VERTEX,    5.13591,   0.79305, 111.78721,
     VERTEX,    4.61587,   1.51371, 112.15026,
     VERTEX,    4.22510,   1.86061, 112.95560,
     VERTEX,    4.11287,   1.70125, 113.89560,
     VERTEX,    4.32204,   1.09649, 114.61122,
     VERTEX,    4.77271,   0.27733, 114.82912,
     VERTEX,    5.29275,  -0.44333, 114.46606,
     VERTEX,    5.68352,  -0.79023, 113.66074,
     VERTEX,    5.79575,  -0.63086, 112.72073,
     VERTEX,    5.58658,  -0.02610, 112.00510,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    4.95431,   0.53519, 113.30817,
                       
     VERTEX,    5.58658,  -0.02610, 112.00510,
     VERTEX,    5.13591,   0.79305, 111.78721,
     VERTEX,    4.61587,   1.51371, 112.15026,
     VERTEX,    4.22510,   1.86061, 112.95560,
     VERTEX,    4.11287,   1.70125, 113.89560,
     VERTEX,    4.32204,   1.09649, 114.61122,
     VERTEX,    4.77271,   0.27733, 114.82912,
     VERTEX,    5.29275,  -0.44333, 114.46606,
     VERTEX,    5.68352,  -0.79023, 113.66074,
     VERTEX,    5.79575,  -0.63086, 112.72073,
     VERTEX,    5.58658,  -0.02610, 112.00510,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,   4.95431,   0.53519, 113.30817,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.78527,  -1.57524, 113.60706,
                       
     VERTEX,    7.38260,  -4.65167, 111.23096,
     VERTEX,    6.93407,  -3.83294, 111.00716,
     VERTEX,    6.39716,  -3.11983, 111.36047,
     VERTEX,    5.97697,  -2.78475, 112.15592,
     VERTEX,    5.83399,  -2.95567, 113.08971,
     VERTEX,    6.02283,  -3.56731, 113.80513,
     VERTEX,    6.47136,  -4.38605, 114.02893,
     VERTEX,    7.00826,  -5.09915, 113.67563,
     VERTEX,    7.42846,  -5.43424, 112.88017,
     VERTEX,    7.57144,  -5.26332, 111.94640,
     VERTEX,    7.38260,  -4.65167, 111.23096,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.70271,  -4.10949, 112.51805,
                       
     VERTEX,    7.38260,  -4.65167, 111.23096,
     VERTEX,    6.93407,  -3.83294, 111.00716,
     VERTEX,    6.39716,  -3.11983, 111.36047,
     VERTEX,    5.97697,  -2.78475, 112.15592,
     VERTEX,    5.83399,  -2.95567, 113.08971,
     VERTEX,    6.02283,  -3.56731, 113.80513,
     VERTEX,    6.47136,  -4.38605, 114.02893,
     VERTEX,    7.00826,  -5.09915, 113.67563,
     VERTEX,    7.42846,  -5.43424, 112.88017,
     VERTEX,    7.57144,  -5.26332, 111.94640,
     VERTEX,    7.38260,  -4.65167, 111.23096,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,   6.70271,  -4.10949, 112.51805,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.69591,  -4.90737, 110.17999,
                       
     VERTEX,   17.30643,  -8.24152, 108.44570,
     VERTEX,   16.81099,  -7.46260, 108.18224,
     VERTEX,   16.28095,  -6.73196, 108.50910,
     VERTEX,   15.91879,  -6.32869, 109.30145,
     VERTEX,   15.86283,  -6.40682, 110.25662,
     VERTEX,   16.13445,  -6.93651, 111.00979,
     VERTEX,   16.62990,  -7.71543, 111.27325,
     VERTEX,   17.15993,  -8.44606, 110.94639,
     VERTEX,   17.52209,  -8.84933, 110.15405,
     VERTEX,   17.57805,  -8.77120, 109.19887,
     VERTEX,   17.30643,  -8.24152, 108.44570,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.72044,  -7.58901, 109.72775,
                       
     VERTEX,   17.30643,  -8.24152, 108.44570,
     VERTEX,   16.81099,  -7.46260, 108.18224,
     VERTEX,   16.28095,  -6.73196, 108.50910,
     VERTEX,   15.91879,  -6.32869, 109.30145,
     VERTEX,   15.86283,  -6.40682, 110.25662,
     VERTEX,   16.13445,  -6.93651, 111.00979,
     VERTEX,   16.62990,  -7.71543, 111.27325,
     VERTEX,   17.15993,  -8.44606, 110.94639,
     VERTEX,   17.52209,  -8.84933, 110.15405,
     VERTEX,   17.57805,  -8.77120, 109.19887,
     VERTEX,   17.30643,  -8.24152, 108.44570,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  16.72044,  -7.58901, 109.72775,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -2.86941,  26.94913,  21.28499,
                       
     VERTEX,    2.17067,  28.32630,  25.39583,
     VERTEX,    1.79464,  29.20797,  25.44940,
     VERTEX,    1.70527,  30.04370,  24.98554,
     VERTEX,    1.93668,  30.51427,  24.18142,
     VERTEX,    2.40050,  30.43995,  23.34419,
     VERTEX,    2.91955,  29.84911,  22.79365,
     VERTEX,    3.29558,  28.96745,  22.74008,
     VERTEX,    3.38496,  28.13172,  23.20394,
     VERTEX,    3.15354,  27.66115,  24.00806,
     VERTEX,    2.68973,  27.73547,  24.84529,
     VERTEX,    2.17067,  28.32630,  25.39583,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    2.54511,  29.08771,  24.09474,
                       
     VERTEX,    2.17067,  28.32630,  25.39583,
     VERTEX,    1.79464,  29.20797,  25.44940,
     VERTEX,    1.70527,  30.04370,  24.98554,
     VERTEX,    1.93668,  30.51427,  24.18142,
     VERTEX,    2.40050,  30.43995,  23.34419,
     VERTEX,    2.91955,  29.84911,  22.79365,
     VERTEX,    3.29558,  28.96745,  22.74008,
     VERTEX,    3.38496,  28.13172,  23.20394,
     VERTEX,    3.15354,  27.66115,  24.00806,
     VERTEX,    2.68973,  27.73547,  24.84529,
     VERTEX,    2.17067,  28.32630,  25.39583,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,   2.54511,  29.08771,  24.09474,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.17259,  44.87510,  34.59138,
                       
     VERTEX,   25.86963,  44.18796,  41.02368,
     VERTEX,   26.50709,  44.80156,  40.65120,
     VERTEX,   27.24822,  44.87934,  40.04599,
     VERTEX,   27.80993,  44.39159,  39.43921,
     VERTEX,   27.97766,  43.52460,  39.06263,
     VERTEX,   27.68736,  42.60955,  39.06010,
     VERTEX,   27.04990,  41.99595,  39.43258,
     VERTEX,   26.30877,  41.91818,  40.03780,
     VERTEX,   25.74706,  42.40593,  40.64457,
     VERTEX,   25.57933,  43.27291,  41.02115,
     VERTEX,   25.86963,  44.18796,  41.02368,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.77849,  43.39876,  40.04189,
                       
     VERTEX,   25.86963,  44.18796,  41.02368,
     VERTEX,   26.50709,  44.80156,  40.65120,
     VERTEX,   27.24822,  44.87934,  40.04599,
     VERTEX,   27.80993,  44.39159,  39.43921,
     VERTEX,   27.97766,  43.52460,  39.06263,
     VERTEX,   27.68736,  42.60955,  39.06010,
     VERTEX,   27.04990,  41.99595,  39.43258,
     VERTEX,   26.30877,  41.91818,  40.03780,
     VERTEX,   25.74706,  42.40593,  40.64457,
     VERTEX,   25.57933,  43.27291,  41.02115,
     VERTEX,   25.86963,  44.18796,  41.02368,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  26.77849,  43.39876,  40.04189,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.34635,  46.64447,  36.82721,
                       
     VERTEX,   11.32610,  46.53621,  42.62217,
     VERTEX,   11.59479,  47.42400,  42.37471,
     VERTEX,   12.16171,  47.92832,  41.78662,
     VERTEX,   12.81031,  47.85655,  41.08252,
     VERTEX,   13.29286,  47.23609,  40.53135,
     VERTEX,   13.42503,  46.30394,  40.34365,
     VERTEX,   13.15634,  45.41616,  40.59111,
     VERTEX,   12.58942,  44.91183,  41.17921,
     VERTEX,   11.94081,  44.98360,  41.88331,
     VERTEX,   11.45827,  45.60406,  42.43447,
     VERTEX,   11.32610,  46.53621,  42.62217,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.37556,  46.42007,  41.48291,
                       
     VERTEX,   11.32610,  46.53621,  42.62217,
     VERTEX,   11.59479,  47.42400,  42.37471,
     VERTEX,   12.16171,  47.92832,  41.78662,
     VERTEX,   12.81031,  47.85655,  41.08252,
     VERTEX,   13.29286,  47.23609,  40.53135,
     VERTEX,   13.42503,  46.30394,  40.34365,
     VERTEX,   13.15634,  45.41616,  40.59111,
     VERTEX,   12.58942,  44.91183,  41.17921,
     VERTEX,   11.94081,  44.98360,  41.88331,
     VERTEX,   11.45827,  45.60406,  42.43447,
     VERTEX,   11.32610,  46.53621,  42.62217,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  12.37556,  46.42007,  41.48291,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    0.34115,  42.75762,  25.88026,
                       
     VERTEX,    5.51884,  43.43880,  31.37056,
     VERTEX,    5.41199,  44.38749,  31.26969,
     VERTEX,    5.65314,  45.14306,  30.72880,
     VERTEX,    6.15018,  45.41690,  29.95448,
     VERTEX,    6.71325,  45.10442,  29.24251,
     VERTEX,    7.12728,  44.32498,  28.86482,
     VERTEX,    7.23413,  43.37629,  28.96569,
     VERTEX,    6.99298,  42.62072,  29.50659,
     VERTEX,    6.49594,  42.34688,  30.28091,
     VERTEX,    5.93287,  42.65936,  30.99288,
     VERTEX,    5.51884,  43.43880,  31.37056,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.32306,  43.88189,  30.11769,
                       
     VERTEX,    5.51884,  43.43880,  31.37056,
     VERTEX,    5.41199,  44.38749,  31.26969,
     VERTEX,    5.65314,  45.14306,  30.72880,
     VERTEX,    6.15018,  45.41690,  29.95448,
     VERTEX,    6.71325,  45.10442,  29.24251,
     VERTEX,    7.12728,  44.32498,  28.86482,
     VERTEX,    7.23413,  43.37629,  28.96569,
     VERTEX,    6.99298,  42.62072,  29.50659,
     VERTEX,    6.49594,  42.34688,  30.28091,
     VERTEX,    5.93287,  42.65936,  30.99288,
     VERTEX,    5.51884,  43.43880,  31.37056,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,   6.32306,  43.88189,  30.11769,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.35730,  29.74600,  19.42813,
                       
     VERTEX,   18.68613,  30.06384,  24.75620,
     VERTEX,   18.69550,  31.01190,  24.60555,
     VERTEX,   19.05315,  31.70607,  24.04714,
     VERTEX,   19.62246,  31.88121,  23.29428,
     VERTEX,   20.18599,  31.47041,  22.63452,
     VERTEX,   20.52848,  30.63058,  22.31987,
     VERTEX,   20.51911,  29.68253,  22.47053,
     VERTEX,   20.16147,  28.98836,  23.02893,
     VERTEX,   19.59215,  28.81322,  23.78180,
     VERTEX,   19.02862,  29.22402,  24.44156,
     VERTEX,   18.68613,  30.06384,  24.75620,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.60731,  30.34722,  23.53804,
                       
     VERTEX,   18.68613,  30.06384,  24.75620,
     VERTEX,   18.69550,  31.01190,  24.60555,
     VERTEX,   19.05315,  31.70607,  24.04714,
     VERTEX,   19.62246,  31.88121,  23.29428,
     VERTEX,   20.18599,  31.47041,  22.63452,
     VERTEX,   20.52848,  30.63058,  22.31987,
     VERTEX,   20.51911,  29.68253,  22.47053,
     VERTEX,   20.16147,  28.98836,  23.02893,
     VERTEX,   19.59215,  28.81322,  23.78180,
     VERTEX,   19.02862,  29.22402,  24.44156,
     VERTEX,   18.68613,  30.06384,  24.75620,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  19.60731,  30.34722,  23.53804,   0.80000,
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
                       
     SPHERE,   39.37100, -64.31900, 120.71000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   41.09400, -58.60500, 123.56100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   39.21000, -53.96500, 124.67200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   64.06000, -69.74500, 116.64100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   29.02900, -43.98700, 126.93700,   0.80000,
                       
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