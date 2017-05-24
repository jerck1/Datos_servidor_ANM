from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.42338, -63.47903,  35.72427,
                       
     VERTEX,   21.72820, -60.71021,  35.93410,
     VERTEX,   21.23044, -59.94561,  36.23284,
     VERTEX,   20.64581, -59.23961,  35.94758,
     VERTEX,   20.19762, -58.86186,  35.18729,
     VERTEX,   20.05706, -58.95666,  34.24238,
     VERTEX,   20.27782, -59.48779,  33.47377,
     VERTEX,   20.77558, -60.25238,  33.17504,
     VERTEX,   21.36021, -60.95839,  33.46030,
     VERTEX,   21.80840, -61.33613,  34.22058,
     VERTEX,   21.94896, -61.24134,  35.16550,
     VERTEX,   21.72820, -60.71021,  35.93410,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.00301, -60.09900,  34.70394,
                       
     VERTEX,   21.72820, -60.71021,  35.93410,
     VERTEX,   21.23044, -59.94561,  36.23284,
     VERTEX,   20.64581, -59.23961,  35.94758,
     VERTEX,   20.19762, -58.86186,  35.18729,
     VERTEX,   20.05706, -58.95666,  34.24238,
     VERTEX,   20.27782, -59.48779,  33.47377,
     VERTEX,   20.77558, -60.25238,  33.17504,
     VERTEX,   21.36021, -60.95839,  33.46030,
     VERTEX,   21.80840, -61.33613,  34.22058,
     VERTEX,   21.94896, -61.24134,  35.16550,
     VERTEX,   21.72820, -60.71021,  35.93410,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  21.00301, -60.09900,  34.70394,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -4.26235, -76.03238,  58.89002,
                       
     VERTEX,    0.63429, -74.30749,  55.43399,
     VERTEX,    0.30027, -73.41376,  55.54013,
     VERTEX,   -0.37234, -72.79581,  55.24462,
     VERTEX,   -1.12664, -72.68967,  54.66035,
     VERTEX,   -1.67449, -73.13591,  54.01048,
     VERTEX,   -1.80665, -73.96406,  53.54324,
     VERTEX,   -1.47263, -74.85779,  53.43710,
     VERTEX,   -0.80001, -75.47574,  53.73261,
     VERTEX,   -0.04572, -75.58187,  54.31689,
     VERTEX,    0.50214, -75.13564,  54.96676,
     VERTEX,    0.63429, -74.30749,  55.43399,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.58618, -74.13577,  54.48862,
                       
     VERTEX,    0.63429, -74.30749,  55.43399,
     VERTEX,    0.30027, -73.41376,  55.54013,
     VERTEX,   -0.37234, -72.79581,  55.24462,
     VERTEX,   -1.12664, -72.68967,  54.66035,
     VERTEX,   -1.67449, -73.13591,  54.01048,
     VERTEX,   -1.80665, -73.96406,  53.54324,
     VERTEX,   -1.47263, -74.85779,  53.43710,
     VERTEX,   -0.80001, -75.47574,  53.73261,
     VERTEX,   -0.04572, -75.58187,  54.31689,
     VERTEX,    0.50214, -75.13564,  54.96676,
     VERTEX,    0.63429, -74.30749,  55.43399,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  -0.58618, -74.13577,  54.48862,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.81602, -81.68083,  54.48961,
                       
     VERTEX,   13.84704, -79.64643,  52.10659,
     VERTEX,   13.48025, -78.77444,  52.27000,
     VERTEX,   12.83550, -78.13300,  51.96266,
     VERTEX,   12.15907, -77.96712,  51.30196,
     VERTEX,   11.70933, -78.34015,  50.54026,
     VERTEX,   11.65807, -79.10962,  49.96851,
     VERTEX,   12.02487, -79.98160,  49.80510,
     VERTEX,   12.66961, -80.62304,  50.11243,
     VERTEX,   13.34604, -80.78893,  50.77314,
     VERTEX,   13.79578, -80.41589,  51.53484,
     VERTEX,   13.84704, -79.64643,  52.10659,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.75256, -79.37802,  51.03755,
                       
     VERTEX,   13.84704, -79.64643,  52.10659,
     VERTEX,   13.48025, -78.77444,  52.27000,
     VERTEX,   12.83550, -78.13300,  51.96266,
     VERTEX,   12.15907, -77.96712,  51.30196,
     VERTEX,   11.70933, -78.34015,  50.54026,
     VERTEX,   11.65807, -79.10962,  49.96851,
     VERTEX,   12.02487, -79.98160,  49.80510,
     VERTEX,   12.66961, -80.62304,  50.11243,
     VERTEX,   13.34604, -80.78893,  50.77314,
     VERTEX,   13.79578, -80.41589,  51.53484,
     VERTEX,   13.84704, -79.64643,  52.10659,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  12.75256, -79.37802,  51.03755,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.19941, -78.46926,  41.67149,
                       
     VERTEX,   16.90998, -75.69626,  40.23198,
     VERTEX,   16.48660, -74.86777,  40.46854,
     VERTEX,   15.87233, -74.19518,  40.16540,
     VERTEX,   15.30178, -73.93540,  39.43835,
     VERTEX,   14.99290, -74.18766,  38.56511,
     VERTEX,   15.06365, -74.85560,  37.87922,
     VERTEX,   15.48703, -75.68409,  37.64266,
     VERTEX,   16.10130, -76.35667,  37.94580,
     VERTEX,   16.67184, -76.61646,  38.67284,
     VERTEX,   16.98073, -76.36420,  39.54609,
     VERTEX,   16.90998, -75.69626,  40.23198,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.98681, -75.27592,  39.05560,
                       
     VERTEX,   16.90998, -75.69626,  40.23198,
     VERTEX,   16.48660, -74.86777,  40.46854,
     VERTEX,   15.87233, -74.19518,  40.16540,
     VERTEX,   15.30178, -73.93540,  39.43835,
     VERTEX,   14.99290, -74.18766,  38.56511,
     VERTEX,   15.06365, -74.85560,  37.87922,
     VERTEX,   15.48703, -75.68409,  37.64266,
     VERTEX,   16.10130, -76.35667,  37.94580,
     VERTEX,   16.67184, -76.61646,  38.67284,
     VERTEX,   16.98073, -76.36420,  39.54609,
     VERTEX,   16.90998, -75.69626,  40.23198,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  15.98681, -75.27592,  39.05560,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.06828, -62.02096,  41.23693,
                       
     VERTEX,    5.31671, -59.45935,  39.94372,
     VERTEX,    4.89386, -58.63071,  40.18066,
     VERTEX,    4.27787, -57.95902,  39.87900,
     VERTEX,    3.70404, -57.70086,  39.15397,
     VERTEX,    3.39154, -57.95483,  38.28251,
     VERTEX,    3.45974, -58.62392,  37.59748,
     VERTEX,    3.88259, -59.45257,  37.36055,
     VERTEX,    4.49858, -60.12426,  37.66221,
     VERTEX,    5.07242, -60.38242,  38.38723,
     VERTEX,    5.38492, -60.12845,  39.25869,
     VERTEX,    5.31671, -59.45935,  39.94372,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    4.38823, -59.04164,  38.77060,
                       
     VERTEX,    5.31671, -59.45935,  39.94372,
     VERTEX,    4.89386, -58.63071,  40.18066,
     VERTEX,    4.27787, -57.95902,  39.87900,
     VERTEX,    3.70404, -57.70086,  39.15397,
     VERTEX,    3.39154, -57.95483,  38.28251,
     VERTEX,    3.45974, -58.62392,  37.59748,
     VERTEX,    3.88259, -59.45257,  37.36055,
     VERTEX,    4.49858, -60.12426,  37.66221,
     VERTEX,    5.07242, -60.38242,  38.38723,
     VERTEX,    5.38492, -60.12845,  39.25869,
     VERTEX,    5.31671, -59.45935,  39.94372,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,   4.38823, -59.04164,  38.77060,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   53.03346, -49.32632, 124.06532,
                       
     VERTEX,   49.09016, -53.59798, 122.64687,
     VERTEX,   48.54466, -52.87835, 122.32104,
     VERTEX,   47.97179, -52.15570, 122.58788,
     VERTEX,   47.59036, -51.70607, 123.34547,
     VERTEX,   47.54607, -51.70119, 124.30444,
     VERTEX,   47.85583, -52.14294, 125.09849,
     VERTEX,   48.40132, -52.86257, 125.42432,
     VERTEX,   48.97419, -53.58521, 125.15748,
     VERTEX,   49.35562, -54.03484, 124.39989,
     VERTEX,   49.39992, -54.03972, 123.44093,
     VERTEX,   49.09016, -53.59798, 122.64687,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.47299, -52.87046, 123.87268,
                       
     VERTEX,   49.09016, -53.59798, 122.64687,
     VERTEX,   48.54466, -52.87835, 122.32104,
     VERTEX,   47.97179, -52.15570, 122.58788,
     VERTEX,   47.59036, -51.70607, 123.34547,
     VERTEX,   47.54607, -51.70119, 124.30444,
     VERTEX,   47.85583, -52.14294, 125.09849,
     VERTEX,   48.40132, -52.86257, 125.42432,
     VERTEX,   48.97419, -53.58521, 125.15748,
     VERTEX,   49.35562, -54.03484, 124.39989,
     VERTEX,   49.39992, -54.03972, 123.44093,
     VERTEX,   49.09016, -53.59798, 122.64687,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  48.47299, -52.87046, 123.87268,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   51.17823, -44.56967, 124.73576,
                       
     VERTEX,   47.20306, -48.90965, 123.48961,
     VERTEX,   46.64758, -48.19982, 123.15919,
     VERTEX,   46.07652, -47.47415, 123.42165,
     VERTEX,   45.70799, -47.00983, 124.17677,
     VERTEX,   45.68277, -46.98421, 125.13609,
     VERTEX,   46.01049, -47.40708, 125.93320,
     VERTEX,   46.56596, -48.11691, 126.26363,
     VERTEX,   47.13702, -48.84258, 126.00116,
     VERTEX,   47.50555, -49.30690, 125.24605,
     VERTEX,   47.53077, -49.33252, 124.28672,
     VERTEX,   47.20306, -48.90965, 123.48961,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.60677, -48.15836, 124.71141,
                       
     VERTEX,   47.20306, -48.90965, 123.48961,
     VERTEX,   46.64758, -48.19982, 123.15919,
     VERTEX,   46.07652, -47.47415, 123.42165,
     VERTEX,   45.70799, -47.00983, 124.17677,
     VERTEX,   45.68277, -46.98421, 125.13609,
     VERTEX,   46.01049, -47.40708, 125.93320,
     VERTEX,   46.56596, -48.11691, 126.26363,
     VERTEX,   47.13702, -48.84258, 126.00116,
     VERTEX,   47.50555, -49.30690, 125.24605,
     VERTEX,   47.53077, -49.33252, 124.28672,
     VERTEX,   47.20306, -48.90965, 123.48961,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  46.60677, -48.15836, 124.71141,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   74.85784, -60.45038, 112.87672,
                       
     VERTEX,   71.16661, -64.96481, 113.17636,
     VERTEX,   70.51714, -64.35548, 112.81786,
     VERTEX,   69.95029, -63.61062, 113.03105,
     VERTEX,   69.68257, -63.01471, 113.73449,
     VERTEX,   69.81625, -62.79539, 114.65948,
     VERTEX,   70.30025, -63.03642, 115.45274,
     VERTEX,   70.94972, -63.64573, 115.81123,
     VERTEX,   71.51658, -64.39060, 115.59805,
     VERTEX,   71.78429, -64.98650, 114.89461,
     VERTEX,   71.65062, -65.20583, 113.96961,
     VERTEX,   71.16661, -64.96481, 113.17636,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   70.73344, -64.00061, 114.31454,
                       
     VERTEX,   71.16661, -64.96481, 113.17636,
     VERTEX,   70.51714, -64.35548, 112.81786,
     VERTEX,   69.95029, -63.61062, 113.03105,
     VERTEX,   69.68257, -63.01471, 113.73449,
     VERTEX,   69.81625, -62.79539, 114.65948,
     VERTEX,   70.30025, -63.03642, 115.45274,
     VERTEX,   70.94972, -63.64573, 115.81123,
     VERTEX,   71.51658, -64.39060, 115.59805,
     VERTEX,   71.78429, -64.98650, 114.89461,
     VERTEX,   71.65062, -65.20583, 113.96961,
     VERTEX,   71.16661, -64.96481, 113.17636,
                       
     END,              
                       
     CYLINDER,   64.06000, -69.74500, 116.64100,  70.73344, -64.00061, 114.31454,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.53732, -34.25338, 127.54785,
                       
     VERTEX,   37.38268, -38.69515, 126.08955,
     VERTEX,   36.83820, -37.97498, 125.76321,
     VERTEX,   36.26369, -37.25341, 126.02941,
     VERTEX,   35.87858, -36.80604, 126.78648,
     VERTEX,   35.82999, -36.80376, 127.74525,
     VERTEX,   36.13646, -37.24743, 128.53949,
     VERTEX,   36.68093, -37.96760, 128.86584,
     VERTEX,   37.25544, -38.68918, 128.59964,
     VERTEX,   37.64054, -39.13655, 127.84257,
     VERTEX,   37.68914, -39.13883, 126.88380,
     VERTEX,   37.38268, -38.69515, 126.08955,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.75956, -37.97129, 127.31452,
                       
     VERTEX,   37.38268, -38.69515, 126.08955,
     VERTEX,   36.83820, -37.97498, 125.76321,
     VERTEX,   36.26369, -37.25341, 126.02941,
     VERTEX,   35.87858, -36.80604, 126.78648,
     VERTEX,   35.82999, -36.80376, 127.74525,
     VERTEX,   36.13646, -37.24743, 128.53949,
     VERTEX,   36.68093, -37.96760, 128.86584,
     VERTEX,   37.25544, -38.68918, 128.59964,
     VERTEX,   37.64054, -39.13655, 127.84257,
     VERTEX,   37.68914, -39.13883, 126.88380,
     VERTEX,   37.38268, -38.69515, 126.08955,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  36.75956, -37.97129, 127.31452,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.97551, -40.89233, 126.81303,
                       
     VERTEX,   37.11266, -44.97998, 124.79272,
     VERTEX,   36.60032, -44.22974, 124.48247,
     VERTEX,   36.01647, -43.51995, 124.75981,
     VERTEX,   35.58413, -43.12173, 125.51882,
     VERTEX,   35.46843, -43.18716, 126.46957,
     VERTEX,   35.71357, -43.69128, 127.24892,
     VERTEX,   36.22591, -44.44152, 127.55917,
     VERTEX,   36.80976, -45.15131, 127.28182,
     VERTEX,   37.24210, -45.54954, 126.52281,
     VERTEX,   37.35780, -45.48410, 125.57206,
     VERTEX,   37.11266, -44.97998, 124.79272,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.41311, -44.33563, 126.02082,
                       
     VERTEX,   37.11266, -44.97998, 124.79272,
     VERTEX,   36.60032, -44.22974, 124.48247,
     VERTEX,   36.01647, -43.51995, 124.75981,
     VERTEX,   35.58413, -43.12173, 125.51882,
     VERTEX,   35.46843, -43.18716, 126.46957,
     VERTEX,   35.71357, -43.69128, 127.24892,
     VERTEX,   36.22591, -44.44152, 127.55917,
     VERTEX,   36.80976, -45.15131, 127.28182,
     VERTEX,   37.24210, -45.54954, 126.52281,
     VERTEX,   37.35780, -45.48410, 125.57206,
     VERTEX,   37.11266, -44.97998, 124.79272,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  36.41311, -44.33563, 126.02082,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -25.24253, -23.96705,  86.61432,
                       
     VERTEX,  -22.57669, -23.63966,  90.98677,
     VERTEX,  -22.83042, -22.71401,  90.96677,
     VERTEX,  -22.67030, -21.87407,  90.53035,
     VERTEX,  -22.15750, -21.44067,  89.84421,
     VERTEX,  -21.48788, -21.57934,  89.17043,
     VERTEX,  -20.91722, -22.23713,  88.76637,
     VERTEX,  -20.66350, -23.16278,  88.78636,
     VERTEX,  -20.82361, -24.00272,  89.22279,
     VERTEX,  -21.33642, -24.43612,  89.90893,
     VERTEX,  -22.00603, -24.29745,  90.58271,
     VERTEX,  -22.57669, -23.63966,  90.98677,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -21.74696, -22.93839,  89.87656,
                       
     VERTEX,  -22.57669, -23.63966,  90.98677,
     VERTEX,  -22.83042, -22.71401,  90.96677,
     VERTEX,  -22.67030, -21.87407,  90.53035,
     VERTEX,  -22.15750, -21.44067,  89.84421,
     VERTEX,  -21.48788, -21.57934,  89.17043,
     VERTEX,  -20.91722, -22.23713,  88.76637,
     VERTEX,  -20.66350, -23.16278,  88.78636,
     VERTEX,  -20.82361, -24.00272,  89.22279,
     VERTEX,  -21.33642, -24.43612,  89.90893,
     VERTEX,  -22.00603, -24.29745,  90.58271,
     VERTEX,  -22.57669, -23.63966,  90.98677,
                       
     END,              
                       
     CYLINDER,  -16.09100, -21.27400,  95.15500, -21.74696, -22.93839,  89.87656,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -10.84568,  -4.46153, 110.90824,
                       
     VERTEX,   -6.29630,  -2.44504, 112.51910,
     VERTEX,   -6.82595,  -1.68884, 112.78223,
     VERTEX,   -7.31169,  -0.92876, 112.45367,
     VERTEX,   -7.56800,  -0.45514, 111.65895,
     VERTEX,   -7.49697,  -0.44888, 110.70160,
     VERTEX,   -7.12573,  -0.91237, 109.94730,
     VERTEX,   -6.59609,  -1.66858, 109.68418,
     VERTEX,   -6.11035,  -2.42865, 110.01273,
     VERTEX,   -5.85404,  -2.90227, 110.80746,
     VERTEX,   -5.92507,  -2.90853, 111.76480,
     VERTEX,   -6.29630,  -2.44504, 112.51910,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.71102,  -1.67871, 111.23320,
                       
     VERTEX,   -6.29630,  -2.44504, 112.51910,
     VERTEX,   -6.82595,  -1.68884, 112.78223,
     VERTEX,   -7.31169,  -0.92876, 112.45367,
     VERTEX,   -7.56800,  -0.45514, 111.65895,
     VERTEX,   -7.49697,  -0.44888, 110.70160,
     VERTEX,   -7.12573,  -0.91237, 109.94730,
     VERTEX,   -6.59609,  -1.66858, 109.68418,
     VERTEX,   -6.11035,  -2.42865, 110.01273,
     VERTEX,   -5.85404,  -2.90227, 110.80746,
     VERTEX,   -5.92507,  -2.90853, 111.76480,
     VERTEX,   -6.29630,  -2.44504, 112.51910,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,  -6.71102,  -1.67871, 111.23320,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -12.99506, -10.80926, 109.30193,
                       
     VERTEX,   -8.44870,  -8.87715, 111.54369,
     VERTEX,   -8.99011,  -8.12213, 111.78539,
     VERTEX,   -9.42196,  -7.33527, 111.44487,
     VERTEX,   -9.57928,  -6.81712, 110.65217,
     VERTEX,   -9.40201,  -6.76559, 109.71009,
     VERTEX,   -8.95783,  -7.20038, 108.97847,
     VERTEX,   -8.41642,  -7.95539, 108.73676,
     VERTEX,   -7.98458,  -8.74226, 109.07729,
     VERTEX,   -7.82725,  -9.26041, 109.86998,
     VERTEX,   -8.00453,  -9.31193, 110.81206,
     VERTEX,   -8.44870,  -8.87715, 111.54369,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -8.70327,  -8.03876, 110.26108,
                       
     VERTEX,   -8.44870,  -8.87715, 111.54369,
     VERTEX,   -8.99011,  -8.12213, 111.78539,
     VERTEX,   -9.42196,  -7.33527, 111.44487,
     VERTEX,   -9.57928,  -6.81712, 110.65217,
     VERTEX,   -9.40201,  -6.76559, 109.71009,
     VERTEX,   -8.95783,  -7.20038, 108.97847,
     VERTEX,   -8.41642,  -7.95539, 108.73676,
     VERTEX,   -7.98458,  -8.74226, 109.07729,
     VERTEX,   -7.82725,  -9.26041, 109.86998,
     VERTEX,   -8.00453,  -9.31193, 110.81206,
     VERTEX,   -8.44870,  -8.87715, 111.54369,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,  -8.70327,  -8.03876, 110.26108,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.05391, -15.54764, 107.73983,
                       
     VERTEX,   -6.56418, -13.61539, 110.15758,
     VERTEX,   -7.11985, -12.87281, 110.40540,
     VERTEX,   -7.55130, -12.08138, 110.07511,
     VERTEX,   -7.69373, -11.54340, 109.29288,
     VERTEX,   -7.49274, -11.46435, 108.35749,
     VERTEX,   -7.02509, -11.87443, 107.62623,
     VERTEX,   -6.46943, -12.61700, 107.37841,
     VERTEX,   -6.03798, -13.40844, 107.70870,
     VERTEX,   -5.89555, -13.94642, 108.49093,
     VERTEX,   -6.09654, -14.02547, 109.42632,
     VERTEX,   -6.56418, -13.61539, 110.15758,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.79464, -12.74491, 108.89191,
                       
     VERTEX,   -6.56418, -13.61539, 110.15758,
     VERTEX,   -7.11985, -12.87281, 110.40540,
     VERTEX,   -7.55130, -12.08138, 110.07511,
     VERTEX,   -7.69373, -11.54340, 109.29288,
     VERTEX,   -7.49274, -11.46435, 108.35749,
     VERTEX,   -7.02509, -11.87443, 107.62623,
     VERTEX,   -6.46943, -12.61700, 107.37841,
     VERTEX,   -6.03798, -13.40844, 107.70870,
     VERTEX,   -5.89555, -13.94642, 108.49093,
     VERTEX,   -6.09654, -14.02547, 109.42632,
     VERTEX,   -6.56418, -13.61539, 110.15758,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,  -6.79464, -12.74491, 108.89191,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.65177, -19.62258, 107.71713,
                       
     VERTEX,    3.94204, -17.48402, 109.47037,
     VERTEX,    3.39222, -16.74907, 109.75170,
     VERTEX,    2.89382, -15.98908, 109.44248,
     VERTEX,    2.63722, -15.49434, 108.66082,
     VERTEX,    2.72043, -15.45382, 107.70529,
     VERTEX,    3.11166, -15.88301, 106.94087,
     VERTEX,    3.66148, -16.61796, 106.65954,
     VERTEX,    4.15987, -17.37795, 106.96876,
     VERTEX,    4.41648, -17.87269, 107.75042,
     VERTEX,    4.33327, -17.91320, 108.70595,
     VERTEX,    3.94204, -17.48402, 109.47037,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.52685, -16.68351, 108.20562,
                       
     VERTEX,    3.94204, -17.48402, 109.47037,
     VERTEX,    3.39222, -16.74907, 109.75170,
     VERTEX,    2.89382, -15.98908, 109.44248,
     VERTEX,    2.63722, -15.49434, 108.66082,
     VERTEX,    2.72043, -15.45382, 107.70529,
     VERTEX,    3.11166, -15.88301, 106.94087,
     VERTEX,    3.66148, -16.61796, 106.65954,
     VERTEX,    4.15987, -17.37795, 106.96876,
     VERTEX,    4.41648, -17.87269, 107.75042,
     VERTEX,    4.33327, -17.91320, 108.70595,
     VERTEX,    3.94204, -17.48402, 109.47037,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,   3.52685, -16.68351, 108.20562,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.37392,  38.45201,  36.34842,
                       
     VERTEX,   20.82859,  35.89254,  32.12603,
     VERTEX,   20.49154,  36.78860,  32.05482,
     VERTEX,   19.96691,  37.45865,  32.49913,
     VERTEX,   19.45510,  37.64674,  33.28923,
     VERTEX,   19.15159,  37.28104,  34.12334,
     VERTEX,   19.17232,  36.50122,  34.68286,
     VERTEX,   19.50937,  35.60516,  34.75407,
     VERTEX,   20.03399,  34.93512,  34.30976,
     VERTEX,   20.54581,  34.74702,  33.51966,
     VERTEX,   20.84931,  35.11272,  32.68555,
     VERTEX,   20.82859,  35.89254,  32.12603,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.00045,  36.19688,  33.40445,
                       
     VERTEX,   20.82859,  35.89254,  32.12603,
     VERTEX,   20.49154,  36.78860,  32.05482,
     VERTEX,   19.96691,  37.45865,  32.49913,
     VERTEX,   19.45510,  37.64674,  33.28923,
     VERTEX,   19.15159,  37.28104,  34.12334,
     VERTEX,   19.17232,  36.50122,  34.68286,
     VERTEX,   19.50937,  35.60516,  34.75407,
     VERTEX,   20.03399,  34.93512,  34.30976,
     VERTEX,   20.54581,  34.74702,  33.51966,
     VERTEX,   20.84931,  35.11272,  32.68555,
     VERTEX,   20.82859,  35.89254,  32.12603,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,  20.00045,  36.19688,  33.40445,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.91927,  37.70377,  63.52150,
                       
     VERTEX,   42.67731,  39.06019,  56.96808,
     VERTEX,   42.49881,  39.93978,  57.30875,
     VERTEX,   41.92152,  40.44766,  57.88354,
     VERTEX,   41.16593,  40.38984,  58.47291,
     VERTEX,   40.52066,  39.78840,  58.85172,
     VERTEX,   40.23219,  38.87308,  58.87529,
     VERTEX,   40.41068,  37.99348,  58.53461,
     VERTEX,   40.98798,  37.48560,  57.95982,
     VERTEX,   41.74356,  37.54343,  57.37046,
     VERTEX,   42.38883,  38.14487,  56.99165,
     VERTEX,   42.67731,  39.06019,  56.96808,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.45475,  38.96663,  57.92168,
                       
     VERTEX,   42.67731,  39.06019,  56.96808,
     VERTEX,   42.49881,  39.93978,  57.30875,
     VERTEX,   41.92152,  40.44766,  57.88354,
     VERTEX,   41.16593,  40.38984,  58.47291,
     VERTEX,   40.52066,  39.78840,  58.85172,
     VERTEX,   40.23219,  38.87308,  58.87529,
     VERTEX,   40.41068,  37.99348,  58.53461,
     VERTEX,   40.98798,  37.48560,  57.95982,
     VERTEX,   41.74356,  37.54343,  57.37046,
     VERTEX,   42.38883,  38.14487,  56.99165,
     VERTEX,   42.67731,  39.06019,  56.96808,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  41.45475,  38.96663,  57.92168,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.23167,  45.74049,  61.61258,
                       
     VERTEX,   29.46674,  45.87284,  55.69764,
     VERTEX,   29.26469,  46.78350,  55.92453,
     VERTEX,   28.72227,  47.34194,  56.48624,
     VERTEX,   28.04666,  47.33487,  57.16822,
     VERTEX,   27.49592,  46.76497,  57.70998,
     VERTEX,   27.28041,  45.84993,  57.90459,
     VERTEX,   27.48246,  44.93927,  57.67770,
     VERTEX,   28.02488,  44.38083,  57.11599,
     VERTEX,   28.70049,  44.38791,  56.43401,
     VERTEX,   29.25123,  44.95780,  55.89225,
     VERTEX,   29.46674,  45.87284,  55.69764,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.37357,  45.86139,  56.80111,
                       
     VERTEX,   29.46674,  45.87284,  55.69764,
     VERTEX,   29.26469,  46.78350,  55.92453,
     VERTEX,   28.72227,  47.34194,  56.48624,
     VERTEX,   28.04666,  47.33487,  57.16822,
     VERTEX,   27.49592,  46.76497,  57.70998,
     VERTEX,   27.28041,  45.84993,  57.90459,
     VERTEX,   27.48246,  44.93927,  57.67770,
     VERTEX,   28.02488,  44.38083,  57.11599,
     VERTEX,   28.70049,  44.38791,  56.43401,
     VERTEX,   29.25123,  44.95780,  55.89225,
     VERTEX,   29.46674,  45.87284,  55.69764,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  28.37357,  45.86139,  56.80111,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.27919,  48.90264,  48.52190,
                       
     VERTEX,   26.39413,  47.55335,  42.88882,
     VERTEX,   26.13836,  48.47493,  42.97168,
     VERTEX,   25.61730,  49.09277,  43.48973,
     VERTEX,   25.02997,  49.17087,  44.24507,
     VERTEX,   24.60072,  48.67941,  44.94920,
     VERTEX,   24.49350,  47.80609,  45.33317,
     VERTEX,   24.74928,  46.88451,  45.25031,
     VERTEX,   25.27034,  46.26667,  44.73226,
     VERTEX,   25.85767,  46.18857,  43.97692,
     VERTEX,   26.28692,  46.68004,  43.27279,
     VERTEX,   26.39413,  47.55335,  42.88882,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.44382,  47.67972,  44.11100,
                       
     VERTEX,   26.39413,  47.55335,  42.88882,
     VERTEX,   26.13836,  48.47493,  42.97168,
     VERTEX,   25.61730,  49.09277,  43.48973,
     VERTEX,   25.02997,  49.17087,  44.24507,
     VERTEX,   24.60072,  48.67941,  44.94920,
     VERTEX,   24.49350,  47.80609,  45.33317,
     VERTEX,   24.74928,  46.88451,  45.25031,
     VERTEX,   25.27034,  46.26667,  44.73226,
     VERTEX,   25.85767,  46.18857,  43.97692,
     VERTEX,   26.28692,  46.68004,  43.27279,
     VERTEX,   26.39413,  47.55335,  42.88882,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,  25.44382,  47.67972,  44.11100,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.71265,  33.46479,  41.30391,
                       
     VERTEX,   37.50317,  32.55668,  35.86381,
     VERTEX,   37.26199,  33.47844,  35.98127,
     VERTEX,   36.73504,  34.08206,  36.51001,
     VERTEX,   36.12360,  34.13699,  37.24807,
     VERTEX,   35.66123,  33.62224,  37.91353,
     VERTEX,   35.52452,  32.73443,  38.25222,
     VERTEX,   35.76571,  31.81267,  38.13476,
     VERTEX,   36.29266,  31.20905,  37.60601,
     VERTEX,   36.90409,  31.15412,  36.86796,
     VERTEX,   37.36646,  31.66887,  36.20249,
     VERTEX,   37.50317,  32.55668,  35.86381,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.51385,  32.64555,  37.05801,
                       
     VERTEX,   37.50317,  32.55668,  35.86381,
     VERTEX,   37.26199,  33.47844,  35.98127,
     VERTEX,   36.73504,  34.08206,  36.51001,
     VERTEX,   36.12360,  34.13699,  37.24807,
     VERTEX,   35.66123,  33.62224,  37.91353,
     VERTEX,   35.52452,  32.73443,  38.25222,
     VERTEX,   35.76571,  31.81267,  38.13476,
     VERTEX,   36.29266,  31.20905,  37.60601,
     VERTEX,   36.90409,  31.15412,  36.86796,
     VERTEX,   37.36646,  31.66887,  36.20249,
     VERTEX,   37.50317,  32.55668,  35.86381,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  36.51385,  32.64555,  37.05801,   0.80000,
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
