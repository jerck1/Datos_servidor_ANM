from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   41.06844, -52.22535,  30.56780,
                       
     VERTEX,   36.00463, -53.48267,  30.01868,
     VERTEX,   35.84937, -52.54278,  30.13750,
     VERTEX,   35.84122, -51.83249,  30.78327,
     VERTEX,   35.98328, -51.62309,  31.70932,
     VERTEX,   36.22130, -51.99456,  32.56194,
     VERTEX,   36.46436, -52.80503,  33.01545,
     VERTEX,   36.61961, -53.74491,  32.89663,
     VERTEX,   36.62776, -54.45520,  32.25086,
     VERTEX,   36.48569, -54.66461,  31.32481,
     VERTEX,   36.24768, -54.29313,  30.47220,
     VERTEX,   36.00463, -53.48267,  30.01868,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.23449, -53.14384,  31.51707,
                       
     VERTEX,   36.00463, -53.48267,  30.01868,
     VERTEX,   35.84937, -52.54278,  30.13750,
     VERTEX,   35.84122, -51.83249,  30.78327,
     VERTEX,   35.98328, -51.62309,  31.70932,
     VERTEX,   36.22130, -51.99456,  32.56194,
     VERTEX,   36.46436, -52.80503,  33.01545,
     VERTEX,   36.61961, -53.74491,  32.89663,
     VERTEX,   36.62776, -54.45520,  32.25086,
     VERTEX,   36.48569, -54.66461,  31.32481,
     VERTEX,   36.24768, -54.29313,  30.47220,
     VERTEX,   36.00463, -53.48267,  30.01868,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  36.23449, -53.14384,  31.51707,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.57750, -44.67879,  35.04921,
                       
     VERTEX,   44.04081, -45.87264,  33.46764,
     VERTEX,   43.85609, -44.93768,  33.58311,
     VERTEX,   43.71299, -44.24921,  34.23666,
     VERTEX,   43.66618, -44.07019,  35.17867,
     VERTEX,   43.73354, -44.46901,  36.04930,
     VERTEX,   43.88932, -45.29333,  36.51602,
     VERTEX,   44.07404, -46.22829,  36.40055,
     VERTEX,   44.21714, -46.91676,  35.74700,
     VERTEX,   44.26395, -47.09578,  34.80500,
     VERTEX,   44.19660, -46.69696,  33.93436,
     VERTEX,   44.04081, -45.87264,  33.46764,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   43.96507, -45.58299,  34.99183,
                       
     VERTEX,   44.04081, -45.87264,  33.46764,
     VERTEX,   43.85609, -44.93768,  33.58311,
     VERTEX,   43.71299, -44.24921,  34.23666,
     VERTEX,   43.66618, -44.07019,  35.17867,
     VERTEX,   43.73354, -44.46901,  36.04930,
     VERTEX,   43.88932, -45.29333,  36.51602,
     VERTEX,   44.07404, -46.22829,  36.40055,
     VERTEX,   44.21714, -46.91676,  35.74700,
     VERTEX,   44.26395, -47.09578,  34.80500,
     VERTEX,   44.19660, -46.69696,  33.93436,
     VERTEX,   44.04081, -45.87264,  33.46764,
                       
     END,              
                       
     CYLINDER,   36.50200, -47.04600,  34.89900,  43.96507, -45.58299,  34.99183,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.04234, -69.39859,  37.48368,
                       
     VERTEX,    9.66552, -70.53840,  40.24189,
     VERTEX,    9.57282, -69.58618,  40.32122,
     VERTEX,    9.92088, -68.80573,  40.75866,
     VERTEX,   10.57675, -68.49516,  41.38713,
     VERTEX,   11.28991, -68.77307,  41.96657,
     VERTEX,   11.78797, -69.53334,  42.27566,
     VERTEX,   11.88067, -70.48556,  42.19633,
     VERTEX,   11.53261, -71.26601,  41.75890,
     VERTEX,   10.87674, -71.57658,  41.13042,
     VERTEX,   10.16358, -71.29866,  40.55098,
     VERTEX,    9.66552, -70.53840,  40.24189,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.72674, -70.03587,  41.25877,
                       
     VERTEX,    9.66552, -70.53840,  40.24189,
     VERTEX,    9.57282, -69.58618,  40.32122,
     VERTEX,    9.92088, -68.80573,  40.75866,
     VERTEX,   10.57675, -68.49516,  41.38713,
     VERTEX,   11.28991, -68.77307,  41.96657,
     VERTEX,   11.78797, -69.53334,  42.27566,
     VERTEX,   11.88067, -70.48556,  42.19633,
     VERTEX,   11.53261, -71.26601,  41.75890,
     VERTEX,   10.87674, -71.57658,  41.13042,
     VERTEX,   10.16358, -71.29866,  40.55098,
     VERTEX,    9.66552, -70.53840,  40.24189,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  10.72674, -70.03587,  41.25877,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.04012, -67.80014,  30.33937,
                       
     VERTEX,   30.88620, -69.05844,  30.61465,
     VERTEX,   30.75148, -68.11504,  30.73066,
     VERTEX,   30.84126, -67.38823,  31.35136,
     VERTEX,   31.12124, -67.15560,  32.23967,
     VERTEX,   31.48448, -67.50603,  33.05629,
     VERTEX,   31.79224, -68.30565,  33.48928,
     VERTEX,   31.92696, -69.24905,  33.37328,
     VERTEX,   31.83718, -69.97586,  32.75257,
     VERTEX,   31.55721, -70.20849,  31.86426,
     VERTEX,   31.19396, -69.85806,  31.04765,
     VERTEX,   30.88620, -69.05844,  30.61465,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.33922, -68.68204,  32.05197,
                       
     VERTEX,   30.88620, -69.05844,  30.61465,
     VERTEX,   30.75148, -68.11504,  30.73066,
     VERTEX,   30.84126, -67.38823,  31.35136,
     VERTEX,   31.12124, -67.15560,  32.23967,
     VERTEX,   31.48448, -67.50603,  33.05629,
     VERTEX,   31.79224, -68.30565,  33.48928,
     VERTEX,   31.92696, -69.24905,  33.37328,
     VERTEX,   31.83718, -69.97586,  32.75257,
     VERTEX,   31.55721, -70.20849,  31.86426,
     VERTEX,   31.19396, -69.85806,  31.04765,
     VERTEX,   30.88620, -69.05844,  30.61465,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  31.33922, -68.68204,  32.05197,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.80903, -51.96003,  27.43630,
                       
     VERTEX,   18.43223, -53.24330,  28.92669,
     VERTEX,   18.32173, -52.29581,  29.03468,
     VERTEX,   18.52577, -51.54994,  29.60357,
     VERTEX,   18.96642, -51.29058,  30.41607,
     VERTEX,   19.47536, -51.61679,  31.16183,
     VERTEX,   19.85820, -52.40398,  31.55600,
     VERTEX,   19.96870, -53.35147,  31.44801,
     VERTEX,   19.76466, -54.09734,  30.87912,
     VERTEX,   19.32401, -54.35670,  30.06662,
     VERTEX,   18.81507, -54.03049,  29.32086,
     VERTEX,   18.43223, -53.24330,  28.92669,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.14521, -52.82364,  30.24134,
                       
     VERTEX,   18.43223, -53.24330,  28.92669,
     VERTEX,   18.32173, -52.29581,  29.03468,
     VERTEX,   18.52577, -51.54994,  29.60357,
     VERTEX,   18.96642, -51.29058,  30.41607,
     VERTEX,   19.47536, -51.61679,  31.16183,
     VERTEX,   19.85820, -52.40398,  31.55600,
     VERTEX,   19.96870, -53.35147,  31.44801,
     VERTEX,   19.76466, -54.09734,  30.87912,
     VERTEX,   19.32401, -54.35670,  30.06662,
     VERTEX,   18.81507, -54.03049,  29.32086,
     VERTEX,   18.43223, -53.24330,  28.92669,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,  19.14521, -52.82364,  30.24134,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.04994, -59.14880, 125.12883,
                       
     VERTEX,   31.33082, -58.98856, 126.07504,
     VERTEX,   31.27377, -58.06743, 125.81075,
     VERTEX,   31.18023, -57.48000, 125.05723,
     VERTEX,   31.08592, -57.45066, 124.10233,
     VERTEX,   31.02687, -57.99061, 123.31077,
     VERTEX,   31.02563, -58.89361, 122.98490,
     VERTEX,   31.08268, -59.81475, 123.24920,
     VERTEX,   31.17622, -60.40217, 124.00272,
     VERTEX,   31.27053, -60.43151, 124.95762,
     VERTEX,   31.32958, -59.89156, 125.74918,
     VERTEX,   31.33082, -58.98856, 126.07504,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.17822, -58.94109, 124.52997,
                       
     VERTEX,   31.33082, -58.98856, 126.07504,
     VERTEX,   31.27377, -58.06743, 125.81075,
     VERTEX,   31.18023, -57.48000, 125.05723,
     VERTEX,   31.08592, -57.45066, 124.10233,
     VERTEX,   31.02687, -57.99061, 123.31077,
     VERTEX,   31.02563, -58.89361, 122.98490,
     VERTEX,   31.08268, -59.81475, 123.24920,
     VERTEX,   31.17622, -60.40217, 124.00272,
     VERTEX,   31.27053, -60.43151, 124.95762,
     VERTEX,   31.32958, -59.89156, 125.74918,
     VERTEX,   31.33082, -58.98856, 126.07504,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  31.17822, -58.94109, 124.52997,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.90557, -54.49792, 125.74958,
                       
     VERTEX,   29.23724, -54.34173, 126.88709,
     VERTEX,   29.18955, -53.42058, 126.62099,
     VERTEX,   29.12037, -52.83318, 125.86484,
     VERTEX,   29.05614, -52.80391, 124.90743,
     VERTEX,   29.02138, -53.34393, 124.11449,
     VERTEX,   29.02938, -54.24699, 123.78887,
     VERTEX,   29.07707, -55.16814, 124.05496,
     VERTEX,   29.14625, -55.75554, 124.81113,
     VERTEX,   29.21048, -55.78482, 125.76852,
     VERTEX,   29.24524, -55.24479, 126.56148,
     VERTEX,   29.23724, -54.34173, 126.88709,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.13331, -54.29436, 125.33798,
                       
     VERTEX,   29.23724, -54.34173, 126.88709,
     VERTEX,   29.18955, -53.42058, 126.62099,
     VERTEX,   29.12037, -52.83318, 125.86484,
     VERTEX,   29.05614, -52.80391, 124.90743,
     VERTEX,   29.02138, -53.34393, 124.11449,
     VERTEX,   29.02938, -54.24699, 123.78887,
     VERTEX,   29.07707, -55.16814, 124.05496,
     VERTEX,   29.14625, -55.75554, 124.81113,
     VERTEX,   29.21048, -55.78482, 125.76852,
     VERTEX,   29.24524, -55.24479, 126.56148,
     VERTEX,   29.23724, -54.34173, 126.88709,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  29.13331, -54.29436, 125.33798,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.99173, -70.66846, 125.55906,
                       
     VERTEX,   56.19880, -70.36298, 123.46258,
     VERTEX,   56.01185, -69.44276, 123.26295,
     VERTEX,   55.57795, -68.85600, 122.63922,
     VERTEX,   55.06283, -68.82679, 121.82965,
     VERTEX,   54.66326, -69.36631, 121.14346,
     VERTEX,   54.53186, -70.26848, 120.84275,
     VERTEX,   54.71881, -71.18870, 121.04238,
     VERTEX,   55.15271, -71.77547, 121.66610,
     VERTEX,   55.66782, -71.80467, 122.47567,
     VERTEX,   56.06739, -71.26515, 123.16187,
     VERTEX,   56.19880, -70.36298, 123.46258,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   55.36533, -70.31573, 122.15266,
                       
     VERTEX,   56.19880, -70.36298, 123.46258,
     VERTEX,   56.01185, -69.44276, 123.26295,
     VERTEX,   55.57795, -68.85600, 122.63922,
     VERTEX,   55.06283, -68.82679, 121.82965,
     VERTEX,   54.66326, -69.36631, 121.14346,
     VERTEX,   54.53186, -70.26848, 120.84275,
     VERTEX,   54.71881, -71.18870, 121.04238,
     VERTEX,   55.15271, -71.77547, 121.66610,
     VERTEX,   55.66782, -71.80467, 122.47567,
     VERTEX,   56.06739, -71.26515, 123.16187,
     VERTEX,   56.19880, -70.36298, 123.46258,
                       
     END,              
                       
     CYLINDER,   64.06000, -69.74500, 116.64100,  55.36533, -70.31573, 122.15266,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.12374, -44.39409, 124.96338,
                       
     VERTEX,   18.40191, -44.28031, 127.25963,
     VERTEX,   18.41159, -43.35992, 126.98689,
     VERTEX,   18.48597, -42.77515, 126.22919,
     VERTEX,   18.59663, -42.74937, 125.27593,
     VERTEX,   18.70132, -43.29242, 124.49124,
     VERTEX,   18.76004, -44.19688, 124.17484,
     VERTEX,   18.75036, -45.11727, 124.44758,
     VERTEX,   18.67598, -45.70203, 125.20528,
     VERTEX,   18.56532, -45.72782, 126.15854,
     VERTEX,   18.46063, -45.18477, 126.94322,
     VERTEX,   18.40191, -44.28031, 127.25963,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.58097, -44.23859, 125.71723,
                       
     VERTEX,   18.40191, -44.28031, 127.25963,
     VERTEX,   18.41159, -43.35992, 126.98689,
     VERTEX,   18.48597, -42.77515, 126.22919,
     VERTEX,   18.59663, -42.74937, 125.27593,
     VERTEX,   18.70132, -43.29242, 124.49124,
     VERTEX,   18.76004, -44.19688, 124.17484,
     VERTEX,   18.75036, -45.11727, 124.44758,
     VERTEX,   18.67598, -45.70203, 125.20528,
     VERTEX,   18.56532, -45.72782, 126.15854,
     VERTEX,   18.46063, -45.18477, 126.94322,
     VERTEX,   18.40191, -44.28031, 127.25963,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  18.58097, -44.23859, 125.71723,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.75923, -50.23616, 122.56641,
                       
     VERTEX,   18.76968, -50.14599, 124.93561,
     VERTEX,   18.78789, -49.22661, 124.65992,
     VERTEX,   18.87738, -48.64482, 123.90157,
     VERTEX,   19.00396, -48.62284, 122.95020,
     VERTEX,   19.11929, -49.16907, 122.16921,
     VERTEX,   19.17930, -50.07487, 121.85693,
     VERTEX,   19.16109, -50.99425, 122.13261,
     VERTEX,   19.07161, -51.57604, 122.89097,
     VERTEX,   18.94503, -51.59802, 123.84233,
     VERTEX,   18.82970, -51.05179, 124.62331,
     VERTEX,   18.76968, -50.14599, 124.93561,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.97449, -50.11043, 123.39626,
                       
     VERTEX,   18.76968, -50.14599, 124.93561,
     VERTEX,   18.78789, -49.22661, 124.65992,
     VERTEX,   18.87738, -48.64482, 123.90157,
     VERTEX,   19.00396, -48.62284, 122.95020,
     VERTEX,   19.11929, -49.16907, 122.16921,
     VERTEX,   19.17930, -50.07487, 121.85693,
     VERTEX,   19.16109, -50.99425, 122.13261,
     VERTEX,   19.07161, -51.57604, 122.89097,
     VERTEX,   18.94503, -51.59802, 123.84233,
     VERTEX,   18.82970, -51.05179, 124.62331,
     VERTEX,   18.76968, -50.14599, 124.93561,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  18.97449, -50.11043, 123.39626,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.35011,  -5.44646, 112.78000,
                       
     VERTEX,    9.53128,  -4.57247, 110.86790,
     VERTEX,    9.60181,  -3.69778, 111.25719,
     VERTEX,    9.60787,  -3.21522, 112.08707,
     VERTEX,    9.54715,  -3.30910, 113.04054,
     VERTEX,    9.44285,  -3.94356, 113.75341,
     VERTEX,    9.33481,  -4.87627, 113.95338,
     VERTEX,    9.26429,  -5.75095, 113.56408,
     VERTEX,    9.25822,  -6.23351, 112.73421,
     VERTEX,    9.31894,  -6.13963, 111.78074,
     VERTEX,    9.42324,  -5.50517, 111.06787,
     VERTEX,    9.53128,  -4.57247, 110.86790,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.43305,  -4.72437, 112.41064,
                       
     VERTEX,    9.53128,  -4.57247, 110.86790,
     VERTEX,    9.60181,  -3.69778, 111.25719,
     VERTEX,    9.60787,  -3.21522, 112.08707,
     VERTEX,    9.54715,  -3.30910, 113.04054,
     VERTEX,    9.44285,  -3.94356, 113.75341,
     VERTEX,    9.33481,  -4.87627, 113.95338,
     VERTEX,    9.26429,  -5.75095, 113.56408,
     VERTEX,    9.25822,  -6.23351, 112.73421,
     VERTEX,    9.31894,  -6.13963, 111.78074,
     VERTEX,    9.42324,  -5.50517, 111.06787,
     VERTEX,    9.53128,  -4.57247, 110.86790,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,   9.43305,  -4.72437, 112.41064,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.51698,  -9.81702, 111.02158,
                       
     VERTEX,   11.51505,  -9.07063, 109.37286,
     VERTEX,   11.58649,  -8.18973, 109.74771,
     VERTEX,   11.61771,  -7.69594, 110.57039,
     VERTEX,   11.59678,  -7.77787, 111.52666,
     VERTEX,   11.53168,  -8.40422, 112.25126,
     VERTEX,   11.44730,  -9.33575, 112.46741,
     VERTEX,   11.37585, -10.21665, 112.09257,
     VERTEX,   11.34463, -10.71045, 111.26989,
     VERTEX,   11.36557, -10.62852, 110.31362,
     VERTEX,   11.43066, -10.00216, 109.58902,
     VERTEX,   11.51505,  -9.07063, 109.37286,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.48117,  -9.20319, 110.92014,
                       
     VERTEX,   11.51505,  -9.07063, 109.37286,
     VERTEX,   11.58649,  -8.18973, 109.74771,
     VERTEX,   11.61771,  -7.69594, 110.57039,
     VERTEX,   11.59678,  -7.77787, 111.52666,
     VERTEX,   11.53168,  -8.40422, 112.25126,
     VERTEX,   11.44730,  -9.33575, 112.46741,
     VERTEX,   11.37585, -10.21665, 112.09257,
     VERTEX,   11.34463, -10.71045, 111.26989,
     VERTEX,   11.36557, -10.62852, 110.31362,
     VERTEX,   11.43066, -10.00216, 109.58902,
     VERTEX,   11.51505,  -9.07063, 109.37286,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,  11.48117,  -9.20319, 110.92014,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -8.86023,   4.36536, 119.69601,
                       
     VERTEX,  -14.08349,   6.58130, 114.91257,
     VERTEX,  -14.10095,   7.40302, 115.40863,
     VERTEX,  -14.42675,   7.81986, 116.20969,
     VERTEX,  -14.93645,   7.67261, 117.00977,
     VERTEX,  -15.43535,   7.01751, 117.50327,
     VERTEX,  -15.73289,   6.10479, 117.50169,
     VERTEX,  -15.71543,   5.28307, 117.00563,
     VERTEX,  -15.38964,   4.86623, 116.20457,
     VERTEX,  -14.87994,   5.01348, 115.40449,
     VERTEX,  -14.38104,   5.66858, 114.91099,
     VERTEX,  -14.08349,   6.58130, 114.91257,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -14.90819,   6.34304, 116.20713,
                       
     VERTEX,  -14.08349,   6.58130, 114.91257,
     VERTEX,  -14.10095,   7.40302, 115.40863,
     VERTEX,  -14.42675,   7.81986, 116.20969,
     VERTEX,  -14.93645,   7.67261, 117.00977,
     VERTEX,  -15.43535,   7.01751, 117.50327,
     VERTEX,  -15.73289,   6.10479, 117.50169,
     VERTEX,  -15.71543,   5.28307, 117.00563,
     VERTEX,  -15.38964,   4.86623, 116.20457,
     VERTEX,  -14.87994,   5.01348, 115.40449,
     VERTEX,  -14.38104,   5.66858, 114.91099,
     VERTEX,  -14.08349,   6.58130, 114.91257,
                       
     END,              
                       
     CYLINDER,  -24.69400,   9.54300, 110.56200, -14.90819,   6.34304, 116.20713,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.39966, -18.29032, 105.03425,
                       
     VERTEX,   21.82691, -18.25439, 104.77344,
     VERTEX,   21.88190, -17.34276, 105.06925,
     VERTEX,   22.01743, -16.78208, 105.83663,
     VERTEX,   22.18175, -16.78650, 106.78245,
     VERTEX,   22.31208, -17.35435, 107.54545,
     VERTEX,   22.35865, -18.26871, 107.83418,
     VERTEX,   22.30367, -19.18035, 107.53837,
     VERTEX,   22.16813, -19.74103, 106.77099,
     VERTEX,   22.00381, -19.73660, 105.82516,
     VERTEX,   21.87347, -19.16875, 105.06217,
     VERTEX,   21.82691, -18.25439, 104.77344,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.09278, -18.26155, 106.30381,
                       
     VERTEX,   21.82691, -18.25439, 104.77344,
     VERTEX,   21.88190, -17.34276, 105.06925,
     VERTEX,   22.01743, -16.78208, 105.83663,
     VERTEX,   22.18175, -16.78650, 106.78245,
     VERTEX,   22.31208, -17.35435, 107.54545,
     VERTEX,   22.35865, -18.26871, 107.83418,
     VERTEX,   22.30367, -19.18035, 107.53837,
     VERTEX,   22.16813, -19.74103, 106.77099,
     VERTEX,   22.00381, -19.73660, 105.82516,
     VERTEX,   21.87347, -19.16875, 105.06217,
     VERTEX,   21.82691, -18.25439, 104.77344,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,  22.09278, -18.26155, 106.30381,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.68621, -12.00942, 105.71100,
                       
     VERTEX,   21.38573, -11.97024, 105.43665,
     VERTEX,   21.44262, -11.05879, 105.73265,
     VERTEX,   21.58205, -10.49857, 106.49967,
     VERTEX,   21.75076, -10.50356, 107.44472,
     VERTEX,   21.88432, -11.07186, 108.20682,
     VERTEX,   21.93171, -11.98640, 108.49487,
     VERTEX,   21.87482, -12.89785, 108.19886,
     VERTEX,   21.73539, -13.45807, 107.43185,
     VERTEX,   21.56667, -13.45308, 106.48680,
     VERTEX,   21.43312, -12.88477, 105.72470,
     VERTEX,   21.38573, -11.97024, 105.43665,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.65872, -11.97832, 106.96576,
                       
     VERTEX,   21.38573, -11.97024, 105.43665,
     VERTEX,   21.44262, -11.05879, 105.73265,
     VERTEX,   21.58205, -10.49857, 106.49967,
     VERTEX,   21.75076, -10.50356, 107.44472,
     VERTEX,   21.88432, -11.07186, 108.20682,
     VERTEX,   21.93171, -11.98640, 108.49487,
     VERTEX,   21.87482, -12.89785, 108.19886,
     VERTEX,   21.73539, -13.45807, 107.43185,
     VERTEX,   21.56667, -13.45308, 106.48680,
     VERTEX,   21.43312, -12.88477, 105.72470,
     VERTEX,   21.38573, -11.97024, 105.43665,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  21.65872, -11.97832, 106.96576,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -4.52647,  33.47364,  25.43611,
                       
     VERTEX,    1.21966,  33.22850,  28.18021,
     VERTEX,    1.34095,  34.11708,  27.83769,
     VERTEX,    1.53100,  34.62484,  27.04544,
     VERTEX,    1.71724,  34.55783,  26.10607,
     VERTEX,    1.82852,  33.94164,  25.37838,
     VERTEX,    1.82233,  33.01164,  25.14033,
     VERTEX,    1.70105,  32.12306,  25.48284,
     VERTEX,    1.51099,  31.61531,  26.27509,
     VERTEX,    1.32476,  31.68232,  27.21447,
     VERTEX,    1.21348,  32.29851,  27.94216,
     VERTEX,    1.21966,  33.22850,  28.18021,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    1.52100,  33.12008,  26.66027,
                       
     VERTEX,    1.21966,  33.22850,  28.18021,
     VERTEX,    1.34095,  34.11708,  27.83769,
     VERTEX,    1.53100,  34.62484,  27.04544,
     VERTEX,    1.71724,  34.55783,  26.10607,
     VERTEX,    1.82852,  33.94164,  25.37838,
     VERTEX,    1.82233,  33.01164,  25.14033,
     VERTEX,    1.70105,  32.12306,  25.48284,
     VERTEX,    1.51099,  31.61531,  26.27509,
     VERTEX,    1.32476,  31.68232,  27.21447,
     VERTEX,    1.21348,  32.29851,  27.94216,
     VERTEX,    1.21966,  33.22850,  28.18021,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,   1.52100,  33.12008,  26.66027,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -11.99520,  24.60289,  26.39080,
                       
     VERTEX,   -6.25347,  24.70309,  28.15318,
     VERTEX,   -6.26550,  25.62292,  27.87863,
     VERTEX,   -6.25177,  26.20610,  27.11620,
     VERTEX,   -6.21750,  26.22989,  26.15710,
     VERTEX,   -6.17580,  25.68519,  25.36769,
     VERTEX,   -6.14259,  24.78007,  25.04949,
     VERTEX,   -6.13055,  23.86025,  25.32405,
     VERTEX,   -6.14429,  23.27706,  26.08648,
     VERTEX,   -6.17855,  23.25328,  27.04557,
     VERTEX,   -6.22026,  23.79797,  27.83498,
     VERTEX,   -6.25347,  24.70309,  28.15318,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -6.19803,  24.74158,  26.60134,
                       
     VERTEX,   -6.25347,  24.70309,  28.15318,
     VERTEX,   -6.26550,  25.62292,  27.87863,
     VERTEX,   -6.25177,  26.20610,  27.11620,
     VERTEX,   -6.21750,  26.22989,  26.15710,
     VERTEX,   -6.17580,  25.68519,  25.36769,
     VERTEX,   -6.14259,  24.78007,  25.04949,
     VERTEX,   -6.13055,  23.86025,  25.32405,
     VERTEX,   -6.14429,  23.27706,  26.08648,
     VERTEX,   -6.17855,  23.25328,  27.04557,
     VERTEX,   -6.22026,  23.79797,  27.83498,
     VERTEX,   -6.25347,  24.70309,  28.15318,
                       
     END,              
                       
     CYLINDER,    3.18200,  24.96600,  26.94200,  -6.19803,  24.74158,  26.60134,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.70244,  45.55763,  38.02113,
                       
     VERTEX,   27.06901,  44.77443,  43.19793,
     VERTEX,   27.75475,  45.26311,  42.73690,
     VERTEX,   28.42874,  45.20080,  42.05612,
     VERTEX,   28.83354,  44.61130,  41.41563,
     VERTEX,   28.81453,  43.71977,  41.06008,
     VERTEX,   28.37897,  42.86676,  41.12526,
     VERTEX,   27.69323,  42.37807,  41.58629,
     VERTEX,   27.01924,  42.44038,  42.26707,
     VERTEX,   26.61444,  43.02988,  42.90755,
     VERTEX,   26.63345,  43.92141,  43.26311,
     VERTEX,   27.06901,  44.77443,  43.19793,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.72399,  43.82059,  42.16159,
                       
     VERTEX,   27.06901,  44.77443,  43.19793,
     VERTEX,   27.75475,  45.26311,  42.73690,
     VERTEX,   28.42874,  45.20080,  42.05612,
     VERTEX,   28.83354,  44.61130,  41.41563,
     VERTEX,   28.81453,  43.71977,  41.06008,
     VERTEX,   28.37897,  42.86676,  41.12526,
     VERTEX,   27.69323,  42.37807,  41.58629,
     VERTEX,   27.01924,  42.44038,  42.26707,
     VERTEX,   26.61444,  43.02988,  42.90755,
     VERTEX,   26.63345,  43.92141,  43.26311,
     VERTEX,   27.06901,  44.77443,  43.19793,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  27.72399,  43.82059,  42.16159,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    1.09907,  44.00677,  30.43392,
                       
     VERTEX,    6.48584,  43.57726,  33.75527,
     VERTEX,    6.70166,  44.43285,  33.37714,
     VERTEX,    7.00388,  44.87625,  32.58111,
     VERTEX,    7.27705,  44.73808,  31.67123,
     VERTEX,    7.41684,  44.07112,  30.99504,
     VERTEX,    7.36985,  43.13013,  30.81083,
     VERTEX,    7.15403,  42.27454,  31.18895,
     VERTEX,    6.85181,  41.83115,  31.98499,
     VERTEX,    6.57864,  41.96931,  32.89487,
     VERTEX,    6.43885,  42.63627,  33.57106,
     VERTEX,    6.48584,  43.57726,  33.75527,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.92785,  43.35370,  32.28305,
                       
     VERTEX,    6.48584,  43.57726,  33.75527,
     VERTEX,    6.70166,  44.43285,  33.37714,
     VERTEX,    7.00388,  44.87625,  32.58111,
     VERTEX,    7.27705,  44.73808,  31.67123,
     VERTEX,    7.41684,  44.07112,  30.99504,
     VERTEX,    7.36985,  43.13013,  30.81083,
     VERTEX,    7.15403,  42.27454,  31.18895,
     VERTEX,    6.85181,  41.83115,  31.98499,
     VERTEX,    6.57864,  41.96931,  32.89487,
     VERTEX,    6.43885,  42.63627,  33.57106,
     VERTEX,    6.48584,  43.57726,  33.75527,
                       
     END,              
                       
     CYLINDER,   16.35900,  42.29700,  35.27500,   6.92785,  43.35370,  32.28305,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.95397,  34.94635,  21.37487,
                       
     VERTEX,   18.10073,  34.08610,  26.05595,
     VERTEX,   18.53134,  34.82501,  25.61984,
     VERTEX,   19.04166,  35.08119,  24.84813,
     VERTEX,   19.43675,  34.75679,  24.03556,
     VERTEX,   19.56571,  33.97572,  23.49252,
     VERTEX,   19.37927,  33.03632,  23.42642,
     VERTEX,   18.94866,  32.29741,  23.86252,
     VERTEX,   18.43834,  32.04123,  24.63424,
     VERTEX,   18.04325,  32.36563,  25.44681,
     VERTEX,   17.91429,  33.14670,  25.98985,
     VERTEX,   18.10073,  34.08610,  26.05595,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.74000,  33.56121,  24.74118,
                       
     VERTEX,   18.10073,  34.08610,  26.05595,
     VERTEX,   18.53134,  34.82501,  25.61984,
     VERTEX,   19.04166,  35.08119,  24.84813,
     VERTEX,   19.43675,  34.75679,  24.03556,
     VERTEX,   19.56571,  33.97572,  23.49252,
     VERTEX,   19.37927,  33.03632,  23.42642,
     VERTEX,   18.94866,  32.29741,  23.86252,
     VERTEX,   18.43834,  32.04123,  24.63424,
     VERTEX,   18.04325,  32.36563,  25.44681,
     VERTEX,   17.91429,  33.14670,  25.98985,
     VERTEX,   18.10073,  34.08610,  26.05595,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  18.74000,  33.56121,  24.74118,   0.80000,
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
                       
     SPHERE,  -24.69400,   9.54300, 110.56200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.27000, -18.21500, 108.35800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   10.28800, -11.92800, 108.99600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   11.30600,  32.54800,  28.64100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    3.18200,  24.96600,  26.94200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   34.23100,  41.01000,  48.86100,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   16.35900,  42.29700,  35.27500,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   28.10200,  31.32000,  30.18800,   0.80000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00001_arror_pos') 