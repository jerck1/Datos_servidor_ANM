from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.91818, -64.78145,  35.97953,
                       
     VERTEX,   21.47575, -61.52818,  36.04783,
     VERTEX,   20.95892, -60.79404,  36.38774,
     VERTEX,   20.33966, -60.10189,  36.14474,
     VERTEX,   19.85452, -59.71609,  35.41167,
     VERTEX,   19.68880, -59.78401,  34.46853,
     VERTEX,   19.90580, -60.27971,  33.67556,
     VERTEX,   20.42263, -61.01384,  33.33566,
     VERTEX,   21.04189, -61.70599,  33.57865,
     VERTEX,   21.52703, -62.09179,  34.31172,
     VERTEX,   21.69275, -62.02387,  35.25486,
     VERTEX,   21.47575, -61.52818,  36.04783,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.69077, -60.90394,  34.86170,
                       
     VERTEX,   21.47575, -61.52818,  36.04783,
     VERTEX,   20.95892, -60.79404,  36.38774,
     VERTEX,   20.33966, -60.10189,  36.14474,
     VERTEX,   19.85452, -59.71609,  35.41167,
     VERTEX,   19.68880, -59.78401,  34.46853,
     VERTEX,   19.90580, -60.27971,  33.67556,
     VERTEX,   20.42263, -61.01384,  33.33566,
     VERTEX,   21.04189, -61.70599,  33.57865,
     VERTEX,   21.52703, -62.09179,  34.31172,
     VERTEX,   21.69275, -62.02387,  35.25486,
     VERTEX,   21.47575, -61.52818,  36.04783,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  20.69077, -60.90394,  34.86170,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -5.30106, -75.92084,  59.80971,
                       
     VERTEX,   -0.02473, -74.22612,  56.02617,
     VERTEX,   -0.34818, -73.32530,  56.10038,
     VERTEX,   -1.00775, -72.70773,  55.77607,
     VERTEX,   -1.75149, -72.60928,  55.17710,
     VERTEX,   -2.29532, -73.06758,  54.53227,
     VERTEX,   -2.43153, -73.90755,  54.08788,
     VERTEX,   -2.10808, -74.80837,  54.01366,
     VERTEX,   -1.44852, -75.42595,  54.33797,
     VERTEX,   -0.70477, -75.52439,  54.93694,
     VERTEX,   -0.16094, -75.06609,  55.58177,
     VERTEX,   -0.02473, -74.22612,  56.02617,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -1.22813, -74.06683,  55.05702,
                       
     VERTEX,   -0.02473, -74.22612,  56.02617,
     VERTEX,   -0.34818, -73.32530,  56.10038,
     VERTEX,   -1.00775, -72.70773,  55.77607,
     VERTEX,   -1.75149, -72.60928,  55.17710,
     VERTEX,   -2.29532, -73.06758,  54.53227,
     VERTEX,   -2.43153, -73.90755,  54.08788,
     VERTEX,   -2.10808, -74.80837,  54.01366,
     VERTEX,   -1.44852, -75.42595,  54.33797,
     VERTEX,   -0.70477, -75.52439,  54.93694,
     VERTEX,   -0.16094, -75.06609,  55.58177,
     VERTEX,   -0.02473, -74.22612,  56.02617,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  -1.22813, -74.06683,  55.05702,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.60531, -82.11551,  55.58980,
                       
     VERTEX,   13.09564, -79.90594,  52.79199,
     VERTEX,   12.73482, -79.02894,  52.94124,
     VERTEX,   12.09496, -78.38789,  52.62306,
     VERTEX,   11.42047, -78.22765,  51.95899,
     VERTEX,   10.96898, -78.60943,  51.20268,
     VERTEX,   10.91294, -79.38740,  50.64302,
     VERTEX,   11.27377, -80.26440,  50.49377,
     VERTEX,   11.91363, -80.90545,  50.81195,
     VERTEX,   12.58812, -81.06569,  51.47602,
     VERTEX,   13.03961, -80.68391,  52.23233,
     VERTEX,   13.09564, -79.90594,  52.79199,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.00429, -79.64667,  51.71751,
                       
     VERTEX,   13.09564, -79.90594,  52.79199,
     VERTEX,   12.73482, -79.02894,  52.94124,
     VERTEX,   12.09496, -78.38789,  52.62306,
     VERTEX,   11.42047, -78.22765,  51.95899,
     VERTEX,   10.96898, -78.60943,  51.20268,
     VERTEX,   10.91294, -79.38740,  50.64302,
     VERTEX,   11.27377, -80.26440,  50.49377,
     VERTEX,   11.91363, -80.90545,  50.81195,
     VERTEX,   12.58812, -81.06569,  51.47602,
     VERTEX,   13.03961, -80.68391,  52.23233,
     VERTEX,   13.09564, -79.90594,  52.79199,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  12.00429, -79.64667,  51.71751,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.17443, -79.50359,  42.54174,
                       
     VERTEX,   16.30199, -76.33414,  40.74987,
     VERTEX,   15.87455, -75.51175,  40.99999,
     VERTEX,   15.24803, -74.84345,  40.71286,
     VERTEX,   14.66173, -74.58451,  39.99815,
     VERTEX,   14.33961, -74.83384,  39.12886,
     VERTEX,   14.40470, -75.49621,  38.43702,
     VERTEX,   14.83214, -76.31860,  38.18690,
     VERTEX,   15.45866, -76.98691,  38.47403,
     VERTEX,   16.04496, -77.24584,  39.18874,
     VERTEX,   16.36708, -76.99651,  40.05804,
     VERTEX,   16.30199, -76.33414,  40.74987,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.35335, -75.91518,  39.59344,
                       
     VERTEX,   16.30199, -76.33414,  40.74987,
     VERTEX,   15.87455, -75.51175,  40.99999,
     VERTEX,   15.24803, -74.84345,  40.71286,
     VERTEX,   14.66173, -74.58451,  39.99815,
     VERTEX,   14.33961, -74.83384,  39.12886,
     VERTEX,   14.40470, -75.49621,  38.43702,
     VERTEX,   14.83214, -76.31860,  38.18690,
     VERTEX,   15.45866, -76.98691,  38.47403,
     VERTEX,   16.04496, -77.24584,  39.18874,
     VERTEX,   16.36708, -76.99651,  40.05804,
     VERTEX,   16.30199, -76.33414,  40.74987,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  15.35335, -75.91518,  39.59344,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.52236, -62.59362,  41.50903,
                       
     VERTEX,    5.04623, -59.82014,  40.10130,
     VERTEX,    4.61740, -58.99842,  40.35127,
     VERTEX,    3.99385, -58.32839,  40.06171,
     VERTEX,    3.41374, -58.06599,  39.34322,
     VERTEX,    3.09866, -58.31144,  38.47025,
     VERTEX,    3.16895, -58.97099,  37.77624,
     VERTEX,    3.59778, -59.79271,  37.52627,
     VERTEX,    4.22133, -60.46273,  37.81583,
     VERTEX,    4.80144, -60.72514,  38.53432,
     VERTEX,    5.11652, -60.47969,  39.40729,
     VERTEX,    5.04623, -59.82014,  40.10130,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    4.10759, -59.39557,  38.93877,
                       
     VERTEX,    5.04623, -59.82014,  40.10130,
     VERTEX,    4.61740, -58.99842,  40.35127,
     VERTEX,    3.99385, -58.32839,  40.06171,
     VERTEX,    3.41374, -58.06599,  39.34322,
     VERTEX,    3.09866, -58.31144,  38.47025,
     VERTEX,    3.16895, -58.97099,  37.77624,
     VERTEX,    3.59778, -59.79271,  37.52627,
     VERTEX,    4.22133, -60.46273,  37.81583,
     VERTEX,    4.80144, -60.72514,  38.53432,
     VERTEX,    5.11652, -60.47969,  39.40729,
     VERTEX,    5.04623, -59.82014,  40.10130,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,   4.10759, -59.39557,  38.93877,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   65.35728, -26.32489, 107.30499,
                       
     VERTEX,   61.73971, -30.95889, 109.82398,
     VERTEX,   60.99170, -30.45037, 109.50230,
     VERTEX,   60.44954, -29.67595, 109.66943,
     VERTEX,   60.32032, -28.93143, 110.26153,
     VERTEX,   60.65340, -28.50118, 111.05244,
     VERTEX,   61.32156, -28.54956, 111.74007,
     VERTEX,   62.06958, -29.05807, 112.06175,
     VERTEX,   62.61174, -29.83250, 111.89462,
     VERTEX,   62.74095, -30.57702, 111.30252,
     VERTEX,   62.40787, -31.00727, 110.51161,
     VERTEX,   61.73971, -30.95889, 109.82398,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   61.53064, -29.75422, 110.78203,
                       
     VERTEX,   61.73971, -30.95889, 109.82398,
     VERTEX,   60.99170, -30.45037, 109.50230,
     VERTEX,   60.44954, -29.67595, 109.66943,
     VERTEX,   60.32032, -28.93143, 110.26153,
     VERTEX,   60.65340, -28.50118, 111.05244,
     VERTEX,   61.32156, -28.54956, 111.74007,
     VERTEX,   62.06958, -29.05807, 112.06175,
     VERTEX,   62.61174, -29.83250, 111.89462,
     VERTEX,   62.74095, -30.57702, 111.30252,
     VERTEX,   62.40787, -31.00727, 110.51161,
     VERTEX,   61.73971, -30.95889, 109.82398,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  61.53064, -29.75422, 110.78203,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   53.31007, -47.62928, 124.29635,
                       
     VERTEX,   49.37621, -52.55931, 122.86118,
     VERTEX,   48.80276, -51.89499, 122.47204,
     VERTEX,   48.16865, -51.20264, 122.67244,
     VERTEX,   47.71609, -50.74673, 123.38583,
     VERTEX,   47.61793, -50.70139, 124.33972,
     VERTEX,   47.91168, -51.08395, 125.16976,
     VERTEX,   48.48513, -51.74827, 125.55890,
     VERTEX,   49.11924, -52.44062, 125.35850,
     VERTEX,   49.57181, -52.89653, 124.64511,
     VERTEX,   49.66996, -52.94187, 123.69122,
     VERTEX,   49.37621, -52.55931, 122.86118,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.64395, -51.82163, 124.01547,
                       
     VERTEX,   49.37621, -52.55931, 122.86118,
     VERTEX,   48.80276, -51.89499, 122.47204,
     VERTEX,   48.16865, -51.20264, 122.67244,
     VERTEX,   47.71609, -50.74673, 123.38583,
     VERTEX,   47.61793, -50.70139, 124.33972,
     VERTEX,   47.91168, -51.08395, 125.16976,
     VERTEX,   48.48513, -51.74827, 125.55890,
     VERTEX,   49.11924, -52.44062, 125.35850,
     VERTEX,   49.57181, -52.89653, 124.64511,
     VERTEX,   49.66996, -52.94187, 123.69122,
     VERTEX,   49.37621, -52.55931, 122.86118,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  48.64395, -51.82163, 124.01547,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   51.77182, -42.71342, 124.80021,
                       
     VERTEX,   47.67163, -47.77724, 123.59423,
     VERTEX,   47.08803, -47.12125, 123.20606,
     VERTEX,   46.46072, -46.42319, 123.40810,
     VERTEX,   46.02934, -45.94972, 124.12317,
     VERTEX,   45.95863, -45.88167, 125.07814,
     VERTEX,   46.27563, -46.24504, 125.90824,
     VERTEX,   46.85924, -46.90103, 126.29642,
     VERTEX,   47.48654, -47.59908, 126.09438,
     VERTEX,   47.91793, -48.07256, 125.37931,
     VERTEX,   47.98863, -48.14061, 124.42434,
     VERTEX,   47.67163, -47.77724, 123.59423,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.97363, -47.01114, 124.75124,
                       
     VERTEX,   47.67163, -47.77724, 123.59423,
     VERTEX,   47.08803, -47.12125, 123.20606,
     VERTEX,   46.46072, -46.42319, 123.40810,
     VERTEX,   46.02934, -45.94972, 124.12317,
     VERTEX,   45.95863, -45.88167, 125.07814,
     VERTEX,   46.27563, -46.24504, 125.90824,
     VERTEX,   46.85924, -46.90103, 126.29642,
     VERTEX,   47.48654, -47.59908, 126.09438,
     VERTEX,   47.91793, -48.07256, 125.37931,
     VERTEX,   47.98863, -48.14061, 124.42434,
     VERTEX,   47.67163, -47.77724, 123.59423,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  46.97363, -47.01114, 124.75124,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.58757, -31.91279, 127.48913,
                       
     VERTEX,   38.12199, -37.27274, 126.11875,
     VERTEX,   37.54609, -36.60841, 125.73328,
     VERTEX,   36.91769, -35.91211, 125.93793,
     VERTEX,   36.47681, -35.44981, 126.65453,
     VERTEX,   36.39188, -35.39810, 127.60936,
     VERTEX,   36.69531, -35.77671, 128.43771,
     VERTEX,   37.27122, -36.44105, 128.82320,
     VERTEX,   37.89962, -37.13735, 128.61855,
     VERTEX,   38.34049, -37.59965, 127.90195,
     VERTEX,   38.42543, -37.65136, 126.94711,
     VERTEX,   38.12199, -37.27274, 126.11875,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.40865, -36.52473, 127.27824,
                       
     VERTEX,   38.12199, -37.27274, 126.11875,
     VERTEX,   37.54609, -36.60841, 125.73328,
     VERTEX,   36.91769, -35.91211, 125.93793,
     VERTEX,   36.47681, -35.44981, 126.65453,
     VERTEX,   36.39188, -35.39810, 127.60936,
     VERTEX,   36.69531, -35.77671, 128.43771,
     VERTEX,   37.27122, -36.44105, 128.82320,
     VERTEX,   37.89962, -37.13735, 128.61855,
     VERTEX,   38.34049, -37.59965, 127.90195,
     VERTEX,   38.42543, -37.65136, 126.94711,
     VERTEX,   38.12199, -37.27274, 126.11875,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  37.40865, -36.52473, 127.27824,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.70946, -38.49288, 126.92107,
                       
     VERTEX,   37.67094, -43.52708, 124.94251,
     VERTEX,   37.12094, -42.84213, 124.55527,
     VERTEX,   36.47385, -42.16122, 124.75331,
     VERTEX,   35.97681, -41.74442, 125.46101,
     VERTEX,   35.81969, -41.75094, 126.40804,
     VERTEX,   36.06250, -42.17829, 127.23267,
     VERTEX,   36.61249, -42.86324, 127.61993,
     VERTEX,   37.25958, -43.54415, 127.42188,
     VERTEX,   37.75662, -43.96095, 126.71418,
     VERTEX,   37.91374, -43.95443, 125.76715,
     VERTEX,   37.67094, -43.52708, 124.94251,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.86671, -42.85268, 126.08759,
                       
     VERTEX,   37.67094, -43.52708, 124.94251,
     VERTEX,   37.12094, -42.84213, 124.55527,
     VERTEX,   36.47385, -42.16122, 124.75331,
     VERTEX,   35.97681, -41.74442, 125.46101,
     VERTEX,   35.81969, -41.75094, 126.40804,
     VERTEX,   36.06250, -42.17829, 127.23267,
     VERTEX,   36.61249, -42.86324, 127.61993,
     VERTEX,   37.25958, -43.54415, 127.42188,
     VERTEX,   37.75662, -43.96095, 126.71418,
     VERTEX,   37.91374, -43.95443, 125.76715,
     VERTEX,   37.67094, -43.52708, 124.94251,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  36.86671, -42.85268, 126.08759,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -25.58733, -24.73695,  85.81169,
                       
     VERTEX,  -22.70835, -24.25353,  90.45215,
     VERTEX,  -23.05877, -23.36012,  90.47718,
     VERTEX,  -22.98952, -22.48738,  90.08333,
     VERTEX,  -22.52705, -21.96866,  89.42102,
     VERTEX,  -21.84800, -22.00209,  88.74325,
     VERTEX,  -21.21176, -22.57491,  88.30889,
     VERTEX,  -20.86134, -23.46832,  88.28386,
     VERTEX,  -20.93059, -24.34106,  88.67771,
     VERTEX,  -21.39306, -24.85979,  89.34001,
     VERTEX,  -22.07211, -24.82635,  90.01779,
     VERTEX,  -22.70835, -24.25353,  90.45215,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -21.96005, -23.41422,  89.38052,
                       
     VERTEX,  -22.70835, -24.25353,  90.45215,
     VERTEX,  -23.05877, -23.36012,  90.47718,
     VERTEX,  -22.98952, -22.48738,  90.08333,
     VERTEX,  -22.52705, -21.96866,  89.42102,
     VERTEX,  -21.84800, -22.00209,  88.74325,
     VERTEX,  -21.21176, -22.57491,  88.30889,
     VERTEX,  -20.86134, -23.46832,  88.28386,
     VERTEX,  -20.93059, -24.34106,  88.67771,
     VERTEX,  -21.39306, -24.85979,  89.34001,
     VERTEX,  -22.07211, -24.82635,  90.01779,
     VERTEX,  -22.70835, -24.25353,  90.45215,
                       
     END,              
                       
     CYLINDER,  -16.09100, -21.27400,  95.15500, -21.96005, -23.41422,  89.38052,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.34910,  -5.63051, 110.88924,
                       
     VERTEX,   -6.52773,  -3.19146, 112.46394,
     VERTEX,   -7.08668,  -2.47420, 112.77171,
     VERTEX,   -7.62098,  -1.72905, 112.48733,
     VERTEX,   -7.92654,  -1.24062, 111.71943,
     VERTEX,   -7.88666,  -1.19549, 110.76132,
     VERTEX,   -7.51657,  -1.61089, 109.97897,
     VERTEX,   -6.95762,  -2.32815, 109.67120,
     VERTEX,   -6.42333,  -3.07330, 109.95558,
     VERTEX,   -6.11776,  -3.56173, 110.72348,
     VERTEX,   -6.15764,  -3.60686, 111.68159,
     VERTEX,   -6.52773,  -3.19146, 112.46394,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.02215,  -2.40117, 111.22146,
                       
     VERTEX,   -6.52773,  -3.19146, 112.46394,
     VERTEX,   -7.08668,  -2.47420, 112.77171,
     VERTEX,   -7.62098,  -1.72905, 112.48733,
     VERTEX,   -7.92654,  -1.24062, 111.71943,
     VERTEX,   -7.88666,  -1.19549, 110.76132,
     VERTEX,   -7.51657,  -1.61089, 109.97897,
     VERTEX,   -6.95762,  -2.32815, 109.67120,
     VERTEX,   -6.42333,  -3.07330, 109.95558,
     VERTEX,   -6.11776,  -3.56173, 110.72348,
     VERTEX,   -6.15764,  -3.60686, 111.68159,
     VERTEX,   -6.52773,  -3.19146, 112.46394,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,  -7.02215,  -2.40117, 111.22146,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.57637, -11.93855, 109.16771,
                       
     VERTEX,   -8.72819,  -9.60136, 111.42446,
     VERTEX,   -9.30028,  -8.88372, 111.70608,
     VERTEX,   -9.78156,  -8.10992, 111.40407,
     VERTEX,   -9.98820,  -7.57553, 110.63379,
     VERTEX,   -9.84127,  -7.48467, 109.68946,
     VERTEX,   -9.39689,  -7.87204, 108.93179,
     VERTEX,   -8.82480,  -8.58968, 108.65017,
     VERTEX,   -8.34352,  -9.36347, 108.95218,
     VERTEX,   -8.13688,  -9.89786, 109.72246,
     VERTEX,   -8.28381,  -9.98873, 110.66679,
     VERTEX,   -8.72819,  -9.60136, 111.42446,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -9.06254,  -8.73670, 110.17812,
                       
     VERTEX,   -8.72819,  -9.60136, 111.42446,
     VERTEX,   -9.30028,  -8.88372, 111.70608,
     VERTEX,   -9.78156,  -8.10992, 111.40407,
     VERTEX,   -9.98820,  -7.57553, 110.63379,
     VERTEX,   -9.84127,  -7.48467, 109.68946,
     VERTEX,   -9.39689,  -7.87204, 108.93179,
     VERTEX,   -8.82480,  -8.58968, 108.65017,
     VERTEX,   -8.34352,  -9.36347, 108.95218,
     VERTEX,   -8.13688,  -9.89786, 109.72246,
     VERTEX,   -8.28381,  -9.98873, 110.66679,
     VERTEX,   -8.72819,  -9.60136, 111.42446,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,  -9.06254,  -8.73670, 110.17812,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.58885, -16.68477, 107.54202,
                       
     VERTEX,   -6.81110, -14.34636, 109.99705,
     VERTEX,   -7.39932, -13.64479, 110.28584,
     VERTEX,   -7.88285, -12.86794, 109.99550,
     VERTEX,   -8.07701, -12.31254, 109.23693,
     VERTEX,   -7.90763, -12.19073, 108.29987,
     VERTEX,   -7.43940, -12.54904, 107.54226,
     VERTEX,   -6.85119, -13.25061, 107.25346,
     VERTEX,   -6.36765, -14.02746, 107.54381,
     VERTEX,   -6.17350, -14.58286, 108.30238,
     VERTEX,   -6.34288, -14.70467, 109.23943,
     VERTEX,   -6.81110, -14.34636, 109.99705,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -7.12525, -13.44770, 108.76965,
                       
     VERTEX,   -6.81110, -14.34636, 109.99705,
     VERTEX,   -7.39932, -13.64479, 110.28584,
     VERTEX,   -7.88285, -12.86794, 109.99550,
     VERTEX,   -8.07701, -12.31254, 109.23693,
     VERTEX,   -7.90763, -12.19073, 108.29987,
     VERTEX,   -7.43940, -12.54904, 107.54226,
     VERTEX,   -6.85119, -13.25061, 107.25346,
     VERTEX,   -6.36765, -14.02746, 107.54381,
     VERTEX,   -6.17350, -14.58286, 108.30238,
     VERTEX,   -6.34288, -14.70467, 109.23943,
     VERTEX,   -6.81110, -14.34636, 109.99705,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,  -7.12525, -13.44770, 108.76965,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -1.12571, -20.80396, 107.56210,
                       
     VERTEX,    3.72378, -18.24066, 109.33000,
     VERTEX,    3.14412, -17.54772, 109.65471,
     VERTEX,    2.59877, -16.80357, 109.38932,
     VERTEX,    2.29603, -16.29245, 108.63519,
     VERTEX,    2.35154, -16.20958, 107.68039,
     VERTEX,    2.74410, -16.58663, 106.88960,
     VERTEX,    3.32376, -17.27956, 106.56490,
     VERTEX,    3.86911, -18.02371, 106.83029,
     VERTEX,    4.17185, -18.53483, 107.58441,
     VERTEX,    4.11634, -18.61770, 108.53922,
     VERTEX,    3.72378, -18.24066, 109.33000,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    3.23394, -17.41364, 108.10980,
                       
     VERTEX,    3.72378, -18.24066, 109.33000,
     VERTEX,    3.14412, -17.54772, 109.65471,
     VERTEX,    2.59877, -16.80357, 109.38932,
     VERTEX,    2.29603, -16.29245, 108.63519,
     VERTEX,    2.35154, -16.20958, 107.68039,
     VERTEX,    2.74410, -16.58663, 106.88960,
     VERTEX,    3.32376, -17.27956, 106.56490,
     VERTEX,    3.86911, -18.02371, 106.83029,
     VERTEX,    4.17185, -18.53483, 107.58441,
     VERTEX,    4.11634, -18.61770, 108.53922,
     VERTEX,    3.72378, -18.24066, 109.33000,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,   3.23394, -17.41364, 108.10980,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.34887,  38.90315,  36.83991,
                       
     VERTEX,   20.85448,  36.16624,  32.45882,
     VERTEX,   20.50652,  37.05604,  32.36509,
     VERTEX,   19.95935,  37.72417,  32.78438,
     VERTEX,   19.42197,  37.91542,  33.55655,
     VERTEX,   19.09963,  37.55676,  34.38664,
     VERTEX,   19.11547,  36.78516,  34.95760,
     VERTEX,   19.46343,  35.89536,  35.05133,
     VERTEX,   20.01060,  35.22723,  34.63203,
     VERTEX,   20.54798,  35.03598,  33.85987,
     VERTEX,   20.87031,  35.39465,  33.02977,
     VERTEX,   20.85448,  36.16624,  32.45882,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.98497,  36.47570,  33.70821,
                       
     VERTEX,   20.85448,  36.16624,  32.45882,
     VERTEX,   20.50652,  37.05604,  32.36509,
     VERTEX,   19.95935,  37.72417,  32.78438,
     VERTEX,   19.42197,  37.91542,  33.55655,
     VERTEX,   19.09963,  37.55676,  34.38664,
     VERTEX,   19.11547,  36.78516,  34.95760,
     VERTEX,   19.46343,  35.89536,  35.05133,
     VERTEX,   20.01060,  35.22723,  34.63203,
     VERTEX,   20.54798,  35.03598,  33.85987,
     VERTEX,   20.87031,  35.39465,  33.02977,
     VERTEX,   20.85448,  36.16624,  32.45882,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,  19.98497,  36.47570,  33.70821,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.20548,  38.75141,  64.46185,
                       
     VERTEX,   42.28710,  39.67170,  57.61535,
     VERTEX,   42.07773,  40.56675,  57.89220,
     VERTEX,   41.46190,  41.09793,  58.40231,
     VERTEX,   40.67484,  41.06234,  58.95082,
     VERTEX,   40.01717,  40.47357,  59.32822,
     VERTEX,   39.74011,  39.55653,  59.39037,
     VERTEX,   39.94947,  38.66148,  59.11350,
     VERTEX,   40.56530,  38.13030,  58.60340,
     VERTEX,   41.35237,  38.16589,  58.05489,
     VERTEX,   42.01003,  38.75465,  57.67748,
     VERTEX,   42.28710,  39.67170,  57.61535,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.01360,  39.61411,  58.50285,
                       
     VERTEX,   42.28710,  39.67170,  57.61535,
     VERTEX,   42.07773,  40.56675,  57.89220,
     VERTEX,   41.46190,  41.09793,  58.40231,
     VERTEX,   40.67484,  41.06234,  58.95082,
     VERTEX,   40.01717,  40.47357,  59.32822,
     VERTEX,   39.74011,  39.55653,  59.39037,
     VERTEX,   39.94947,  38.66148,  59.11350,
     VERTEX,   40.56530,  38.13030,  58.60340,
     VERTEX,   41.35237,  38.16589,  58.05489,
     VERTEX,   42.01003,  38.75465,  57.67748,
     VERTEX,   42.28710,  39.67170,  57.61535,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  41.01360,  39.61411,  58.50285,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.37215,  46.31549,  62.35702,
                       
     VERTEX,   29.00336,  46.20821,  56.22932,
     VERTEX,   28.77660,  47.12274,  56.41317,
     VERTEX,   28.19299,  47.69122,  56.92094,
     VERTEX,   27.47545,  47.69651,  57.55868,
     VERTEX,   26.89806,  47.13658,  58.08279,
     VERTEX,   26.68135,  46.22531,  58.29308,
     VERTEX,   26.90811,  45.31077,  58.10923,
     VERTEX,   27.49172,  44.74229,  57.60146,
     VERTEX,   28.20926,  44.73700,  56.96373,
     VERTEX,   28.78666,  45.29693,  56.43961,
     VERTEX,   29.00336,  46.20821,  56.22932,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.84236,  46.21675,  57.26120,
                       
     VERTEX,   29.00336,  46.20821,  56.22932,
     VERTEX,   28.77660,  47.12274,  56.41317,
     VERTEX,   28.19299,  47.69122,  56.92094,
     VERTEX,   27.47545,  47.69651,  57.55868,
     VERTEX,   26.89806,  47.13658,  58.08279,
     VERTEX,   26.68135,  46.22531,  58.29308,
     VERTEX,   26.90811,  45.31077,  58.10923,
     VERTEX,   27.49172,  44.74229,  57.60146,
     VERTEX,   28.20926,  44.73700,  56.96373,
     VERTEX,   28.78666,  45.29693,  56.43961,
     VERTEX,   29.00336,  46.20821,  56.22932,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.84236,  46.21675,  57.26120,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.64664,  49.42451,  49.16690,
                       
     VERTEX,   26.06341,  47.86425,  43.33806,
     VERTEX,   25.78930,  48.78299,  43.38672,
     VERTEX,   25.23390,  49.40352,  43.86429,
     VERTEX,   24.60936,  49.48882,  44.58836,
     VERTEX,   24.15424,  49.00629,  45.28236,
     VERTEX,   24.04237,  48.14026,  45.68120,
     VERTEX,   24.31648,  47.22152,  45.63254,
     VERTEX,   24.87187,  46.60099,  45.15497,
     VERTEX,   25.49641,  46.51569,  44.43090,
     VERTEX,   25.95154,  46.99821,  43.73690,
     VERTEX,   26.06341,  47.86425,  43.33806,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.05289,  48.00225,  44.50963,
                       
     VERTEX,   26.06341,  47.86425,  43.33806,
     VERTEX,   25.78930,  48.78299,  43.38672,
     VERTEX,   25.23390,  49.40352,  43.86429,
     VERTEX,   24.60936,  49.48882,  44.58836,
     VERTEX,   24.15424,  49.00629,  45.28236,
     VERTEX,   24.04237,  48.14026,  45.68120,
     VERTEX,   24.31648,  47.22152,  45.63254,
     VERTEX,   24.87187,  46.60099,  45.15497,
     VERTEX,   25.49641,  46.51569,  44.43090,
     VERTEX,   25.95154,  46.99821,  43.73690,
     VERTEX,   26.06341,  47.86425,  43.33806,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,  25.05289,  48.00225,  44.50963,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.65105,  34.37888,  42.08850,
                       
     VERTEX,   37.51272,  33.09391,  36.39229,
     VERTEX,   37.24616,  34.01372,  36.45935,
     VERTEX,   36.68534,  34.62672,  36.94030,
     VERTEX,   36.04447,  34.69877,  37.65142,
     VERTEX,   35.56835,  34.20235,  38.32110,
     VERTEX,   35.43883,  33.32706,  38.69354,
     VERTEX,   35.70539,  32.40726,  38.62648,
     VERTEX,   36.26621,  31.79426,  38.14553,
     VERTEX,   36.90708,  31.72221,  37.43441,
     VERTEX,   37.38320,  32.21863,  36.76473,
     VERTEX,   37.51272,  33.09391,  36.39229,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.47578,  33.21049,  37.54292,
                       
     VERTEX,   37.51272,  33.09391,  36.39229,
     VERTEX,   37.24616,  34.01372,  36.45935,
     VERTEX,   36.68534,  34.62672,  36.94030,
     VERTEX,   36.04447,  34.69877,  37.65142,
     VERTEX,   35.56835,  34.20235,  38.32110,
     VERTEX,   35.43883,  33.32706,  38.69354,
     VERTEX,   35.70539,  32.40726,  38.62648,
     VERTEX,   36.26621,  31.79426,  38.14553,
     VERTEX,   36.90708,  31.72221,  37.43441,
     VERTEX,   37.38320,  32.21863,  36.76473,
     VERTEX,   37.51272,  33.09391,  36.39229,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  36.47578,  33.21049,  37.54292,   0.80000,
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
