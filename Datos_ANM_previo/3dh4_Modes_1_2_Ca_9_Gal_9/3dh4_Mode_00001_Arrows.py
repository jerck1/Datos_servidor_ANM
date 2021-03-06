from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.18785, -63.63713,  35.80921,
                       
     VERTEX,   21.58376, -60.80602,  35.98687,
     VERTEX,   21.08691, -60.04050,  36.28474,
     VERTEX,   20.50241, -59.33466,  35.99884,
     VERTEX,   20.05351, -58.95808,  35.23839,
     VERTEX,   19.91169, -59.05463,  34.29384,
     VERTEX,   20.13112, -59.58741,  33.52599,
     VERTEX,   20.62797, -60.35293,  33.22813,
     VERTEX,   21.21247, -61.05877,  33.51402,
     VERTEX,   21.66137, -61.43534,  34.27448,
     VERTEX,   21.80319, -61.33880,  35.21902,
     VERTEX,   21.58376, -60.80602,  35.98687,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.85744, -60.19672,  34.75643,
                       
     VERTEX,   21.58376, -60.80602,  35.98687,
     VERTEX,   21.08691, -60.04050,  36.28474,
     VERTEX,   20.50241, -59.33466,  35.99884,
     VERTEX,   20.05351, -58.95808,  35.23839,
     VERTEX,   19.91169, -59.05463,  34.29384,
     VERTEX,   20.13112, -59.58741,  33.52599,
     VERTEX,   20.62797, -60.35293,  33.22813,
     VERTEX,   21.21247, -61.05877,  33.51402,
     VERTEX,   21.66137, -61.43534,  34.27448,
     VERTEX,   21.80319, -61.33880,  35.21902,
     VERTEX,   21.58376, -60.80602,  35.98687,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  20.85744, -60.19672,  34.75643,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -4.55766, -75.93169,  59.15056,
                       
     VERTEX,    0.44592, -74.23965,  55.60354,
     VERTEX,    0.11631, -73.34280,  55.69633,
     VERTEX,   -0.55133, -72.72506,  55.38932,
     VERTEX,   -1.30200, -72.62240,  54.79977,
     VERTEX,   -1.84896, -73.07403,  54.15289,
     VERTEX,   -1.98329, -73.90744,  53.69574,
     VERTEX,   -1.65368, -74.80430,  53.60295,
     VERTEX,   -0.98604, -75.42203,  53.90996,
     VERTEX,   -0.23538, -75.52469,  54.49950,
     VERTEX,    0.31158, -75.07306,  55.14640,
     VERTEX,    0.44592, -74.23965,  55.60354,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.76869, -74.07355,  54.64964,
                       
     VERTEX,    0.44592, -74.23965,  55.60354,
     VERTEX,    0.11631, -73.34280,  55.69633,
     VERTEX,   -0.55133, -72.72506,  55.38932,
     VERTEX,   -1.30200, -72.62240,  54.79977,
     VERTEX,   -1.84896, -73.07403,  54.15289,
     VERTEX,   -1.98329, -73.90744,  53.69574,
     VERTEX,   -1.65368, -74.80430,  53.60295,
     VERTEX,   -0.98604, -75.42203,  53.90996,
     VERTEX,   -0.23538, -75.52469,  54.49950,
     VERTEX,    0.31158, -75.07306,  55.14640,
     VERTEX,    0.44592, -74.23965,  55.60354,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  -0.76869, -74.07355,  54.64964,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.47851, -81.69600,  54.74851,
                       
     VERTEX,   13.63314, -79.65096,  52.27320,
     VERTEX,   13.27020, -78.77558,  52.42680,
     VERTEX,   12.62987, -78.13390,  52.11087,
     VERTEX,   11.95672, -77.97101,  51.44608,
     VERTEX,   11.50788, -78.34913,  50.68637,
     VERTEX,   11.45478, -79.12383,  50.12192,
     VERTEX,   11.81771, -79.99921,  49.96832,
     VERTEX,   12.45805, -80.64090,  50.28425,
     VERTEX,   13.13120, -80.80379,  50.94903,
     VERTEX,   13.58004, -80.42567,  51.70874,
     VERTEX,   13.63314, -79.65096,  52.27320,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.54396, -79.38740,  51.19756,
                       
     VERTEX,   13.63314, -79.65096,  52.27320,
     VERTEX,   13.27020, -78.77558,  52.42680,
     VERTEX,   12.62987, -78.13390,  52.11087,
     VERTEX,   11.95672, -77.97101,  51.44608,
     VERTEX,   11.50788, -78.34913,  50.68637,
     VERTEX,   11.45478, -79.12383,  50.12192,
     VERTEX,   11.81771, -79.99921,  49.96832,
     VERTEX,   12.45805, -80.64090,  50.28425,
     VERTEX,   13.13120, -80.80379,  50.94903,
     VERTEX,   13.58004, -80.42567,  51.70874,
     VERTEX,   13.63314, -79.65096,  52.27320,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  12.54396, -79.38740,  51.19756,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.85972, -78.59407,  41.87070,
                       
     VERTEX,   16.69750, -75.77008,  40.35826,
     VERTEX,   16.27656, -74.93898,  40.58997,
     VERTEX,   15.66476, -74.26605,  40.28263,
     VERTEX,   15.09578, -74.00832,  39.55363,
     VERTEX,   14.78696, -74.26424,  38.68143,
     VERTEX,   14.85625, -74.93604,  37.99918,
     VERTEX,   15.27719, -75.76714,  37.76747,
     VERTEX,   15.88900, -76.44007,  38.07481,
     VERTEX,   16.45797, -76.69780,  38.80381,
     VERTEX,   16.76680, -76.44189,  39.67601,
     VERTEX,   16.69750, -75.77008,  40.35826,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.77688, -75.35306,  39.17872,
                       
     VERTEX,   16.69750, -75.77008,  40.35826,
     VERTEX,   16.27656, -74.93898,  40.58997,
     VERTEX,   15.66476, -74.26605,  40.28263,
     VERTEX,   15.09578, -74.00832,  39.55363,
     VERTEX,   14.78696, -74.26424,  38.68143,
     VERTEX,   14.85625, -74.93604,  37.99918,
     VERTEX,   15.27719, -75.76714,  37.76747,
     VERTEX,   15.88900, -76.44007,  38.07481,
     VERTEX,   16.45797, -76.69780,  38.80381,
     VERTEX,   16.76680, -76.44189,  39.67601,
     VERTEX,   16.69750, -75.77008,  40.35826,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  15.77688, -75.35306,  39.17872,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.25314, -62.04288,  41.35360,
                       
     VERTEX,    5.19980, -59.46930,  40.01920,
     VERTEX,    4.77957, -58.63784,  40.25089,
     VERTEX,    4.16622, -57.96579,  39.94469,
     VERTEX,    3.59403, -57.70985,  39.21758,
     VERTEX,    3.28156, -57.96779,  38.34727,
     VERTEX,    3.34816, -58.64107,  37.66621,
     VERTEX,    3.76838, -59.47253,  37.43452,
     VERTEX,    4.38173, -60.14458,  37.74072,
     VERTEX,    4.95392, -60.40052,  38.46783,
     VERTEX,    5.26639, -60.14259,  39.33813,
     VERTEX,    5.19980, -59.46930,  40.01920,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    4.27398, -59.05519,  38.84270,
                       
     VERTEX,    5.19980, -59.46930,  40.01920,
     VERTEX,    4.77957, -58.63784,  40.25089,
     VERTEX,    4.16622, -57.96579,  39.94469,
     VERTEX,    3.59403, -57.70985,  39.21758,
     VERTEX,    3.28156, -57.96779,  38.34727,
     VERTEX,    3.34816, -58.64107,  37.66621,
     VERTEX,    3.76838, -59.47253,  37.43452,
     VERTEX,    4.38173, -60.14458,  37.74072,
     VERTEX,    4.95392, -60.40052,  38.46783,
     VERTEX,    5.26639, -60.14259,  39.33813,
     VERTEX,    5.19980, -59.46930,  40.01920,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,   4.27398, -59.05519,  38.84270,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   64.22483, -26.78028, 108.00816,
                       
     VERTEX,   61.11907, -31.24897, 110.29057,
     VERTEX,   60.35085, -30.78825, 109.94535,
     VERTEX,   59.76593, -30.04007, 110.08572,
     VERTEX,   59.58773, -29.29021, 110.65804,
     VERTEX,   59.88433, -28.82509, 111.44373,
     VERTEX,   60.54242, -28.82237, 112.14265,
     VERTEX,   61.31065, -29.28309, 112.48787,
     VERTEX,   61.89557, -30.03127, 112.34750,
     VERTEX,   62.07376, -30.78112, 111.77518,
     VERTEX,   61.77716, -31.24624, 110.98949,
     VERTEX,   61.11907, -31.24897, 110.29057,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   60.83075, -30.03567, 111.21661,
                       
     VERTEX,   61.11907, -31.24897, 110.29057,
     VERTEX,   60.35085, -30.78825, 109.94535,
     VERTEX,   59.76593, -30.04007, 110.08572,
     VERTEX,   59.58773, -29.29021, 110.65804,
     VERTEX,   59.88433, -28.82509, 111.44373,
     VERTEX,   60.54242, -28.82237, 112.14265,
     VERTEX,   61.31065, -29.28309, 112.48787,
     VERTEX,   61.89557, -30.03127, 112.34750,
     VERTEX,   62.07376, -30.78112, 111.77518,
     VERTEX,   61.77716, -31.24624, 110.98949,
     VERTEX,   61.11907, -31.24897, 110.29057,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  60.83075, -30.03567, 111.21661,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   53.26564, -49.00405, 124.09099,
                       
     VERTEX,   49.24498, -53.40078, 122.66969,
     VERTEX,   48.69617, -52.68667, 122.33736,
     VERTEX,   48.11691, -51.96668, 122.59753,
     VERTEX,   47.72849, -51.51583, 123.35082,
     VERTEX,   47.67924, -51.50632, 124.30952,
     VERTEX,   47.98800, -51.94180, 125.10741,
     VERTEX,   48.53681, -52.65591, 125.43974,
     VERTEX,   49.11606, -53.37589, 125.17957,
     VERTEX,   49.50449, -53.82674, 124.42628,
     VERTEX,   49.55374, -53.83625, 123.46759,
     VERTEX,   49.24498, -53.40078, 122.66969,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.61649, -52.67129, 123.88855,
                       
     VERTEX,   49.24498, -53.40078, 122.66969,
     VERTEX,   48.69617, -52.68667, 122.33736,
     VERTEX,   48.11691, -51.96668, 122.59753,
     VERTEX,   47.72849, -51.51583, 123.35082,
     VERTEX,   47.67924, -51.50632, 124.30952,
     VERTEX,   47.98800, -51.94180, 125.10741,
     VERTEX,   48.53681, -52.65591, 125.43974,
     VERTEX,   49.11606, -53.37589, 125.17957,
     VERTEX,   49.50449, -53.82674, 124.42628,
     VERTEX,   49.55374, -53.83625, 123.46759,
     VERTEX,   49.24498, -53.40078, 122.66969,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  48.61649, -52.67129, 123.88855,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   51.51840, -44.17973, 124.72195,
                       
     VERTEX,   47.42158, -48.67162, 123.48698,
     VERTEX,   46.86278, -47.96702, 123.15102,
     VERTEX,   46.28649, -47.24345, 123.40781,
     VERTEX,   45.91285, -46.77729, 124.15927,
     VERTEX,   45.88456, -46.74660, 125.11836,
     VERTEX,   46.21243, -47.16311, 125.91875,
     VERTEX,   46.77124, -47.86772, 126.25471,
     VERTEX,   47.34753, -48.59129, 125.99792,
     VERTEX,   47.72117, -49.05744, 125.24646,
     VERTEX,   47.74946, -49.08813, 124.28737,
     VERTEX,   47.42158, -48.67162, 123.48698,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.81701, -47.91737, 124.70287,
                       
     VERTEX,   47.42158, -48.67162, 123.48698,
     VERTEX,   46.86278, -47.96702, 123.15102,
     VERTEX,   46.28649, -47.24345, 123.40781,
     VERTEX,   45.91285, -46.77729, 124.15927,
     VERTEX,   45.88456, -46.74660, 125.11836,
     VERTEX,   46.21243, -47.16311, 125.91875,
     VERTEX,   46.77124, -47.86772, 126.25471,
     VERTEX,   47.34753, -48.59129, 125.99792,
     VERTEX,   47.72117, -49.05744, 125.24646,
     VERTEX,   47.74946, -49.08813, 124.28737,
     VERTEX,   47.42158, -48.67162, 123.48698,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  46.81701, -47.91737, 124.70287,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.02596, -33.74982, 127.58749,
                       
     VERTEX,   37.69394, -38.38546, 126.11973,
     VERTEX,   37.14680, -37.66974, 125.78809,
     VERTEX,   36.56710, -36.95033, 126.04885,
     VERTEX,   36.17627, -36.50202, 126.80242,
     VERTEX,   36.12358, -36.49605, 127.76096,
     VERTEX,   36.42918, -36.93469, 128.55833,
     VERTEX,   36.97632, -37.65041, 128.88997,
     VERTEX,   37.55602, -38.36982, 128.62920,
     VERTEX,   37.94685, -38.81813, 127.87563,
     VERTEX,   37.99953, -38.82410, 126.91710,
     VERTEX,   37.69394, -38.38546, 126.11973,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.06156, -37.66008, 127.33903,
                       
     VERTEX,   37.69394, -38.38546, 126.11973,
     VERTEX,   37.14680, -37.66974, 125.78809,
     VERTEX,   36.56710, -36.95033, 126.04885,
     VERTEX,   36.17627, -36.50202, 126.80242,
     VERTEX,   36.12358, -36.49605, 127.76096,
     VERTEX,   36.42918, -36.93469, 128.55833,
     VERTEX,   36.97632, -37.65041, 128.88997,
     VERTEX,   37.55602, -38.36982, 128.62920,
     VERTEX,   37.94685, -38.81813, 127.87563,
     VERTEX,   37.99953, -38.82410, 126.91710,
     VERTEX,   37.69394, -38.38546, 126.11973,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  37.06156, -37.66008, 127.33903,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.36358, -40.35798, 126.89069,
                       
     VERTEX,   37.36787, -44.65455, 124.85216,
     VERTEX,   36.84977, -43.91300, 124.53079,
     VERTEX,   36.25648, -43.20674, 124.79691,
     VERTEX,   35.81464, -42.80553, 125.54884,
     VERTEX,   35.69301, -42.86263, 126.49939,
     VERTEX,   35.93804, -43.35622, 127.28548,
     VERTEX,   36.45615, -44.09777, 127.60683,
     VERTEX,   37.04943, -44.80403, 127.34073,
     VERTEX,   37.49127, -45.20523, 126.58879,
     VERTEX,   37.61290, -45.14814, 125.63824,
     VERTEX,   37.36787, -44.65455, 124.85216,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.65295, -44.00538, 126.06882,
                       
     VERTEX,   37.36787, -44.65455, 124.85216,
     VERTEX,   36.84977, -43.91300, 124.53079,
     VERTEX,   36.25648, -43.20674, 124.79691,
     VERTEX,   35.81464, -42.80553, 125.54884,
     VERTEX,   35.69301, -42.86263, 126.49939,
     VERTEX,   35.93804, -43.35622, 127.28548,
     VERTEX,   36.45615, -44.09777, 127.60683,
     VERTEX,   37.04943, -44.80403, 127.34073,
     VERTEX,   37.49127, -45.20523, 126.58879,
     VERTEX,   37.61290, -45.14814, 125.63824,
     VERTEX,   37.36787, -44.65455, 124.85216,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  36.65295, -44.00538, 126.06882,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.15723,  -4.70493, 110.88731,
                       
     VERTEX,   -6.48528,  -2.59650, 112.50439,
     VERTEX,   -7.01622,  -1.84188, 112.76943,
     VERTEX,   -7.50412,  -1.08238, 112.44275,
     VERTEX,   -7.76263,  -0.60813, 111.64912,
     VERTEX,   -7.69301,  -0.60025, 110.69168,
     VERTEX,   -7.32185,  -1.06177, 109.93614,
     VERTEX,   -6.79092,  -1.81640, 109.67110,
     VERTEX,   -6.30301,  -2.57589, 109.99778,
     VERTEX,   -6.04450,  -3.05015, 110.79140,
     VERTEX,   -6.11412,  -3.05802, 111.74885,
     VERTEX,   -6.48528,  -2.59650, 112.50439,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.90357,  -1.82914, 111.22027,
                       
     VERTEX,   -6.48528,  -2.59650, 112.50439,
     VERTEX,   -7.01622,  -1.84188, 112.76943,
     VERTEX,   -7.50412,  -1.08238, 112.44275,
     VERTEX,   -7.76263,  -0.60813, 111.64912,
     VERTEX,   -7.69301,  -0.60025, 110.69168,
     VERTEX,   -7.32185,  -1.06177, 109.93614,
     VERTEX,   -6.79092,  -1.81640, 109.67110,
     VERTEX,   -6.30301,  -2.57589, 109.99778,
     VERTEX,   -6.04450,  -3.05015, 110.79140,
     VERTEX,   -6.11412,  -3.05802, 111.74885,
     VERTEX,   -6.48528,  -2.59650, 112.50439,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,  -6.90357,  -1.82914, 111.22027,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.29362, -11.02230, 109.27799,
                       
     VERTEX,   -8.62774,  -9.00756, 111.52861,
     VERTEX,   -9.16945,  -8.25317, 111.77160,
     VERTEX,   -9.60358,  -7.46718, 111.43196,
     VERTEX,   -9.76430,  -6.94980, 110.63943,
     VERTEX,   -9.59022,  -6.89867, 109.69674,
     VERTEX,   -9.14783,  -7.33330, 108.96394,
     VERTEX,   -8.60611,  -8.08769, 108.72096,
     VERTEX,   -8.17199,  -8.87368, 109.06059,
     VERTEX,   -8.01127,  -9.39106, 109.85312,
     VERTEX,   -8.18535,  -9.44219, 110.79581,
     VERTEX,   -8.62774,  -9.00756, 111.52861,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -8.88778,  -8.17043, 110.24628,
                       
     VERTEX,   -8.62774,  -9.00756, 111.52861,
     VERTEX,   -9.16945,  -8.25317, 111.77160,
     VERTEX,   -9.60358,  -7.46718, 111.43196,
     VERTEX,   -9.76430,  -6.94980, 110.63943,
     VERTEX,   -9.59022,  -6.89867, 109.69674,
     VERTEX,   -9.14783,  -7.33330, 108.96394,
     VERTEX,   -8.60611,  -8.08769, 108.72096,
     VERTEX,   -8.17199,  -8.87368, 109.06059,
     VERTEX,   -8.01127,  -9.39106, 109.85312,
     VERTEX,   -8.18535,  -9.44219, 110.79581,
     VERTEX,   -8.62774,  -9.00756, 111.52861,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,  -8.88778,  -8.17043, 110.24628,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.40432, -15.84834, 107.63708,
                       
     VERTEX,   -6.77329, -13.80435, 110.09055,
     VERTEX,   -7.33222, -13.06551, 110.34219,
     VERTEX,   -7.76853, -12.27521, 110.01563,
     VERTEX,   -7.91556, -11.73529, 109.23557,
     VERTEX,   -7.71717, -11.65201, 108.30000,
     VERTEX,   -7.24912, -12.05716, 107.56625,
     VERTEX,   -6.69019, -12.79600, 107.31461,
     VERTEX,   -6.25389, -13.58631, 107.64117,
     VERTEX,   -6.10685, -14.12622, 108.42122,
     VERTEX,   -6.30525, -14.20950, 109.35680,
     VERTEX,   -6.77329, -13.80435, 110.09055,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.01121, -12.93076, 108.82840,
                       
     VERTEX,   -6.77329, -13.80435, 110.09055,
     VERTEX,   -7.33222, -13.06551, 110.34219,
     VERTEX,   -7.76853, -12.27521, 110.01563,
     VERTEX,   -7.91556, -11.73529, 109.23557,
     VERTEX,   -7.71717, -11.65201, 108.30000,
     VERTEX,   -7.24912, -12.05716, 107.56625,
     VERTEX,   -6.69019, -12.79600, 107.31461,
     VERTEX,   -6.25389, -13.58631, 107.64117,
     VERTEX,   -6.10685, -14.12622, 108.42122,
     VERTEX,   -6.30525, -14.20950, 109.35680,
     VERTEX,   -6.77329, -13.80435, 110.09055,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,  -7.01121, -12.93076, 108.82840,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.04923, -25.89655, 105.43332,
                       
     VERTEX,    4.22462, -23.87140, 107.76544,
     VERTEX,    3.62690, -23.18250, 108.06501,
     VERTEX,    3.13058, -22.40955, 107.78606,
     VERTEX,    2.92523, -21.84779, 107.03516,
     VERTEX,    3.08930, -21.71180, 106.09911,
     VERTEX,    3.56011, -22.05352, 105.33546,
     VERTEX,    4.15783, -22.74242, 105.03589,
     VERTEX,    4.65415, -23.51538, 105.31483,
     VERTEX,    4.85949, -24.07713, 106.06573,
     VERTEX,    4.69543, -24.21312, 107.00179,
     VERTEX,    4.22462, -23.87140, 107.76544,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.89236, -22.96246, 106.55045,
                       
     VERTEX,    4.22462, -23.87140, 107.76544,
     VERTEX,    3.62690, -23.18250, 108.06501,
     VERTEX,    3.13058, -22.40955, 107.78606,
     VERTEX,    2.92523, -21.84779, 107.03516,
     VERTEX,    3.08930, -21.71180, 106.09911,
     VERTEX,    3.56011, -22.05352, 105.33546,
     VERTEX,    4.15783, -22.74242, 105.03589,
     VERTEX,    4.65415, -23.51538, 105.31483,
     VERTEX,    4.85949, -24.07713, 106.06573,
     VERTEX,    4.69543, -24.21312, 107.00179,
     VERTEX,    4.22462, -23.87140, 107.76544,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,   3.89236, -22.96246, 106.55045,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.92989, -19.86167, 107.69936,
                       
     VERTEX,    3.77558, -17.63236, 109.45722,
     VERTEX,    3.22438, -16.89936, 109.74095,
     VERTEX,    2.72307, -16.14036, 109.43404,
     VERTEX,    2.46311, -15.64526, 108.65371,
     VERTEX,    2.54382, -15.60318, 107.69804,
     VERTEX,    2.93435, -16.03019, 106.93204,
     VERTEX,    3.48555, -16.76319, 106.64832,
     VERTEX,    3.98686, -17.52219, 106.95523,
     VERTEX,    4.24682, -18.01729, 107.73555,
     VERTEX,    4.16611, -18.05937, 108.69123,
     VERTEX,    3.77558, -17.63236, 109.45722,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.35496, -16.83128, 108.19463,
                       
     VERTEX,    3.77558, -17.63236, 109.45722,
     VERTEX,    3.22438, -16.89936, 109.74095,
     VERTEX,    2.72307, -16.14036, 109.43404,
     VERTEX,    2.46311, -15.64526, 108.65371,
     VERTEX,    2.54382, -15.60318, 107.69804,
     VERTEX,    2.93435, -16.03019, 106.93204,
     VERTEX,    3.48555, -16.76319, 106.64832,
     VERTEX,    3.98686, -17.52219, 106.95523,
     VERTEX,    4.24682, -18.01729, 107.73555,
     VERTEX,    4.16611, -18.05937, 108.69123,
     VERTEX,    3.77558, -17.63236, 109.45722,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,   3.35496, -16.83128, 108.19463,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.43509,  38.47347,  36.45059,
                       
     VERTEX,   20.87049,  35.90773,  32.19138,
     VERTEX,   20.53379,  36.80396,  32.12052,
     VERTEX,   20.00782,  37.47337,  32.56420,
     VERTEX,   19.49348,  37.66026,  33.35294,
     VERTEX,   19.18722,  37.29327,  34.18548,
     VERTEX,   19.20603,  36.51255,  34.74381,
     VERTEX,   19.54272,  35.61633,  34.81467,
     VERTEX,   20.06870,  34.94692,  34.37099,
     VERTEX,   20.58304,  34.76003,  33.58224,
     VERTEX,   20.88930,  35.12702,  32.74971,
     VERTEX,   20.87049,  35.90773,  32.19138,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.03826,  36.21014,  33.46759,
                       
     VERTEX,   20.87049,  35.90773,  32.19138,
     VERTEX,   20.53379,  36.80396,  32.12052,
     VERTEX,   20.00782,  37.47337,  32.56420,
     VERTEX,   19.49348,  37.66026,  33.35294,
     VERTEX,   19.18722,  37.29327,  34.18548,
     VERTEX,   19.20603,  36.51255,  34.74381,
     VERTEX,   19.54272,  35.61633,  34.81467,
     VERTEX,   20.06870,  34.94692,  34.37099,
     VERTEX,   20.58304,  34.76003,  33.58224,
     VERTEX,   20.88930,  35.12702,  32.74971,
     VERTEX,   20.87049,  35.90773,  32.19138,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,  20.03826,  36.21014,  33.46759,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.77711,  37.90892,  63.73494,
                       
     VERTEX,   42.60064,  39.17925,  57.11377,
     VERTEX,   42.41546,  40.06232,  57.44164,
     VERTEX,   41.82977,  40.57531,  58.00324,
     VERTEX,   41.06726,  40.52227,  58.58408,
     VERTEX,   40.41921,  39.92345,  58.96230,
     VERTEX,   40.13313,  39.00760,  58.99342,
     VERTEX,   40.31831,  38.12452,  58.66556,
     VERTEX,   40.90401,  37.61154,  58.10395,
     VERTEX,   41.66651,  37.66458,  57.52311,
     VERTEX,   42.31457,  38.26340,  57.14490,
     VERTEX,   42.60064,  39.17925,  57.11377,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.36689,  39.09343,  58.05360,
                       
     VERTEX,   42.60064,  39.17925,  57.11377,
     VERTEX,   42.41546,  40.06232,  57.44164,
     VERTEX,   41.82977,  40.57531,  58.00324,
     VERTEX,   41.06726,  40.52227,  58.58408,
     VERTEX,   40.41921,  39.92345,  58.96230,
     VERTEX,   40.13313,  39.00760,  58.99342,
     VERTEX,   40.31831,  38.12452,  58.66556,
     VERTEX,   40.90401,  37.61154,  58.10395,
     VERTEX,   41.66651,  37.66458,  57.52311,
     VERTEX,   42.31457,  38.26340,  57.14490,
     VERTEX,   42.60064,  39.17925,  57.11377,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  41.36689,  39.09343,  58.05360,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.06004,  45.82471,  61.75450,
                       
     VERTEX,   29.37420,  45.92170,  55.79890,
     VERTEX,   29.16770,  46.83305,  56.01892,
     VERTEX,   28.61735,  47.39313,  56.57121,
     VERTEX,   27.93337,  47.38802,  57.24482,
     VERTEX,   27.37701,  46.81967,  57.78245,
     VERTEX,   27.16079,  45.90517,  57.97874,
     VERTEX,   27.36729,  44.99382,  57.75873,
     VERTEX,   27.91764,  44.43373,  57.20644,
     VERTEX,   28.60162,  44.43885,  56.53283,
     VERTEX,   29.15797,  45.00720,  55.99520,
     VERTEX,   29.37420,  45.92170,  55.79890,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.26749,  45.91343,  56.88882,
                       
     VERTEX,   29.37420,  45.92170,  55.79890,
     VERTEX,   29.16770,  46.83305,  56.01892,
     VERTEX,   28.61735,  47.39313,  56.57121,
     VERTEX,   27.93337,  47.38802,  57.24482,
     VERTEX,   27.37701,  46.81967,  57.78245,
     VERTEX,   27.16079,  45.90517,  57.97874,
     VERTEX,   27.36729,  44.99382,  57.75873,
     VERTEX,   27.91764,  44.43373,  57.20644,
     VERTEX,   28.60162,  44.43885,  56.53283,
     VERTEX,   29.15797,  45.00720,  55.99520,
     VERTEX,   29.37420,  45.92170,  55.79890,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  28.26749,  45.91343,  56.88882,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.17364,  48.95351,  48.64617,
                       
     VERTEX,   26.33958,  47.58418,  42.97406,
     VERTEX,   26.08141,  48.50544,  43.05293,
     VERTEX,   25.55479,  49.12332,  43.56527,
     VERTEX,   24.96086,  49.20180,  44.31539,
     VERTEX,   24.52649,  48.71091,  45.01678,
     VERTEX,   24.41759,  47.83814,  45.40153,
     VERTEX,   24.67576,  46.91688,  45.32267,
     VERTEX,   25.20239,  46.29900,  44.81033,
     VERTEX,   25.79632,  46.22052,  44.06020,
     VERTEX,   26.23069,  46.71142,  43.35881,
     VERTEX,   26.33958,  47.58418,  42.97406,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.37859,  47.71116,  44.18779,
                       
     VERTEX,   26.33958,  47.58418,  42.97406,
     VERTEX,   26.08141,  48.50544,  43.05293,
     VERTEX,   25.55479,  49.12332,  43.56527,
     VERTEX,   24.96086,  49.20180,  44.31539,
     VERTEX,   24.52649,  48.71091,  45.01678,
     VERTEX,   24.41759,  47.83814,  45.40153,
     VERTEX,   24.67576,  46.91688,  45.32267,
     VERTEX,   25.20239,  46.29900,  44.81033,
     VERTEX,   25.79632,  46.22052,  44.06020,
     VERTEX,   26.23069,  46.71142,  43.35881,
     VERTEX,   26.33958,  47.58418,  42.97406,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,  25.37859,  47.71116,  44.18779,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.74391,  33.61360,  41.48993,
                       
     VERTEX,   37.53162,  32.64424,  35.98673,
     VERTEX,   37.28609,  33.56585,  36.09605,
     VERTEX,   36.75298,  34.17107,  36.61672,
     VERTEX,   36.13590,  34.22872,  37.34986,
     VERTEX,   35.67056,  33.71679,  38.01543,
     VERTEX,   35.53471,  32.83081,  38.35921,
     VERTEX,   35.78023,  31.90920,  38.24989,
     VERTEX,   36.31335,  31.30398,  37.72923,
     VERTEX,   36.93042,  31.24633,  36.99609,
     VERTEX,   37.39576,  31.75826,  36.33051,
     VERTEX,   37.53162,  32.64424,  35.98673,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.53316,  32.73753,  37.17297,
                       
     VERTEX,   37.53162,  32.64424,  35.98673,
     VERTEX,   37.28609,  33.56585,  36.09605,
     VERTEX,   36.75298,  34.17107,  36.61672,
     VERTEX,   36.13590,  34.22872,  37.34986,
     VERTEX,   35.67056,  33.71679,  38.01543,
     VERTEX,   35.53471,  32.83081,  38.35921,
     VERTEX,   35.78023,  31.90920,  38.24989,
     VERTEX,   36.31335,  31.30398,  37.72923,
     VERTEX,   36.93042,  31.24633,  36.99609,
     VERTEX,   37.39576,  31.75826,  36.33051,
     VERTEX,   37.53162,  32.64424,  35.98673,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  36.53316,  32.73753,  37.17297,   0.80000,
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
                       
     SPHERE,   55.33900, -35.30300, 116.40800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   41.09400, -58.60500, 123.56100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   39.21000, -53.96500, 124.67200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   29.02900, -43.98700, 126.93700,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   29.03100, -49.90700, 124.73900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   -0.02100,   2.82400, 111.75900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   -1.75900,  -3.55600, 111.81300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    0.09700,  -8.21000, 110.75600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.27000, -18.21500, 108.35800,   0.80000,
                       
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
