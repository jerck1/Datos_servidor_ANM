from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.52422, -77.82950,  44.99717,
                       
     VERTEX,   10.85363, -74.15922,  46.22692,
     VERTEX,   11.47515, -73.89131,  46.90776,
     VERTEX,   11.84666, -74.13373,  47.75912,
     VERTEX,   11.82624, -74.79387,  48.45583,
     VERTEX,   11.42170, -75.61959,  48.73175,
     VERTEX,   10.78755, -76.29549,  48.48150,
     VERTEX,   10.16603, -76.56339,  47.80067,
     VERTEX,    9.79453, -76.32098,  46.94930,
     VERTEX,    9.81495, -75.66084,  46.25260,
     VERTEX,   10.21949, -74.83511,  45.97668,
     VERTEX,   10.85363, -74.15922,  46.22692,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.82059, -75.22736,  47.35421,
                       
     VERTEX,   10.85363, -74.15922,  46.22692,
     VERTEX,   11.47515, -73.89131,  46.90776,
     VERTEX,   11.84666, -74.13373,  47.75912,
     VERTEX,   11.82624, -74.79387,  48.45583,
     VERTEX,   11.42170, -75.61959,  48.73175,
     VERTEX,   10.78755, -76.29549,  48.48150,
     VERTEX,   10.16603, -76.56339,  47.80067,
     VERTEX,    9.79453, -76.32098,  46.94930,
     VERTEX,    9.81495, -75.66084,  46.25260,
     VERTEX,   10.21949, -74.83511,  45.97668,
     VERTEX,   10.85363, -74.15922,  46.22692,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,  10.82059, -75.22736,  47.35421,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.95433, -76.13155,  39.62386,
                       
     VERTEX,   25.75255, -75.85777,  40.45749,
     VERTEX,   25.93610, -74.96423,  40.75661,
     VERTEX,   26.31013, -74.44659,  41.47337,
     VERTEX,   26.73178, -74.50258,  42.33400,
     VERTEX,   27.03998, -75.11082,  43.00977,
     VERTEX,   27.11702, -76.03899,  43.24254,
     VERTEX,   26.93346, -76.93253,  42.94342,
     VERTEX,   26.55943, -77.45017,  42.22665,
     VERTEX,   26.13779, -77.39418,  41.36602,
     VERTEX,   25.82959, -76.78593,  40.69026,
     VERTEX,   25.75255, -75.85777,  40.45749,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.43478, -75.94838,  41.85001,
                       
     VERTEX,   25.75255, -75.85777,  40.45749,
     VERTEX,   25.93610, -74.96423,  40.75661,
     VERTEX,   26.31013, -74.44659,  41.47337,
     VERTEX,   26.73178, -74.50258,  42.33400,
     VERTEX,   27.03998, -75.11082,  43.00977,
     VERTEX,   27.11702, -76.03899,  43.24254,
     VERTEX,   26.93346, -76.93253,  42.94342,
     VERTEX,   26.55943, -77.45017,  42.22665,
     VERTEX,   26.13779, -77.39418,  41.36602,
     VERTEX,   25.82959, -76.78593,  40.69026,
     VERTEX,   25.75255, -75.85777,  40.45749,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  26.43478, -75.94838,  41.85001,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.73328, -72.50911,  35.33247,
                       
     VERTEX,   27.73529, -73.14391,  35.97020,
     VERTEX,   27.73188, -72.20248,  36.15808,
     VERTEX,   27.97221, -71.53967,  36.80963,
     VERTEX,   28.36447, -71.40864,  37.67598,
     VERTEX,   28.75883, -71.85944,  38.42622,
     VERTEX,   29.00466, -72.71989,  38.77377,
     VERTEX,   29.00807, -73.66132,  38.58590,
     VERTEX,   28.76774, -74.32413,  37.93435,
     VERTEX,   28.37548, -74.45517,  37.06799,
     VERTEX,   27.98112, -74.00436,  36.31776,
     VERTEX,   27.73529, -73.14391,  35.97020,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.36998, -72.93190,  37.37199,
                       
     VERTEX,   27.73529, -73.14391,  35.97020,
     VERTEX,   27.73188, -72.20248,  36.15808,
     VERTEX,   27.97221, -71.53967,  36.80963,
     VERTEX,   28.36447, -71.40864,  37.67598,
     VERTEX,   28.75883, -71.85944,  38.42622,
     VERTEX,   29.00466, -72.71989,  38.77377,
     VERTEX,   29.00807, -73.66132,  38.58590,
     VERTEX,   28.76774, -74.32413,  37.93435,
     VERTEX,   28.37548, -74.45517,  37.06799,
     VERTEX,   27.98112, -74.00436,  36.31776,
     VERTEX,   27.73529, -73.14391,  35.97020,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  28.36998, -72.93190,  37.37199,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.78003, -18.64629,  92.60094,
                       
     VERTEX,   36.00010, -19.10530,  92.20023,
     VERTEX,   35.96015, -18.22442,  91.82068,
     VERTEX,   35.71276, -17.72641,  91.03814,
     VERTEX,   35.35244, -17.80147,  90.15150,
     VERTEX,   35.01681, -18.42096,  89.49943,
     VERTEX,   34.83407, -19.34823,  89.33100,
     VERTEX,   34.87402, -20.22911,  89.71055,
     VERTEX,   35.12140, -20.72713,  90.49310,
     VERTEX,   35.48173, -20.65206,  91.37973,
     VERTEX,   35.81736, -20.03258,  92.03180,
     VERTEX,   36.00010, -19.10530,  92.20023,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.41708, -19.22677,  90.76562,
                       
     VERTEX,   36.00010, -19.10530,  92.20023,
     VERTEX,   35.96015, -18.22442,  91.82068,
     VERTEX,   35.71276, -17.72641,  91.03814,
     VERTEX,   35.35244, -17.80147,  90.15150,
     VERTEX,   35.01681, -18.42096,  89.49943,
     VERTEX,   34.83407, -19.34823,  89.33100,
     VERTEX,   34.87402, -20.22911,  89.71055,
     VERTEX,   35.12140, -20.72713,  90.49310,
     VERTEX,   35.48173, -20.65206,  91.37973,
     VERTEX,   35.81736, -20.03258,  92.03180,
     VERTEX,   36.00010, -19.10530,  92.20023,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  35.41708, -19.22677,  90.76562,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.07716, -17.66603,  85.50842,
                       
     VERTEX,   31.23343, -17.88201,  85.20422,
     VERTEX,   31.16240, -16.98252,  84.87640,
     VERTEX,   30.90615, -16.44945,  84.12024,
     VERTEX,   30.56257, -16.48640,  83.22459,
     VERTEX,   30.26288, -17.07926,  82.53156,
     VERTEX,   30.12157, -18.00159,  82.30585,
     VERTEX,   30.19260, -18.90108,  82.63368,
     VERTEX,   30.44884, -19.43416,  83.38983,
     VERTEX,   30.79243, -19.39721,  84.28548,
     VERTEX,   31.09212, -18.80434,  84.97852,
     VERTEX,   31.23343, -17.88201,  85.20422,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.67750, -17.94180,  83.75504,
                       
     VERTEX,   31.23343, -17.88201,  85.20422,
     VERTEX,   31.16240, -16.98252,  84.87640,
     VERTEX,   30.90615, -16.44945,  84.12024,
     VERTEX,   30.56257, -16.48640,  83.22459,
     VERTEX,   30.26288, -17.07926,  82.53156,
     VERTEX,   30.12157, -18.00159,  82.30585,
     VERTEX,   30.19260, -18.90108,  82.63368,
     VERTEX,   30.44884, -19.43416,  83.38983,
     VERTEX,   30.79243, -19.39721,  84.28548,
     VERTEX,   31.09212, -18.80434,  84.97852,
     VERTEX,   31.23343, -17.88201,  85.20422,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  30.67750, -17.94180,  83.75504,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   86.86314, -60.86735,  91.66080,
                       
     VERTEX,   83.43108, -67.60770,  92.11304,
     VERTEX,   82.74200, -67.22524,  91.56487,
     VERTEX,   81.97109, -66.65319,  91.57290,
     VERTEX,   81.41282, -66.11005,  92.13408,
     VERTEX,   81.28043, -65.80327,  93.03406,
     VERTEX,   81.62447, -65.85004,  93.92907,
     VERTEX,   82.31355, -66.23248,  94.47725,
     VERTEX,   83.08446, -66.80453,  94.46922,
     VERTEX,   83.64272, -67.34768,  93.90804,
     VERTEX,   83.77512, -67.65446,  93.00806,
     VERTEX,   83.43108, -67.60770,  92.11304,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   82.52777, -66.72887,  93.02106,
                       
     VERTEX,   83.43108, -67.60770,  92.11304,
     VERTEX,   82.74200, -67.22524,  91.56487,
     VERTEX,   81.97109, -66.65319,  91.57290,
     VERTEX,   81.41282, -66.11005,  92.13408,
     VERTEX,   81.28043, -65.80327,  93.03406,
     VERTEX,   81.62447, -65.85004,  93.92907,
     VERTEX,   82.31355, -66.23248,  94.47725,
     VERTEX,   83.08446, -66.80453,  94.46922,
     VERTEX,   83.64272, -67.34768,  93.90804,
     VERTEX,   83.77512, -67.65446,  93.00806,
     VERTEX,   83.43108, -67.60770,  92.11304,
                       
     END,              
                       
     CYLINDER,   75.51300, -76.21300,  95.22200,  82.52777, -66.72887,  93.02106,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   80.39713, -55.46376,  87.47972,
                       
     VERTEX,   78.16055, -61.80381,  87.67196,
     VERTEX,   77.49136, -61.51399,  87.04762,
     VERTEX,   76.66406, -61.03444,  86.96275,
     VERTEX,   75.99464, -60.54832,  87.44975,
     VERTEX,   75.73881, -60.24132,  88.32262,
     VERTEX,   75.99427, -60.23071,  89.24794,
     VERTEX,   76.66346, -60.52052,  89.87228,
     VERTEX,   77.49076, -61.00008,  89.95715,
     VERTEX,   78.16017, -61.48619,  89.47015,
     VERTEX,   78.41601, -61.79319,  88.59728,
     VERTEX,   78.16055, -61.80381,  87.67196,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   77.07741, -61.01726,  88.45995,
                       
     VERTEX,   78.16055, -61.80381,  87.67196,
     VERTEX,   77.49136, -61.51399,  87.04762,
     VERTEX,   76.66406, -61.03444,  86.96275,
     VERTEX,   75.99464, -60.54832,  87.44975,
     VERTEX,   75.73881, -60.24132,  88.32262,
     VERTEX,   75.99427, -60.23071,  89.24794,
     VERTEX,   76.66346, -60.52052,  89.87228,
     VERTEX,   77.49076, -61.00008,  89.95715,
     VERTEX,   78.16017, -61.48619,  89.47015,
     VERTEX,   78.41601, -61.79319,  88.59728,
     VERTEX,   78.16055, -61.80381,  87.67196,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  77.07741, -61.01726,  88.45995,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.99546, -74.26279,  87.03276,
                       
     VERTEX,   73.32166, -79.12447,  88.00046,
     VERTEX,   72.74123, -78.40235,  87.74898,
     VERTEX,   72.31944, -77.59936,  88.06345,
     VERTEX,   72.21739, -77.02221,  88.82378,
     VERTEX,   72.47408, -76.89136,  89.73952,
     VERTEX,   72.99144, -77.25677,  90.46091,
     VERTEX,   73.57188, -77.97889,  90.71239,
     VERTEX,   73.99367, -78.78188,  90.39791,
     VERTEX,   74.09571, -79.35903,  89.63760,
     VERTEX,   73.83903, -79.48988,  88.72185,
     VERTEX,   73.32166, -79.12447,  88.00046,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   73.15656, -78.19062,  89.23068,
                       
     VERTEX,   73.32166, -79.12447,  88.00046,
     VERTEX,   72.74123, -78.40235,  87.74898,
     VERTEX,   72.31944, -77.59936,  88.06345,
     VERTEX,   72.21739, -77.02221,  88.82378,
     VERTEX,   72.47408, -76.89136,  89.73952,
     VERTEX,   72.99144, -77.25677,  90.46091,
     VERTEX,   73.57188, -77.97889,  90.71239,
     VERTEX,   73.99367, -78.78188,  90.39791,
     VERTEX,   74.09571, -79.35903,  89.63760,
     VERTEX,   73.83903, -79.48988,  88.72185,
     VERTEX,   73.32166, -79.12447,  88.00046,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  73.15656, -78.19062,  89.23068,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   77.29144, -78.04436,  91.41874,
                       
     VERTEX,   71.17370, -82.07105,  92.49797,
     VERTEX,   70.68684, -81.25787,  92.34526,
     VERTEX,   70.41061, -80.43092,  92.74706,
     VERTEX,   70.45052, -79.90605,  93.54988,
     VERTEX,   70.79131, -79.88375,  94.44707,
     VERTEX,   71.30283, -80.37254,  95.09595,
     VERTEX,   71.78967, -81.18572,  95.24866,
     VERTEX,   72.06590, -82.01268,  94.84686,
     VERTEX,   72.02600, -82.53755,  94.04404,
     VERTEX,   71.68520, -82.55984,  93.14684,
     VERTEX,   71.17370, -82.07105,  92.49797,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   71.23826, -81.22180,  93.79696,
                       
     VERTEX,   71.17370, -82.07105,  92.49797,
     VERTEX,   70.68684, -81.25787,  92.34526,
     VERTEX,   70.41061, -80.43092,  92.74706,
     VERTEX,   70.45052, -79.90605,  93.54988,
     VERTEX,   70.79131, -79.88375,  94.44707,
     VERTEX,   71.30283, -80.37254,  95.09595,
     VERTEX,   71.78967, -81.18572,  95.24866,
     VERTEX,   72.06590, -82.01268,  94.84686,
     VERTEX,   72.02600, -82.53755,  94.04404,
     VERTEX,   71.68520, -82.55984,  93.14684,
     VERTEX,   71.17370, -82.07105,  92.49797,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  71.23826, -81.22180,  93.79696,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   74.72778, -81.93594,  97.50700,
                       
     VERTEX,   68.27672, -84.83468,  98.69559,
     VERTEX,   67.93908, -83.93651,  98.66582,
     VERTEX,   67.85257, -83.12230,  99.16701,
     VERTEX,   68.05023, -82.70306, 100.00770,
     VERTEX,   68.45657, -82.83892, 100.86679,
     VERTEX,   68.91637, -83.47799, 101.41613,
     VERTEX,   69.25402, -84.37616, 101.44589,
     VERTEX,   69.34053, -85.19037, 100.94470,
     VERTEX,   69.14286, -85.60961, 100.10401,
     VERTEX,   68.73653, -85.47375,  99.24493,
     VERTEX,   68.27672, -84.83468,  98.69559,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   68.59655, -84.15633, 100.05585,
                       
     VERTEX,   68.27672, -84.83468,  98.69559,
     VERTEX,   67.93908, -83.93651,  98.66582,
     VERTEX,   67.85257, -83.12230,  99.16701,
     VERTEX,   68.05023, -82.70306, 100.00770,
     VERTEX,   68.45657, -82.83892, 100.86679,
     VERTEX,   68.91637, -83.47799, 101.41613,
     VERTEX,   69.25402, -84.37616, 101.44589,
     VERTEX,   69.34053, -85.19037, 100.94470,
     VERTEX,   69.14286, -85.60961, 100.10401,
     VERTEX,   68.73653, -85.47375,  99.24493,
     VERTEX,   68.27672, -84.83468,  98.69559,
                       
     END,              
                       
     CYLINDER,   58.67600, -87.74900, 104.18000,  68.59655, -84.15633, 100.05585,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -25.18149,  31.69457,  94.91026,
                       
     VERTEX,  -25.55077,  26.28759,  94.32639,
     VERTEX,  -26.09924,  26.49243,  93.56559,
     VERTEX,  -26.96574,  26.80404,  93.29414,
     VERTEX,  -27.81929,  27.10339,  93.61575,
     VERTEX,  -28.33388,  27.27615,  94.40755,
     VERTEX,  -28.31294,  27.25632,  95.36712,
     VERTEX,  -27.76447,  27.05149,  96.12793,
     VERTEX,  -26.89797,  26.73988,  96.39937,
     VERTEX,  -26.04441,  26.44053,  96.07777,
     VERTEX,  -25.52983,  26.26777,  95.28596,
     VERTEX,  -25.55077,  26.28759,  94.32639,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.93185,  26.77196,  94.84676,
                       
     VERTEX,  -25.55077,  26.28759,  94.32639,
     VERTEX,  -26.09924,  26.49243,  93.56559,
     VERTEX,  -26.96574,  26.80404,  93.29414,
     VERTEX,  -27.81929,  27.10339,  93.61575,
     VERTEX,  -28.33388,  27.27615,  94.40755,
     VERTEX,  -28.31294,  27.25632,  95.36712,
     VERTEX,  -27.76447,  27.05149,  96.12793,
     VERTEX,  -26.89797,  26.73988,  96.39937,
     VERTEX,  -26.04441,  26.44053,  96.07777,
     VERTEX,  -25.52983,  26.26777,  95.28596,
     VERTEX,  -25.55077,  26.28759,  94.32639,
                       
     END,              
                       
     CYLINDER,  -29.76400,  18.80700,  94.74400, -26.93185,  26.77196,  94.84676,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -29.11856,  40.35189,  94.22718,
                       
     VERTEX,  -30.51764,  33.83493,  93.59109,
     VERTEX,  -31.10719,  34.10143,  92.88185,
     VERTEX,  -31.96375,  34.48932,  92.68836,
     VERTEX,  -32.76015,  34.85044,  93.08451,
     VERTEX,  -33.19219,  35.04686,  93.91900,
     VERTEX,  -33.09484,  35.00354,  94.87306,
     VERTEX,  -32.50529,  34.73705,  95.58230,
     VERTEX,  -31.64873,  34.34916,  95.77579,
     VERTEX,  -30.85233,  33.98803,  95.37964,
     VERTEX,  -30.42029,  33.79162,  94.54516,
     VERTEX,  -30.51764,  33.83493,  93.59109,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.80624,  34.41924,  94.23208,
                       
     VERTEX,  -30.51764,  33.83493,  93.59109,
     VERTEX,  -31.10719,  34.10143,  92.88185,
     VERTEX,  -31.96375,  34.48932,  92.68836,
     VERTEX,  -32.76015,  34.85044,  93.08451,
     VERTEX,  -33.19219,  35.04686,  93.91900,
     VERTEX,  -33.09484,  35.00354,  94.87306,
     VERTEX,  -32.50529,  34.73705,  95.58230,
     VERTEX,  -31.64873,  34.34916,  95.77579,
     VERTEX,  -30.85233,  33.98803,  95.37964,
     VERTEX,  -30.42029,  33.79162,  94.54516,
     VERTEX,  -30.51764,  33.83493,  93.59109,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.80624,  34.41924,  94.23208,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.72432,  35.26683,  86.94714,
                       
     VERTEX,  -27.56155,  29.46766,  86.31844,
     VERTEX,  -28.13502,  29.70916,  85.58741,
     VERTEX,  -28.99713,  30.06612,  85.36172,
     VERTEX,  -29.81860,  30.40219,  85.72758,
     VERTEX,  -30.28564,  30.58900,  86.54523,
     VERTEX,  -30.21987,  30.55520,  87.50239,
     VERTEX,  -29.64640,  30.31369,  88.23342,
     VERTEX,  -28.78428,  29.95674,  88.45911,
     VERTEX,  -27.96282,  29.62067,  88.09325,
     VERTEX,  -27.49578,  29.43386,  87.27559,
     VERTEX,  -27.56155,  29.46766,  86.31844,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.89071,  30.01143,  86.91042,
                       
     VERTEX,  -27.56155,  29.46766,  86.31844,
     VERTEX,  -28.13502,  29.70916,  85.58741,
     VERTEX,  -28.99713,  30.06612,  85.36172,
     VERTEX,  -29.81860,  30.40219,  85.72758,
     VERTEX,  -30.28564,  30.58900,  86.54523,
     VERTEX,  -30.21987,  30.55520,  87.50239,
     VERTEX,  -29.64640,  30.31369,  88.23342,
     VERTEX,  -28.78428,  29.95674,  88.45911,
     VERTEX,  -27.96282,  29.62067,  88.09325,
     VERTEX,  -27.49578,  29.43386,  87.27559,
     VERTEX,  -27.56155,  29.46766,  86.31844,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.89071,  30.01143,  86.91042,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.93263,  44.13460,  95.38840,
                       
     VERTEX,  -17.10597,  39.21709,  94.42741,
     VERTEX,  -17.72263,  39.79718,  93.97483,
     VERTEX,  -18.40641,  40.45808,  94.10619,
     VERTEX,  -18.89612,  40.94736,  94.77132,
     VERTEX,  -19.00471,  41.07812,  95.71615,
     VERTEX,  -18.69072,  40.80042,  96.57980,
     VERTEX,  -18.07405,  40.22033,  97.03237,
     VERTEX,  -17.39028,  39.55943,  96.90101,
     VERTEX,  -16.90057,  39.07015,  96.23589,
     VERTEX,  -16.79197,  38.93939,  95.29105,
     VERTEX,  -17.10597,  39.21709,  94.42741,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.89834,  40.00875,  95.50360,
                       
     VERTEX,  -17.10597,  39.21709,  94.42741,
     VERTEX,  -17.72263,  39.79718,  93.97483,
     VERTEX,  -18.40641,  40.45808,  94.10619,
     VERTEX,  -18.89612,  40.94736,  94.77132,
     VERTEX,  -19.00471,  41.07812,  95.71615,
     VERTEX,  -18.69072,  40.80042,  96.57980,
     VERTEX,  -18.07405,  40.22033,  97.03237,
     VERTEX,  -17.39028,  39.55943,  96.90101,
     VERTEX,  -16.90057,  39.07015,  96.23589,
     VERTEX,  -16.79197,  38.93939,  95.29105,
     VERTEX,  -17.10597,  39.21709,  94.42741,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -17.89834,  40.00875,  95.50360,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -15.97686,  42.38915, 100.88828,
                       
     VERTEX,  -18.65063,  37.25226,  99.98953,
     VERTEX,  -19.28060,  37.76022,  99.47309,
     VERTEX,  -20.01997,  38.36981,  99.53086,
     VERTEX,  -20.58633,  38.84818, 100.14079,
     VERTEX,  -20.76334,  39.01260, 101.06989,
     VERTEX,  -20.48340,  38.80029, 101.96328,
     VERTEX,  -19.85343,  38.29233, 102.47972,
     VERTEX,  -19.11406,  37.68275, 102.42195,
     VERTEX,  -18.54770,  37.20438, 101.81203,
     VERTEX,  -18.37069,  37.03995, 100.88293,
     VERTEX,  -18.65063,  37.25226,  99.98953,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.56701,  38.02628, 100.97640,
                       
     VERTEX,  -18.65063,  37.25226,  99.98953,
     VERTEX,  -19.28060,  37.76022,  99.47309,
     VERTEX,  -20.01997,  38.36981,  99.53086,
     VERTEX,  -20.58633,  38.84818, 100.14079,
     VERTEX,  -20.76334,  39.01260, 101.06989,
     VERTEX,  -20.48340,  38.80029, 101.96328,
     VERTEX,  -19.85343,  38.29233, 102.47972,
     VERTEX,  -19.11406,  37.68275, 102.42195,
     VERTEX,  -18.54770,  37.20438, 101.81203,
     VERTEX,  -18.37069,  37.03995, 100.88293,
     VERTEX,  -18.65063,  37.25226,  99.98953,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.56701,  38.02628, 100.97640,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.95570,  27.76502,  47.84723,
                       
     VERTEX,   42.86198,  33.64296,  47.15995,
     VERTEX,   43.19683,  33.89864,  48.02256,
     VERTEX,   43.11094,  33.74390,  48.96611,
     VERTEX,   42.63711,  33.23785,  49.63019,
     VERTEX,   41.95633,  32.57379,  49.76115,
     VERTEX,   41.32862,  32.00535,  49.30896,
     VERTEX,   40.99377,  31.74967,  48.44635,
     VERTEX,   41.07966,  31.90441,  47.50280,
     VERTEX,   41.55349,  32.41045,  46.83872,
     VERTEX,   42.23427,  33.07452,  46.70777,
     VERTEX,   42.86198,  33.64296,  47.15995,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.09530,  32.82415,  48.23446,
                       
     VERTEX,   42.86198,  33.64296,  47.15995,
     VERTEX,   43.19683,  33.89864,  48.02256,
     VERTEX,   43.11094,  33.74390,  48.96611,
     VERTEX,   42.63711,  33.23785,  49.63019,
     VERTEX,   41.95633,  32.57379,  49.76115,
     VERTEX,   41.32862,  32.00535,  49.30896,
     VERTEX,   40.99377,  31.74967,  48.44635,
     VERTEX,   41.07966,  31.90441,  47.50280,
     VERTEX,   41.55349,  32.41045,  46.83872,
     VERTEX,   42.23427,  33.07452,  46.70777,
     VERTEX,   42.86198,  33.64296,  47.15995,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  42.09530,  32.82415,  48.23446,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   42.17111,  22.96143,  54.19469,
                       
     VERTEX,   39.02285,  28.37641,  53.47751,
     VERTEX,   39.33414,  28.58922,  54.36035,
     VERTEX,   39.20076,  28.41261,  55.29449,
     VERTEX,   38.67366,  27.91403,  55.92312,
     VERTEX,   37.95416,  27.28392,  56.00613,
     VERTEX,   37.31710,  26.76297,  55.51180,
     VERTEX,   37.00581,  26.55015,  54.62896,
     VERTEX,   37.13919,  26.72676,  53.69482,
     VERTEX,   37.66629,  27.22534,  53.06619,
     VERTEX,   38.38579,  27.85545,  52.98318,
     VERTEX,   39.02285,  28.37641,  53.47751,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   38.16998,  27.56969,  54.49466,
                       
     VERTEX,   39.02285,  28.37641,  53.47751,
     VERTEX,   39.33414,  28.58922,  54.36035,
     VERTEX,   39.20076,  28.41261,  55.29449,
     VERTEX,   38.67366,  27.91403,  55.92312,
     VERTEX,   37.95416,  27.28392,  56.00613,
     VERTEX,   37.31710,  26.76297,  55.51180,
     VERTEX,   37.00581,  26.55015,  54.62896,
     VERTEX,   37.13919,  26.72676,  53.69482,
     VERTEX,   37.66629,  27.22534,  53.06619,
     VERTEX,   38.38579,  27.85545,  52.98318,
     VERTEX,   39.02285,  28.37641,  53.47751,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  38.16998,  27.56969,  54.49466,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   37.15073,  26.64701,  55.88557,
                       
     VERTEX,   33.56807,  31.20552,  54.99809,
     VERTEX,   33.92050,  31.54242,  55.82506,
     VERTEX,   33.89289,  31.44187,  56.77938,
     VERTEX,   33.49578,  30.94227,  57.49653,
     VERTEX,   32.88085,  30.23445,  57.70258,
     VERTEX,   32.28299,  29.58878,  57.31883,
     VERTEX,   31.93056,  29.25187,  56.49186,
     VERTEX,   31.95817,  29.35242,  55.53754,
     VERTEX,   32.35528,  29.85202,  54.82039,
     VERTEX,   32.97020,  30.55984,  54.61433,
     VERTEX,   33.56807,  31.20552,  54.99809,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.92553,  30.39715,  56.15846,
                       
     VERTEX,   33.56807,  31.20552,  54.99809,
     VERTEX,   33.92050,  31.54242,  55.82506,
     VERTEX,   33.89289,  31.44187,  56.77938,
     VERTEX,   33.49578,  30.94227,  57.49653,
     VERTEX,   32.88085,  30.23445,  57.70258,
     VERTEX,   32.28299,  29.58878,  57.31883,
     VERTEX,   31.93056,  29.25187,  56.49186,
     VERTEX,   31.95817,  29.35242,  55.53754,
     VERTEX,   32.35528,  29.85202,  54.82039,
     VERTEX,   32.97020,  30.55984,  54.61433,
     VERTEX,   33.56807,  31.20552,  54.99809,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  32.92553,  30.39715,  56.15846,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.11105,  38.13007,  48.07009,
                       
     VERTEX,   29.82061,  41.84632,  47.06856,
     VERTEX,   30.17073,  42.40812,  47.76382,
     VERTEX,   30.27806,  42.49238,  48.71407,
     VERTEX,   30.10160,  42.06691,  49.55635,
     VERTEX,   29.70875,  41.29422,  49.96894,
     VERTEX,   29.24957,  40.46946,  49.79423,
     VERTEX,   28.89945,  39.90765,  49.09897,
     VERTEX,   28.79213,  39.82339,  48.14872,
     VERTEX,   28.96859,  40.24886,  47.30644,
     VERTEX,   29.36143,  41.02155,  46.89385,
     VERTEX,   29.82061,  41.84632,  47.06856,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.53509,  41.15789,  48.43140,
                       
     VERTEX,   29.82061,  41.84632,  47.06856,
     VERTEX,   30.17073,  42.40812,  47.76382,
     VERTEX,   30.27806,  42.49238,  48.71407,
     VERTEX,   30.10160,  42.06691,  49.55635,
     VERTEX,   29.70875,  41.29422,  49.96894,
     VERTEX,   29.24957,  40.46946,  49.79423,
     VERTEX,   28.89945,  39.90765,  49.09897,
     VERTEX,   28.79213,  39.82339,  48.14872,
     VERTEX,   28.96859,  40.24886,  47.30644,
     VERTEX,   29.36143,  41.02155,  46.89385,
     VERTEX,   29.82061,  41.84632,  47.06856,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  29.53509,  41.15789,  48.43140,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.34158,  36.82502,  42.25708,
                       
     VERTEX,   31.24691,  40.89355,  41.30566,
     VERTEX,   31.60866,  41.40363,  42.03405,
     VERTEX,   31.69560,  41.43938,  42.98944,
     VERTEX,   31.47451,  40.98717,  43.80689,
     VERTEX,   31.02984,  40.21973,  44.17417,
     VERTEX,   30.53144,  39.43018,  43.95098,
     VERTEX,   30.16969,  38.92011,  43.22258,
     VERTEX,   30.08275,  38.88435,  42.26720,
     VERTEX,   30.30384,  39.33656,  41.44975,
     VERTEX,   30.74851,  40.10400,  41.08247,
     VERTEX,   31.24691,  40.89355,  41.30566,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.88918,  40.16187,  42.62832,
                       
     VERTEX,   31.24691,  40.89355,  41.30566,
     VERTEX,   31.60866,  41.40363,  42.03405,
     VERTEX,   31.69560,  41.43938,  42.98944,
     VERTEX,   31.47451,  40.98717,  43.80689,
     VERTEX,   31.02984,  40.21973,  44.17417,
     VERTEX,   30.53144,  39.43018,  43.95098,
     VERTEX,   30.16969,  38.92011,  43.22258,
     VERTEX,   30.08275,  38.88435,  42.26720,
     VERTEX,   30.30384,  39.33656,  41.44975,
     VERTEX,   30.74851,  40.10400,  41.08247,
     VERTEX,   31.24691,  40.89355,  41.30566,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  30.88918,  40.16187,  42.62832,   0.80000,
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
                       
     SPHERE,  -29.76400,  18.80700,  94.74400,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -36.15500,  24.82000,  94.24000,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,  -32.39600,  21.50800,  86.85100,   0.80000,
                       
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
