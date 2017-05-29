from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.63515, -45.62932,  30.29848,
                       
     VERTEX,   36.33306, -49.94138,  30.11996,
     VERTEX,   35.74931, -49.23979,  29.82230,
     VERTEX,   35.24859, -48.47231,  30.10840,
     VERTEX,   35.02217, -47.93208,  30.86898,
     VERTEX,   35.15653, -47.82546,  31.81354,
     VERTEX,   35.60035, -48.19317,  32.58127,
     VERTEX,   36.18410, -48.89476,  32.87894,
     VERTEX,   36.68481, -49.66225,  32.59283,
     VERTEX,   36.91124, -50.20247,  31.83225,
     VERTEX,   36.77688, -50.30909,  30.88770,
     VERTEX,   36.33306, -49.94138,  30.11996,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.96670, -49.06728,  31.35062,
                       
     VERTEX,   36.33306, -49.94138,  30.11996,
     VERTEX,   35.74931, -49.23979,  29.82230,
     VERTEX,   35.24859, -48.47231,  30.10840,
     VERTEX,   35.02217, -47.93208,  30.86898,
     VERTEX,   35.15653, -47.82546,  31.81354,
     VERTEX,   35.60035, -48.19317,  32.58127,
     VERTEX,   36.18410, -48.89476,  32.87894,
     VERTEX,   36.68481, -49.66225,  32.59283,
     VERTEX,   36.91124, -50.20247,  31.83225,
     VERTEX,   36.77688, -50.30909,  30.88770,
     VERTEX,   36.33306, -49.94138,  30.11996,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  35.96670, -49.06728,  31.35062,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.28469, -66.21258,  35.59197,
                       
     VERTEX,   10.88046, -69.12715,  39.13500,
     VERTEX,   10.37449, -68.31654,  39.04280,
     VERTEX,   10.29634, -67.41054,  39.35046,
     VERTEX,   10.67587, -66.75521,  39.94046,
     VERTEX,   11.36811, -66.60086,  40.58743,
     VERTEX,   12.10865, -67.00645,  41.04427,
     VERTEX,   12.61463, -67.81706,  41.13646,
     VERTEX,   12.69278, -68.72307,  40.82880,
     VERTEX,   12.31324, -69.37840,  40.23881,
     VERTEX,   11.62100, -69.53275,  39.59183,
     VERTEX,   10.88046, -69.12715,  39.13500,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.49456, -68.06680,  40.08963,
                       
     VERTEX,   10.88046, -69.12715,  39.13500,
     VERTEX,   10.37449, -68.31654,  39.04280,
     VERTEX,   10.29634, -67.41054,  39.35046,
     VERTEX,   10.67587, -66.75521,  39.94046,
     VERTEX,   11.36811, -66.60086,  40.58743,
     VERTEX,   12.10865, -67.00645,  41.04427,
     VERTEX,   12.61463, -67.81706,  41.13646,
     VERTEX,   12.69278, -68.72307,  40.82880,
     VERTEX,   12.31324, -69.37840,  40.23881,
     VERTEX,   11.62100, -69.53275,  39.59183,
     VERTEX,   10.88046, -69.12715,  39.13500,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  11.49456, -68.06680,  40.08963,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.76872, -69.61571,  36.16250,
                       
     VERTEX,   25.36921, -72.99074,  38.63446,
     VERTEX,   24.80422, -72.22986,  38.48133,
     VERTEX,   24.58216, -71.35115,  38.79781,
     VERTEX,   24.78786, -70.69025,  39.46301,
     VERTEX,   25.34274, -70.49959,  40.22285,
     VERTEX,   26.03486, -70.85201,  40.78709,
     VERTEX,   26.59985, -71.61288,  40.94022,
     VERTEX,   26.82191, -72.49158,  40.62374,
     VERTEX,   26.61622, -73.15249,  39.95854,
     VERTEX,   26.06134, -73.34315,  39.19870,
     VERTEX,   25.36921, -72.99074,  38.63446,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.70204, -71.92137,  39.71077,
                       
     VERTEX,   25.36921, -72.99074,  38.63446,
     VERTEX,   24.80422, -72.22986,  38.48133,
     VERTEX,   24.58216, -71.35115,  38.79781,
     VERTEX,   24.78786, -70.69025,  39.46301,
     VERTEX,   25.34274, -70.49959,  40.22285,
     VERTEX,   26.03486, -70.85201,  40.78709,
     VERTEX,   26.59985, -71.61288,  40.94022,
     VERTEX,   26.82191, -72.49158,  40.62374,
     VERTEX,   26.61622, -73.15249,  39.95854,
     VERTEX,   26.06134, -73.34315,  39.19870,
     VERTEX,   25.36921, -72.99074,  38.63446,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.70204, -71.92137,  39.71077,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.60658, -61.63241,  27.78020,
                       
     VERTEX,   31.70877, -65.88014,  29.29032,
     VERTEX,   31.11142, -65.16512,  29.05899,
     VERTEX,   30.73480, -64.33745,  29.36674,
     VERTEX,   30.72277, -63.71326,  30.09601,
     VERTEX,   31.07993, -63.53097,  30.96826,
     VERTEX,   31.66985, -63.86022,  31.65030,
     VERTEX,   32.26720, -64.57523,  31.88163,
     VERTEX,   32.64383, -65.40292,  31.57388,
     VERTEX,   32.65586, -66.02710,  30.84461,
     VERTEX,   32.29870, -66.20939,  29.97237,
     VERTEX,   31.70877, -65.88014,  29.29032,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.68931, -64.87018,  30.47031,
                       
     VERTEX,   31.70877, -65.88014,  29.29032,
     VERTEX,   31.11142, -65.16512,  29.05899,
     VERTEX,   30.73480, -64.33745,  29.36674,
     VERTEX,   30.72277, -63.71326,  30.09601,
     VERTEX,   31.07993, -63.53097,  30.96826,
     VERTEX,   31.66985, -63.86022,  31.65030,
     VERTEX,   32.26720, -64.57523,  31.88163,
     VERTEX,   32.64383, -65.40292,  31.57388,
     VERTEX,   32.65586, -66.02710,  30.84461,
     VERTEX,   32.29870, -66.20939,  29.97237,
     VERTEX,   31.70877, -65.88014,  29.29032,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  31.68931, -64.87018,  30.47031,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.44862, -46.40973,  28.21090,
                       
     VERTEX,   18.93817, -50.40696,  29.54314,
     VERTEX,   18.33939, -49.69310,  29.31189,
     VERTEX,   17.96333, -48.86476,  29.61852,
     VERTEX,   17.95363, -48.23832,  30.34590,
     VERTEX,   18.31399, -48.05307,  31.21620,
     VERTEX,   18.90676, -48.37978,  31.89700,
     VERTEX,   19.50554, -49.09364,  32.12825,
     VERTEX,   19.88160, -49.92198,  31.82162,
     VERTEX,   19.89130, -50.54842,  31.09424,
     VERTEX,   19.53094, -50.73366,  30.22394,
     VERTEX,   18.93817, -50.40696,  29.54314,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.92247, -49.39337,  30.72007,
                       
     VERTEX,   18.93817, -50.40696,  29.54314,
     VERTEX,   18.33939, -49.69310,  29.31189,
     VERTEX,   17.96333, -48.86476,  29.61852,
     VERTEX,   17.95363, -48.23832,  30.34590,
     VERTEX,   18.31399, -48.05307,  31.21620,
     VERTEX,   18.90676, -48.37978,  31.89700,
     VERTEX,   19.50554, -49.09364,  32.12825,
     VERTEX,   19.88160, -49.92198,  31.82162,
     VERTEX,   19.89130, -50.54842,  31.09424,
     VERTEX,   19.53094, -50.73366,  30.22394,
     VERTEX,   18.93817, -50.40696,  29.54314,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,  18.92247, -49.39337,  30.72007,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.45496, -43.81728, 124.80564,
                       
     VERTEX,   51.04842, -40.90368, 122.52433,
     VERTEX,   50.62023, -40.11672, 122.86922,
     VERTEX,   49.89721, -39.50104, 122.72857,
     VERTEX,   49.15554, -39.29179, 122.15608,
     VERTEX,   48.67850, -39.56892, 121.37044,
     VERTEX,   48.64831, -40.22656, 120.67172,
     VERTEX,   49.07650, -41.01352, 120.32683,
     VERTEX,   49.79951, -41.62920, 120.46748,
     VERTEX,   50.54119, -41.83844, 121.03997,
     VERTEX,   51.01823, -41.56131, 121.82561,
     VERTEX,   51.04842, -40.90368, 122.52433,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.84837, -40.56512, 121.59803,
                       
     VERTEX,   51.04842, -40.90368, 122.52433,
     VERTEX,   50.62023, -40.11672, 122.86922,
     VERTEX,   49.89721, -39.50104, 122.72857,
     VERTEX,   49.15554, -39.29179, 122.15608,
     VERTEX,   48.67850, -39.56892, 121.37044,
     VERTEX,   48.64831, -40.22656, 120.67172,
     VERTEX,   49.07650, -41.01352, 120.32683,
     VERTEX,   49.79951, -41.62920, 120.46748,
     VERTEX,   50.54119, -41.83844, 121.03997,
     VERTEX,   51.01823, -41.56131, 121.82561,
     VERTEX,   51.04842, -40.90368, 122.52433,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  49.84837, -40.56512, 121.59803,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.92938, -68.18967, 123.03096,
                       
     VERTEX,   34.13803, -65.30958, 124.45280,
     VERTEX,   33.57164, -64.60909, 124.78464,
     VERTEX,   33.00687, -63.87787, 124.52397,
     VERTEX,   32.65942, -63.39523, 123.77035,
     VERTEX,   32.66203, -63.34552, 122.81164,
     VERTEX,   33.01368, -63.74772, 122.01404,
     VERTEX,   33.58006, -64.44821, 121.68220,
     VERTEX,   34.14484, -65.17943, 121.94286,
     VERTEX,   34.49228, -65.66207, 122.69649,
     VERTEX,   34.48968, -65.71178, 123.65519,
     VERTEX,   34.13803, -65.30958, 124.45280,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.57585, -64.52865, 123.23341,
                       
     VERTEX,   34.13803, -65.30958, 124.45280,
     VERTEX,   33.57164, -64.60909, 124.78464,
     VERTEX,   33.00687, -63.87787, 124.52397,
     VERTEX,   32.65942, -63.39523, 123.77035,
     VERTEX,   32.66203, -63.34552, 122.81164,
     VERTEX,   33.01368, -63.74772, 122.01404,
     VERTEX,   33.58006, -64.44821, 121.68220,
     VERTEX,   34.14484, -65.17943, 121.94286,
     VERTEX,   34.49228, -65.66207, 122.69649,
     VERTEX,   34.48968, -65.71178, 123.65519,
     VERTEX,   34.13803, -65.30958, 124.45280,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  33.57585, -64.52865, 123.23341,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.90930, -63.73336, 124.61923,
                       
     VERTEX,   32.20528, -60.76119, 125.85579,
     VERTEX,   31.64503, -60.05750, 126.19127,
     VERTEX,   31.07053, -59.33269, 125.93398,
     VERTEX,   30.70124, -58.86359, 125.18220,
     VERTEX,   30.67820, -58.82940, 124.22308,
     VERTEX,   31.01021, -59.24316, 123.42298,
     VERTEX,   31.57047, -59.94685, 123.08751,
     VERTEX,   32.14496, -60.67167, 123.34480,
     VERTEX,   32.51426, -61.14076, 124.09657,
     VERTEX,   32.53730, -61.17495, 125.05569,
     VERTEX,   32.20528, -60.76119, 125.85579,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.60775, -60.00217, 124.63939,
                       
     VERTEX,   32.20528, -60.76119, 125.85579,
     VERTEX,   31.64503, -60.05750, 126.19127,
     VERTEX,   31.07053, -59.33269, 125.93398,
     VERTEX,   30.70124, -58.86359, 125.18220,
     VERTEX,   30.67820, -58.82940, 124.22308,
     VERTEX,   31.01021, -59.24316, 123.42298,
     VERTEX,   31.57047, -59.94685, 123.08751,
     VERTEX,   32.14496, -60.67167, 123.34480,
     VERTEX,   32.51426, -61.14076, 124.09657,
     VERTEX,   32.53730, -61.17495, 125.05569,
     VERTEX,   32.20528, -60.76119, 125.85579,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  31.60775, -60.00217, 124.63939,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.03679, -54.20882, 126.28358,
                       
     VERTEX,   21.55537, -51.08909, 127.75298,
     VERTEX,   20.98797, -50.38908, 128.08412,
     VERTEX,   20.42493, -49.65674, 127.82285,
     VERTEX,   20.08131, -49.17180, 127.06895,
     VERTEX,   20.08836, -49.11948, 126.11041,
     VERTEX,   20.44338, -49.51978, 125.31334,
     VERTEX,   21.01078, -50.21978, 124.98220,
     VERTEX,   21.57382, -50.95212, 125.24348,
     VERTEX,   21.91744, -51.43707, 125.99737,
     VERTEX,   21.91039, -51.48938, 126.95591,
     VERTEX,   21.55537, -51.08909, 127.75298,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.99937, -50.30443, 126.53316,
                       
     VERTEX,   21.55537, -51.08909, 127.75298,
     VERTEX,   20.98797, -50.38908, 128.08412,
     VERTEX,   20.42493, -49.65674, 127.82285,
     VERTEX,   20.08131, -49.17180, 127.06895,
     VERTEX,   20.08836, -49.11948, 126.11041,
     VERTEX,   20.44338, -49.51978, 125.31334,
     VERTEX,   21.01078, -50.21978, 124.98220,
     VERTEX,   21.57382, -50.95212, 125.24348,
     VERTEX,   21.91744, -51.43707, 125.99737,
     VERTEX,   21.91039, -51.48938, 126.95591,
     VERTEX,   21.55537, -51.08909, 127.75298,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  20.99937, -50.30443, 126.53316,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.70332, -59.44168, 122.58672,
                       
     VERTEX,   21.86052, -56.65431, 124.62596,
     VERTEX,   21.27258, -55.96658, 124.94683,
     VERTEX,   20.73793, -55.21513, 124.68024,
     VERTEX,   20.46078, -54.68699, 123.92801,
     VERTEX,   20.54699, -54.58389, 122.97746,
     VERTEX,   20.96363, -54.94521, 122.19168,
     VERTEX,   21.55157, -55.63294, 121.87080,
     VERTEX,   22.08622, -56.38438, 122.13740,
     VERTEX,   22.36338, -56.91253, 122.88963,
     VERTEX,   22.27716, -57.01563, 123.84017,
     VERTEX,   21.86052, -56.65431, 124.62596,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.41208, -55.79976, 123.40882,
                       
     VERTEX,   21.86052, -56.65431, 124.62596,
     VERTEX,   21.27258, -55.96658, 124.94683,
     VERTEX,   20.73793, -55.21513, 124.68024,
     VERTEX,   20.46078, -54.68699, 123.92801,
     VERTEX,   20.54699, -54.58389, 122.97746,
     VERTEX,   20.96363, -54.94521, 122.19168,
     VERTEX,   21.55157, -55.63294, 121.87080,
     VERTEX,   22.08622, -56.38438, 122.13740,
     VERTEX,   22.36338, -56.91253, 122.88963,
     VERTEX,   22.27716, -57.01563, 123.84017,
     VERTEX,   21.86052, -56.65431, 124.62596,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  21.41208, -55.79976, 123.40882,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.10180,  10.33733, 112.62428,
                       
     VERTEX,    7.40857,   6.79335, 111.00927,
     VERTEX,    6.90627,   7.56745, 110.74458,
     VERTEX,    6.38372,   8.30337, 111.07164,
     VERTEX,    6.04052,   8.72001, 111.86550,
     VERTEX,    6.00777,   8.65824, 112.82295,
     VERTEX,    6.29797,   8.14164, 113.57828,
     VERTEX,    6.80027,   7.36753, 113.84296,
     VERTEX,    7.32282,   6.63161, 113.51591,
     VERTEX,    7.66602,   6.21497, 112.72204,
     VERTEX,    7.69877,   6.27675, 111.76459,
     VERTEX,    7.40857,   6.79335, 111.00927,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.85327,   7.46749, 112.29377,
                       
     VERTEX,    7.40857,   6.79335, 111.00927,
     VERTEX,    6.90627,   7.56745, 110.74458,
     VERTEX,    6.38372,   8.30337, 111.07164,
     VERTEX,    6.04052,   8.72001, 111.86550,
     VERTEX,    6.00777,   8.65824, 112.82295,
     VERTEX,    6.29797,   8.14164, 113.57828,
     VERTEX,    6.80027,   7.36753, 113.84296,
     VERTEX,    7.32282,   6.63161, 113.51591,
     VERTEX,    7.66602,   6.21497, 112.72204,
     VERTEX,    7.69877,   6.27675, 111.76459,
     VERTEX,    7.40857,   6.79335, 111.00927,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,   6.85327,   7.46749, 112.29377,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.77085,   3.89663, 114.34178,
                       
     VERTEX,    6.02304,   0.47010, 112.09293,
     VERTEX,    5.55687,   1.27355, 111.85052,
     VERTEX,    5.01812,   1.99160, 112.19075,
     VERTEX,    4.61257,   2.34998, 112.98365,
     VERTEX,    4.49512,   2.21181, 113.92636,
     VERTEX,    4.71064,   1.62985, 114.65881,
     VERTEX,    5.17681,   0.82640, 114.90122,
     VERTEX,    5.71556,   0.10835, 114.56100,
     VERTEX,    6.12111,  -0.25003, 113.76810,
     VERTEX,    6.23855,  -0.11185, 112.82538,
     VERTEX,    6.02304,   0.47010, 112.09293,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    5.36684,   1.04998, 113.37587,
                       
     VERTEX,    6.02304,   0.47010, 112.09293,
     VERTEX,    5.55687,   1.27355, 111.85052,
     VERTEX,    5.01812,   1.99160, 112.19075,
     VERTEX,    4.61257,   2.34998, 112.98365,
     VERTEX,    4.49512,   2.21181, 113.92636,
     VERTEX,    4.71064,   1.62985, 114.65881,
     VERTEX,    5.17681,   0.82640, 114.90122,
     VERTEX,    5.71556,   0.10835, 114.56100,
     VERTEX,    6.12111,  -0.25003, 113.76810,
     VERTEX,    6.23855,  -0.11185, 112.82538,
     VERTEX,    6.02304,   0.47010, 112.09293,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,   5.36684,   1.04998, 113.37587,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.60186,  -0.58360, 113.87273,
                       
     VERTEX,    7.91926,  -4.05441, 111.41935,
     VERTEX,    7.45545,  -3.25220, 111.16847,
     VERTEX,    6.89689,  -2.54335, 111.49580,
     VERTEX,    6.45693,  -2.19862, 112.27632,
     VERTEX,    6.30362,  -2.34969, 113.21188,
     VERTEX,    6.49552,  -2.93885, 113.94514,
     VERTEX,    6.95933,  -3.74106, 114.19601,
     VERTEX,    7.51789,  -4.44991, 113.86868,
     VERTEX,    7.95785,  -4.79463, 113.08817,
     VERTEX,    8.11116,  -4.64357, 112.15260,
     VERTEX,    7.91926,  -4.05441, 111.41935,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.20739,  -3.49663, 112.68224,
                       
     VERTEX,    7.91926,  -4.05441, 111.41935,
     VERTEX,    7.45545,  -3.25220, 111.16847,
     VERTEX,    6.89689,  -2.54335, 111.49580,
     VERTEX,    6.45693,  -2.19862, 112.27632,
     VERTEX,    6.30362,  -2.34969, 113.21188,
     VERTEX,    6.49552,  -2.93885, 113.94514,
     VERTEX,    6.95933,  -3.74106, 114.19601,
     VERTEX,    7.51789,  -4.44991, 113.86868,
     VERTEX,    7.95785,  -4.79463, 113.08817,
     VERTEX,    8.11116,  -4.64357, 112.15260,
     VERTEX,    7.91926,  -4.05441, 111.41935,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,   7.20739,  -3.49663, 112.68224,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.59815, -10.53743, 111.27875,
                       
     VERTEX,   17.42743, -14.04910, 108.94743,
     VERTEX,   16.93916, -13.27852, 108.64842,
     VERTEX,   16.34165, -12.58108, 108.92798,
     VERTEX,   15.86312, -12.22317, 109.67932,
     VERTEX,   15.68635, -12.34151, 110.61546,
     VERTEX,   15.87887, -12.89089, 111.37881,
     VERTEX,   16.36713, -13.66147, 111.67783,
     VERTEX,   16.96464, -14.35892, 111.39826,
     VERTEX,   17.44317, -14.71682, 110.64693,
     VERTEX,   17.61994, -14.59849, 109.71079,
     VERTEX,   17.42743, -14.04910, 108.94743,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.65314, -13.47000, 110.16312,
                       
     VERTEX,   17.42743, -14.04910, 108.94743,
     VERTEX,   16.93916, -13.27852, 108.64842,
     VERTEX,   16.34165, -12.58108, 108.92798,
     VERTEX,   15.86312, -12.22317, 109.67932,
     VERTEX,   15.68635, -12.34151, 110.61546,
     VERTEX,   15.87887, -12.89089, 111.37881,
     VERTEX,   16.36713, -13.66147, 111.67783,
     VERTEX,   16.96464, -14.35892, 111.39826,
     VERTEX,   17.44317, -14.71682, 110.64693,
     VERTEX,   17.61994, -14.59849, 109.71079,
     VERTEX,   17.42743, -14.04910, 108.94743,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,  16.65314, -13.47000, 110.16312,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.50999,  -3.99850, 110.28935,
                       
     VERTEX,   17.83794,  -7.69076, 108.53234,
     VERTEX,   17.33063,  -6.92660, 108.24899,
     VERTEX,   16.78243,  -6.20089, 108.55629,
     VERTEX,   16.40273,  -5.79085, 109.33687,
     VERTEX,   16.33656,  -5.85309, 110.29256,
     VERTEX,   16.60920,  -6.36384, 111.05833,
     VERTEX,   17.11651,  -7.12801, 111.34168,
     VERTEX,   17.66471,  -7.85371, 111.03438,
     VERTEX,   18.04441,  -8.26375, 110.25381,
     VERTEX,   18.11058,  -8.20151, 109.29811,
     VERTEX,   17.83794,  -7.69076, 108.53234,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.22357,  -7.02730, 109.79533,
                       
     VERTEX,   17.83794,  -7.69076, 108.53234,
     VERTEX,   17.33063,  -6.92660, 108.24899,
     VERTEX,   16.78243,  -6.20089, 108.55629,
     VERTEX,   16.40273,  -5.79085, 109.33687,
     VERTEX,   16.33656,  -5.85309, 110.29256,
     VERTEX,   16.60920,  -6.36384, 111.05833,
     VERTEX,   17.11651,  -7.12801, 111.34168,
     VERTEX,   17.66471,  -7.85371, 111.03438,
     VERTEX,   18.04441,  -8.26375, 110.25381,
     VERTEX,   18.11058,  -8.20151, 109.29811,
     VERTEX,   17.83794,  -7.69076, 108.53234,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  17.22357,  -7.02730, 109.79533,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -2.82245,  26.62875,  20.83488,
                       
     VERTEX,    2.20612,  28.08474,  25.09303,
     VERTEX,    1.80326,  28.95326,  25.16359,
     VERTEX,    1.69485,  29.79750,  24.71962,
     VERTEX,    1.92230,  30.29499,  23.93072,
     VERTEX,    2.39873,  30.25571,  23.09821,
     VERTEX,    2.94216,  29.69466,  22.54008,
     VERTEX,    3.34501,  28.82614,  22.46953,
     VERTEX,    3.45342,  27.98190,  22.91349,
     VERTEX,    3.22598,  27.48441,  23.70239,
     VERTEX,    2.74955,  27.52369,  24.53490,
     VERTEX,    2.20612,  28.08474,  25.09303,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    2.57414,  28.88970,  23.81656,
                       
     VERTEX,    2.20612,  28.08474,  25.09303,
     VERTEX,    1.80326,  28.95326,  25.16359,
     VERTEX,    1.69485,  29.79750,  24.71962,
     VERTEX,    1.92230,  30.29499,  23.93072,
     VERTEX,    2.39873,  30.25571,  23.09821,
     VERTEX,    2.94216,  29.69466,  22.54008,
     VERTEX,    3.34501,  28.82614,  22.46953,
     VERTEX,    3.45342,  27.98190,  22.91349,
     VERTEX,    3.22598,  27.48441,  23.70239,
     VERTEX,    2.74955,  27.52369,  24.53490,
     VERTEX,    2.20612,  28.08474,  25.09303,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,   2.57414,  28.88970,  23.81656,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.67695,  44.12237,  33.99860,
                       
     VERTEX,   26.06723,  43.62753,  40.61612,
     VERTEX,   26.67052,  44.29813,  40.28755,
     VERTEX,   27.43411,  44.44750,  39.72522,
     VERTEX,   28.06634,  44.01859,  39.14391,
     VERTEX,   28.32572,  43.17524,  38.76565,
     VERTEX,   28.11317,  42.23956,  38.73494,
     VERTEX,   27.50989,  41.56897,  39.06351,
     VERTEX,   26.74630,  41.41960,  39.62584,
     VERTEX,   26.11407,  41.84851,  40.20715,
     VERTEX,   25.85469,  42.69186,  40.58541,
     VERTEX,   26.06723,  43.62753,  40.61612,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.09020,  42.93355,  39.67553,
                       
     VERTEX,   26.06723,  43.62753,  40.61612,
     VERTEX,   26.67052,  44.29813,  40.28755,
     VERTEX,   27.43411,  44.44750,  39.72522,
     VERTEX,   28.06634,  44.01859,  39.14391,
     VERTEX,   28.32572,  43.17524,  38.76565,
     VERTEX,   28.11317,  42.23956,  38.73494,
     VERTEX,   27.50989,  41.56897,  39.06351,
     VERTEX,   26.74630,  41.41960,  39.62584,
     VERTEX,   26.11407,  41.84851,  40.20715,
     VERTEX,   25.85469,  42.69186,  40.58541,
     VERTEX,   26.06723,  43.62753,  40.61612,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  27.09020,  42.93355,  39.67553,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.95601,  46.29583,  36.28603,
                       
     VERTEX,   11.64757,  46.25516,  42.23917,
     VERTEX,   11.88828,  47.15796,  42.01867,
     VERTEX,   12.45904,  47.69660,  41.46577,
     VERTEX,   13.14183,  47.66536,  40.79166,
     VERTEX,   13.67586,  47.07615,  40.25384,
     VERTEX,   13.85714,  46.15405,  40.05772,
     VERTEX,   13.61643,  45.25126,  40.27823,
     VERTEX,   13.04567,  44.71261,  40.83113,
     VERTEX,   12.36287,  44.74385,  41.50523,
     VERTEX,   11.82885,  45.33306,  42.04305,
     VERTEX,   11.64757,  46.25516,  42.23917,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.75235,  46.20461,  41.14845,
                       
     VERTEX,   11.64757,  46.25516,  42.23917,
     VERTEX,   11.88828,  47.15796,  42.01867,
     VERTEX,   12.45904,  47.69660,  41.46577,
     VERTEX,   13.14183,  47.66536,  40.79166,
     VERTEX,   13.67586,  47.07615,  40.25384,
     VERTEX,   13.85714,  46.15405,  40.05772,
     VERTEX,   13.61643,  45.25126,  40.27823,
     VERTEX,   13.04567,  44.71261,  40.83113,
     VERTEX,   12.36287,  44.74385,  41.50523,
     VERTEX,   11.82885,  45.33306,  42.04305,
     VERTEX,   11.64757,  46.25516,  42.23917,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  12.75235,  46.20461,  41.14845,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    0.82380,  42.45533,  25.30847,
                       
     VERTEX,    5.79684,  43.18660,  30.97856,
     VERTEX,    5.65544,  44.13281,  30.89928,
     VERTEX,    5.88298,  44.91182,  30.38647,
     VERTEX,    6.39256,  45.22607,  29.63602,
     VERTEX,    6.98953,  44.95553,  28.93457,
     VERTEX,    7.44587,  44.20353,  28.55005,
     VERTEX,    7.58727,  43.25732,  28.62933,
     VERTEX,    7.35973,  42.47831,  29.14213,
     VERTEX,    6.85015,  42.16406,  29.89259,
     VERTEX,    6.25318,  42.43460,  30.59404,
     VERTEX,    5.79684,  43.18660,  30.97856,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.62136,  43.69506,  29.76431,
                       
     VERTEX,    5.79684,  43.18660,  30.97856,
     VERTEX,    5.65544,  44.13281,  30.89928,
     VERTEX,    5.88298,  44.91182,  30.38647,
     VERTEX,    6.39256,  45.22607,  29.63602,
     VERTEX,    6.98953,  44.95553,  28.93457,
     VERTEX,    7.44587,  44.20353,  28.55005,
     VERTEX,    7.58727,  43.25732,  28.62933,
     VERTEX,    7.35973,  42.47831,  29.14213,
     VERTEX,    6.85015,  42.16406,  29.89259,
     VERTEX,    6.25318,  42.43460,  30.59404,
     VERTEX,    5.79684,  43.18660,  30.97856,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,   6.62136,  43.69506,  29.76431,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.46074,  29.03879,  18.89460,
                       
     VERTEX,   18.75778,  29.49762,  24.39498,
     VERTEX,   18.68977,  30.44887,  24.28499,
     VERTEX,   18.99664,  31.19434,  23.76374,
     VERTEX,   19.56118,  31.44929,  23.03033,
     VERTEX,   20.16776,  31.11633,  22.36489,
     VERTEX,   20.58469,  30.32265,  22.02161,
     VERTEX,   20.65271,  29.37140,  22.13161,
     VERTEX,   20.34583,  28.62593,  22.65286,
     VERTEX,   19.78129,  28.37098,  23.38627,
     VERTEX,   19.17471,  28.70393,  24.05170,
     VERTEX,   18.75778,  29.49762,  24.39498,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.67124,  29.91013,  23.20830,
                       
     VERTEX,   18.75778,  29.49762,  24.39498,
     VERTEX,   18.68977,  30.44887,  24.28499,
     VERTEX,   18.99664,  31.19434,  23.76374,
     VERTEX,   19.56118,  31.44929,  23.03033,
     VERTEX,   20.16776,  31.11633,  22.36489,
     VERTEX,   20.58469,  30.32265,  22.02161,
     VERTEX,   20.65271,  29.37140,  22.13161,
     VERTEX,   20.34583,  28.62593,  22.65286,
     VERTEX,   19.78129,  28.37098,  23.38627,
     VERTEX,   19.17471,  28.70393,  24.05170,
     VERTEX,   18.75778,  29.49762,  24.39498,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  19.67124,  29.91013,  23.20830,   0.80000,
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