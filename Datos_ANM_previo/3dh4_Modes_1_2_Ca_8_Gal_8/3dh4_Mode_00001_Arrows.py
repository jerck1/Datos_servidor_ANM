from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.86526, -45.80244,  30.54924,
                       
     VERTEX,   35.90357, -50.05348,  30.29338,
     VERTEX,   35.30797, -49.37090,  29.97567,
     VERTEX,   34.78223, -48.61321,  30.24234,
     VERTEX,   34.52718, -48.06983,  30.99153,
     VERTEX,   34.64023, -47.94831,  31.93707,
     VERTEX,   35.07820, -48.29506,  32.71781,
     VERTEX,   35.67380, -48.97765,  33.03551,
     VERTEX,   36.19954, -49.73533,  32.76884,
     VERTEX,   36.45459, -50.27871,  32.01966,
     VERTEX,   36.34154, -50.40024,  31.07411,
     VERTEX,   35.90357, -50.05348,  30.29338,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.49089, -49.17427,  31.50559,
                       
     VERTEX,   35.90357, -50.05348,  30.29338,
     VERTEX,   35.30797, -49.37090,  29.97567,
     VERTEX,   34.78223, -48.61321,  30.24234,
     VERTEX,   34.52718, -48.06983,  30.99153,
     VERTEX,   34.64023, -47.94831,  31.93707,
     VERTEX,   35.07820, -48.29506,  32.71781,
     VERTEX,   35.67380, -48.97765,  33.03551,
     VERTEX,   36.19954, -49.73533,  32.76884,
     VERTEX,   36.45459, -50.27871,  32.01966,
     VERTEX,   36.34154, -50.40024,  31.07411,
     VERTEX,   35.90357, -50.05348,  30.29338,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  35.49089, -49.17427,  31.50559,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.49938, -66.02768,  36.31214,
                       
     VERTEX,   10.50535, -69.08707,  39.60107,
     VERTEX,    9.93471, -68.32516,  39.47672,
     VERTEX,    9.77449, -67.42092,  39.75649,
     VERTEX,   10.08590, -66.71973,  40.33352,
     VERTEX,   10.74998, -66.48943,  40.98740,
     VERTEX,   11.51308, -66.81798,  41.46837,
     VERTEX,   12.08372, -67.57989,  41.59272,
     VERTEX,   12.24394, -68.48414,  41.31295,
     VERTEX,   11.93253, -69.18533,  40.73592,
     VERTEX,   11.26845, -69.41563,  40.08204,
     VERTEX,   10.50535, -69.08707,  39.60107,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.00921, -67.95253,  40.53472,
                       
     VERTEX,   10.50535, -69.08707,  39.60107,
     VERTEX,    9.93471, -68.32516,  39.47672,
     VERTEX,    9.77449, -67.42092,  39.75649,
     VERTEX,   10.08590, -66.71973,  40.33352,
     VERTEX,   10.74998, -66.48943,  40.98740,
     VERTEX,   11.51308, -66.81798,  41.46837,
     VERTEX,   12.08372, -67.57989,  41.59272,
     VERTEX,   12.24394, -68.48414,  41.31295,
     VERTEX,   11.93253, -69.18533,  40.73592,
     VERTEX,   11.26845, -69.41563,  40.08204,
     VERTEX,   10.50535, -69.08707,  39.60107,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  11.00921, -67.95253,  40.53472,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.90064, -69.65610,  36.63858,
                       
     VERTEX,   24.90216, -73.06026,  38.95497,
     VERTEX,   24.29771, -72.33597,  38.77707,
     VERTEX,   24.02474, -71.46285,  39.06820,
     VERTEX,   24.18751, -70.77441,  39.71716,
     VERTEX,   24.72385, -70.53360,  40.47606,
     VERTEX,   25.42891, -70.83240,  41.05505,
     VERTEX,   26.03335, -71.55669,  41.23295,
     VERTEX,   26.30632, -72.42980,  40.94182,
     VERTEX,   26.14355, -73.11825,  40.29286,
     VERTEX,   25.60720, -73.35905,  39.53395,
     VERTEX,   24.90216, -73.06026,  38.95497,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.16553, -71.94633,  40.00501,
                       
     VERTEX,   24.90216, -73.06026,  38.95497,
     VERTEX,   24.29771, -72.33597,  38.77707,
     VERTEX,   24.02474, -71.46285,  39.06820,
     VERTEX,   24.18751, -70.77441,  39.71716,
     VERTEX,   24.72385, -70.53360,  40.47606,
     VERTEX,   25.42891, -70.83240,  41.05505,
     VERTEX,   26.03335, -71.55669,  41.23295,
     VERTEX,   26.30632, -72.42980,  40.94182,
     VERTEX,   26.14355, -73.11825,  40.29286,
     VERTEX,   25.60720, -73.35905,  39.53395,
     VERTEX,   24.90216, -73.06026,  38.95497,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.16553, -71.94633,  40.00501,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.63213, -61.77505,  28.16228,
                       
     VERTEX,   31.16394, -65.99242,  29.54992,
     VERTEX,   30.54144, -65.30761,  29.29469,
     VERTEX,   30.12736, -64.48940,  29.57870,
     VERTEX,   30.07985, -63.85030,  30.29347,
     VERTEX,   30.41707, -63.63444,  31.16599,
     VERTEX,   31.01020, -63.92426,  31.86298,
     VERTEX,   31.63270, -64.60906,  32.11821,
     VERTEX,   32.04678, -65.42728,  31.83420,
     VERTEX,   32.09429, -66.06637,  31.11943,
     VERTEX,   31.75707, -66.28223,  30.24691,
     VERTEX,   31.16394, -65.99242,  29.54992,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.08707, -64.95834,  30.70645,
                       
     VERTEX,   31.16394, -65.99242,  29.54992,
     VERTEX,   30.54144, -65.30761,  29.29469,
     VERTEX,   30.12736, -64.48940,  29.57870,
     VERTEX,   30.07985, -63.85030,  30.29347,
     VERTEX,   30.41707, -63.63444,  31.16599,
     VERTEX,   31.01020, -63.92426,  31.86298,
     VERTEX,   31.63270, -64.60906,  32.11821,
     VERTEX,   32.04678, -65.42728,  31.83420,
     VERTEX,   32.09429, -66.06637,  31.11943,
     VERTEX,   31.75707, -66.28223,  30.24691,
     VERTEX,   31.16394, -65.99242,  29.54992,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  31.08707, -64.95834,  30.70645,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.70805, -46.39793,  28.75661,
                       
     VERTEX,   18.55888, -50.41366,  29.89630,
     VERTEX,   17.93691, -49.72973,  29.63746,
     VERTEX,   17.51657, -48.91454,  29.92097,
     VERTEX,   17.45840, -48.27946,  30.63853,
     VERTEX,   17.78464, -48.06707,  31.51606,
     VERTEX,   18.37066, -48.35850,  32.21837,
     VERTEX,   18.99263, -49.04243,  32.47721,
     VERTEX,   19.41298, -49.85762,  32.19371,
     VERTEX,   19.47114, -50.49269,  31.47615,
     VERTEX,   19.14491, -50.70509,  30.59862,
     VERTEX,   18.55888, -50.41366,  29.89630,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.46477, -49.38608,  31.05734,
                       
     VERTEX,   18.55888, -50.41366,  29.89630,
     VERTEX,   17.93691, -49.72973,  29.63746,
     VERTEX,   17.51657, -48.91454,  29.92097,
     VERTEX,   17.45840, -48.27946,  30.63853,
     VERTEX,   17.78464, -48.06707,  31.51606,
     VERTEX,   18.37066, -48.35850,  32.21837,
     VERTEX,   18.99263, -49.04243,  32.47721,
     VERTEX,   19.41298, -49.85762,  32.19371,
     VERTEX,   19.47114, -50.49269,  31.47615,
     VERTEX,   19.14491, -50.70509,  30.59862,
     VERTEX,   18.55888, -50.41366,  29.89630,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,  18.46477, -49.38608,  31.05734,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.74274, -43.99547, 124.74077,
                       
     VERTEX,   51.24408, -41.01445, 122.46045,
     VERTEX,   50.81210, -40.23827, 122.82451,
     VERTEX,   50.07995, -39.62899, 122.70478,
     VERTEX,   49.32727, -39.41935, 122.14700,
     VERTEX,   48.84157, -39.68941, 121.36420,
     VERTEX,   48.80836, -40.33604, 120.65542,
     VERTEX,   49.24033, -41.11222, 120.29136,
     VERTEX,   49.97248, -41.72149, 120.41109,
     VERTEX,   50.72516, -41.93114, 120.96887,
     VERTEX,   51.21087, -41.66107, 121.75166,
     VERTEX,   51.24408, -41.01445, 122.46045,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   50.02622, -40.67524, 121.55794,
                       
     VERTEX,   51.24408, -41.01445, 122.46045,
     VERTEX,   50.81210, -40.23827, 122.82451,
     VERTEX,   50.07995, -39.62899, 122.70478,
     VERTEX,   49.32727, -39.41935, 122.14700,
     VERTEX,   48.84157, -39.68941, 121.36420,
     VERTEX,   48.80836, -40.33604, 120.65542,
     VERTEX,   49.24033, -41.11222, 120.29136,
     VERTEX,   49.97248, -41.72149, 120.41109,
     VERTEX,   50.72516, -41.93114, 120.96887,
     VERTEX,   51.21087, -41.66107, 121.75166,
     VERTEX,   51.24408, -41.01445, 122.46045,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  50.02622, -40.67524, 121.55794,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.36608, -68.35183, 123.15732,
                       
     VERTEX,   34.45600, -65.41263, 124.50570,
     VERTEX,   33.87878, -64.73279, 124.86099,
     VERTEX,   33.28893, -64.01326, 124.62443,
     VERTEX,   32.91177, -63.52887, 123.88638,
     VERTEX,   32.89136, -63.46465, 122.92874,
     VERTEX,   33.23549, -63.84512, 122.11732,
     VERTEX,   33.81272, -64.52496, 121.76202,
     VERTEX,   34.40256, -65.24448, 121.99859,
     VERTEX,   34.77972, -65.72887, 122.73664,
     VERTEX,   34.80013, -65.79310, 123.69427,
     VERTEX,   34.45600, -65.41263, 124.50570,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.84575, -64.62887, 123.31151,
                       
     VERTEX,   34.45600, -65.41263, 124.50570,
     VERTEX,   33.87878, -64.73279, 124.86099,
     VERTEX,   33.28893, -64.01326, 124.62443,
     VERTEX,   32.91177, -63.52887, 123.88638,
     VERTEX,   32.89136, -63.46465, 122.92874,
     VERTEX,   33.23549, -63.84512, 122.11732,
     VERTEX,   33.81272, -64.52496, 121.76202,
     VERTEX,   34.40256, -65.24448, 121.99859,
     VERTEX,   34.77972, -65.72887, 122.73664,
     VERTEX,   34.80013, -65.79310, 123.69427,
     VERTEX,   34.45600, -65.41263, 124.50570,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  33.84575, -64.62887, 123.31151,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.37330, -63.86497, 124.75368,
                       
     VERTEX,   32.53870, -60.84390, 125.91396,
     VERTEX,   31.96874, -60.15947, 126.27216,
     VERTEX,   31.37042, -59.44604, 126.03842,
     VERTEX,   30.97229, -58.97610, 125.30205,
     VERTEX,   30.92642, -58.92916, 124.34429,
     VERTEX,   31.25033, -59.32315, 123.53099,
     VERTEX,   31.82030, -60.00757, 123.17280,
     VERTEX,   32.41861, -60.72100, 123.40653,
     VERTEX,   32.81674, -61.19094, 124.14291,
     VERTEX,   32.86261, -61.23788, 125.10066,
     VERTEX,   32.53870, -60.84390, 125.91396,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.89452, -60.08352, 124.72248,
                       
     VERTEX,   32.53870, -60.84390, 125.91396,
     VERTEX,   31.96874, -60.15947, 126.27216,
     VERTEX,   31.37042, -59.44604, 126.03842,
     VERTEX,   30.97229, -58.97610, 125.30205,
     VERTEX,   30.92642, -58.92916, 124.34429,
     VERTEX,   31.25033, -59.32315, 123.53099,
     VERTEX,   31.82030, -60.00757, 123.17280,
     VERTEX,   32.41861, -60.72100, 123.40653,
     VERTEX,   32.81674, -61.19094, 124.14291,
     VERTEX,   32.86261, -61.23788, 125.10066,
     VERTEX,   32.53870, -60.84390, 125.91396,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  31.89452, -60.08352, 124.72248,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.73757, -54.13554, 126.44771,
                       
     VERTEX,   22.03381, -51.04516, 127.83183,
     VERTEX,   21.45695, -50.36349, 128.18420,
     VERTEX,   20.87075, -49.64197, 127.94469,
     VERTEX,   20.49911, -49.15619, 127.20477,
     VERTEX,   20.48399, -49.09169, 126.24705,
     VERTEX,   20.83115, -49.47313, 125.43737,
     VERTEX,   21.40801, -50.15479, 125.08499,
     VERTEX,   21.99421, -50.87632, 125.32451,
     VERTEX,   22.36585, -51.36211, 126.06444,
     VERTEX,   22.38097, -51.42660, 127.02216,
     VERTEX,   22.03381, -51.04516, 127.83183,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.43248, -50.25915, 126.63460,
                       
     VERTEX,   22.03381, -51.04516, 127.83183,
     VERTEX,   21.45695, -50.36349, 128.18420,
     VERTEX,   20.87075, -49.64197, 127.94469,
     VERTEX,   20.49911, -49.15619, 127.20477,
     VERTEX,   20.48399, -49.09169, 126.24705,
     VERTEX,   20.83115, -49.47313, 125.43737,
     VERTEX,   21.40801, -50.15479, 125.08499,
     VERTEX,   21.99421, -50.87632, 125.32451,
     VERTEX,   22.36585, -51.36211, 126.06444,
     VERTEX,   22.38097, -51.42660, 127.02216,
     VERTEX,   22.03381, -51.04516, 127.83183,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  21.43248, -50.25915, 126.63460,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.27441, -59.47516, 122.84233,
                       
     VERTEX,   22.26793, -56.67533, 124.76222,
     VERTEX,   21.66939, -56.00801, 125.10577,
     VERTEX,   21.10739, -55.26904, 124.86149,
     VERTEX,   20.79658, -54.74069, 124.12267,
     VERTEX,   20.85569, -54.62477, 123.17153,
     VERTEX,   21.26213, -54.96556, 122.37137,
     VERTEX,   21.86066, -55.63289, 122.02782,
     VERTEX,   22.42267, -56.37186, 122.27210,
     VERTEX,   22.73348, -56.90021, 123.01092,
     VERTEX,   22.67437, -57.01613, 123.96205,
     VERTEX,   22.26793, -56.67533, 124.76222,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.76503, -55.82045, 123.56680,
                       
     VERTEX,   22.26793, -56.67533, 124.76222,
     VERTEX,   21.66939, -56.00801, 125.10577,
     VERTEX,   21.10739, -55.26904, 124.86149,
     VERTEX,   20.79658, -54.74069, 124.12267,
     VERTEX,   20.85569, -54.62477, 123.17153,
     VERTEX,   21.26213, -54.96556, 122.37137,
     VERTEX,   21.86066, -55.63289, 122.02782,
     VERTEX,   22.42267, -56.37186, 122.27210,
     VERTEX,   22.73348, -56.90021, 123.01092,
     VERTEX,   22.67437, -57.01613, 123.96205,
     VERTEX,   22.26793, -56.67533, 124.76222,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  21.76503, -55.82045, 123.56680,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.94576,   3.91836, 114.11296,
                       
     VERTEX,    6.10515,   0.47394, 111.94289,
     VERTEX,    5.63831,   1.27828, 111.70477,
     VERTEX,    5.10906,   2.00055, 112.05094,
     VERTEX,    4.71957,   2.36486, 112.84917,
     VERTEX,    4.61860,   2.23206, 113.79457,
     VERTEX,    4.84473,   1.65288, 114.52602,
     VERTEX,    5.31157,   0.84854, 114.76414,
     VERTEX,    5.84081,   0.12628, 114.41796,
     VERTEX,    6.23030,  -0.23804, 113.61974,
     VERTEX,    6.33127,  -0.10524, 112.67434,
     VERTEX,    6.10515,   0.47394, 111.94289,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    5.47494,   1.06341, 113.23445,
                       
     VERTEX,    6.10515,   0.47394, 111.94289,
     VERTEX,    5.63831,   1.27828, 111.70477,
     VERTEX,    5.10906,   2.00055, 112.05094,
     VERTEX,    4.71957,   2.36486, 112.84917,
     VERTEX,    4.61860,   2.23206, 113.79457,
     VERTEX,    4.84473,   1.65288, 114.52602,
     VERTEX,    5.31157,   0.84854, 114.76414,
     VERTEX,    5.84081,   0.12628, 114.41796,
     VERTEX,    6.23030,  -0.23804, 113.61974,
     VERTEX,    6.33127,  -0.10524, 112.67434,
     VERTEX,    6.10515,   0.47394, 111.94289,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,   5.47494,   1.06341, 113.23445,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.92231,  -0.59623, 113.52796,
                       
     VERTEX,    8.07300,  -4.07473, 111.18779,
     VERTEX,    7.61029,  -3.26863, 110.94758,
     VERTEX,    7.06934,  -2.55259, 111.28856,
     VERTEX,    6.65677,  -2.20013, 112.08049,
     VERTEX,    6.53017,  -2.34587, 113.02088,
     VERTEX,    6.73789,  -2.93413, 113.75053,
     VERTEX,    7.20060,  -3.74024, 113.99075,
     VERTEX,    7.74155,  -4.45627, 113.64977,
     VERTEX,    8.15412,  -4.80874, 112.85783,
     VERTEX,    8.28072,  -4.66300, 111.91744,
     VERTEX,    8.07300,  -4.07473, 111.18779,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.40544,  -3.50443, 112.46916,
                       
     VERTEX,    8.07300,  -4.07473, 111.18779,
     VERTEX,    7.61029,  -3.26863, 110.94758,
     VERTEX,    7.06934,  -2.55259, 111.28856,
     VERTEX,    6.65677,  -2.20013, 112.08049,
     VERTEX,    6.53017,  -2.34587, 113.02088,
     VERTEX,    6.73789,  -2.93413, 113.75053,
     VERTEX,    7.20060,  -3.74024, 113.99075,
     VERTEX,    7.74155,  -4.45627, 113.64977,
     VERTEX,    8.15412,  -4.80874, 112.85783,
     VERTEX,    8.28072,  -4.66300, 111.91744,
     VERTEX,    8.07300,  -4.07473, 111.18779,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,   7.40544,  -3.50443, 112.46916,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.45720,  -9.90029, 110.98389,
                       
     VERTEX,   17.92203, -13.68222, 108.75575,
     VERTEX,   17.42490, -12.91821, 108.45451,
     VERTEX,   16.83578, -12.21455, 108.73631,
     VERTEX,   16.37969, -11.84003, 109.49348,
     VERTEX,   16.23085, -11.93769, 110.43683,
     VERTEX,   16.44611, -12.47023, 111.20602,
     VERTEX,   16.94324, -13.23424, 111.50726,
     VERTEX,   17.53236, -13.93790, 111.22547,
     VERTEX,   17.98845, -14.31243, 110.46830,
     VERTEX,   18.13729, -14.21477, 109.52495,
     VERTEX,   17.92203, -13.68222, 108.75575,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.18407, -13.07623, 109.98089,
                       
     VERTEX,   17.92203, -13.68222, 108.75575,
     VERTEX,   17.42490, -12.91821, 108.45451,
     VERTEX,   16.83578, -12.21455, 108.73631,
     VERTEX,   16.37969, -11.84003, 109.49348,
     VERTEX,   16.23085, -11.93769, 110.43683,
     VERTEX,   16.44611, -12.47023, 111.20602,
     VERTEX,   16.94324, -13.23424, 111.50726,
     VERTEX,   17.53236, -13.93790, 111.22547,
     VERTEX,   17.98845, -14.31243, 110.46830,
     VERTEX,   18.13729, -14.21477, 109.52495,
     VERTEX,   17.92203, -13.68222, 108.75575,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,  17.18407, -13.07623, 109.98089,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.98058,  -3.46132, 110.05389,
                       
     VERTEX,   18.12319,  -7.37925, 108.39507,
     VERTEX,   17.60491,  -6.62672, 108.10066,
     VERTEX,   17.05206,  -5.90038, 108.39797,
     VERTEX,   16.67582,  -5.47768, 109.17345,
     VERTEX,   16.61989,  -5.52007, 110.13088,
     VERTEX,   16.90564,  -6.01136, 110.90456,
     VERTEX,   17.42392,  -6.76390, 111.19897,
     VERTEX,   17.97676,  -7.49023, 110.90166,
     VERTEX,   18.35301,  -7.91293, 110.12618,
     VERTEX,   18.40894,  -7.87054, 109.16875,
     VERTEX,   18.12319,  -7.37925, 108.39507,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.51441,  -6.69531, 109.64982,
                       
     VERTEX,   18.12319,  -7.37925, 108.39507,
     VERTEX,   17.60491,  -6.62672, 108.10066,
     VERTEX,   17.05206,  -5.90038, 108.39797,
     VERTEX,   16.67582,  -5.47768, 109.17345,
     VERTEX,   16.61989,  -5.52007, 110.13088,
     VERTEX,   16.90564,  -6.01136, 110.90456,
     VERTEX,   17.42392,  -6.76390, 111.19897,
     VERTEX,   17.97676,  -7.49023, 110.90166,
     VERTEX,   18.35301,  -7.91293, 110.12618,
     VERTEX,   18.40894,  -7.87054, 109.16875,
     VERTEX,   18.12319,  -7.37925, 108.39507,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  17.51441,  -6.69531, 109.64982,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.41599,   2.30217, 106.76205,
                       
     VERTEX,   17.78078,  -1.51653, 105.68938,
     VERTEX,   17.23229,  -0.78886, 105.38729,
     VERTEX,   16.69810,  -0.04613, 105.67815,
     VERTEX,   16.38227,   0.42797, 106.45085,
     VERTEX,   16.40542,   0.45234, 107.41026,
     VERTEX,   16.75872,   0.01769, 108.18992,
     VERTEX,   17.30721,  -0.70998, 108.49201,
     VERTEX,   17.84140,  -1.45271, 108.20115,
     VERTEX,   18.15723,  -1.92681, 107.42844,
     VERTEX,   18.13408,  -1.95118, 106.46903,
     VERTEX,   17.78078,  -1.51653, 105.68938,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.26975,  -0.74942, 106.93965,
                       
     VERTEX,   17.78078,  -1.51653, 105.68938,
     VERTEX,   17.23229,  -0.78886, 105.38729,
     VERTEX,   16.69810,  -0.04613, 105.67815,
     VERTEX,   16.38227,   0.42797, 106.45085,
     VERTEX,   16.40542,   0.45234, 107.41026,
     VERTEX,   16.75872,   0.01769, 108.18992,
     VERTEX,   17.30721,  -0.70998, 108.49201,
     VERTEX,   17.84140,  -1.45271, 108.20115,
     VERTEX,   18.15723,  -1.92681, 107.42844,
     VERTEX,   18.13408,  -1.95118, 106.46903,
     VERTEX,   17.78078,  -1.51653, 105.68938,
                       
     END,              
                       
     CYLINDER,   10.56100,  -5.68700, 107.22700,  17.26975,  -0.74942, 106.93965,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -2.96731,  27.25382,  20.92789,
                       
     VERTEX,    2.05534,  28.54065,  25.17316,
     VERTEX,    1.70508,  29.43378,  25.20829,
     VERTEX,    1.65258,  30.26665,  24.73377,
     VERTEX,    1.91788,  30.72114,  23.93086,
     VERTEX,    2.39966,  30.62364,  23.10625,
     VERTEX,    2.91388,  30.01139,  22.57491,
     VERTEX,    3.26414,  29.11826,  22.53978,
     VERTEX,    3.31664,  28.28538,  23.01430,
     VERTEX,    3.05134,  27.83090,  23.81721,
     VERTEX,    2.56956,  27.92840,  24.64182,
     VERTEX,    2.05534,  28.54065,  25.17316,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    2.48461,  29.27602,  23.87403,
                       
     VERTEX,    2.05534,  28.54065,  25.17316,
     VERTEX,    1.70508,  29.43378,  25.20829,
     VERTEX,    1.65258,  30.26665,  24.73377,
     VERTEX,    1.91788,  30.72114,  23.93086,
     VERTEX,    2.39966,  30.62364,  23.10625,
     VERTEX,    2.91388,  30.01139,  22.57491,
     VERTEX,    3.26414,  29.11826,  22.53978,
     VERTEX,    3.31664,  28.28538,  23.01430,
     VERTEX,    3.05134,  27.83090,  23.81721,
     VERTEX,    2.56956,  27.92840,  24.64182,
     VERTEX,    2.05534,  28.54065,  25.17316,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,   2.48461,  29.27602,  23.87403,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.38802,  44.74364,  34.26609,
                       
     VERTEX,   25.97596,  44.10220,  40.80083,
     VERTEX,   26.61588,  44.71995,  40.43960,
     VERTEX,   27.36877,  44.80201,  39.84966,
     VERTEX,   27.94705,  44.31705,  39.25636,
     VERTEX,   28.12983,  43.45030,  38.88631,
     VERTEX,   27.84731,  42.53284,  38.88086,
     VERTEX,   27.20738,  41.91509,  39.24210,
     VERTEX,   26.45449,  41.83302,  39.83203,
     VERTEX,   25.87622,  42.31799,  40.42533,
     VERTEX,   25.69343,  43.18473,  40.79538,
     VERTEX,   25.97596,  44.10220,  40.80083,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.91163,  43.31752,  39.84085,
                       
     VERTEX,   25.97596,  44.10220,  40.80083,
     VERTEX,   26.61588,  44.71995,  40.43960,
     VERTEX,   27.36877,  44.80201,  39.84966,
     VERTEX,   27.94705,  44.31705,  39.25636,
     VERTEX,   28.12983,  43.45030,  38.88631,
     VERTEX,   27.84731,  42.53284,  38.88086,
     VERTEX,   27.20738,  41.91509,  39.24210,
     VERTEX,   26.45449,  41.83302,  39.83203,
     VERTEX,   25.87622,  42.31799,  40.42533,
     VERTEX,   25.69343,  43.18473,  40.79538,
     VERTEX,   25.97596,  44.10220,  40.80083,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  26.91163,  43.31752,  39.84085,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.60505,  46.81331,  36.52784,
                       
     VERTEX,   11.46536,  46.67814,  42.41326,
     VERTEX,   11.76008,  47.55650,  42.16183,
     VERTEX,   12.35096,  48.04065,  41.58041,
     VERTEX,   13.01232,  47.94565,  40.89107,
     VERTEX,   13.49152,  47.30779,  40.35712,
     VERTEX,   13.60554,  46.37071,  40.18252,
     VERTEX,   13.31083,  45.49235,  40.43395,
     VERTEX,   12.71994,  45.00820,  41.01538,
     VERTEX,   12.05859,  45.10320,  41.70472,
     VERTEX,   11.57938,  45.74106,  42.23866,
     VERTEX,   11.46536,  46.67814,  42.41326,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.53545,  46.52443,  41.29789,
                       
     VERTEX,   11.46536,  46.67814,  42.41326,
     VERTEX,   11.76008,  47.55650,  42.16183,
     VERTEX,   12.35096,  48.04065,  41.58041,
     VERTEX,   13.01232,  47.94565,  40.89107,
     VERTEX,   13.49152,  47.30779,  40.35712,
     VERTEX,   13.60554,  46.37071,  40.18252,
     VERTEX,   13.31083,  45.49235,  40.43395,
     VERTEX,   12.71994,  45.00820,  41.01538,
     VERTEX,   12.05859,  45.10320,  41.70472,
     VERTEX,   11.57938,  45.74106,  42.23866,
     VERTEX,   11.46536,  46.67814,  42.41326,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  12.53545,  46.52443,  41.29789,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    0.52001,  43.05116,  25.55983,
                       
     VERTEX,    5.59067,  43.65318,  31.15821,
     VERTEX,    5.51058,  44.60326,  31.04627,
     VERTEX,    5.78306,  45.34710,  30.50400,
     VERTEX,    6.30403,  45.60057,  29.73853,
     VERTEX,    6.87449,  45.26687,  29.04224,
     VERTEX,    7.27654,  44.47344,  28.68110,
     VERTEX,    7.35662,  43.52336,  28.79304,
     VERTEX,    7.08415,  42.77952,  29.33531,
     VERTEX,    6.56318,  42.52605,  30.10078,
     VERTEX,    5.99272,  42.85975,  30.79707,
     VERTEX,    5.59067,  43.65318,  31.15821,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.43360,  44.06331,  29.91965,
                       
     VERTEX,    5.59067,  43.65318,  31.15821,
     VERTEX,    5.51058,  44.60326,  31.04627,
     VERTEX,    5.78306,  45.34710,  30.50400,
     VERTEX,    6.30403,  45.60057,  29.73853,
     VERTEX,    6.87449,  45.26687,  29.04224,
     VERTEX,    7.27654,  44.47344,  28.68110,
     VERTEX,    7.35662,  43.52336,  28.79304,
     VERTEX,    7.08415,  42.77952,  29.33531,
     VERTEX,    6.56318,  42.52605,  30.10078,
     VERTEX,    5.99272,  42.85975,  30.79707,
     VERTEX,    5.59067,  43.65318,  31.15821,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,   6.43360,  44.06331,  29.91965,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.33211,  29.80227,  19.05303,
                       
     VERTEX,   18.64893,  30.10687,  24.50962,
     VERTEX,   18.66728,  31.05460,  24.35775,
     VERTEX,   19.03874,  31.74542,  23.80423,
     VERTEX,   19.62143,  31.91546,  23.06049,
     VERTEX,   20.19277,  31.49976,  22.41059,
     VERTEX,   20.53455,  30.65712,  22.10280,
     VERTEX,   20.51620,  29.70938,  22.25467,
     VERTEX,   20.14474,  29.01856,  22.80819,
     VERTEX,   19.56205,  28.84853,  23.55194,
     VERTEX,   18.99071,  29.26422,  24.20183,
     VERTEX,   18.64893,  30.10687,  24.50962,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.59174,  30.38199,  23.30621,
                       
     VERTEX,   18.64893,  30.10687,  24.50962,
     VERTEX,   18.66728,  31.05460,  24.35775,
     VERTEX,   19.03874,  31.74542,  23.80423,
     VERTEX,   19.62143,  31.91546,  23.06049,
     VERTEX,   20.19277,  31.49976,  22.41059,
     VERTEX,   20.53455,  30.65712,  22.10280,
     VERTEX,   20.51620,  29.70938,  22.25467,
     VERTEX,   20.14474,  29.01856,  22.80819,
     VERTEX,   19.56205,  28.84853,  23.55194,
     VERTEX,   18.99071,  29.26422,  24.20183,
     VERTEX,   18.64893,  30.10687,  24.50962,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  19.59174,  30.38199,  23.30621,   0.80000,
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
                       
     SPHERE,   -1.75900,  -3.55600, 111.81300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    0.09700,  -8.21000, 110.75600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.27000, -18.21500, 108.35800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.28800, -11.92800, 108.99600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.56100,  -5.68700, 107.22700,   0.80000,
                       
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
