from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.13020, -54.88709,  35.49469,
                       
     VERTEX,   21.12515, -54.81505,  36.08523,
     VERTEX,   21.05184, -53.89736,  35.81306,
     VERTEX,   20.89067, -53.32021,  35.06306,
     VERTEX,   20.70319, -53.30404,  34.12168,
     VERTEX,   20.56103, -53.85503,  33.34851,
     VERTEX,   20.51847, -54.76273,  33.03886,
     VERTEX,   20.59178, -55.68042,  33.31103,
     VERTEX,   20.75296, -56.25757,  34.06104,
     VERTEX,   20.94043, -56.27374,  35.00241,
     VERTEX,   21.08260, -55.72275,  35.77559,
     VERTEX,   21.12515, -54.81505,  36.08523,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.82181, -54.78889,  34.56205,
                       
     VERTEX,   21.12515, -54.81505,  36.08523,
     VERTEX,   21.05184, -53.89736,  35.81306,
     VERTEX,   20.89067, -53.32021,  35.06306,
     VERTEX,   20.70319, -53.30404,  34.12168,
     VERTEX,   20.56103, -53.85503,  33.34851,
     VERTEX,   20.51847, -54.76273,  33.03886,
     VERTEX,   20.59178, -55.68042,  33.31103,
     VERTEX,   20.75296, -56.25757,  34.06104,
     VERTEX,   20.94043, -56.27374,  35.00241,
     VERTEX,   21.08260, -55.72275,  35.77559,
     VERTEX,   21.12515, -54.81505,  36.08523,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  20.82181, -54.78889,  34.56205,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.91822, -47.50876,  35.12889,
                       
     VERTEX,   29.37605, -47.39273,  36.59285,
     VERTEX,   29.33401, -46.46954,  36.33292,
     VERTEX,   29.29534, -45.87579,  35.57956,
     VERTEX,   29.27481, -45.83825,  34.62051,
     VERTEX,   29.28026, -46.37128,  33.82211,
     VERTEX,   29.30961, -47.27127,  33.48931,
     VERTEX,   29.35164, -48.19446,  33.74923,
     VERTEX,   29.39032, -48.78822,  34.50260,
     VERTEX,   29.41085, -48.82575,  35.46165,
     VERTEX,   29.40540, -48.29272,  36.26005,
     VERTEX,   29.37605, -47.39273,  36.59285,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.34283, -47.33200,  35.04108,
                       
     VERTEX,   29.37605, -47.39273,  36.59285,
     VERTEX,   29.33401, -46.46954,  36.33292,
     VERTEX,   29.29534, -45.87579,  35.57956,
     VERTEX,   29.27481, -45.83825,  34.62051,
     VERTEX,   29.28026, -46.37128,  33.82211,
     VERTEX,   29.30961, -47.27127,  33.48931,
     VERTEX,   29.35164, -48.19446,  33.74923,
     VERTEX,   29.39032, -48.78822,  34.50260,
     VERTEX,   29.41085, -48.82575,  35.46165,
     VERTEX,   29.40540, -48.29272,  36.26005,
     VERTEX,   29.37605, -47.39273,  36.59285,
                       
     END,              
                       
     CYLINDER,   36.50200, -47.04600,  34.89900,  29.34283, -47.33200,  35.04108,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -3.29609, -70.91232,  56.20356,
                       
     VERTEX,    1.12057, -70.96348,  53.91531,
     VERTEX,    0.91332, -70.05206,  53.69629,
     VERTEX,    0.36142, -69.49181,  53.14573,
     VERTEX,   -0.32433, -69.49670,  52.47392,
     VERTEX,   -0.88199, -70.06489,  51.93747,
     VERTEX,   -1.09855, -70.97933,  51.74129,
     VERTEX,   -0.89131, -71.89075,  51.96030,
     VERTEX,   -0.33941, -72.45101,  52.51086,
     VERTEX,    0.34634, -72.44611,  53.18267,
     VERTEX,    0.90400, -71.87792,  53.71912,
     VERTEX,    1.12057, -70.96348,  53.91531,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    0.01101, -70.97141,  52.82830,
                       
     VERTEX,    1.12057, -70.96348,  53.91531,
     VERTEX,    0.91332, -70.05206,  53.69629,
     VERTEX,    0.36142, -69.49181,  53.14573,
     VERTEX,   -0.32433, -69.49670,  52.47392,
     VERTEX,   -0.88199, -70.06489,  51.93747,
     VERTEX,   -1.09855, -70.97933,  51.74129,
     VERTEX,   -0.89131, -71.89075,  51.96030,
     VERTEX,   -0.33941, -72.45101,  52.51086,
     VERTEX,    0.34634, -72.44611,  53.18267,
     VERTEX,    0.90400, -71.87792,  53.71912,
     VERTEX,    1.12057, -70.96348,  53.91531,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,   0.01101, -70.97141,  52.82830,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.48462, -70.23393,  38.43624,
                       
     VERTEX,   16.60268, -70.19757,  38.54588,
     VERTEX,   16.51204, -69.28246,  38.27029,
     VERTEX,   16.28812, -68.71255,  37.53092,
     VERTEX,   16.01644, -68.70553,  36.61020,
     VERTEX,   15.80077, -69.26408,  35.85979,
     VERTEX,   15.72349, -70.17485,  35.56634,
     VERTEX,   15.81412, -71.08997,  35.84193,
     VERTEX,   16.03804, -71.65988,  36.58129,
     VERTEX,   16.30973, -71.66690,  37.50202,
     VERTEX,   16.52540, -71.10835,  38.25242,
     VERTEX,   16.60268, -70.19757,  38.54588,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.16308, -70.18621,  37.05611,
                       
     VERTEX,   16.60268, -70.19757,  38.54588,
     VERTEX,   16.51204, -69.28246,  38.27029,
     VERTEX,   16.28812, -68.71255,  37.53092,
     VERTEX,   16.01644, -68.70553,  36.61020,
     VERTEX,   15.80077, -69.26408,  35.85979,
     VERTEX,   15.72349, -70.17485,  35.56634,
     VERTEX,   15.81412, -71.08997,  35.84193,
     VERTEX,   16.03804, -71.65988,  36.58129,
     VERTEX,   16.30973, -71.66690,  37.50202,
     VERTEX,   16.52540, -71.10835,  38.25242,
     VERTEX,   16.60268, -70.19757,  38.54588,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  16.16308, -70.18621,  37.05611,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.27586, -54.12582,  42.04260,
                       
     VERTEX,    5.07040, -54.15622,  40.59363,
     VERTEX,    4.91912, -53.24437,  40.33431,
     VERTEX,    4.51604, -52.68309,  39.66791,
     VERTEX,    4.01515, -52.68677,  38.84895,
     VERTEX,    3.60775, -53.25401,  38.19026,
     VERTEX,    3.44946, -54.16813,  37.94344,
     VERTEX,    3.60075, -55.07998,  38.20275,
     VERTEX,    4.00382, -55.64125,  38.86916,
     VERTEX,    4.50472, -55.63758,  39.68811,
     VERTEX,    4.91212, -55.07034,  40.34680,
     VERTEX,    5.07040, -54.15622,  40.59363,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    4.25993, -54.16217,  39.26853,
                       
     VERTEX,    5.07040, -54.15622,  40.59363,
     VERTEX,    4.91912, -53.24437,  40.33431,
     VERTEX,    4.51604, -52.68309,  39.66791,
     VERTEX,    4.01515, -52.68677,  38.84895,
     VERTEX,    3.60775, -53.25401,  38.19026,
     VERTEX,    3.44946, -54.16813,  37.94344,
     VERTEX,    3.60075, -55.07998,  38.20275,
     VERTEX,    4.00382, -55.64125,  38.86916,
     VERTEX,    4.50472, -55.63758,  39.68811,
     VERTEX,    4.91212, -55.07034,  40.34680,
     VERTEX,    5.07040, -54.15622,  40.59363,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,   4.25993, -54.16217,  39.26853,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   56.92545, -60.71014, 121.85148,
                       
     VERTEX,   50.74291, -59.68149, 120.97344,
     VERTEX,   50.90078, -58.82891, 121.38550,
     VERTEX,   51.05008, -58.38776, 122.22496,
     VERTEX,   51.13380, -58.52655, 123.17118,
     VERTEX,   51.11996, -59.19226, 123.86273,
     VERTEX,   51.01384, -60.13061, 124.03547,
     VERTEX,   50.85597, -60.98318, 123.62341,
     VERTEX,   50.70667, -61.42433, 122.78394,
     VERTEX,   50.62295, -61.28554, 121.83773,
     VERTEX,   50.63679, -60.61983, 121.14618,
     VERTEX,   50.74291, -59.68149, 120.97344,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   50.87838, -59.90605, 122.50446,
                       
     VERTEX,   50.74291, -59.68149, 120.97344,
     VERTEX,   50.90078, -58.82891, 121.38550,
     VERTEX,   51.05008, -58.38776, 122.22496,
     VERTEX,   51.13380, -58.52655, 123.17118,
     VERTEX,   51.11996, -59.19226, 123.86273,
     VERTEX,   51.01384, -60.13061, 124.03547,
     VERTEX,   50.85597, -60.98318, 123.62341,
     VERTEX,   50.70667, -61.42433, 122.78394,
     VERTEX,   50.62295, -61.28554, 121.83773,
     VERTEX,   50.63679, -60.61983, 121.14618,
     VERTEX,   50.74291, -59.68149, 120.97344,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  50.87838, -59.90605, 122.50446,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   55.38777, -56.09946, 123.67467,
                       
     VERTEX,   49.14185, -55.07045, 122.51852,
     VERTEX,   49.28019, -54.21482, 122.93128,
     VERTEX,   49.39111, -53.76765, 123.77350,
     VERTEX,   49.43224, -53.89974, 124.72348,
     VERTEX,   49.38789, -54.56063, 125.41836,
     VERTEX,   49.27497, -55.49789, 125.59271,
     VERTEX,   49.13664, -56.35351, 125.17995,
     VERTEX,   49.02572, -56.80068, 124.33773,
     VERTEX,   48.98458, -56.66859, 123.38775,
     VERTEX,   49.02894, -56.00770, 122.69287,
     VERTEX,   49.14185, -55.07045, 122.51852,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.20841, -55.28417, 124.05562,
                       
     VERTEX,   49.14185, -55.07045, 122.51852,
     VERTEX,   49.28019, -54.21482, 122.93128,
     VERTEX,   49.39111, -53.76765, 123.77350,
     VERTEX,   49.43224, -53.89974, 124.72348,
     VERTEX,   49.38789, -54.56063, 125.41836,
     VERTEX,   49.27497, -55.49789, 125.59271,
     VERTEX,   49.13664, -56.35351, 125.17995,
     VERTEX,   49.02572, -56.80068, 124.33773,
     VERTEX,   48.98458, -56.66859, 123.38775,
     VERTEX,   49.02894, -56.00770, 122.69287,
     VERTEX,   49.14185, -55.07045, 122.51852,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  49.20841, -55.28417, 124.05562,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   77.67413, -71.65977, 107.12666,
                       
     VERTEX,   71.63733, -70.59225, 109.49599,
     VERTEX,   71.99470, -69.77122, 109.84211,
     VERTEX,   72.53514, -69.39220, 110.53915,
     VERTEX,   73.05222, -69.59994, 111.32085,
     VERTEX,   73.34844, -70.31511, 111.88864,
     VERTEX,   73.31065, -71.26453, 112.02564,
     VERTEX,   72.95329, -72.08556, 111.67952,
     VERTEX,   72.41285, -72.46459, 110.98248,
     VERTEX,   71.89577, -72.25684, 110.20078,
     VERTEX,   71.59954, -71.54168, 109.63298,
     VERTEX,   71.63733, -70.59225, 109.49599,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   72.47399, -70.92839, 110.76081,
                       
     VERTEX,   71.63733, -70.59225, 109.49599,
     VERTEX,   71.99470, -69.77122, 109.84211,
     VERTEX,   72.53514, -69.39220, 110.53915,
     VERTEX,   73.05222, -69.59994, 111.32085,
     VERTEX,   73.34844, -70.31511, 111.88864,
     VERTEX,   73.31065, -71.26453, 112.02564,
     VERTEX,   72.95329, -72.08556, 111.67952,
     VERTEX,   72.41285, -72.46459, 110.98248,
     VERTEX,   71.89577, -72.25684, 110.20078,
     VERTEX,   71.59954, -71.54168, 109.63298,
     VERTEX,   71.63733, -70.59225, 109.49599,
                       
     END,              
                       
     CYLINDER,   64.06000, -69.74500, 116.64100,  72.47399, -70.92839, 110.76081,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.03200, -46.09978, 129.43520,
                       
     VERTEX,   39.78176, -45.13012, 126.95564,
     VERTEX,   39.83070, -44.26005, 127.35836,
     VERTEX,   39.76763, -43.78444, 128.18988,
     VERTEX,   39.61663, -43.88497, 129.13258,
     VERTEX,   39.43538, -44.52323, 129.82640,
     VERTEX,   39.29311, -45.45543, 130.00630,
     VERTEX,   39.24416, -46.32550, 129.60358,
     VERTEX,   39.30724, -46.80110, 128.77206,
     VERTEX,   39.45824, -46.70058, 127.82936,
     VERTEX,   39.63949, -46.06232, 127.13554,
     VERTEX,   39.78176, -45.13012, 126.95564,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.53743, -45.29277, 128.48097,
                       
     VERTEX,   39.78176, -45.13012, 126.95564,
     VERTEX,   39.83070, -44.26005, 127.35836,
     VERTEX,   39.76763, -43.78444, 128.18988,
     VERTEX,   39.61663, -43.88497, 129.13258,
     VERTEX,   39.43538, -44.52323, 129.82640,
     VERTEX,   39.29311, -45.45543, 130.00630,
     VERTEX,   39.24416, -46.32550, 129.60358,
     VERTEX,   39.30724, -46.80110, 128.77206,
     VERTEX,   39.45824, -46.70058, 127.82936,
     VERTEX,   39.63949, -46.06232, 127.13554,
     VERTEX,   39.78176, -45.13012, 126.95564,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  39.53743, -45.29277, 128.48097,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.27592, -51.98112, 127.12969,
                       
     VERTEX,   39.31660, -51.02192, 124.69189,
     VERTEX,   39.36781, -50.15332, 125.09749,
     VERTEX,   39.30561, -49.68027, 125.93053,
     VERTEX,   39.15377, -49.78345, 126.87280,
     VERTEX,   38.97028, -50.42346, 127.56441,
     VERTEX,   38.82522, -51.35583, 127.74117,
     VERTEX,   38.77401, -52.22443, 127.33557,
     VERTEX,   38.83620, -52.69748, 126.50253,
     VERTEX,   38.98805, -52.59430, 125.56025,
     VERTEX,   39.17155, -51.95429, 124.86864,
     VERTEX,   39.31660, -51.02192, 124.69189,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.07091, -51.18888, 126.21653,
                       
     VERTEX,   39.31660, -51.02192, 124.69189,
     VERTEX,   39.36781, -50.15332, 125.09749,
     VERTEX,   39.30561, -49.68027, 125.93053,
     VERTEX,   39.15377, -49.78345, 126.87280,
     VERTEX,   38.97028, -50.42346, 127.56441,
     VERTEX,   38.82522, -51.35583, 127.74117,
     VERTEX,   38.77401, -52.22443, 127.33557,
     VERTEX,   38.83620, -52.69748, 126.50253,
     VERTEX,   38.98805, -52.59430, 125.56025,
     VERTEX,   39.17155, -51.95429, 124.86864,
     VERTEX,   39.31660, -51.02192, 124.69189,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  39.07091, -51.18888, 126.21653,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.12150,   0.63770, 111.13438,
                       
     VERTEX,  -12.45971,  -0.59619, 112.90240,
     VERTEX,  -12.24914,   0.19431, 112.40003,
     VERTEX,  -12.13042,   0.54232, 111.51324,
     VERTEX,  -12.14890,   0.31491, 110.58075,
     VERTEX,  -12.29752,  -0.40106, 109.95873,
     VERTEX,  -12.51952,  -1.33211, 109.88479,
     VERTEX,  -12.73009,  -2.12261, 110.38715,
     VERTEX,  -12.84881,  -2.47062, 111.27394,
     VERTEX,  -12.83032,  -2.24320, 112.20644,
     VERTEX,  -12.68170,  -1.52724, 112.82845,
     VERTEX,  -12.45971,  -0.59619, 112.90240,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -12.48961,  -0.96415, 111.39359,
                       
     VERTEX,  -12.45971,  -0.59619, 112.90240,
     VERTEX,  -12.24914,   0.19431, 112.40003,
     VERTEX,  -12.13042,   0.54232, 111.51324,
     VERTEX,  -12.14890,   0.31491, 110.58075,
     VERTEX,  -12.29752,  -0.40106, 109.95873,
     VERTEX,  -12.51952,  -1.33211, 109.88479,
     VERTEX,  -12.73009,  -2.12261, 110.38715,
     VERTEX,  -12.84881,  -2.47062, 111.27394,
     VERTEX,  -12.83032,  -2.24320, 112.20644,
     VERTEX,  -12.68170,  -1.52724, 112.82845,
     VERTEX,  -12.45971,  -0.59619, 112.90240,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300, -12.48961,  -0.96415, 111.39359,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.32541,  -4.25129, 111.00416,
                       
     VERTEX,  -10.57387,  -5.43243, 112.42393,
     VERTEX,  -10.39782,  -4.62682, 111.93240,
     VERTEX,  -10.32598,  -4.25534, 111.05010,
     VERTEX,  -10.38579,  -4.45988, 110.11405,
     VERTEX,  -10.55440,  -5.16232, 109.48179,
     VERTEX,  -10.76742,  -6.09434, 109.39481,
     VERTEX,  -10.94346,  -6.89994, 109.88634,
     VERTEX,  -11.01530,  -7.27142, 110.76864,
     VERTEX,  -10.95550,  -7.06688, 111.70469,
     VERTEX,  -10.78688,  -6.36445, 112.33695,
     VERTEX,  -10.57387,  -5.43243, 112.42393,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -10.67064,  -5.76338, 110.90937,
                       
     VERTEX,  -10.57387,  -5.43243, 112.42393,
     VERTEX,  -10.39782,  -4.62682, 111.93240,
     VERTEX,  -10.32598,  -4.25534, 111.05010,
     VERTEX,  -10.38579,  -4.45988, 110.11405,
     VERTEX,  -10.55440,  -5.16232, 109.48179,
     VERTEX,  -10.76742,  -6.09434, 109.39481,
     VERTEX,  -10.94346,  -6.89994, 109.88634,
     VERTEX,  -11.01530,  -7.27142, 110.76864,
     VERTEX,  -10.95550,  -7.06688, 111.70469,
     VERTEX,  -10.78688,  -6.36445, 112.33695,
     VERTEX,  -10.57387,  -5.43243, 112.42393,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600, -10.67064,  -5.76338, 110.90937,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -41.89623,  19.12686,  99.73923,
                       
     VERTEX,  -36.53024,  17.54662, 104.85048,
     VERTEX,  -35.94865,  18.09563, 104.31950,
     VERTEX,  -35.41066,  18.11502, 103.52465,
     VERTEX,  -35.12174,  17.59739, 102.76955,
     VERTEX,  -35.19226,  16.74044, 102.34261,
     VERTEX,  -35.59528,  15.87151, 102.40692,
     VERTEX,  -36.17686,  15.32250, 102.93791,
     VERTEX,  -36.71486,  15.30311, 103.73276,
     VERTEX,  -37.00378,  15.82075, 104.48786,
     VERTEX,  -36.93326,  16.67769, 104.91479,
     VERTEX,  -36.53024,  17.54662, 104.85048,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -36.06276,  16.70907, 103.62870,
                       
     VERTEX,  -36.53024,  17.54662, 104.85048,
     VERTEX,  -35.94865,  18.09563, 104.31950,
     VERTEX,  -35.41066,  18.11502, 103.52465,
     VERTEX,  -35.12174,  17.59739, 102.76955,
     VERTEX,  -35.19226,  16.74044, 102.34261,
     VERTEX,  -35.59528,  15.87151, 102.40692,
     VERTEX,  -36.17686,  15.32250, 102.93791,
     VERTEX,  -36.71486,  15.30311, 103.73276,
     VERTEX,  -37.00378,  15.82075, 104.48786,
     VERTEX,  -36.93326,  16.67769, 104.91479,
     VERTEX,  -36.53024,  17.54662, 104.85048,
                       
     END,              
                       
     CYLINDER,  -26.62400,  12.79700, 109.92200, -36.06276,  16.70907, 103.62870,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.34789, -15.38067, 112.61927,
                       
     VERTEX,   -0.22758, -16.27628, 112.48326,
     VERTEX,   -0.19231, -15.41666, 112.05733,
     VERTEX,   -0.31981, -14.95682, 111.22433,
     VERTEX,   -0.56138, -15.07240, 110.30244,
     VERTEX,   -0.82475, -15.71925, 109.64378,
     VERTEX,   -1.00933, -16.65030, 109.49995,
     VERTEX,   -1.04460, -17.50991, 109.92589,
     VERTEX,   -0.91710, -17.96975, 110.75890,
     VERTEX,   -0.67552, -17.85417, 111.68079,
     VERTEX,   -0.41215, -17.20732, 112.33943,
     VERTEX,   -0.22758, -16.27628, 112.48326,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.61845, -16.46329, 110.99161,
                       
     VERTEX,   -0.22758, -16.27628, 112.48326,
     VERTEX,   -0.19231, -15.41666, 112.05733,
     VERTEX,   -0.31981, -14.95682, 111.22433,
     VERTEX,   -0.56138, -15.07240, 110.30244,
     VERTEX,   -0.82475, -15.71925, 109.64378,
     VERTEX,   -1.00933, -16.65030, 109.49995,
     VERTEX,   -1.04460, -17.50991, 109.92589,
     VERTEX,   -0.91710, -17.96975, 110.75890,
     VERTEX,   -0.67552, -17.85417, 111.68079,
     VERTEX,   -0.41215, -17.20732, 112.33943,
     VERTEX,   -0.22758, -16.27628, 112.48326,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,  -0.61845, -16.46329, 110.99161,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.93342,  -9.05458, 112.87398,
                       
     VERTEX,    0.01433,  -9.95465, 112.88840,
     VERTEX,    0.05979,  -9.09872, 112.45607,
     VERTEX,   -0.05335,  -8.64515, 111.61757,
     VERTEX,   -0.28187,  -8.76720, 110.69319,
     VERTEX,   -0.53848,  -9.41824, 110.03600,
     VERTEX,   -0.72517, -10.34961, 109.89704,
     VERTEX,   -0.77063, -11.20554, 110.32938,
     VERTEX,   -0.65750, -11.65910, 111.16788,
     VERTEX,   -0.42898, -11.53705, 112.09225,
     VERTEX,   -0.17236, -10.88601, 112.74944,
     VERTEX,    0.01433,  -9.95465, 112.88840,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.35542, -10.15213, 111.39272,
                       
     VERTEX,    0.01433,  -9.95465, 112.88840,
     VERTEX,    0.05979,  -9.09872, 112.45607,
     VERTEX,   -0.05335,  -8.64515, 111.61757,
     VERTEX,   -0.28187,  -8.76720, 110.69319,
     VERTEX,   -0.53848,  -9.41824, 110.03600,
     VERTEX,   -0.72517, -10.34961, 109.89704,
     VERTEX,   -0.77063, -11.20554, 110.32938,
     VERTEX,   -0.65750, -11.65910, 111.16788,
     VERTEX,   -0.42898, -11.53705, 112.09225,
     VERTEX,   -0.17236, -10.88601, 112.74944,
     VERTEX,    0.01433,  -9.95465, 112.88840,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  -0.35542, -10.15213, 111.39272,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.24861,  30.44881,  30.11043,
                       
     VERTEX,   20.11488,  31.45561,  28.02143,
     VERTEX,   20.19871,  32.31134,  28.44840,
     VERTEX,   20.17724,  32.76191,  29.29582,
     VERTEX,   20.05866,  32.63523,  30.24001,
     VERTEX,   19.88826,  31.97968,  30.92032,
     VERTEX,   19.73113,  31.04565,  31.07689,
     VERTEX,   19.64729,  30.18993,  30.64992,
     VERTEX,   19.66877,  29.73935,  29.80250,
     VERTEX,   19.78735,  29.86604,  28.85831,
     VERTEX,   19.95775,  30.52159,  28.17801,
     VERTEX,   20.11488,  31.45561,  28.02143,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.92300,  31.25063,  29.54916,
                       
     VERTEX,   20.11488,  31.45561,  28.02143,
     VERTEX,   20.19871,  32.31134,  28.44840,
     VERTEX,   20.17724,  32.76191,  29.29582,
     VERTEX,   20.05866,  32.63523,  30.24001,
     VERTEX,   19.88826,  31.97968,  30.92032,
     VERTEX,   19.73113,  31.04565,  31.07689,
     VERTEX,   19.64729,  30.18993,  30.64992,
     VERTEX,   19.66877,  29.73935,  29.80250,
     VERTEX,   19.78735,  29.86604,  28.85831,
     VERTEX,   19.95775,  30.52159,  28.17801,
     VERTEX,   20.11488,  31.45561,  28.02143,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,  19.92300,  31.25063,  29.54916,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.95081,  23.56158,  26.14269,
                       
     VERTEX,   11.61895,  24.26387,  24.90528,
     VERTEX,   11.73031,  25.13527,  25.29240,
     VERTEX,   11.82687,  25.61047,  26.12093,
     VERTEX,   11.87177,  25.50797,  27.07438,
     VERTEX,   11.84784,  24.86692,  27.78858,
     VERTEX,   11.76423,  23.93217,  27.99072,
     VERTEX,   11.65288,  23.06078,  27.60360,
     VERTEX,   11.55631,  22.58557,  26.77507,
     VERTEX,   11.51141,  22.68807,  25.82162,
     VERTEX,   11.53534,  23.32912,  25.10742,
     VERTEX,   11.61895,  24.26387,  24.90528,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.69159,  24.09802,  26.44800,
                       
     VERTEX,   11.61895,  24.26387,  24.90528,
     VERTEX,   11.73031,  25.13527,  25.29240,
     VERTEX,   11.82687,  25.61047,  26.12093,
     VERTEX,   11.87177,  25.50797,  27.07438,
     VERTEX,   11.84784,  24.86692,  27.78858,
     VERTEX,   11.76423,  23.93217,  27.99072,
     VERTEX,   11.65288,  23.06078,  27.60360,
     VERTEX,   11.55631,  22.58557,  26.77507,
     VERTEX,   11.51141,  22.68807,  25.82162,
     VERTEX,   11.53534,  23.32912,  25.10742,
     VERTEX,   11.61895,  24.26387,  24.90528,
                       
     END,              
                       
     CYLINDER,    3.18200,  24.96600,  26.94200,  11.69159,  24.09802,  26.44800,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.27060,   7.67915,  24.89133,
                       
     VERTEX,   17.32093,   8.73192,  22.61637,
     VERTEX,   17.39582,   9.58479,  23.05067,
     VERTEX,   17.34476,  10.03159,  23.89882,
     VERTEX,   17.18726,   9.90168,  24.83685,
     VERTEX,   16.98347,   9.24466,  25.50648,
     VERTEX,   16.81124,   8.31150,  25.65192,
     VERTEX,   16.73635,   7.45864,  25.21763,
     VERTEX,   16.78741,   7.01183,  24.36948,
     VERTEX,   16.94492,   7.14175,  23.43144,
     VERTEX,   17.14870,   7.79876,  22.76181,
     VERTEX,   17.32093,   8.73192,  22.61637,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.06609,   8.52171,  24.13415,
                       
     VERTEX,   17.32093,   8.73192,  22.61637,
     VERTEX,   17.39582,   9.58479,  23.05067,
     VERTEX,   17.34476,  10.03159,  23.89882,
     VERTEX,   17.18726,   9.90168,  24.83685,
     VERTEX,   16.98347,   9.24466,  25.50648,
     VERTEX,   16.81124,   8.31150,  25.65192,
     VERTEX,   16.73635,   7.45864,  25.21763,
     VERTEX,   16.78741,   7.01183,  24.36948,
     VERTEX,   16.94492,   7.14175,  23.43144,
     VERTEX,   17.14870,   7.79876,  22.76181,
     VERTEX,   17.32093,   8.73192,  22.61637,
                       
     END,              
                       
     CYLINDER,    8.64500,   9.88500,  22.90900,  17.06609,   8.52171,  24.13415,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.62895,  24.28287,  35.72140,
                       
     VERTEX,   36.23178,  25.89549,  31.67756,
     VERTEX,   36.21296,  26.73321,  32.14604,
     VERTEX,   35.91099,  27.16884,  32.94644,
     VERTEX,   35.44122,  27.03599,  33.77304,
     VERTEX,   34.98307,  26.38540,  34.31009,
     VERTEX,   34.71155,  25.46557,  34.35248,
     VERTEX,   34.73037,  24.62785,  33.88400,
     VERTEX,   35.03233,  24.19222,  33.08359,
     VERTEX,   35.50211,  24.32508,  32.25700,
     VERTEX,   35.96025,  24.97567,  31.71994,
     VERTEX,   36.23178,  25.89549,  31.67756,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.47166,  25.68053,  33.01501,
                       
     VERTEX,   36.23178,  25.89549,  31.67756,
     VERTEX,   36.21296,  26.73321,  32.14604,
     VERTEX,   35.91099,  27.16884,  32.94644,
     VERTEX,   35.44122,  27.03599,  33.77304,
     VERTEX,   34.98307,  26.38540,  34.31009,
     VERTEX,   34.71155,  25.46557,  34.35248,
     VERTEX,   34.73037,  24.62785,  33.88400,
     VERTEX,   35.03233,  24.19222,  33.08359,
     VERTEX,   35.50211,  24.32508,  32.25700,
     VERTEX,   35.96025,  24.97567,  31.71994,
     VERTEX,   36.23178,  25.89549,  31.67756,
                       
     END,              
                       
     CYLINDER,   27.12700,  27.94200,  28.63600,  35.47166,  25.68053,  33.01501,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.59906,  22.36219,  34.91956,
                       
     VERTEX,   31.27048,  23.78729,  31.35938,
     VERTEX,   31.27244,  24.62795,  31.82293,
     VERTEX,   31.02246,  25.06462,  32.64051,
     VERTEX,   30.61603,  24.93050,  33.49982,
     VERTEX,   30.20838,  24.27682,  34.07265,
     VERTEX,   29.95523,  23.35327,  34.14018,
     VERTEX,   29.95327,  22.51260,  33.67663,
     VERTEX,   30.20325,  22.07594,  32.85905,
     VERTEX,   30.60968,  22.21006,  31.99973,
     VERTEX,   31.01732,  22.86374,  31.42691,
     VERTEX,   31.27048,  23.78729,  31.35938,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.61285,  23.57028,  32.74978,
                       
     VERTEX,   31.27048,  23.78729,  31.35938,
     VERTEX,   31.27244,  24.62795,  31.82293,
     VERTEX,   31.02246,  25.06462,  32.64051,
     VERTEX,   30.61603,  24.93050,  33.49982,
     VERTEX,   30.20838,  24.27682,  34.07265,
     VERTEX,   29.95523,  23.35327,  34.14018,
     VERTEX,   29.95327,  22.51260,  33.67663,
     VERTEX,   30.20325,  22.07594,  32.85905,
     VERTEX,   30.60968,  22.21006,  31.99973,
     VERTEX,   31.01732,  22.86374,  31.42691,
     VERTEX,   31.27048,  23.78729,  31.35938,
                       
     END,              
                       
     CYLINDER,   22.54500,  25.52500,  29.23900,  30.61285,  23.57028,  32.74978,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00001_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   28.41300, -54.63000,  33.05300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   36.50200, -47.04600,  34.89900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    5.36200, -71.06700,  47.36700,   0.80000,
                       
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
                       
     SPHERE,   -1.75900,  -3.55600, 111.81300,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    0.09700,  -8.21000, 110.75600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -26.62400,  12.79700, 109.92200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.27000, -18.21500, 108.35800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.28800, -11.92800, 108.99600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   11.30600,  32.54800,  28.64100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    3.18200,  24.96600,  26.94200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    8.64500,   9.88500,  22.90900,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   27.12700,  27.94200,  28.63600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   22.54500,  25.52500,  29.23900,   0.80000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00001_arror_pos') 