from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.19744, -65.13416,  36.19630,
                       
     VERTEX,   21.02098, -61.74004,  36.19111,
     VERTEX,   20.50952, -60.99776,  36.52131,
     VERTEX,   19.89716, -60.30290,  36.26876,
     VERTEX,   19.41778, -59.92088,  35.52993,
     VERTEX,   19.25451, -59.99762,  34.58703,
     VERTEX,   19.46970, -60.50380,  33.80022,
     VERTEX,   19.98116, -61.24609,  33.47003,
     VERTEX,   20.59352, -61.94094,  33.72258,
     VERTEX,   21.07289, -62.32297,  34.46141,
     VERTEX,   21.23616, -62.24623,  35.40430,
     VERTEX,   21.02098, -61.74004,  36.19111,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.24534, -61.12193,  34.99567,
                       
     VERTEX,   21.02098, -61.74004,  36.19111,
     VERTEX,   20.50952, -60.99776,  36.52131,
     VERTEX,   19.89716, -60.30290,  36.26876,
     VERTEX,   19.41778, -59.92088,  35.52993,
     VERTEX,   19.25451, -59.99762,  34.58703,
     VERTEX,   19.46970, -60.50380,  33.80022,
     VERTEX,   19.98116, -61.24609,  33.47003,
     VERTEX,   20.59352, -61.94094,  33.72258,
     VERTEX,   21.07289, -62.32297,  34.46141,
     VERTEX,   21.23616, -62.24623,  35.40430,
     VERTEX,   21.02098, -61.74004,  36.19111,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  20.24534, -61.12193,  34.99567,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.42728, -75.21609,  60.50987,
                       
     VERTEX,   -0.75142, -73.76521,  56.49944,
     VERTEX,   -1.05412, -72.85432,  56.51547,
     VERTEX,   -1.68915, -72.24020,  56.13971,
     VERTEX,   -2.41395, -72.15743,  55.51569,
     VERTEX,   -2.95168, -72.63762,  54.88175,
     VERTEX,   -3.09693, -73.49734,  54.48005,
     VERTEX,   -2.79423, -74.40823,  54.46401,
     VERTEX,   -2.15920, -75.02235,  54.83977,
     VERTEX,   -1.43440, -75.10513,  55.46379,
     VERTEX,   -0.89667, -74.62494,  56.09773,
     VERTEX,   -0.75142, -73.76521,  56.49944,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -1.92418, -73.63128,  55.48974,
                       
     VERTEX,   -0.75142, -73.76521,  56.49944,
     VERTEX,   -1.05412, -72.85432,  56.51547,
     VERTEX,   -1.68915, -72.24020,  56.13971,
     VERTEX,   -2.41395, -72.15743,  55.51569,
     VERTEX,   -2.95168, -72.63762,  54.88175,
     VERTEX,   -3.09693, -73.49734,  54.48005,
     VERTEX,   -2.79423, -74.40823,  54.46401,
     VERTEX,   -2.15920, -75.02235,  54.83977,
     VERTEX,   -1.43440, -75.10513,  55.46379,
     VERTEX,   -0.89667, -74.62494,  56.09773,
     VERTEX,   -0.75142, -73.76521,  56.49944,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  -1.92418, -73.63128,  55.48974,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.30538, -81.95805,  56.18140,
                       
     VERTEX,   12.25471, -79.79511,  53.19751,
     VERTEX,   11.90900, -78.90623,  53.30697,
     VERTEX,   11.29281, -78.26301,  52.94896,
     VERTEX,   10.64151, -78.11111,  52.26023,
     VERTEX,   10.20388, -78.50858,  51.50386,
     VERTEX,   10.14707, -79.30359,  50.96875,
     VERTEX,   10.49279, -80.19247,  50.85930,
     VERTEX,   11.10898, -80.83569,  51.21731,
     VERTEX,   11.76027, -80.98758,  51.90603,
     VERTEX,   12.19791, -80.59011,  52.66240,
     VERTEX,   12.25471, -79.79511,  53.19751,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.20089, -79.54935,  52.08313,
                       
     VERTEX,   12.25471, -79.79511,  53.19751,
     VERTEX,   11.90900, -78.90623,  53.30697,
     VERTEX,   11.29281, -78.26301,  52.94896,
     VERTEX,   10.64151, -78.11111,  52.26023,
     VERTEX,   10.20388, -78.50858,  51.50386,
     VERTEX,   10.14707, -79.30359,  50.96875,
     VERTEX,   10.49279, -80.19247,  50.85930,
     VERTEX,   11.10898, -80.83569,  51.21731,
     VERTEX,   11.76027, -80.98758,  51.90603,
     VERTEX,   12.19791, -80.59011,  52.66240,
     VERTEX,   12.25471, -79.79511,  53.19751,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  11.20089, -79.54935,  52.08313,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.93100, -79.64413,  43.00708,
                       
     VERTEX,   15.50312, -76.41113,  41.06520,
     VERTEX,   15.08729, -75.57488,  41.28741,
     VERTEX,   14.47955, -74.90179,  40.97244,
     VERTEX,   13.91204, -74.64896,  40.24059,
     VERTEX,   13.60152, -74.91296,  39.37140,
     VERTEX,   13.66661, -75.59294,  38.69688,
     VERTEX,   14.08244, -76.42919,  38.47467,
     VERTEX,   14.69018, -77.10228,  38.78964,
     VERTEX,   15.25769, -77.35511,  39.52149,
     VERTEX,   15.56820, -77.09111,  40.39068,
     VERTEX,   15.50312, -76.41113,  41.06520,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.58486, -76.00204,  39.88104,
                       
     VERTEX,   15.50312, -76.41113,  41.06520,
     VERTEX,   15.08729, -75.57488,  41.28741,
     VERTEX,   14.47955, -74.90179,  40.97244,
     VERTEX,   13.91204, -74.64896,  40.24059,
     VERTEX,   13.60152, -74.91296,  39.37140,
     VERTEX,   13.66661, -75.59294,  38.69688,
     VERTEX,   14.08244, -76.42919,  38.47467,
     VERTEX,   14.69018, -77.10228,  38.78964,
     VERTEX,   15.25769, -77.35511,  39.52149,
     VERTEX,   15.56820, -77.09111,  40.39068,
     VERTEX,   15.50312, -76.41113,  41.06520,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  14.58486, -76.00204,  39.88104,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -1.20832, -62.28548,  41.95322,
                       
     VERTEX,    4.60104, -59.60555,  40.40107,
     VERTEX,    4.19047, -58.76426,  40.61384,
     VERTEX,    3.58631, -58.09137,  40.29165,
     VERTEX,    3.01932, -57.84389,  39.55756,
     VERTEX,    2.70609, -58.11636,  38.69197,
     VERTEX,    2.76624, -58.80470,  38.02551,
     VERTEX,    3.17681, -59.64599,  37.81274,
     VERTEX,    3.78097, -60.31888,  38.13493,
     VERTEX,    4.34795, -60.56635,  38.86902,
     VERTEX,    4.66119, -60.29388,  39.73461,
     VERTEX,    4.60104, -59.60555,  40.40107,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.68364, -59.20512,  39.21329,
                       
     VERTEX,    4.60104, -59.60555,  40.40107,
     VERTEX,    4.19047, -58.76426,  40.61384,
     VERTEX,    3.58631, -58.09137,  40.29165,
     VERTEX,    3.01932, -57.84389,  39.55756,
     VERTEX,    2.70609, -58.11636,  38.69197,
     VERTEX,    2.76624, -58.80470,  38.02551,
     VERTEX,    3.17681, -59.64599,  37.81274,
     VERTEX,    3.78097, -60.31888,  38.13493,
     VERTEX,    4.34795, -60.56635,  38.86902,
     VERTEX,    4.66119, -60.29388,  39.73461,
     VERTEX,    4.60104, -59.60555,  40.40107,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,   3.68364, -59.20512,  39.21329,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   66.39887, -26.83536, 106.99584,
                       
     VERTEX,   62.20012, -31.23924, 109.56905,
     VERTEX,   61.50777, -30.62918, 109.30434,
     VERTEX,   61.07004, -29.80542, 109.53107,
     VERTEX,   61.05413, -29.08261, 110.16265,
     VERTEX,   61.46611, -28.73684, 110.95783,
     VERTEX,   62.14863, -28.90018, 111.61288,
     VERTEX,   62.84098, -29.51024, 111.87759,
     VERTEX,   63.27871, -30.33400, 111.65086,
     VERTEX,   63.29462, -31.05681, 111.01928,
     VERTEX,   62.88264, -31.40258, 110.22410,
     VERTEX,   62.20012, -31.23924, 109.56905,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   62.17438, -30.06971, 110.59097,
                       
     VERTEX,   62.20012, -31.23924, 109.56905,
     VERTEX,   61.50777, -30.62918, 109.30434,
     VERTEX,   61.07004, -29.80542, 109.53107,
     VERTEX,   61.05413, -29.08261, 110.16265,
     VERTEX,   61.46611, -28.73684, 110.95783,
     VERTEX,   62.14863, -28.90018, 111.61288,
     VERTEX,   62.84098, -29.51024, 111.87759,
     VERTEX,   63.27871, -30.33400, 111.65086,
     VERTEX,   63.29462, -31.05681, 111.01928,
     VERTEX,   62.88264, -31.40258, 110.22410,
     VERTEX,   62.20012, -31.23924, 109.56905,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  62.17438, -30.06971, 110.59097,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   53.48083, -47.53203, 124.32887,
                       
     VERTEX,   49.47928, -52.49770, 122.87874,
     VERTEX,   48.90720, -51.83089, 122.49184,
     VERTEX,   48.27487, -51.13760, 122.69458,
     VERTEX,   47.82383, -50.68262, 123.40954,
     VERTEX,   47.72636, -50.63975, 124.36361,
     VERTEX,   48.01969, -51.02536, 125.19238,
     VERTEX,   48.59178, -51.69216, 125.57929,
     VERTEX,   49.22411, -52.38545, 125.37655,
     VERTEX,   49.67514, -52.84043, 124.66159,
     VERTEX,   49.77261, -52.88330, 123.70751,
     VERTEX,   49.47928, -52.49770, 122.87874,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.74949, -51.76153, 124.03556,
                       
     VERTEX,   49.47928, -52.49770, 122.87874,
     VERTEX,   48.90720, -51.83089, 122.49184,
     VERTEX,   48.27487, -51.13760, 122.69458,
     VERTEX,   47.82383, -50.68262, 123.40954,
     VERTEX,   47.72636, -50.63975, 124.36361,
     VERTEX,   48.01969, -51.02536, 125.19238,
     VERTEX,   48.59178, -51.69216, 125.57929,
     VERTEX,   49.22411, -52.38545, 125.37655,
     VERTEX,   49.67514, -52.84043, 124.66159,
     VERTEX,   49.77261, -52.88330, 123.70751,
     VERTEX,   49.47928, -52.49770, 122.87874,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  48.74949, -51.76153, 124.03556,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   52.16312, -42.49859, 124.80173,
                       
     VERTEX,   47.90443, -47.64351, 123.58913,
     VERTEX,   47.32312, -46.98248, 123.20610,
     VERTEX,   46.70068, -46.28169, 123.41362,
     VERTEX,   46.27488, -45.80881, 124.13242,
     VERTEX,   46.20834, -45.74446, 125.08794,
     VERTEX,   46.52650, -46.11323, 125.91522,
     VERTEX,   47.10782, -46.77425, 126.29826,
     VERTEX,   47.73026, -47.47505, 126.09074,
     VERTEX,   48.15606, -47.94793, 125.37194,
     VERTEX,   48.22259, -48.01228, 124.41641,
     VERTEX,   47.90443, -47.64351, 123.58913,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   47.21547, -46.87837, 124.75218,
                       
     VERTEX,   47.90443, -47.64351, 123.58913,
     VERTEX,   47.32312, -46.98248, 123.20610,
     VERTEX,   46.70068, -46.28169, 123.41362,
     VERTEX,   46.27488, -45.80881, 124.13242,
     VERTEX,   46.20834, -45.74446, 125.08794,
     VERTEX,   46.52650, -46.11323, 125.91522,
     VERTEX,   47.10782, -46.77425, 126.29826,
     VERTEX,   47.73026, -47.47505, 126.09074,
     VERTEX,   48.15606, -47.94793, 125.37194,
     VERTEX,   48.22259, -48.01228, 124.41641,
     VERTEX,   47.90443, -47.64351, 123.58913,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  47.21547, -46.87837, 124.75218,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   43.34501, -31.33773, 127.55103,
                       
     VERTEX,   38.58581, -36.91530, 126.15307,
     VERTEX,   38.01192, -36.24725, 125.77103,
     VERTEX,   37.38641, -35.54943, 125.97932,
     VERTEX,   36.94820, -35.08838, 126.69835,
     VERTEX,   36.86468, -35.04022, 127.65350,
     VERTEX,   37.16774, -35.42334, 128.47992,
     VERTEX,   37.74164, -36.09139, 128.86195,
     VERTEX,   38.36715, -36.78922, 128.65367,
     VERTEX,   38.80536, -37.25026, 127.93464,
     VERTEX,   38.88888, -37.29842, 126.97949,
     VERTEX,   38.58581, -36.91530, 126.15307,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.87678, -36.16932, 127.31649,
                       
     VERTEX,   38.58581, -36.91530, 126.15307,
     VERTEX,   38.01192, -36.24725, 125.77103,
     VERTEX,   37.38641, -35.54943, 125.97932,
     VERTEX,   36.94820, -35.08838, 126.69835,
     VERTEX,   36.86468, -35.04022, 127.65350,
     VERTEX,   37.16774, -35.42334, 128.47992,
     VERTEX,   37.74164, -36.09139, 128.86195,
     VERTEX,   38.36715, -36.78922, 128.65367,
     VERTEX,   38.80536, -37.25026, 127.93464,
     VERTEX,   38.88888, -37.29842, 126.97949,
     VERTEX,   38.58581, -36.91530, 126.15307,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  37.87678, -36.16932, 127.31649,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.23853, -37.90642, 126.99315,
                       
     VERTEX,   38.00278, -43.16645, 124.99157,
     VERTEX,   37.45079, -42.48544, 124.60026,
     VERTEX,   36.80060, -41.80626, 124.79407,
     VERTEX,   36.30056, -41.38834, 125.49898,
     VERTEX,   36.14166, -41.39130, 126.44573,
     VERTEX,   36.38461, -41.81402, 127.27271,
     VERTEX,   36.93661, -42.49503, 127.66402,
     VERTEX,   37.58680, -43.17421, 127.47021,
     VERTEX,   38.08684, -43.59214, 126.76530,
     VERTEX,   38.24574, -43.58917, 125.81854,
     VERTEX,   38.00278, -43.16645, 124.99157,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.19370, -42.49023, 126.13214,
                       
     VERTEX,   38.00278, -43.16645, 124.99157,
     VERTEX,   37.45079, -42.48544, 124.60026,
     VERTEX,   36.80060, -41.80626, 124.79407,
     VERTEX,   36.30056, -41.38834, 125.49898,
     VERTEX,   36.14166, -41.39130, 126.44573,
     VERTEX,   36.38461, -41.81402, 127.27271,
     VERTEX,   36.93661, -42.49503, 127.66402,
     VERTEX,   37.58680, -43.17421, 127.47021,
     VERTEX,   38.08684, -43.59214, 126.76530,
     VERTEX,   38.24574, -43.58917, 125.81854,
     VERTEX,   38.00278, -43.16645, 124.99157,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  37.19370, -42.49023, 126.13214,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.66786,  -5.25612, 110.84238,
                       
     VERTEX,   -6.78212,  -2.94422, 112.46609,
     VERTEX,   -7.32079,  -2.19910, 112.74221,
     VERTEX,   -7.82063,  -1.44278, 112.42638,
     VERTEX,   -8.09073,  -0.96416, 111.63926,
     VERTEX,   -8.02792,  -0.94604, 110.68149,
     VERTEX,   -7.65619,  -1.39536, 109.91891,
     VERTEX,   -7.11753,  -2.14048, 109.64279,
     VERTEX,   -6.61768,  -2.89679, 109.95862,
     VERTEX,   -6.34758,  -3.37542, 110.74574,
     VERTEX,   -6.41039,  -3.39353, 111.70351,
     VERTEX,   -6.78212,  -2.94422, 112.46609,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.21916,  -2.16979, 111.19250,
                       
     VERTEX,   -6.78212,  -2.94422, 112.46609,
     VERTEX,   -7.32079,  -2.19910, 112.74221,
     VERTEX,   -7.82063,  -1.44278, 112.42638,
     VERTEX,   -8.09073,  -0.96416, 111.63926,
     VERTEX,   -8.02792,  -0.94604, 110.68149,
     VERTEX,   -7.65619,  -1.39536, 109.91891,
     VERTEX,   -7.11753,  -2.14048, 109.64279,
     VERTEX,   -6.61768,  -2.89679, 109.95862,
     VERTEX,   -6.34758,  -3.37542, 110.74574,
     VERTEX,   -6.41039,  -3.39353, 111.70351,
     VERTEX,   -6.78212,  -2.94422, 112.46609,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,  -7.21916,  -2.16979, 111.19250,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.77564, -11.56174, 109.20683,
                       
     VERTEX,   -8.89928,  -9.34786, 111.47444,
     VERTEX,   -9.45009,  -8.60417, 111.72965,
     VERTEX,   -9.89991,  -7.82215, 111.40146,
     VERTEX,  -10.07692,  -7.30050, 110.61523,
     VERTEX,   -9.91351,  -7.23849, 109.67128,
     VERTEX,   -9.47210,  -7.65978, 108.93015,
     VERTEX,   -8.92129,  -8.40347, 108.67495,
     VERTEX,   -8.47147,  -9.18549, 109.00314,
     VERTEX,   -8.29446,  -9.70714, 109.78937,
     VERTEX,   -8.45787,  -9.76915, 110.73332,
     VERTEX,   -8.89928,  -9.34786, 111.47444,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -9.18569,  -8.50382, 110.20230,
                       
     VERTEX,   -8.89928,  -9.34786, 111.47444,
     VERTEX,   -9.45009,  -8.60417, 111.72965,
     VERTEX,   -9.89991,  -7.82215, 111.40146,
     VERTEX,  -10.07692,  -7.30050, 110.61523,
     VERTEX,   -9.91351,  -7.23849, 109.67128,
     VERTEX,   -9.47210,  -7.65978, 108.93015,
     VERTEX,   -8.92129,  -8.40347, 108.67495,
     VERTEX,   -8.47147,  -9.18549, 109.00314,
     VERTEX,   -8.29446,  -9.70714, 109.78937,
     VERTEX,   -8.45787,  -9.76915, 110.73332,
     VERTEX,   -8.89928,  -9.34786, 111.47444,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,  -9.18569,  -8.50382, 110.20230,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.77765, -16.19672, 107.67947,
                       
     VERTEX,   -6.98291, -14.01659, 110.11471,
     VERTEX,   -7.54406, -13.28147, 110.37222,
     VERTEX,   -7.98980, -12.49463, 110.05004,
     VERTEX,   -8.14989, -11.95662, 109.27126,
     VERTEX,   -7.96317, -11.87293, 108.33331,
     VERTEX,   -7.50096, -12.27555, 107.59448,
     VERTEX,   -6.93981, -13.01067, 107.33698,
     VERTEX,   -6.49406, -13.79751, 107.65915,
     VERTEX,   -6.33398, -14.33552, 108.43794,
     VERTEX,   -6.52070, -14.41920, 109.37588,
     VERTEX,   -6.98291, -14.01659, 110.11471,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.24193, -13.14607, 108.85460,
                       
     VERTEX,   -6.98291, -14.01659, 110.11471,
     VERTEX,   -7.54406, -13.28147, 110.37222,
     VERTEX,   -7.98980, -12.49463, 110.05004,
     VERTEX,   -8.14989, -11.95662, 109.27126,
     VERTEX,   -7.96317, -11.87293, 108.33331,
     VERTEX,   -7.50096, -12.27555, 107.59448,
     VERTEX,   -6.93981, -13.01067, 107.33698,
     VERTEX,   -6.49406, -13.79751, 107.65915,
     VERTEX,   -6.33398, -14.33552, 108.43794,
     VERTEX,   -6.52070, -14.41920, 109.37588,
     VERTEX,   -6.98291, -14.01659, 110.11471,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,  -7.24193, -13.14607, 108.85460,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -35.67400,   3.50235, 104.34978,
                       
     VERTEX,  -31.64871,   4.86231, 107.94199,
     VERTEX,  -32.17333,   5.64991, 108.10342,
     VERTEX,  -32.43314,   6.49853, 107.73743,
     VERTEX,  -32.32888,   7.08403, 106.98383,
     VERTEX,  -31.90038,   7.18277, 106.13046,
     VERTEX,  -31.31132,   6.75704, 105.50327,
     VERTEX,  -30.78669,   5.96944, 105.34185,
     VERTEX,  -30.52689,   5.12082, 105.70783,
     VERTEX,  -30.63115,   4.53532, 106.46144,
     VERTEX,  -31.05964,   4.43658, 107.31481,
     VERTEX,  -31.64871,   4.86231, 107.94199,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.48001,   5.80967, 106.72263,
                       
     VERTEX,  -31.64871,   4.86231, 107.94199,
     VERTEX,  -32.17333,   5.64991, 108.10342,
     VERTEX,  -32.43314,   6.49853, 107.73743,
     VERTEX,  -32.32888,   7.08403, 106.98383,
     VERTEX,  -31.90038,   7.18277, 106.13046,
     VERTEX,  -31.31132,   6.75704, 105.50327,
     VERTEX,  -30.78669,   5.96944, 105.34185,
     VERTEX,  -30.52689,   5.12082, 105.70783,
     VERTEX,  -30.63115,   4.53532, 106.46144,
     VERTEX,  -31.05964,   4.43658, 107.31481,
     VERTEX,  -31.64871,   4.86231, 107.94199,
                       
     END,              
                       
     CYLINDER,  -24.69400,   9.54300, 110.56200, -31.48001,   5.80967, 106.72263,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -1.17334, -20.22364, 107.72651,
                       
     VERTEX,    3.64740, -17.85870, 109.46468,
     VERTEX,    3.09041, -17.13411, 109.75851,
     VERTEX,    2.57699, -16.37931, 109.46140,
     VERTEX,    2.30327, -15.88259, 108.68684,
     VERTEX,    2.37378, -15.83369, 107.73068,
     VERTEX,    2.76160, -16.25128, 106.95815,
     VERTEX,    3.31859, -16.97587, 106.66432,
     VERTEX,    3.83201, -17.73067, 106.96143,
     VERTEX,    4.10574, -18.22739, 107.73598,
     VERTEX,    4.03522, -18.27629, 108.69215,
     VERTEX,    3.64740, -17.85870, 109.46468,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.20450, -17.05499, 108.21141,
                       
     VERTEX,    3.64740, -17.85870, 109.46468,
     VERTEX,    3.09041, -17.13411, 109.75851,
     VERTEX,    2.57699, -16.37931, 109.46140,
     VERTEX,    2.30327, -15.88259, 108.68684,
     VERTEX,    2.37378, -15.83369, 107.73068,
     VERTEX,    2.76160, -16.25128, 106.95815,
     VERTEX,    3.31859, -16.97587, 106.66432,
     VERTEX,    3.83201, -17.73067, 106.96143,
     VERTEX,    4.10574, -18.22739, 107.73598,
     VERTEX,    4.03522, -18.27629, 108.69215,
     VERTEX,    3.64740, -17.85870, 109.46468,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,   3.20450, -17.05499, 108.21141,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.95219,  38.91912,  36.64970,
                       
     VERTEX,   20.61658,  36.16971,  32.34796,
     VERTEX,   20.26348,  37.05637,  32.24427,
     VERTEX,   19.71035,  37.72500,  32.65485,
     VERTEX,   19.16847,  37.92021,  33.42287,
     VERTEX,   18.84482,  37.56744,  34.25498,
     VERTEX,   18.86303,  36.80143,  34.83334,
     VERTEX,   19.21614,  35.91477,  34.93703,
     VERTEX,   19.76927,  35.24614,  34.52645,
     VERTEX,   20.31115,  35.05093,  33.75843,
     VERTEX,   20.63479,  35.40370,  32.92632,
     VERTEX,   20.61658,  36.16971,  32.34796,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.73981,  36.48557,  33.59065,
                       
     VERTEX,   20.61658,  36.16971,  32.34796,
     VERTEX,   20.26348,  37.05637,  32.24427,
     VERTEX,   19.71035,  37.72500,  32.65485,
     VERTEX,   19.16847,  37.92021,  33.42287,
     VERTEX,   18.84482,  37.56744,  34.25498,
     VERTEX,   18.86303,  36.80143,  34.83334,
     VERTEX,   19.21614,  35.91477,  34.93703,
     VERTEX,   19.76927,  35.24614,  34.52645,
     VERTEX,   20.31115,  35.05093,  33.75843,
     VERTEX,   20.63479,  35.40370,  32.92632,
     VERTEX,   20.61658,  36.16971,  32.34796,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,  19.73981,  36.48557,  33.59065,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   44.12027,  39.84911,  64.52891,
                       
     VERTEX,   41.65717,  40.32059,  57.71684,
     VERTEX,   41.42266,  41.22631,  57.93196,
     VERTEX,   40.77572,  41.77536,  58.38098,
     VERTEX,   39.96346,  41.75802,  58.89238,
     VERTEX,   39.29613,  41.18091,  59.27082,
     VERTEX,   39.02863,  40.26447,  59.37176,
     VERTEX,   39.26315,  39.35875,  59.15664,
     VERTEX,   39.91008,  38.80971,  58.70762,
     VERTEX,   40.72235,  38.82705,  58.19622,
     VERTEX,   41.38968,  39.40416,  57.81777,
     VERTEX,   41.65717,  40.32059,  57.71684,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.34290,  40.29253,  58.54430,
                       
     VERTEX,   41.65717,  40.32059,  57.71684,
     VERTEX,   41.42266,  41.22631,  57.93196,
     VERTEX,   40.77572,  41.77536,  58.38098,
     VERTEX,   39.96346,  41.75802,  58.89238,
     VERTEX,   39.29613,  41.18091,  59.27082,
     VERTEX,   39.02863,  40.26447,  59.37176,
     VERTEX,   39.26315,  39.35875,  59.15664,
     VERTEX,   39.91008,  38.80971,  58.70762,
     VERTEX,   40.72235,  38.82705,  58.19622,
     VERTEX,   41.38968,  39.40416,  57.81777,
     VERTEX,   41.65717,  40.32059,  57.71684,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  40.34290,  40.29253,  58.54430,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.08308,  46.90093,  62.16647,
                       
     VERTEX,   28.25703,  46.55128,  56.17152,
     VERTEX,   28.00964,  47.46822,  56.31153,
     VERTEX,   27.39404,  48.04536,  56.76930,
     VERTEX,   26.64537,  48.06223,  57.36998,
     VERTEX,   26.04960,  47.51240,  57.88412,
     VERTEX,   25.83430,  46.60588,  58.11536,
     VERTEX,   26.08170,  45.68893,  57.97535,
     VERTEX,   26.69730,  45.11180,  57.51758,
     VERTEX,   27.44596,  45.09492,  56.91690,
     VERTEX,   28.04173,  45.64476,  56.40275,
     VERTEX,   28.25703,  46.55128,  56.17152,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.04567,  46.57858,  57.14344,
                       
     VERTEX,   28.25703,  46.55128,  56.17152,
     VERTEX,   28.00964,  47.46822,  56.31153,
     VERTEX,   27.39404,  48.04536,  56.76930,
     VERTEX,   26.64537,  48.06223,  57.36998,
     VERTEX,   26.04960,  47.51240,  57.88412,
     VERTEX,   25.83430,  46.60588,  58.11536,
     VERTEX,   26.08170,  45.68893,  57.97535,
     VERTEX,   26.69730,  45.11180,  57.51758,
     VERTEX,   27.44596,  45.09492,  56.91690,
     VERTEX,   28.04173,  45.64476,  56.40275,
     VERTEX,   28.25703,  46.55128,  56.17152,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.04567,  46.57858,  57.14344,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.57466,  49.70556,  48.90992,
                       
     VERTEX,   25.43604,  48.02618,  43.21199,
     VERTEX,   25.14830,  48.94182,  43.23198,
     VERTEX,   24.57105,  49.56493,  43.67933,
     VERTEX,   23.92479,  49.65750,  44.38316,
     VERTEX,   23.45636,  49.18417,  45.07463,
     VERTEX,   23.34468,  48.32573,  45.48962,
     VERTEX,   23.63243,  47.41009,  45.46962,
     VERTEX,   24.20967,  46.78698,  45.02228,
     VERTEX,   24.85594,  46.69441,  44.31845,
     VERTEX,   25.32437,  47.16774,  43.62698,
     VERTEX,   25.43604,  48.02618,  43.21199,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.39036,  48.17596,  44.35080,
                       
     VERTEX,   25.43604,  48.02618,  43.21199,
     VERTEX,   25.14830,  48.94182,  43.23198,
     VERTEX,   24.57105,  49.56493,  43.67933,
     VERTEX,   23.92479,  49.65750,  44.38316,
     VERTEX,   23.45636,  49.18417,  45.07463,
     VERTEX,   23.34468,  48.32573,  45.48962,
     VERTEX,   23.63243,  47.41009,  45.46962,
     VERTEX,   24.20967,  46.78698,  45.02228,
     VERTEX,   24.85594,  46.69441,  44.31845,
     VERTEX,   25.32437,  47.16774,  43.62698,
     VERTEX,   25.43604,  48.02618,  43.21199,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,  24.39036,  48.17596,  44.35080,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.26177,  35.01141,  42.19957,
                       
     VERTEX,   37.29909,  33.46413,  36.48815,
     VERTEX,   37.01521,  34.38073,  36.51747,
     VERTEX,   36.43338,  34.99966,  36.96470,
     VERTEX,   35.77586,  35.08451,  37.65901,
     VERTEX,   35.29378,  34.60286,  38.33519,
     VERTEX,   35.17129,  33.73870,  38.73497,
     VERTEX,   35.45517,  32.82211,  38.70564,
     VERTEX,   36.03699,  32.20318,  38.25841,
     VERTEX,   36.69451,  32.11833,  37.56411,
     VERTEX,   37.17659,  32.59998,  36.88792,
     VERTEX,   37.29909,  33.46413,  36.48815,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.23518,  33.60142,  37.61156,
                       
     VERTEX,   37.29909,  33.46413,  36.48815,
     VERTEX,   37.01521,  34.38073,  36.51747,
     VERTEX,   36.43338,  34.99966,  36.96470,
     VERTEX,   35.77586,  35.08451,  37.65901,
     VERTEX,   35.29378,  34.60286,  38.33519,
     VERTEX,   35.17129,  33.73870,  38.73497,
     VERTEX,   35.45517,  32.82211,  38.70564,
     VERTEX,   36.03699,  32.20318,  38.25841,
     VERTEX,   36.69451,  32.11833,  37.56411,
     VERTEX,   37.17659,  32.59998,  36.88792,
     VERTEX,   37.29909,  33.46413,  36.48815,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  36.23518,  33.60142,  37.61156,   0.80000,
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
                       
     SPHERE,  -24.69400,   9.54300, 110.56200,   0.80000,
                       
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
