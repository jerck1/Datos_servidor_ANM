from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -3.38139, -64.49577,  56.22631,
                       
     VERTEX,    0.76911, -66.55887,  55.38964,
     VERTEX,    0.82675, -65.92729,  54.66896,
     VERTEX,    0.47475, -65.70036,  53.80513,
     VERTEX,   -0.15242, -65.96474,  53.12811,
     VERTEX,   -0.81521, -66.61946,  52.89650,
     VERTEX,   -1.26047, -67.41444,  53.19876,
     VERTEX,   -1.31811, -68.04601,  53.91945,
     VERTEX,   -0.96611, -68.27295,  54.78328,
     VERTEX,   -0.33894, -68.00856,  55.46030,
     VERTEX,    0.32385, -67.35384,  55.69191,
     VERTEX,    0.76911, -66.55887,  55.38964,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.24568, -66.98666,  54.29420,
                       
     VERTEX,    0.76911, -66.55887,  55.38964,
     VERTEX,    0.82675, -65.92729,  54.66896,
     VERTEX,    0.47475, -65.70036,  53.80513,
     VERTEX,   -0.15242, -65.96474,  53.12811,
     VERTEX,   -0.81521, -66.61946,  52.89650,
     VERTEX,   -1.26047, -67.41444,  53.19876,
     VERTEX,   -1.31811, -68.04601,  53.91945,
     VERTEX,   -0.96611, -68.27295,  54.78328,
     VERTEX,   -0.33894, -68.00856,  55.46030,
     VERTEX,    0.32385, -67.35384,  55.69191,
     VERTEX,    0.76911, -66.55887,  55.38964,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,  -0.24568, -66.98666,  54.29420,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.07534, -74.43750,  50.00151,
                       
     VERTEX,   13.56293, -74.79221,  49.67024,
     VERTEX,   13.50295, -73.90781,  49.30169,
     VERTEX,   13.21756, -73.40292,  48.53668,
     VERTEX,   12.81577, -73.47041,  47.66742,
     VERTEX,   12.45105, -74.08447,  47.02594,
     VERTEX,   12.26271, -75.01058,  46.85726,
     VERTEX,   12.32269, -75.89499,  47.22581,
     VERTEX,   12.60809, -76.39987,  47.99083,
     VERTEX,   13.00988, -76.33240,  48.86008,
     VERTEX,   13.37460, -75.71832,  49.50156,
     VERTEX,   13.56293, -74.79221,  49.67024,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.91282, -74.90140,  48.26375,
                       
     VERTEX,   13.56293, -74.79221,  49.67024,
     VERTEX,   13.50295, -73.90781,  49.30169,
     VERTEX,   13.21756, -73.40292,  48.53668,
     VERTEX,   12.81577, -73.47041,  47.66742,
     VERTEX,   12.45105, -74.08447,  47.02594,
     VERTEX,   12.26271, -75.01058,  46.85726,
     VERTEX,   12.32269, -75.89499,  47.22581,
     VERTEX,   12.60809, -76.39987,  47.99083,
     VERTEX,   13.00988, -76.33240,  48.86008,
     VERTEX,   13.37460, -75.71832,  49.50156,
     VERTEX,   13.56293, -74.79221,  49.67024,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  12.91282, -74.90140,  48.26375,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   54.57052, -21.70127,  83.99245,
                       
     VERTEX,   49.67677, -20.85170,  83.98012,
     VERTEX,   49.91617, -20.00932,  84.37343,
     VERTEX,   50.23360, -19.58922,  85.17615,
     VERTEX,   50.50779, -19.75186,  86.08167,
     VERTEX,   50.63402, -20.43512,  86.74411,
     VERTEX,   50.56407, -21.37800,  86.91045,
     VERTEX,   50.32466, -22.22038,  86.51714,
     VERTEX,   50.00724, -22.64048,  85.71442,
     VERTEX,   49.73305, -22.47784,  84.80889,
     VERTEX,   49.60682, -21.79459,  84.14645,
     VERTEX,   49.67677, -20.85170,  83.98012,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   50.12042, -21.11485,  85.44528,
                       
     VERTEX,   49.67677, -20.85170,  83.98012,
     VERTEX,   49.91617, -20.00932,  84.37343,
     VERTEX,   50.23360, -19.58922,  85.17615,
     VERTEX,   50.50779, -19.75186,  86.08167,
     VERTEX,   50.63402, -20.43512,  86.74411,
     VERTEX,   50.56407, -21.37800,  86.91045,
     VERTEX,   50.32466, -22.22038,  86.51714,
     VERTEX,   50.00724, -22.64048,  85.71442,
     VERTEX,   49.73305, -22.47784,  84.80889,
     VERTEX,   49.60682, -21.79459,  84.14645,
     VERTEX,   49.67677, -20.85170,  83.98012,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  50.12042, -21.11485,  85.44528,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.37704, -18.97972,  77.47413,
                       
     VERTEX,   44.62927, -18.64848,  77.30610,
     VERTEX,   44.77674, -17.75881,  77.63525,
     VERTEX,   45.03914, -17.24916,  78.40532,
     VERTEX,   45.31624, -17.31420,  79.32216,
     VERTEX,   45.50219, -17.92907,  80.03557,
     VERTEX,   45.52596, -18.85893,  80.27305,
     VERTEX,   45.37849, -19.74860,  79.94389,
     VERTEX,   45.11609, -20.25825,  79.17382,
     VERTEX,   44.83899, -20.19322,  78.25699,
     VERTEX,   44.65305, -19.57834,  77.54358,
     VERTEX,   44.62927, -18.64848,  77.30610,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.07761, -18.75371,  78.78957,
                       
     VERTEX,   44.62927, -18.64848,  77.30610,
     VERTEX,   44.77674, -17.75881,  77.63525,
     VERTEX,   45.03914, -17.24916,  78.40532,
     VERTEX,   45.31624, -17.31420,  79.32216,
     VERTEX,   45.50219, -17.92907,  80.03557,
     VERTEX,   45.52596, -18.85893,  80.27305,
     VERTEX,   45.37849, -19.74860,  79.94389,
     VERTEX,   45.11609, -20.25825,  79.17382,
     VERTEX,   44.83899, -20.19322,  78.25699,
     VERTEX,   44.65305, -19.57834,  77.54358,
     VERTEX,   44.62927, -18.64848,  77.30610,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  45.07761, -18.75371,  78.78957,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.71136, -19.19493,  81.06805,
                       
     VERTEX,   33.78790, -21.09607,  80.54774,
     VERTEX,   33.46914, -20.19073,  80.52907,
     VERTEX,   33.32573, -19.40663,  81.06408,
     VERTEX,   33.41246, -19.04329,  81.94842,
     VERTEX,   33.69620, -19.23947,  82.84430,
     VERTEX,   34.06857, -19.92025,  83.40953,
     VERTEX,   34.38733, -20.82559,  83.42821,
     VERTEX,   34.53073, -21.60968,  82.89320,
     VERTEX,   34.44400, -21.97303,  82.00886,
     VERTEX,   34.16026, -21.77685,  81.11298,
     VERTEX,   33.78790, -21.09607,  80.54774,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.92823, -20.50816,  81.97864,
                       
     VERTEX,   33.78790, -21.09607,  80.54774,
     VERTEX,   33.46914, -20.19073,  80.52907,
     VERTEX,   33.32573, -19.40663,  81.06408,
     VERTEX,   33.41246, -19.04329,  81.94842,
     VERTEX,   33.69620, -19.23947,  82.84430,
     VERTEX,   34.06857, -19.92025,  83.40953,
     VERTEX,   34.38733, -20.82559,  83.42821,
     VERTEX,   34.53073, -21.60968,  82.89320,
     VERTEX,   34.44400, -21.97303,  82.00886,
     VERTEX,   34.16026, -21.77685,  81.11298,
     VERTEX,   33.78790, -21.09607,  80.54774,
                       
     END,              
                       
     CYLINDER,   27.80700, -22.63300,  83.45200,  33.92823, -20.50816,  81.97864,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   64.46239, -91.91617,  98.10145,
                       
     VERTEX,   69.79849, -86.54073,  97.88564,
     VERTEX,   69.21954, -86.02888,  98.45522,
     VERTEX,   68.43578, -85.47470,  98.46955,
     VERTEX,   67.74658, -85.08988,  97.92318,
     VERTEX,   67.41519, -85.02142,  97.02480,
     VERTEX,   67.56820, -85.29545,  96.11755,
     VERTEX,   68.14716, -85.80731,  95.54797,
     VERTEX,   68.93092, -86.36149,  95.53364,
     VERTEX,   69.62012, -86.74630,  96.08001,
     VERTEX,   69.95150, -86.81477,  96.97840,
     VERTEX,   69.79849, -86.54073,  97.88564,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   68.68335, -85.91809,  97.00159,
                       
     VERTEX,   69.79849, -86.54073,  97.88564,
     VERTEX,   69.21954, -86.02888,  98.45522,
     VERTEX,   68.43578, -85.47470,  98.46955,
     VERTEX,   67.74658, -85.08988,  97.92318,
     VERTEX,   67.41519, -85.02142,  97.02480,
     VERTEX,   67.56820, -85.29545,  96.11755,
     VERTEX,   68.14716, -85.80731,  95.54797,
     VERTEX,   68.93092, -86.36149,  95.53364,
     VERTEX,   69.62012, -86.74630,  96.08001,
     VERTEX,   69.95150, -86.81477,  96.97840,
     VERTEX,   69.79849, -86.54073,  97.88564,
                       
     END,              
                       
     CYLINDER,   75.51300, -76.21300,  95.22200,  68.68335, -85.91809,  97.00159,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   63.42018, -84.72269,  92.08188,
                       
     VERTEX,   67.80936, -79.68480,  92.06071,
     VERTEX,   67.23196, -79.27051,  92.70615,
     VERTEX,   66.40749, -78.79120,  92.81610,
     VERTEX,   65.65084, -78.42994,  92.34857,
     VERTEX,   65.25105, -78.32472,  91.48215,
     VERTEX,   65.36080, -78.51575,  90.54777,
     VERTEX,   65.93819, -78.93003,  89.90234,
     VERTEX,   66.76268, -79.40935,  89.79238,
     VERTEX,   67.51932, -79.77061,  90.25991,
     VERTEX,   67.91912, -79.87582,  91.12634,
     VERTEX,   67.80936, -79.68480,  92.06071,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   66.58508, -79.10027,  91.30424,
                       
     VERTEX,   67.80936, -79.68480,  92.06071,
     VERTEX,   67.23196, -79.27051,  92.70615,
     VERTEX,   66.40749, -78.79120,  92.81610,
     VERTEX,   65.65084, -78.42994,  92.34857,
     VERTEX,   65.25105, -78.32472,  91.48215,
     VERTEX,   65.36080, -78.51575,  90.54777,
     VERTEX,   65.93819, -78.93003,  89.90234,
     VERTEX,   66.76268, -79.40935,  89.79238,
     VERTEX,   67.51932, -79.77061,  90.25991,
     VERTEX,   67.91912, -79.87582,  91.12634,
     VERTEX,   67.80936, -79.68480,  92.06071,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  66.58508, -79.10027,  91.30424,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.67603, -95.02058,  97.39896,
                       
     VERTEX,   55.18102, -91.57039,  96.87325,
     VERTEX,   54.71160, -90.77775,  97.14338,
     VERTEX,   54.13008, -90.07751,  96.83826,
     VERTEX,   53.65858, -89.73713,  96.07443,
     VERTEX,   53.47720, -89.88663,  95.14365,
     VERTEX,   53.65521, -90.46891,  94.40145,
     VERTEX,   54.12463, -91.26155,  94.13132,
     VERTEX,   54.70615, -91.96179,  94.43644,
     VERTEX,   55.17765, -92.30216,  95.20026,
     VERTEX,   55.35903, -92.15266,  96.13104,
     VERTEX,   55.18102, -91.57039,  96.87325,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   54.41811, -91.01965,  95.63735,
                       
     VERTEX,   55.18102, -91.57039,  96.87325,
     VERTEX,   54.71160, -90.77775,  97.14338,
     VERTEX,   54.13008, -90.07751,  96.83826,
     VERTEX,   53.65858, -89.73713,  96.07443,
     VERTEX,   53.47720, -89.88663,  95.14365,
     VERTEX,   53.65521, -90.46891,  94.40145,
     VERTEX,   54.12463, -91.26155,  94.13132,
     VERTEX,   54.70615, -91.96179,  94.43644,
     VERTEX,   55.17765, -92.30216,  95.20026,
     VERTEX,   55.35903, -92.15266,  96.13104,
     VERTEX,   55.18102, -91.57039,  96.87325,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  54.41811, -91.01965,  95.63735,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.83092, -95.04671, 102.64393,
                       
     VERTEX,   52.48123, -92.21185, 102.04177,
     VERTEX,   52.06676, -91.36436, 102.21947,
     VERTEX,   51.54834, -90.65647, 101.82996,
     VERTEX,   51.12397, -90.35856, 101.02203,
     VERTEX,   50.95575, -90.58443, 100.10427,
     VERTEX,   51.10793, -91.24781,  99.42724,
     VERTEX,   51.52240, -92.09530,  99.24953,
     VERTEX,   52.04083, -92.80319,  99.63905,
     VERTEX,   52.46520, -93.10110, 100.44698,
     VERTEX,   52.63342, -92.87523, 101.36474,
     VERTEX,   52.48123, -92.21185, 102.04177,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   51.79458, -91.72984, 100.73450,
                       
     VERTEX,   52.48123, -92.21185, 102.04177,
     VERTEX,   52.06676, -91.36436, 102.21947,
     VERTEX,   51.54834, -90.65647, 101.82996,
     VERTEX,   51.12397, -90.35856, 101.02203,
     VERTEX,   50.95575, -90.58443, 100.10427,
     VERTEX,   51.10793, -91.24781,  99.42724,
     VERTEX,   51.52240, -92.09530,  99.24953,
     VERTEX,   52.04083, -92.80319,  99.63905,
     VERTEX,   52.46520, -93.10110, 100.44698,
     VERTEX,   52.63342, -92.87523, 101.36474,
     VERTEX,   52.48123, -92.21185, 102.04177,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  51.79458, -91.72984, 100.73450,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.80937, -94.14193, 109.56113,
                       
     VERTEX,   49.48784, -92.07692, 108.88008,
     VERTEX,   49.14830, -91.18118, 108.94309,
     VERTEX,   48.70242, -90.48363, 108.45708,
     VERTEX,   48.32050, -90.25072, 107.60767,
     VERTEX,   48.14842, -90.57139, 106.71932,
     VERTEX,   48.25192, -91.32317, 106.13136,
     VERTEX,   48.59146, -92.21892, 106.06835,
     VERTEX,   49.03735, -92.91646, 106.55437,
     VERTEX,   49.41927, -93.14938, 107.40377,
     VERTEX,   49.59134, -92.82870, 108.29211,
     VERTEX,   49.48784, -92.07692, 108.88008,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.86988, -91.70004, 107.50572,
                       
     VERTEX,   49.48784, -92.07692, 108.88008,
     VERTEX,   49.14830, -91.18118, 108.94309,
     VERTEX,   48.70242, -90.48363, 108.45708,
     VERTEX,   48.32050, -90.25072, 107.60767,
     VERTEX,   48.14842, -90.57139, 106.71932,
     VERTEX,   48.25192, -91.32317, 106.13136,
     VERTEX,   48.59146, -92.21892, 106.06835,
     VERTEX,   49.03735, -92.91646, 106.55437,
     VERTEX,   49.41927, -93.14938, 107.40377,
     VERTEX,   49.59134, -92.82870, 108.29211,
     VERTEX,   49.48784, -92.07692, 108.88008,
                       
     END,              
                       
     CYLINDER,   58.67600, -87.74900, 104.18000,  48.86988, -91.70004, 107.50572,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -43.11951,  10.56235,  93.86429,
                       
     VERTEX,  -39.21231,  15.38120,  94.68937,
     VERTEX,  -39.81906,  15.65940,  95.37934,
     VERTEX,  -40.67036,  16.07086,  95.54543,
     VERTEX,  -41.44104,  16.45842,  95.12419,
     VERTEX,  -41.83674,  16.67405,  94.27653,
     VERTEX,  -41.70630,  16.63537,  93.32622,
     VERTEX,  -41.09956,  16.35717,  92.63625,
     VERTEX,  -40.24825,  15.94571,  92.47016,
     VERTEX,  -39.47757,  15.55815,  92.89140,
     VERTEX,  -39.08187,  15.34252,  93.73906,
     VERTEX,  -39.21231,  15.38120,  94.68937,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -40.45930,  16.00829,  94.00780,
                       
     VERTEX,  -39.21231,  15.38120,  94.68937,
     VERTEX,  -39.81906,  15.65940,  95.37934,
     VERTEX,  -40.67036,  16.07086,  95.54543,
     VERTEX,  -41.44104,  16.45842,  95.12419,
     VERTEX,  -41.83674,  16.67405,  94.27653,
     VERTEX,  -41.70630,  16.63537,  93.32622,
     VERTEX,  -41.09956,  16.35717,  92.63625,
     VERTEX,  -40.24825,  15.94571,  92.47016,
     VERTEX,  -39.47757,  15.55815,  92.89140,
     VERTEX,  -39.08187,  15.34252,  93.73906,
     VERTEX,  -39.21231,  15.38120,  94.68937,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -40.45930,  16.00829,  94.00780,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -38.03341,   8.76139,  86.45140,
                       
     VERTEX,  -34.58820,  13.03910,  87.23205,
     VERTEX,  -35.18235,  13.27947,  87.94676,
     VERTEX,  -36.04301,  13.65379,  88.14860,
     VERTEX,  -36.84146,  14.01908,  87.76046,
     VERTEX,  -37.27270,  14.23582,  86.93061,
     VERTEX,  -37.17202,  14.22122,  85.97601,
     VERTEX,  -36.57787,  13.98085,  85.26130,
     VERTEX,  -35.71720,  13.60653,  85.05946,
     VERTEX,  -34.91876,  13.24124,  85.44760,
     VERTEX,  -34.48752,  13.02450,  86.27746,
     VERTEX,  -34.58820,  13.03910,  87.23205,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -35.88011,  13.63016,  86.60403,
                       
     VERTEX,  -34.58820,  13.03910,  87.23205,
     VERTEX,  -35.18235,  13.27947,  87.94676,
     VERTEX,  -36.04301,  13.65379,  88.14860,
     VERTEX,  -36.84146,  14.01908,  87.76046,
     VERTEX,  -37.27270,  14.23582,  86.93061,
     VERTEX,  -37.17202,  14.22122,  85.97601,
     VERTEX,  -36.57787,  13.98085,  85.26130,
     VERTEX,  -35.71720,  13.60653,  85.05946,
     VERTEX,  -34.91876,  13.24124,  85.44760,
     VERTEX,  -34.48752,  13.02450,  86.27746,
     VERTEX,  -34.58820,  13.03910,  87.23205,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -35.88011,  13.63016,  86.60403,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -34.38700,  14.03785,  85.38402,
                       
     VERTEX,  -30.65516,  17.42518,  86.36636,
     VERTEX,  -31.28996,  17.81242,  86.97354,
     VERTEX,  -32.09694,  18.32954,  87.02800,
     VERTEX,  -32.76787,  18.77901,  86.50893,
     VERTEX,  -33.04647,  18.98916,  85.61460,
     VERTEX,  -32.82632,  18.87971,  84.68661,
     VERTEX,  -32.19152,  18.49246,  84.07943,
     VERTEX,  -31.38454,  17.97534,  84.02498,
     VERTEX,  -30.71361,  17.52587,  84.54404,
     VERTEX,  -30.43501,  17.31573,  85.43837,
     VERTEX,  -30.65516,  17.42518,  86.36636,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.74074,  18.15244,  85.52649,
                       
     VERTEX,  -30.65516,  17.42518,  86.36636,
     VERTEX,  -31.28996,  17.81242,  86.97354,
     VERTEX,  -32.09694,  18.32954,  87.02800,
     VERTEX,  -32.76787,  18.77901,  86.50893,
     VERTEX,  -33.04647,  18.98916,  85.61460,
     VERTEX,  -32.82632,  18.87971,  84.68661,
     VERTEX,  -32.19152,  18.49246,  84.07943,
     VERTEX,  -31.38454,  17.97534,  84.02498,
     VERTEX,  -30.71361,  17.52587,  84.54404,
     VERTEX,  -30.43501,  17.31573,  85.43837,
     VERTEX,  -30.65516,  17.42518,  86.36636,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -31.74074,  18.15244,  85.52649,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -34.53535,  23.65796,  95.42963,
                       
     VERTEX,  -29.91257,  26.56366,  96.65693,
     VERTEX,  -30.51413,  27.18804,  97.06909,
     VERTEX,  -31.16053,  27.87561,  96.89302,
     VERTEX,  -31.60488,  28.36376,  96.19598,
     VERTEX,  -31.67743,  28.46602,  95.24419,
     VERTEX,  -31.35049,  28.14333,  94.40124,
     VERTEX,  -30.74892,  27.51896,  93.98907,
     VERTEX,  -30.10252,  26.83138,  94.16515,
     VERTEX,  -29.65818,  26.34323,  94.86219,
     VERTEX,  -29.58562,  26.24097,  95.81397,
     VERTEX,  -29.91257,  26.56366,  96.65693,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -30.63153,  27.35350,  95.52908,
                       
     VERTEX,  -29.91257,  26.56366,  96.65693,
     VERTEX,  -30.51413,  27.18804,  97.06909,
     VERTEX,  -31.16053,  27.87561,  96.89302,
     VERTEX,  -31.60488,  28.36376,  96.19598,
     VERTEX,  -31.67743,  28.46602,  95.24419,
     VERTEX,  -31.35049,  28.14333,  94.40124,
     VERTEX,  -30.74892,  27.51896,  93.98907,
     VERTEX,  -30.10252,  26.83138,  94.16515,
     VERTEX,  -29.65818,  26.34323,  94.86219,
     VERTEX,  -29.58562,  26.24097,  95.81397,
     VERTEX,  -29.91257,  26.56366,  96.65693,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -30.63153,  27.35350,  95.52908,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -34.63267,  20.81899, 100.84293,
                       
     VERTEX,  -30.26326,  23.90626, 101.99497,
     VERTEX,  -30.88620,  24.46157, 102.46950,
     VERTEX,  -31.58963,  25.10612, 102.36301,
     VERTEX,  -32.10487,  25.59370, 101.71618,
     VERTEX,  -32.23512,  25.73808, 100.77608,
     VERTEX,  -31.93062,  25.48411,  99.90179,
     VERTEX,  -31.30768,  24.92879,  99.42727,
     VERTEX,  -30.60424,  24.28425,  99.53376,
     VERTEX,  -30.08900,  23.79667, 100.18059,
     VERTEX,  -29.95876,  23.65228, 101.12069,
     VERTEX,  -30.26326,  23.90626, 101.99497,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.09694,  24.69518, 100.94839,
                       
     VERTEX,  -30.26326,  23.90626, 101.99497,
     VERTEX,  -30.88620,  24.46157, 102.46950,
     VERTEX,  -31.58963,  25.10612, 102.36301,
     VERTEX,  -32.10487,  25.59370, 101.71618,
     VERTEX,  -32.23512,  25.73808, 100.77608,
     VERTEX,  -31.93062,  25.48411,  99.90179,
     VERTEX,  -31.30768,  24.92879,  99.42727,
     VERTEX,  -30.60424,  24.28425,  99.53376,
     VERTEX,  -30.08900,  23.79667, 100.18059,
     VERTEX,  -29.95876,  23.65228, 101.12069,
     VERTEX,  -30.26326,  23.90626, 101.99497,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -31.09694,  24.69518, 100.94839,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.25868,  53.00621,  49.11932,
                       
     VERTEX,   27.62172,  49.18888,  50.11779,
     VERTEX,   27.92038,  49.50538,  49.26209,
     VERTEX,   27.80321,  49.40886,  48.31417,
     VERTEX,   27.31495,  48.93617,  47.63610,
     VERTEX,   26.64211,  48.26788,  47.48689,
     VERTEX,   26.04168,  47.65924,  47.92352,
     VERTEX,   25.74301,  47.34274,  48.77922,
     VERTEX,   25.86018,  47.43927,  49.72714,
     VERTEX,   26.34844,  47.91195,  50.40521,
     VERTEX,   27.02129,  48.58025,  50.55442,
     VERTEX,   27.62172,  49.18888,  50.11779,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.83170,  48.42406,  49.02065,
                       
     VERTEX,   27.62172,  49.18888,  50.11779,
     VERTEX,   27.92038,  49.50538,  49.26209,
     VERTEX,   27.80321,  49.40886,  48.31417,
     VERTEX,   27.31495,  48.93617,  47.63610,
     VERTEX,   26.64211,  48.26788,  47.48689,
     VERTEX,   26.04168,  47.65924,  47.92352,
     VERTEX,   25.74301,  47.34274,  48.77922,
     VERTEX,   25.86018,  47.43927,  49.72714,
     VERTEX,   26.34844,  47.91195,  50.40521,
     VERTEX,   27.02129,  48.58025,  50.55442,
     VERTEX,   27.62172,  49.18888,  50.11779,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  26.83170,  48.42406,  49.02065,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.80597,  46.11039,  55.18816,
                       
     VERTEX,   26.45809,  42.63736,  56.14269,
     VERTEX,   26.73829,  42.90386,  55.26401,
     VERTEX,   26.57744,  42.77796,  54.32600,
     VERTEX,   26.03699,  42.30774,  53.68692,
     VERTEX,   25.32337,  41.67282,  53.59091,
     VERTEX,   24.70916,  41.11571,  54.07462,
     VERTEX,   24.42896,  40.84921,  54.95329,
     VERTEX,   24.58981,  40.97511,  55.89131,
     VERTEX,   25.13026,  41.44532,  56.53038,
     VERTEX,   25.84388,  42.08025,  56.62640,
     VERTEX,   26.45809,  42.63736,  56.14269,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.58363,  41.87653,  55.10865,
                       
     VERTEX,   26.45809,  42.63736,  56.14269,
     VERTEX,   26.73829,  42.90386,  55.26401,
     VERTEX,   26.57744,  42.77796,  54.32600,
     VERTEX,   26.03699,  42.30774,  53.68692,
     VERTEX,   25.32337,  41.67282,  53.59091,
     VERTEX,   24.70916,  41.11571,  54.07462,
     VERTEX,   24.42896,  40.84921,  54.95329,
     VERTEX,   24.58981,  40.97511,  55.89131,
     VERTEX,   25.13026,  41.44532,  56.53038,
     VERTEX,   25.84388,  42.08025,  56.62640,
     VERTEX,   26.45809,  42.63736,  56.14269,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  25.58363,  41.87653,  55.10865,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.62533,  45.41626,  56.63822,
                       
     VERTEX,   20.28097,  42.76234,  57.80396,
     VERTEX,   20.60489,  43.14448,  56.98503,
     VERTEX,   20.55341,  43.08839,  56.02805,
     VERTEX,   20.14620,  42.61550,  55.29856,
     VERTEX,   19.53881,  41.90643,  55.07520,
     VERTEX,   18.96323,  41.23203,  55.44328,
     VERTEX,   18.63931,  40.84988,  56.26221,
     VERTEX,   18.69079,  40.90597,  57.21919,
     VERTEX,   19.09800,  41.37887,  57.94868,
     VERTEX,   19.70539,  42.08794,  58.17204,
     VERTEX,   20.28097,  42.76234,  57.80396,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.62210,  41.99718,  56.62362,
                       
     VERTEX,   20.28097,  42.76234,  57.80396,
     VERTEX,   20.60489,  43.14448,  56.98503,
     VERTEX,   20.55341,  43.08839,  56.02805,
     VERTEX,   20.14620,  42.61550,  55.29856,
     VERTEX,   19.53881,  41.90643,  55.07520,
     VERTEX,   18.96323,  41.23203,  55.44328,
     VERTEX,   18.63931,  40.84988,  56.26221,
     VERTEX,   18.69079,  40.90597,  57.21919,
     VERTEX,   19.09800,  41.37887,  57.94868,
     VERTEX,   19.70539,  42.08794,  58.17204,
     VERTEX,   20.28097,  42.76234,  57.80396,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  19.62210,  41.99718,  56.62362,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.72217,  52.97545,  48.93307,
                       
     VERTEX,   12.29545,  50.95875,  50.35313,
     VERTEX,   12.60498,  51.56766,  49.67857,
     VERTEX,   12.67953,  51.70491,  48.73137,
     VERTEX,   12.49063,  51.31807,  47.87330,
     VERTEX,   12.11042,  50.55491,  47.43213,
     VERTEX,   11.68415,  49.70692,  47.57637,
     VERTEX,   11.37462,  49.09801,  48.25093,
     VERTEX,   11.30007,  48.96076,  49.19814,
     VERTEX,   11.48897,  49.34760,  50.05620,
     VERTEX,   11.86918,  50.11076,  50.49737,
     VERTEX,   12.29545,  50.95875,  50.35313,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.98980,  50.33284,  48.96475,
                       
     VERTEX,   12.29545,  50.95875,  50.35313,
     VERTEX,   12.60498,  51.56766,  49.67857,
     VERTEX,   12.67953,  51.70491,  48.73137,
     VERTEX,   12.49063,  51.31807,  47.87330,
     VERTEX,   12.11042,  50.55491,  47.43213,
     VERTEX,   11.68415,  49.70692,  47.57637,
     VERTEX,   11.37462,  49.09801,  48.25093,
     VERTEX,   11.30007,  48.96076,  49.19814,
     VERTEX,   11.48897,  49.34760,  50.05620,
     VERTEX,   11.86918,  50.11076,  50.49737,
     VERTEX,   12.29545,  50.95875,  50.35313,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  11.98980,  50.33284,  48.96475,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.66622,  53.07902,  43.20034,
                       
     VERTEX,   14.15451,  50.87144,  44.56597,
     VERTEX,   14.47423,  51.43866,  43.86053,
     VERTEX,   14.53064,  51.53558,  42.90710,
     VERTEX,   14.30219,  51.12517,  42.06986,
     VERTEX,   13.87613,  50.36420,  41.66860,
     VERTEX,   13.41522,  49.54334,  41.85660,
     VERTEX,   13.09549,  48.97612,  42.56203,
     VERTEX,   13.03908,  48.87921,  43.51546,
     VERTEX,   13.26754,  49.28962,  44.35271,
     VERTEX,   13.69359,  50.05058,  44.75396,
     VERTEX,   14.15451,  50.87144,  44.56597,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.78486,  50.20739,  43.21128,
                       
     VERTEX,   14.15451,  50.87144,  44.56597,
     VERTEX,   14.47423,  51.43866,  43.86053,
     VERTEX,   14.53064,  51.53558,  42.90710,
     VERTEX,   14.30219,  51.12517,  42.06986,
     VERTEX,   13.87613,  50.36420,  41.66860,
     VERTEX,   13.41522,  49.54334,  41.85660,
     VERTEX,   13.09549,  48.97612,  42.56203,
     VERTEX,   13.03908,  48.87921,  43.51546,
     VERTEX,   13.26754,  49.28962,  44.35271,
     VERTEX,   13.69359,  50.05058,  44.75396,
     VERTEX,   14.15451,  50.87144,  44.56597,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  13.78486,  50.20739,  43.21128,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00002_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    4.82800, -71.01700,  51.16800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   19.12200, -75.65200,  45.45200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   42.92000, -20.16600,  87.79600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   38.12100, -18.38800,  80.91800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   27.80700, -22.63300,  83.45200,   0.80000,
                       
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