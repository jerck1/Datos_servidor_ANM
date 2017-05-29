from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -3.54578, -65.20313,  56.85724,
                       
     VERTEX,    0.66871, -67.05077,  55.79831,
     VERTEX,    0.69395, -66.36124,  55.13083,
     VERTEX,    0.32148, -66.07759,  54.29274,
     VERTEX,   -0.30644, -66.30816,  53.60415,
     VERTEX,   -0.94995, -66.96487,  53.32807,
     VERTEX,   -1.36327, -67.79689,  53.56997,
     VERTEX,   -1.38851, -68.48641,  54.23745,
     VERTEX,   -1.01604, -68.77006,  55.07555,
     VERTEX,   -0.38812, -68.53950,  55.76414,
     VERTEX,    0.25540, -67.88278,  56.04021,
     VERTEX,    0.66871, -67.05077,  55.79831,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -0.34728, -67.42383,  54.68414,
                       
     VERTEX,    0.66871, -67.05077,  55.79831,
     VERTEX,    0.69395, -66.36124,  55.13083,
     VERTEX,    0.32148, -66.07759,  54.29274,
     VERTEX,   -0.30644, -66.30816,  53.60415,
     VERTEX,   -0.94995, -66.96487,  53.32807,
     VERTEX,   -1.36327, -67.79689,  53.56997,
     VERTEX,   -1.38851, -68.48641,  54.23745,
     VERTEX,   -1.01604, -68.77006,  55.07555,
     VERTEX,   -0.38812, -68.53950,  55.76414,
     VERTEX,    0.25540, -67.88278,  56.04021,
     VERTEX,    0.66871, -67.05077,  55.79831,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,  -0.34728, -67.42383,  54.68414,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.91026, -75.14103,  50.54359,
                       
     VERTEX,   13.50536, -75.29323,  49.98749,
     VERTEX,   13.39797, -74.38969,  49.68142,
     VERTEX,   13.06630, -73.84768,  48.96182,
     VERTEX,   12.63704, -73.87424,  48.10355,
     VERTEX,   12.27414, -74.45921,  47.43444,
     VERTEX,   12.11624, -75.37917,  47.21007,
     VERTEX,   12.22363, -76.28271,  47.51613,
     VERTEX,   12.55530, -76.82472,  48.23573,
     VERTEX,   12.98457, -76.79816,  49.09400,
     VERTEX,   13.34746, -76.21319,  49.76311,
     VERTEX,   13.50536, -75.29323,  49.98749,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.81080, -75.33620,  48.59878,
                       
     VERTEX,   13.50536, -75.29323,  49.98749,
     VERTEX,   13.39797, -74.38969,  49.68142,
     VERTEX,   13.06630, -73.84768,  48.96182,
     VERTEX,   12.63704, -73.87424,  48.10355,
     VERTEX,   12.27414, -74.45921,  47.43444,
     VERTEX,   12.11624, -75.37917,  47.21007,
     VERTEX,   12.22363, -76.28271,  47.51613,
     VERTEX,   12.55530, -76.82472,  48.23573,
     VERTEX,   12.98457, -76.79816,  49.09400,
     VERTEX,   13.34746, -76.21319,  49.76311,
     VERTEX,   13.50536, -75.29323,  49.98749,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  12.81080, -75.33620,  48.59878,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.37575, -74.39304,  45.32989,
                       
     VERTEX,   15.83352, -74.16586,  44.95361,
     VERTEX,   15.66593, -73.24274,  44.75019,
     VERTEX,   15.30903, -72.64564,  44.08861,
     VERTEX,   14.89914, -72.60262,  43.22158,
     VERTEX,   14.59282, -73.13010,  42.48027,
     VERTEX,   14.50708, -74.02661,  42.14785,
     VERTEX,   14.67467, -74.94972,  42.35128,
     VERTEX,   15.03157, -75.54683,  43.01286,
     VERTEX,   15.44146, -75.58986,  43.87989,
     VERTEX,   15.74777, -75.06238,  44.62119,
     VERTEX,   15.83352, -74.16586,  44.95361,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.17030, -74.09624,  43.55073,
                       
     VERTEX,   15.83352, -74.16586,  44.95361,
     VERTEX,   15.66593, -73.24274,  44.75019,
     VERTEX,   15.30903, -72.64564,  44.08861,
     VERTEX,   14.89914, -72.60262,  43.22158,
     VERTEX,   14.59282, -73.13010,  42.48027,
     VERTEX,   14.50708, -74.02661,  42.14785,
     VERTEX,   14.67467, -74.94972,  42.35128,
     VERTEX,   15.03157, -75.54683,  43.01286,
     VERTEX,   15.44146, -75.58986,  43.87989,
     VERTEX,   15.74777, -75.06238,  44.62119,
     VERTEX,   15.83352, -74.16586,  44.95361,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  15.17030, -74.09624,  43.55073,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   54.51482, -21.34786,  83.03363,
                       
     VERTEX,   49.52046, -20.68045,  83.42220,
     VERTEX,   49.75541, -19.82163,  83.78111,
     VERTEX,   50.11664, -19.37334,  84.54932,
     VERTEX,   50.46616, -19.50681,  85.43342,
     VERTEX,   50.67047, -20.17108,  86.09570,
     VERTEX,   50.65153, -21.11240,  86.28319,
     VERTEX,   50.41657, -21.97123,  85.92429,
     VERTEX,   50.05535, -22.41952,  85.15607,
     VERTEX,   49.70583, -22.28604,  84.27197,
     VERTEX,   49.50152, -21.62178,  83.60970,
     VERTEX,   49.52046, -20.68045,  83.42220,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   50.08599, -20.89643,  84.85269,
                       
     VERTEX,   49.52046, -20.68045,  83.42220,
     VERTEX,   49.75541, -19.82163,  83.78111,
     VERTEX,   50.11664, -19.37334,  84.54932,
     VERTEX,   50.46616, -19.50681,  85.43342,
     VERTEX,   50.67047, -20.17108,  86.09570,
     VERTEX,   50.65153, -21.11240,  86.28319,
     VERTEX,   50.41657, -21.97123,  85.92429,
     VERTEX,   50.05535, -22.41952,  85.15607,
     VERTEX,   49.70583, -22.28604,  84.27197,
     VERTEX,   49.50152, -21.62178,  83.60970,
     VERTEX,   49.52046, -20.68045,  83.42220,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  50.08599, -20.89643,  84.85269,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.19847, -18.80189,  76.61991,
                       
     VERTEX,   44.40866, -18.56489,  76.81438,
     VERTEX,   44.56172, -17.66868,  77.12257,
     VERTEX,   44.86968, -17.14493,  77.86584,
     VERTEX,   45.21491, -17.19370,  78.76028,
     VERTEX,   45.46554, -17.79635,  79.46427,
     VERTEX,   45.52584, -18.72270,  79.70889,
     VERTEX,   45.37278, -19.61891,  79.40070,
     VERTEX,   45.06482, -20.14266,  78.65743,
     VERTEX,   44.71959, -20.09390,  77.76299,
     VERTEX,   44.46896, -19.49124,  77.05901,
     VERTEX,   44.40866, -18.56489,  76.81438,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   44.96725, -18.64380,  78.26163,
                       
     VERTEX,   44.40866, -18.56489,  76.81438,
     VERTEX,   44.56172, -17.66868,  77.12257,
     VERTEX,   44.86968, -17.14493,  77.86584,
     VERTEX,   45.21491, -17.19370,  78.76028,
     VERTEX,   45.46554, -17.79635,  79.46427,
     VERTEX,   45.52584, -18.72270,  79.70889,
     VERTEX,   45.37278, -19.61891,  79.40070,
     VERTEX,   45.06482, -20.14266,  78.65743,
     VERTEX,   44.71959, -20.09390,  77.76299,
     VERTEX,   44.46896, -19.49124,  77.05901,
     VERTEX,   44.40866, -18.56489,  76.81438,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  44.96725, -18.64380,  78.26163,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   65.53481, -90.18306,  94.63165,
                       
     VERTEX,   70.58455, -84.53460,  94.52712,
     VERTEX,   70.00179, -84.08379,  95.14256,
     VERTEX,   69.19237, -83.57245,  95.21303,
     VERTEX,   68.46547, -83.19587,  94.71162,
     VERTEX,   68.09874, -83.09791,  93.82985,
     VERTEX,   68.23225, -83.31598,  92.90453,
     VERTEX,   68.81503, -83.76678,  92.28910,
     VERTEX,   69.62444, -84.27813,  92.21863,
     VERTEX,   70.35134, -84.65470,  92.72003,
     VERTEX,   70.71807, -84.75266,  93.60180,
     VERTEX,   70.58455, -84.53460,  94.52712,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   69.40840, -83.92529,  93.71583,
                       
     VERTEX,   70.58455, -84.53460,  94.52712,
     VERTEX,   70.00179, -84.08379,  95.14256,
     VERTEX,   69.19237, -83.57245,  95.21303,
     VERTEX,   68.46547, -83.19587,  94.71162,
     VERTEX,   68.09874, -83.09791,  93.82985,
     VERTEX,   68.23225, -83.31598,  92.90453,
     VERTEX,   68.81503, -83.76678,  92.28910,
     VERTEX,   69.62444, -84.27813,  92.21863,
     VERTEX,   70.35134, -84.65470,  92.72003,
     VERTEX,   70.71807, -84.75266,  93.60180,
     VERTEX,   70.58455, -84.53460,  94.52712,
                       
     END,              
                       
     CYLINDER,   75.67600, -73.80000,  92.23400,  69.40840, -83.92529,  93.71583,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   63.36011, -84.74899,  91.99717,
                       
     VERTEX,   67.76752, -79.70620,  92.01196,
     VERTEX,   67.18800, -79.29297,  92.65616,
     VERTEX,   66.36401, -78.81233,  92.76398,
     VERTEX,   65.61028, -78.44790,  92.29423,
     VERTEX,   65.21470, -78.33885,  91.42634,
     VERTEX,   65.32838, -78.52685,  90.49181,
     VERTEX,   65.90791, -78.94008,  89.84761,
     VERTEX,   66.73190, -79.42072,  89.73980,
     VERTEX,   67.48564, -79.78515,  90.20955,
     VERTEX,   67.88121, -79.89420,  91.07744,
     VERTEX,   67.76752, -79.70620,  92.01196,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   66.54796, -79.11652,  91.25188,
                       
     VERTEX,   67.76752, -79.70620,  92.01196,
     VERTEX,   67.18800, -79.29297,  92.65616,
     VERTEX,   66.36401, -78.81233,  92.76398,
     VERTEX,   65.61028, -78.44790,  92.29423,
     VERTEX,   65.21470, -78.33885,  91.42634,
     VERTEX,   65.32838, -78.52685,  90.49181,
     VERTEX,   65.90791, -78.94008,  89.84761,
     VERTEX,   66.73190, -79.42072,  89.73980,
     VERTEX,   67.48564, -79.78515,  90.20955,
     VERTEX,   67.88121, -79.89420,  91.07744,
     VERTEX,   67.76752, -79.70620,  92.01196,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  66.54796, -79.11652,  91.25188,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.42046, -94.80241,  97.99819,
                       
     VERTEX,   55.03401, -91.40771,  97.24886,
     VERTEX,   54.57887, -90.60103,  97.50124,
     VERTEX,   54.00198, -89.90273,  97.18313,
     VERTEX,   53.52371, -89.57956,  96.41605,
     VERTEX,   53.32674, -89.75495,  95.49298,
     VERTEX,   53.48631, -90.36191,  94.76653,
     VERTEX,   53.94145, -91.16859,  94.51414,
     VERTEX,   54.51834, -91.86689,  94.83226,
     VERTEX,   54.99660, -92.19006,  95.59934,
     VERTEX,   55.19357, -92.01467,  96.52240,
     VERTEX,   55.03401, -91.40771,  97.24886,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   54.26016, -90.88481,  96.00769,
                       
     VERTEX,   55.03401, -91.40771,  97.24886,
     VERTEX,   54.57887, -90.60103,  97.50124,
     VERTEX,   54.00198, -89.90273,  97.18313,
     VERTEX,   53.52371, -89.57956,  96.41605,
     VERTEX,   53.32674, -89.75495,  95.49298,
     VERTEX,   53.48631, -90.36191,  94.76653,
     VERTEX,   53.94145, -91.16859,  94.51414,
     VERTEX,   54.51834, -91.86689,  94.83226,
     VERTEX,   54.99660, -92.19006,  95.59934,
     VERTEX,   55.19357, -92.01467,  96.52240,
     VERTEX,   55.03401, -91.40771,  97.24886,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  54.26016, -90.88481,  96.00769,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   45.69320, -94.63868, 103.35069,
                       
     VERTEX,   52.41721, -91.92192, 102.48070,
     VERTEX,   52.02091, -91.06126, 102.63501,
     VERTEX,   51.50565, -90.35965, 102.23023,
     VERTEX,   51.06823, -90.08508, 101.42099,
     VERTEX,   50.87575, -90.34242, 100.51637,
     VERTEX,   51.00172, -91.03338,  99.86192,
     VERTEX,   51.39802, -91.89404,  99.70762,
     VERTEX,   51.91329, -92.59565, 100.11239,
     VERTEX,   52.35070, -92.87022, 100.92164,
     VERTEX,   52.54318, -92.61288, 101.82625,
     VERTEX,   52.41721, -91.92192, 102.48070,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   51.70947, -91.47765, 101.17131,
                       
     VERTEX,   52.41721, -91.92192, 102.48070,
     VERTEX,   52.02091, -91.06126, 102.63501,
     VERTEX,   51.50565, -90.35965, 102.23023,
     VERTEX,   51.06823, -90.08508, 101.42099,
     VERTEX,   50.87575, -90.34242, 100.51637,
     VERTEX,   51.00172, -91.03338,  99.86192,
     VERTEX,   51.39802, -91.89404,  99.70762,
     VERTEX,   51.91329, -92.59565, 100.11239,
     VERTEX,   52.35070, -92.87022, 100.92164,
     VERTEX,   52.54318, -92.61288, 101.82625,
     VERTEX,   52.41721, -91.92192, 102.48070,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  51.70947, -91.47765, 101.17131,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.76125, -93.47586, 110.36308,
                       
     VERTEX,   49.49040, -91.61336, 109.37407,
     VERTEX,   49.17520, -90.70702, 109.40225,
     VERTEX,   48.73203, -90.02274, 108.89533,
     VERTEX,   48.33015, -89.82190, 108.04695,
     VERTEX,   48.12307, -90.18121, 107.18114,
     VERTEX,   48.18989, -90.96343, 106.62864,
     VERTEX,   48.50508, -91.86977, 106.60046,
     VERTEX,   48.94826, -92.55405, 107.10737,
     VERTEX,   49.35014, -92.75489, 107.95576,
     VERTEX,   49.55722, -92.39558, 108.82156,
     VERTEX,   49.49040, -91.61336, 109.37407,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   48.84015, -91.28840, 108.00135,
                       
     VERTEX,   49.49040, -91.61336, 109.37407,
     VERTEX,   49.17520, -90.70702, 109.40225,
     VERTEX,   48.73203, -90.02274, 108.89533,
     VERTEX,   48.33015, -89.82190, 108.04695,
     VERTEX,   48.12307, -90.18121, 107.18114,
     VERTEX,   48.18989, -90.96343, 106.62864,
     VERTEX,   48.50508, -91.86977, 106.60046,
     VERTEX,   48.94826, -92.55405, 107.10737,
     VERTEX,   49.35014, -92.75489, 107.95576,
     VERTEX,   49.55722, -92.39558, 108.82156,
     VERTEX,   49.49040, -91.61336, 109.37407,
                       
     END,              
                       
     CYLINDER,   58.67600, -87.74900, 104.18000,  48.84015, -91.28840, 108.00135,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -43.17861,  10.58027,  93.64503,
                       
     VERTEX,  -39.25785,  15.38006,  94.55893,
     VERTEX,  -39.87006,  15.65331,  95.24605,
     VERTEX,  -40.72129,  16.06639,  95.40843,
     VERTEX,  -41.48641,  16.46151,  94.98407,
     VERTEX,  -41.87315,  16.68774,  94.13504,
     VERTEX,  -41.73381,  16.65868,  93.18565,
     VERTEX,  -41.12160,  16.38542,  92.49854,
     VERTEX,  -40.27037,  15.97234,  92.33615,
     VERTEX,  -39.50525,  15.57722,  92.76051,
     VERTEX,  -39.11851,  15.35099,  93.60954,
     VERTEX,  -39.25785,  15.38006,  94.55893,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -40.49583,  16.01937,  93.87229,
                       
     VERTEX,  -39.25785,  15.38006,  94.55893,
     VERTEX,  -39.87006,  15.65331,  95.24605,
     VERTEX,  -40.72129,  16.06639,  95.40843,
     VERTEX,  -41.48641,  16.46151,  94.98407,
     VERTEX,  -41.87315,  16.68774,  94.13504,
     VERTEX,  -41.73381,  16.65868,  93.18565,
     VERTEX,  -41.12160,  16.38542,  92.49854,
     VERTEX,  -40.27037,  15.97234,  92.33615,
     VERTEX,  -39.50525,  15.57722,  92.76051,
     VERTEX,  -39.11851,  15.35099,  93.60954,
     VERTEX,  -39.25785,  15.38006,  94.55893,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -40.49583,  16.01937,  93.87229,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -37.98042,   8.94868,  86.20329,
                       
     VERTEX,  -34.56253,  13.14211,  87.08109,
     VERTEX,  -35.16282,  13.37225,  87.79404,
     VERTEX,  -36.02458,  13.74512,  87.99387,
     VERTEX,  -36.81865,  14.11830,  87.60426,
     VERTEX,  -37.24172,  14.34923,  86.77403,
     VERTEX,  -37.13220,  14.34971,  85.82030,
     VERTEX,  -36.53191,  14.11957,  85.10736,
     VERTEX,  -35.67015,  13.74670,  84.90752,
     VERTEX,  -34.87608,  13.37352,  85.29713,
     VERTEX,  -34.45300,  13.14259,  86.12736,
     VERTEX,  -34.56253,  13.14211,  87.08109,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -35.84736,  13.74591,  86.45070,
                       
     VERTEX,  -34.56253,  13.14211,  87.08109,
     VERTEX,  -35.16282,  13.37225,  87.79404,
     VERTEX,  -36.02458,  13.74512,  87.99387,
     VERTEX,  -36.81865,  14.11830,  87.60426,
     VERTEX,  -37.24172,  14.34923,  86.77403,
     VERTEX,  -37.13220,  14.34971,  85.82030,
     VERTEX,  -36.53191,  14.11957,  85.10736,
     VERTEX,  -35.67015,  13.74670,  84.90752,
     VERTEX,  -34.87608,  13.37352,  85.29713,
     VERTEX,  -34.45300,  13.14259,  86.12736,
     VERTEX,  -34.56253,  13.14211,  87.08109,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -35.84736,  13.74591,  86.45070,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -34.24476,  14.16926,  85.35420,
                       
     VERTEX,  -30.56292,  17.50701,  86.34283,
     VERTEX,  -31.19819,  17.88904,  86.95281,
     VERTEX,  -32.00712,  18.40270,  87.01096,
     VERTEX,  -32.68073,  18.85180,  86.49503,
     VERTEX,  -32.96171,  19.06479,  85.60213,
     VERTEX,  -32.74274,  18.96032,  84.67329,
     VERTEX,  -32.10748,  18.57828,  84.06331,
     VERTEX,  -31.29854,  18.06462,  84.00517,
     VERTEX,  -30.62494,  17.61552,  84.52109,
     VERTEX,  -30.34396,  17.40253,  85.41399,
     VERTEX,  -30.56292,  17.50701,  86.34283,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.65283,  18.23366,  85.50806,
                       
     VERTEX,  -30.56292,  17.50701,  86.34283,
     VERTEX,  -31.19819,  17.88904,  86.95281,
     VERTEX,  -32.00712,  18.40270,  87.01096,
     VERTEX,  -32.68073,  18.85180,  86.49503,
     VERTEX,  -32.96171,  19.06479,  85.60213,
     VERTEX,  -32.74274,  18.96032,  84.67329,
     VERTEX,  -32.10748,  18.57828,  84.06331,
     VERTEX,  -31.29854,  18.06462,  84.00517,
     VERTEX,  -30.62494,  17.61552,  84.52109,
     VERTEX,  -30.34396,  17.40253,  85.41399,
     VERTEX,  -30.56292,  17.50701,  86.34283,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -31.65283,  18.23366,  85.50806,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -34.48911,  23.46729,  95.71452,
                       
     VERTEX,  -29.84880,  26.46071,  96.82028,
     VERTEX,  -30.44833,  27.08003,  97.24290,
     VERTEX,  -31.10692,  27.75879,  97.07816,
     VERTEX,  -31.57301,  28.23774,  96.38897,
     VERTEX,  -31.66856,  28.33392,  95.43859,
     VERTEX,  -31.35709,  28.01060,  94.59003,
     VERTEX,  -30.75756,  27.39128,  94.16741,
     VERTEX,  -30.09897,  26.71251,  94.33216,
     VERTEX,  -29.63289,  26.23357,  95.02135,
     VERTEX,  -29.53733,  26.13739,  95.97173,
     VERTEX,  -29.84880,  26.46071,  96.82028,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -30.60295,  27.23565,  95.70516,
                       
     VERTEX,  -29.84880,  26.46071,  96.82028,
     VERTEX,  -30.44833,  27.08003,  97.24290,
     VERTEX,  -31.10692,  27.75879,  97.07816,
     VERTEX,  -31.57301,  28.23774,  96.38897,
     VERTEX,  -31.66856,  28.33392,  95.43859,
     VERTEX,  -31.35709,  28.01060,  94.59003,
     VERTEX,  -30.75756,  27.39128,  94.16741,
     VERTEX,  -30.09897,  26.71251,  94.33216,
     VERTEX,  -29.63289,  26.23357,  95.02135,
     VERTEX,  -29.53733,  26.13739,  95.97173,
     VERTEX,  -29.84880,  26.46071,  96.82028,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -30.60295,  27.23565,  95.70516,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -34.73947,  20.49961, 101.04240,
                       
     VERTEX,  -30.30385,  23.72173, 102.10726,
     VERTEX,  -30.92409,  24.27302, 102.58995,
     VERTEX,  -31.63556,  24.91016, 102.49271,
     VERTEX,  -32.16650,  25.38980, 101.85268,
     VERTEX,  -32.31413,  25.52872, 100.91432,
     VERTEX,  -32.02203,  25.27386, 100.03606,
     VERTEX,  -31.40180,  24.72257,  99.55338,
     VERTEX,  -30.69033,  24.08543,  99.65062,
     VERTEX,  -30.15939,  23.60579, 100.29065,
     VERTEX,  -30.01176,  23.46687, 101.22900,
     VERTEX,  -30.30385,  23.72173, 102.10726,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.16294,  24.49780, 101.07166,
                       
     VERTEX,  -30.30385,  23.72173, 102.10726,
     VERTEX,  -30.92409,  24.27302, 102.58995,
     VERTEX,  -31.63556,  24.91016, 102.49271,
     VERTEX,  -32.16650,  25.38980, 101.85268,
     VERTEX,  -32.31413,  25.52872, 100.91432,
     VERTEX,  -32.02203,  25.27386, 100.03606,
     VERTEX,  -31.40180,  24.72257,  99.55338,
     VERTEX,  -30.69033,  24.08543,  99.65062,
     VERTEX,  -30.15939,  23.60579, 100.29065,
     VERTEX,  -30.01176,  23.46687, 101.22900,
     VERTEX,  -30.30385,  23.72173, 102.10726,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -31.16294,  24.49780, 101.07166,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.86943,  52.15633,  50.58474,
                       
     VERTEX,   28.74149,  48.58623,  50.97719,
     VERTEX,   28.97093,  48.93330,  50.11203,
     VERTEX,   28.76350,  48.88524,  49.17594,
     VERTEX,   28.19843,  48.46039,  48.52647,
     VERTEX,   27.49157,  47.82104,  48.41171,
     VERTEX,   26.91290,  47.21140,  48.87547,
     VERTEX,   26.68346,  46.86432,  49.74063,
     VERTEX,   26.89090,  46.91239,  50.67672,
     VERTEX,   27.45596,  47.33723,  51.32618,
     VERTEX,   28.16283,  47.97658,  51.44095,
     VERTEX,   28.74149,  48.58623,  50.97719,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.82720,  47.89881,  49.92633,
                       
     VERTEX,   28.74149,  48.58623,  50.97719,
     VERTEX,   28.97093,  48.93330,  50.11203,
     VERTEX,   28.76350,  48.88524,  49.17594,
     VERTEX,   28.19843,  48.46039,  48.52647,
     VERTEX,   27.49157,  47.82104,  48.41171,
     VERTEX,   26.91290,  47.21140,  48.87547,
     VERTEX,   26.68346,  46.86432,  49.74063,
     VERTEX,   26.89090,  46.91239,  50.67672,
     VERTEX,   27.45596,  47.33723,  51.32618,
     VERTEX,   28.16283,  47.97658,  51.44095,
     VERTEX,   28.74149,  48.58623,  50.97719,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  27.82720,  47.89881,  49.92633,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.16366,  45.09832,  56.37955,
                       
     VERTEX,   27.39550,  41.93635,  56.84338,
     VERTEX,   27.61253,  42.24296,  55.95993,
     VERTEX,   27.37510,  42.17069,  55.03257,
     VERTEX,   26.77389,  41.74714,  54.41551,
     VERTEX,   26.03855,  41.13409,  54.34446,
     VERTEX,   25.44995,  40.56572,  54.84655,
     VERTEX,   25.23291,  40.25911,  55.73001,
     VERTEX,   25.47034,  40.33139,  56.65737,
     VERTEX,   26.07155,  40.75494,  57.27443,
     VERTEX,   26.80689,  41.36798,  57.34547,
     VERTEX,   27.39550,  41.93635,  56.84338,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.42272,  41.25104,  55.84497,
                       
     VERTEX,   27.39550,  41.93635,  56.84338,
     VERTEX,   27.61253,  42.24296,  55.95993,
     VERTEX,   27.37510,  42.17069,  55.03257,
     VERTEX,   26.77389,  41.74714,  54.41551,
     VERTEX,   26.03855,  41.13409,  54.34446,
     VERTEX,   25.44995,  40.56572,  54.84655,
     VERTEX,   25.23291,  40.25911,  55.73001,
     VERTEX,   25.47034,  40.33139,  56.65737,
     VERTEX,   26.07155,  40.75494,  57.27443,
     VERTEX,   26.80689,  41.36798,  57.34547,
     VERTEX,   27.39550,  41.93635,  56.84338,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  26.42272,  41.25104,  55.84497,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.03896,  44.56498,  57.87357,
                       
     VERTEX,   21.27658,  42.16247,  58.53823,
     VERTEX,   21.53386,  42.57970,  57.71280,
     VERTEX,   21.39462,  42.57347,  56.76297,
     VERTEX,   20.91205,  42.14616,  56.05154,
     VERTEX,   20.27048,  41.46099,  55.85025,
     VERTEX,   19.71496,  40.77966,  56.23599,
     VERTEX,   19.45768,  40.36243,  57.06142,
     VERTEX,   19.59692,  40.36866,  58.01125,
     VERTEX,   20.07949,  40.79597,  58.72267,
     VERTEX,   20.72107,  41.48114,  58.92396,
     VERTEX,   21.27658,  42.16247,  58.53823,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.49577,  41.47107,  57.38711,
                       
     VERTEX,   21.27658,  42.16247,  58.53823,
     VERTEX,   21.53386,  42.57970,  57.71280,
     VERTEX,   21.39462,  42.57347,  56.76297,
     VERTEX,   20.91205,  42.14616,  56.05154,
     VERTEX,   20.27048,  41.46099,  55.85025,
     VERTEX,   19.71496,  40.77966,  56.23599,
     VERTEX,   19.45768,  40.36243,  57.06142,
     VERTEX,   19.59692,  40.36866,  58.01125,
     VERTEX,   20.07949,  40.79597,  58.72267,
     VERTEX,   20.72107,  41.48114,  58.92396,
     VERTEX,   21.27658,  42.16247,  58.53823,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  20.49577,  41.47107,  57.38711,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    8.52445,  52.61432,  50.50894,
                       
     VERTEX,   13.59122,  50.69258,  51.29341,
     VERTEX,   13.84074,  51.30685,  50.59914,
     VERTEX,   13.80873,  51.46383,  49.65260,
     VERTEX,   13.50741,  51.10356,  48.81534,
     VERTEX,   13.05187,  50.36364,  48.40716,
     VERTEX,   12.61612,  49.52671,  48.58397,
     VERTEX,   12.36659,  48.91244,  49.27824,
     VERTEX,   12.39860,  48.75546,  50.22477,
     VERTEX,   12.69992,  49.11573,  51.06204,
     VERTEX,   13.15546,  49.85565,  51.47022,
     VERTEX,   13.59122,  50.69258,  51.29341,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.10367,  50.10965,  49.93869,
                       
     VERTEX,   13.59122,  50.69258,  51.29341,
     VERTEX,   13.84074,  51.30685,  50.59914,
     VERTEX,   13.80873,  51.46383,  49.65260,
     VERTEX,   13.50741,  51.10356,  48.81534,
     VERTEX,   13.05187,  50.36364,  48.40716,
     VERTEX,   12.61612,  49.52671,  48.58397,
     VERTEX,   12.36659,  48.91244,  49.27824,
     VERTEX,   12.39860,  48.75546,  50.22477,
     VERTEX,   12.69992,  49.11573,  51.06204,
     VERTEX,   13.15546,  49.85565,  51.47022,
     VERTEX,   13.59122,  50.69258,  51.29341,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  13.10367,  50.10965,  49.93869,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.47587,  52.87084,  44.76394,
                       
     VERTEX,   15.46898,  50.70156,  45.48334,
     VERTEX,   15.72703,  51.26476,  44.74998,
     VERTEX,   15.67045,  51.37492,  43.79800,
     VERTEX,   15.32083,  50.98999,  42.99103,
     VERTEX,   14.81173,  50.25698,  42.63731,
     VERTEX,   14.33760,  49.45589,  42.87194,
     VERTEX,   14.07954,  48.89270,  43.60531,
     VERTEX,   14.13613,  48.78254,  44.55729,
     VERTEX,   14.48574,  49.16747,  45.36425,
     VERTEX,   14.99485,  49.90047,  45.71798,
     VERTEX,   15.46898,  50.70156,  45.48334,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.90329,  50.07873,  44.17764,
                       
     VERTEX,   15.46898,  50.70156,  45.48334,
     VERTEX,   15.72703,  51.26476,  44.74998,
     VERTEX,   15.67045,  51.37492,  43.79800,
     VERTEX,   15.32083,  50.98999,  42.99103,
     VERTEX,   14.81173,  50.25698,  42.63731,
     VERTEX,   14.33760,  49.45589,  42.87194,
     VERTEX,   14.07954,  48.89270,  43.60531,
     VERTEX,   14.13613,  48.78254,  44.55729,
     VERTEX,   14.48574,  49.16747,  45.36425,
     VERTEX,   14.99485,  49.90047,  45.71798,
     VERTEX,   15.46898,  50.70156,  45.48334,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  14.90329,  50.07873,  44.17764,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00002_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    4.82800, -71.01700,  51.16800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   19.12200, -75.65200,  45.45200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   21.31000, -73.61600,  40.67200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   42.92000, -20.16600,  87.79600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   38.12100, -18.38800,  80.91800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   75.67600, -73.80000,  92.23400,   0.80000,
                       
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