from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.29411, -77.35767,  46.51967,
                       
     VERTEX,    9.70629, -73.84077,  47.22554,
     VERTEX,   10.29949, -73.68347,  47.96376,
     VERTEX,   10.56527, -74.00450,  48.82858,
     VERTEX,   10.40212, -74.68124,  49.48964,
     VERTEX,    9.87236, -75.45518,  49.69447,
     VERTEX,    9.17833, -76.03073,  49.36481,
     VERTEX,    8.58513, -76.18803,  48.62658,
     VERTEX,    8.31935, -75.86700,  47.76177,
     VERTEX,    8.48250, -75.19026,  47.10070,
     VERTEX,    9.01226, -74.41631,  46.89588,
     VERTEX,    9.70629, -73.84077,  47.22554,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.44231, -74.93575,  48.29517,
                       
     VERTEX,    9.70629, -73.84077,  47.22554,
     VERTEX,   10.29949, -73.68347,  47.96376,
     VERTEX,   10.56527, -74.00450,  48.82858,
     VERTEX,   10.40212, -74.68124,  49.48964,
     VERTEX,    9.87236, -75.45518,  49.69447,
     VERTEX,    9.17833, -76.03073,  49.36481,
     VERTEX,    8.58513, -76.18803,  48.62658,
     VERTEX,    8.31935, -75.86700,  47.76177,
     VERTEX,    8.48250, -75.19026,  47.10070,
     VERTEX,    9.01226, -74.41631,  46.89588,
     VERTEX,    9.70629, -73.84077,  47.22554,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,   9.44231, -74.93575,  48.29517,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.22134, -77.51688,  41.65058,
                       
     VERTEX,   24.24368, -76.38333,  41.69429,
     VERTEX,   24.58716, -75.60151,  42.13290,
     VERTEX,   24.99119, -75.27921,  42.94191,
     VERTEX,   25.30145, -75.53955,  43.81229,
     VERTEX,   25.39943, -76.28308,  44.41159,
     VERTEX,   25.24771, -77.22580,  44.51090,
     VERTEX,   24.90424, -78.00762,  44.07228,
     VERTEX,   24.50021, -78.32991,  43.26328,
     VERTEX,   24.18995, -78.06958,  42.39290,
     VERTEX,   24.09197, -77.32605,  41.79360,
     VERTEX,   24.24368, -76.38333,  41.69429,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.74570, -76.80457,  43.10260,
                       
     VERTEX,   24.24368, -76.38333,  41.69429,
     VERTEX,   24.58716, -75.60151,  42.13290,
     VERTEX,   24.99119, -75.27921,  42.94191,
     VERTEX,   25.30145, -75.53955,  43.81229,
     VERTEX,   25.39943, -76.28308,  44.41159,
     VERTEX,   25.24771, -77.22580,  44.51090,
     VERTEX,   24.90424, -78.00762,  44.07228,
     VERTEX,   24.50021, -78.32991,  43.26328,
     VERTEX,   24.18995, -78.06958,  42.39290,
     VERTEX,   24.09197, -77.32605,  41.79360,
     VERTEX,   24.24368, -76.38333,  41.69429,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  24.74570, -76.80457,  43.10260,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.29127, -74.57633,  36.75574,
                       
     VERTEX,   22.47257, -73.41680,  36.76344,
     VERTEX,   22.82859, -72.64466,  37.20914,
     VERTEX,   23.23964, -72.33675,  38.02021,
     VERTEX,   23.54870, -72.61067,  38.88684,
     VERTEX,   23.63774, -73.36180,  39.47801,
     VERTEX,   23.47272, -74.30324,  39.56791,
     VERTEX,   23.11670, -75.07537,  39.12220,
     VERTEX,   22.70565, -75.38329,  38.31113,
     VERTEX,   22.39659, -75.10936,  37.44451,
     VERTEX,   22.30756, -74.35823,  36.85334,
     VERTEX,   22.47257, -73.41680,  36.76344,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.97265, -73.86002,  38.16567,
                       
     VERTEX,   22.47257, -73.41680,  36.76344,
     VERTEX,   22.82859, -72.64466,  37.20914,
     VERTEX,   23.23964, -72.33675,  38.02021,
     VERTEX,   23.54870, -72.61067,  38.88684,
     VERTEX,   23.63774, -73.36180,  39.47801,
     VERTEX,   23.47272, -74.30324,  39.56791,
     VERTEX,   23.11670, -75.07537,  39.12220,
     VERTEX,   22.70565, -75.38329,  38.31113,
     VERTEX,   22.39659, -75.10936,  37.44451,
     VERTEX,   22.30756, -74.35823,  36.85334,
     VERTEX,   22.47257, -73.41680,  36.76344,
                       
     END,              
                       
     CYLINDER,   17.60300, -72.70100,  40.44700,  22.97265, -73.86002,  38.16567,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.15997, -19.03847,  91.10425,
                       
     VERTEX,   36.73609, -19.35523,  91.31794,
     VERTEX,   36.71402, -18.47099,  90.94480,
     VERTEX,   36.52233, -17.96801,  90.14990,
     VERTEX,   36.23423, -18.03842,  89.23686,
     VERTEX,   35.95977, -18.65532,  88.55444,
     VERTEX,   35.80378, -19.58307,  88.36328,
     VERTEX,   35.82584, -20.46731,  88.73642,
     VERTEX,   36.01754, -20.97029,  89.53132,
     VERTEX,   36.30564, -20.89988,  90.44436,
     VERTEX,   36.58010, -20.28298,  91.12679,
     VERTEX,   36.73609, -19.35523,  91.31794,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.26993, -19.46915,  89.84061,
                       
     VERTEX,   36.73609, -19.35523,  91.31794,
     VERTEX,   36.71402, -18.47099,  90.94480,
     VERTEX,   36.52233, -17.96801,  90.14990,
     VERTEX,   36.23423, -18.03842,  89.23686,
     VERTEX,   35.95977, -18.65532,  88.55444,
     VERTEX,   35.80378, -19.58307,  88.36328,
     VERTEX,   35.82584, -20.46731,  88.73642,
     VERTEX,   36.01754, -20.97029,  89.53132,
     VERTEX,   36.30564, -20.89988,  90.44436,
     VERTEX,   36.58010, -20.28298,  91.12679,
     VERTEX,   36.73609, -19.35523,  91.31794,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  36.26993, -19.46915,  89.84061,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.31386, -18.25993,  83.67816,
                       
     VERTEX,   32.48083, -18.29406,  84.11897,
     VERTEX,   32.40912, -17.38399,  83.82196,
     VERTEX,   32.20401, -16.82718,  83.06731,
     VERTEX,   31.94382, -16.83632,  82.14330,
     VERTEX,   31.72796, -17.40791,  81.40283,
     VERTEX,   31.63887, -18.32364,  81.12877,
     VERTEX,   31.71058, -19.23372,  81.42578,
     VERTEX,   31.91570, -19.79053,  82.18043,
     VERTEX,   32.17588, -19.78139,  83.10445,
     VERTEX,   32.39174, -19.20979,  83.84491,
     VERTEX,   32.48083, -18.29406,  84.11897,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.05985, -18.30885,  82.62387,
                       
     VERTEX,   32.48083, -18.29406,  84.11897,
     VERTEX,   32.40912, -17.38399,  83.82196,
     VERTEX,   32.20401, -16.82718,  83.06731,
     VERTEX,   31.94382, -16.83632,  82.14330,
     VERTEX,   31.72796, -17.40791,  81.40283,
     VERTEX,   31.63887, -18.32364,  81.12877,
     VERTEX,   31.71058, -19.23372,  81.42578,
     VERTEX,   31.91570, -19.79053,  82.18043,
     VERTEX,   32.17588, -19.78139,  83.10445,
     VERTEX,   32.39174, -19.20979,  83.84491,
     VERTEX,   32.48083, -18.29406,  84.11897,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  32.05985, -18.30885,  82.62387,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   86.15720, -59.97861,  94.84437,
                       
     VERTEX,   83.16872, -66.90570,  94.13707,
     VERTEX,   82.53619, -66.50496,  93.53632,
     VERTEX,   81.73380, -65.97993,  93.49029,
     VERTEX,   81.06803, -65.53117,  94.01656,
     VERTEX,   80.79318, -65.33009,  94.91413,
     VERTEX,   81.01424, -65.45349,  95.84015,
     VERTEX,   81.64677, -65.85424,  96.44090,
     VERTEX,   82.44917, -66.37926,  96.48693,
     VERTEX,   83.11493, -66.82802,  95.96066,
     VERTEX,   83.38978, -67.02911,  95.06309,
     VERTEX,   83.16872, -66.90570,  94.13707,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   82.09148, -66.17960,  94.98861,
                       
     VERTEX,   83.16872, -66.90570,  94.13707,
     VERTEX,   82.53619, -66.50496,  93.53632,
     VERTEX,   81.73380, -65.97993,  93.49029,
     VERTEX,   81.06803, -65.53117,  94.01656,
     VERTEX,   80.79318, -65.33009,  94.91413,
     VERTEX,   81.01424, -65.45349,  95.84015,
     VERTEX,   81.64677, -65.85424,  96.44090,
     VERTEX,   82.44917, -66.37926,  96.48693,
     VERTEX,   83.11493, -66.82802,  95.96066,
     VERTEX,   83.38978, -67.02911,  95.06309,
     VERTEX,   83.16872, -66.90570,  94.13707,
                       
     END,              
                       
     CYLINDER,   75.51300, -76.21300,  95.22200,  82.09148, -66.17960,  94.98861,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   79.74139, -55.22781,  90.13138,
                       
     VERTEX,   77.87271, -61.52006,  89.35666,
     VERTEX,   77.26217, -61.18420,  88.69633,
     VERTEX,   76.42626, -60.72888,  88.57168,
     VERTEX,   75.68427, -60.32800,  89.03032,
     VERTEX,   75.31962, -60.13470,  89.89707,
     VERTEX,   75.47159, -60.22280,  90.84087,
     VERTEX,   76.08213, -60.55865,  91.50120,
     VERTEX,   76.91804, -61.01398,  91.62585,
     VERTEX,   77.66003, -61.41485,  91.16721,
     VERTEX,   78.02467, -61.60816,  90.30045,
     VERTEX,   77.87271, -61.52006,  89.35666,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.67215, -60.87143,  90.09876,
                       
     VERTEX,   77.87271, -61.52006,  89.35666,
     VERTEX,   77.26217, -61.18420,  88.69633,
     VERTEX,   76.42626, -60.72888,  88.57168,
     VERTEX,   75.68427, -60.32800,  89.03032,
     VERTEX,   75.31962, -60.13470,  89.89707,
     VERTEX,   75.47159, -60.22280,  90.84087,
     VERTEX,   76.08213, -60.55865,  91.50120,
     VERTEX,   76.91804, -61.01398,  91.62585,
     VERTEX,   77.66003, -61.41485,  91.16721,
     VERTEX,   78.02467, -61.60816,  90.30045,
     VERTEX,   77.87271, -61.52006,  89.35666,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.67215, -60.87143,  90.09876,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.66152, -74.04777,  90.06565,
                       
     VERTEX,   73.30976, -78.89585,  89.84772,
     VERTEX,   72.74846, -78.16865,  89.56895,
     VERTEX,   72.26419, -77.39908,  89.87695,
     VERTEX,   72.04195, -76.88110,  90.65406,
     VERTEX,   72.16661, -76.81255,  91.60345,
     VERTEX,   72.59057, -77.21962,  92.36251,
     VERTEX,   73.15188, -77.94682,  92.64127,
     VERTEX,   73.63614, -78.71639,  92.33328,
     VERTEX,   73.85838, -79.23438,  91.55617,
     VERTEX,   73.73372, -79.30292,  90.60677,
     VERTEX,   73.30976, -78.89585,  89.84772,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   72.95016, -78.05774,  91.10512,
                       
     VERTEX,   73.30976, -78.89585,  89.84772,
     VERTEX,   72.74846, -78.16865,  89.56895,
     VERTEX,   72.26419, -77.39908,  89.87695,
     VERTEX,   72.04195, -76.88110,  90.65406,
     VERTEX,   72.16661, -76.81255,  91.60345,
     VERTEX,   72.59057, -77.21962,  92.36251,
     VERTEX,   73.15188, -77.94682,  92.64127,
     VERTEX,   73.63614, -78.71639,  92.33328,
     VERTEX,   73.85838, -79.23438,  91.55617,
     VERTEX,   73.73372, -79.30292,  90.60677,
     VERTEX,   73.30976, -78.89585,  89.84772,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  72.95016, -78.05774,  91.10512,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.73057, -77.64070,  94.42511,
                       
     VERTEX,   71.06224, -81.76126,  94.32788,
     VERTEX,   70.56593, -80.96217,  94.13625,
     VERTEX,   70.19402, -80.16695,  94.52472,
     VERTEX,   70.08856, -79.67936,  95.34492,
     VERTEX,   70.28985, -79.68564,  96.28356,
     VERTEX,   70.72099, -80.18338,  96.98211,
     VERTEX,   71.21731, -80.98247,  97.17374,
     VERTEX,   71.58923, -81.77769,  96.78527,
     VERTEX,   71.69467, -82.26527,  95.96507,
     VERTEX,   71.49339, -82.25900,  95.02643,
     VERTEX,   71.06224, -81.76126,  94.32788,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   70.89162, -80.97232,  95.65499,
                       
     VERTEX,   71.06224, -81.76126,  94.32788,
     VERTEX,   70.56593, -80.96217,  94.13625,
     VERTEX,   70.19402, -80.16695,  94.52472,
     VERTEX,   70.08856, -79.67936,  95.34492,
     VERTEX,   70.28985, -79.68564,  96.28356,
     VERTEX,   70.72099, -80.18338,  96.98211,
     VERTEX,   71.21731, -80.98247,  97.17374,
     VERTEX,   71.58923, -81.77769,  96.78527,
     VERTEX,   71.69467, -82.26527,  95.96507,
     VERTEX,   71.49339, -82.25900,  95.02643,
     VERTEX,   71.06224, -81.76126,  94.32788,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  70.89162, -80.97232,  95.65499,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.01077, -55.94020, 121.61366,
                       
     VERTEX,   17.55622, -51.55363, 123.16089,
     VERTEX,   16.89327, -51.17760, 123.74459,
     VERTEX,   16.09883, -50.63940, 123.77293,
     VERTEX,   15.47634, -50.14460, 123.23508,
     VERTEX,   15.26358, -49.88220, 122.33649,
     VERTEX,   15.54180, -49.95242, 121.42038,
     VERTEX,   16.20475, -50.32844, 120.83668,
     VERTEX,   16.99919, -50.86664, 120.80833,
     VERTEX,   17.62168, -51.36144, 121.34618,
     VERTEX,   17.83444, -51.62385, 122.24477,
     VERTEX,   17.55622, -51.55363, 123.16089,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.54901, -50.75302, 122.29063,
                       
     VERTEX,   17.55622, -51.55363, 123.16089,
     VERTEX,   16.89327, -51.17760, 123.74459,
     VERTEX,   16.09883, -50.63940, 123.77293,
     VERTEX,   15.47634, -50.14460, 123.23508,
     VERTEX,   15.26358, -49.88220, 122.33649,
     VERTEX,   15.54180, -49.95242, 121.42038,
     VERTEX,   16.20475, -50.32844, 120.83668,
     VERTEX,   16.99919, -50.86664, 120.80833,
     VERTEX,   17.62168, -51.36144, 121.34618,
     VERTEX,   17.83444, -51.62385, 122.24477,
     VERTEX,   17.55622, -51.55363, 123.16089,
                       
     END,              
                       
     CYLINDER,   22.27400, -42.36000, 123.38600,  16.54901, -50.75302, 122.29063,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.52440,  37.68792,  96.51923,
                       
     VERTEX,  -30.22896,  32.19398,  94.86540,
     VERTEX,  -30.80029,  32.64379,  94.23862,
     VERTEX,  -31.61560,  33.14289,  94.15043,
     VERTEX,  -32.36346,  33.50063,  94.63450,
     VERTEX,  -32.75822,  33.58036,  95.50594,
     VERTEX,  -32.64910,  33.35164,  96.43188,
     VERTEX,  -32.07777,  32.90182,  97.05866,
     VERTEX,  -31.26246,  32.40273,  97.14686,
     VERTEX,  -30.51460,  32.04499,  96.66279,
     VERTEX,  -30.11983,  31.96526,  95.79135,
     VERTEX,  -30.22896,  32.19398,  94.86540,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.43903,  32.77281,  95.64864,
                       
     VERTEX,  -30.22896,  32.19398,  94.86540,
     VERTEX,  -30.80029,  32.64379,  94.23862,
     VERTEX,  -31.61560,  33.14289,  94.15043,
     VERTEX,  -32.36346,  33.50063,  94.63450,
     VERTEX,  -32.75822,  33.58036,  95.50594,
     VERTEX,  -32.64910,  33.35164,  96.43188,
     VERTEX,  -32.07777,  32.90182,  97.05866,
     VERTEX,  -31.26246,  32.40273,  97.14686,
     VERTEX,  -30.51460,  32.04499,  96.66279,
     VERTEX,  -30.11983,  31.96526,  95.79135,
     VERTEX,  -30.22896,  32.19398,  94.86540,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.43903,  32.77281,  95.64864,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.38192,  32.80060,  88.93261,
                       
     VERTEX,  -27.41388,  27.94624,  87.41683,
     VERTEX,  -27.97349,  28.36552,  86.75907,
     VERTEX,  -28.80261,  28.83128,  86.62782,
     VERTEX,  -29.58455,  29.16561,  87.07323,
     VERTEX,  -30.02064,  29.24082,  87.92515,
     VERTEX,  -29.94430,  29.02818,  88.85818,
     VERTEX,  -29.38470,  28.60890,  89.51595,
     VERTEX,  -28.55557,  28.14314,  89.64719,
     VERTEX,  -27.77363,  27.80881,  89.20178,
     VERTEX,  -27.33754,  27.73360,  88.34986,
     VERTEX,  -27.41388,  27.94624,  87.41683,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.67909,  28.48721,  88.13750,
                       
     VERTEX,  -27.41388,  27.94624,  87.41683,
     VERTEX,  -27.97349,  28.36552,  86.75907,
     VERTEX,  -28.80261,  28.83128,  86.62782,
     VERTEX,  -29.58455,  29.16561,  87.07323,
     VERTEX,  -30.02064,  29.24082,  87.92515,
     VERTEX,  -29.94430,  29.02818,  88.85818,
     VERTEX,  -29.38470,  28.60890,  89.51595,
     VERTEX,  -28.55557,  28.14314,  89.64719,
     VERTEX,  -27.77363,  27.80881,  89.20178,
     VERTEX,  -27.33754,  27.73360,  88.34986,
     VERTEX,  -27.41388,  27.94624,  87.41683,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.67909,  28.48721,  88.13750,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.32336,  34.28220,  87.57174,
                       
     VERTEX,  -21.97292,  30.03055,  85.95470,
     VERTEX,  -22.55083,  30.57021,  85.41029,
     VERTEX,  -23.31900,  31.14574,  85.42671,
     VERTEX,  -23.98402,  31.53732,  85.99770,
     VERTEX,  -24.29186,  31.59538,  86.90514,
     VERTEX,  -24.12494,  31.29773,  87.80244,
     VERTEX,  -23.54703,  30.75807,  88.34686,
     VERTEX,  -22.77886,  30.18253,  88.33043,
     VERTEX,  -22.11385,  29.79095,  87.75945,
     VERTEX,  -21.80600,  29.73290,  86.85200,
     VERTEX,  -21.97292,  30.03055,  85.95470,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -23.04893,  30.66414,  86.87857,
                       
     VERTEX,  -21.97292,  30.03055,  85.95470,
     VERTEX,  -22.55083,  30.57021,  85.41029,
     VERTEX,  -23.31900,  31.14574,  85.42671,
     VERTEX,  -23.98402,  31.53732,  85.99770,
     VERTEX,  -24.29186,  31.59538,  86.90514,
     VERTEX,  -24.12494,  31.29773,  87.80244,
     VERTEX,  -23.54703,  30.75807,  88.34686,
     VERTEX,  -22.77886,  30.18253,  88.33043,
     VERTEX,  -22.11385,  29.79095,  87.75945,
     VERTEX,  -21.80600,  29.73290,  86.85200,
     VERTEX,  -21.97292,  30.03055,  85.95470,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -23.04893,  30.66414,  86.87857,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.58303,  41.74722,  97.35130,
                       
     VERTEX,  -16.97461,  37.87026,  95.50331,
     VERTEX,  -17.49948,  38.60435,  95.17586,
     VERTEX,  -18.09416,  39.31129,  95.43697,
     VERTEX,  -18.53152,  39.72106,  96.18690,
     VERTEX,  -18.64450,  39.67714,  97.13922,
     VERTEX,  -18.38994,  39.19629,  97.93016,
     VERTEX,  -17.86508,  38.46220,  98.25762,
     VERTEX,  -17.27039,  37.75526,  97.99651,
     VERTEX,  -16.83303,  37.34549,  97.24657,
     VERTEX,  -16.72005,  37.38942,  96.29426,
     VERTEX,  -16.97461,  37.87026,  95.50331,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.68228,  38.53328,  96.71674,
                       
     VERTEX,  -16.97461,  37.87026,  95.50331,
     VERTEX,  -17.49948,  38.60435,  95.17586,
     VERTEX,  -18.09416,  39.31129,  95.43697,
     VERTEX,  -18.53152,  39.72106,  96.18690,
     VERTEX,  -18.64450,  39.67714,  97.13922,
     VERTEX,  -18.38994,  39.19629,  97.93016,
     VERTEX,  -17.86508,  38.46220,  98.25762,
     VERTEX,  -17.27039,  37.75526,  97.99651,
     VERTEX,  -16.83303,  37.34549,  97.24657,
     VERTEX,  -16.72005,  37.38942,  96.29426,
     VERTEX,  -16.97461,  37.87026,  95.50331,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -17.68228,  38.53328,  96.71674,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -15.26436,  39.74632, 102.82896,
                       
     VERTEX,  -18.34683,  35.72135, 101.01235,
     VERTEX,  -18.89050,  36.41990, 100.64079,
     VERTEX,  -19.52438,  37.10814, 100.85556,
     VERTEX,  -20.00634,  37.52319, 101.57462,
     VERTEX,  -20.15230,  37.50652, 102.52332,
     VERTEX,  -19.90649,  37.06448, 103.33927,
     VERTEX,  -19.36282,  36.36594, 103.71083,
     VERTEX,  -18.72895,  35.67770, 103.49606,
     VERTEX,  -18.24698,  35.26265, 102.77700,
     VERTEX,  -18.10103,  35.27932, 101.82831,
     VERTEX,  -18.34683,  35.72135, 101.01235,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.12666,  36.39292, 102.17581,
                       
     VERTEX,  -18.34683,  35.72135, 101.01235,
     VERTEX,  -18.89050,  36.41990, 100.64079,
     VERTEX,  -19.52438,  37.10814, 100.85556,
     VERTEX,  -20.00634,  37.52319, 101.57462,
     VERTEX,  -20.15230,  37.50652, 102.52332,
     VERTEX,  -19.90649,  37.06448, 103.33927,
     VERTEX,  -19.36282,  36.36594, 103.71083,
     VERTEX,  -18.72895,  35.67770, 103.49606,
     VERTEX,  -18.24698,  35.26265, 102.77700,
     VERTEX,  -18.10103,  35.27932, 101.82831,
     VERTEX,  -18.34683,  35.72135, 101.01235,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.12666,  36.39292, 102.17581,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   43.29391,  31.69423,  47.72929,
                       
     VERTEX,   40.56469,  36.09624,  47.08250,
     VERTEX,   40.92072,  36.33837,  47.94054,
     VERTEX,   40.86096,  36.16574,  48.88300,
     VERTEX,   40.40825,  35.64430,  49.54989,
     VERTEX,   39.73550,  34.97322,  49.68650,
     VERTEX,   39.09969,  34.40883,  49.24063,
     VERTEX,   38.74366,  34.16670,  48.38259,
     VERTEX,   38.80342,  34.33933,  47.44013,
     VERTEX,   39.25613,  34.86077,  46.77324,
     VERTEX,   39.92888,  35.53185,  46.63663,
     VERTEX,   40.56469,  36.09624,  47.08250,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.83219,  35.25254,  48.16156,
                       
     VERTEX,   40.56469,  36.09624,  47.08250,
     VERTEX,   40.92072,  36.33837,  47.94054,
     VERTEX,   40.86096,  36.16574,  48.88300,
     VERTEX,   40.40825,  35.64430,  49.54989,
     VERTEX,   39.73550,  34.97322,  49.68650,
     VERTEX,   39.09969,  34.40883,  49.24063,
     VERTEX,   38.74366,  34.16670,  48.38259,
     VERTEX,   38.80342,  34.33933,  47.44013,
     VERTEX,   39.25613,  34.86077,  46.77324,
     VERTEX,   39.92888,  35.53185,  46.63663,
     VERTEX,   40.56469,  36.09624,  47.08250,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  39.83219,  35.25254,  48.16156,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.18838,  26.64073,  54.03129,
                       
     VERTEX,   37.13231,  30.68026,  53.36237,
     VERTEX,   37.47018,  30.88312,  54.23775,
     VERTEX,   37.37123,  30.68893,  55.17268,
     VERTEX,   36.87325,  30.17186,  55.81005,
     VERTEX,   36.16644,  29.52941,  55.90641,
     VERTEX,   35.52078,  29.00698,  55.42495,
     VERTEX,   35.18291,  28.80412,  54.54958,
     VERTEX,   35.28186,  28.99831,  53.61465,
     VERTEX,   35.77985,  29.51539,  52.97727,
     VERTEX,   36.48665,  30.15783,  52.88091,
     VERTEX,   37.13231,  30.68026,  53.36237,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.32655,  29.84362,  54.39366,
                       
     VERTEX,   37.13231,  30.68026,  53.36237,
     VERTEX,   37.47018,  30.88312,  54.23775,
     VERTEX,   37.37123,  30.68893,  55.17268,
     VERTEX,   36.87325,  30.17186,  55.81005,
     VERTEX,   36.16644,  29.52941,  55.90641,
     VERTEX,   35.52078,  29.00698,  55.42495,
     VERTEX,   35.18291,  28.80412,  54.54958,
     VERTEX,   35.28186,  28.99831,  53.61465,
     VERTEX,   35.77985,  29.51539,  52.97727,
     VERTEX,   36.48665,  30.15783,  52.88091,
     VERTEX,   37.13231,  30.68026,  53.36237,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  36.32655,  29.84362,  54.39366,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   34.07783,  29.81178,  55.96145,
                       
     VERTEX,   31.60628,  33.16375,  55.01401,
     VERTEX,   31.97202,  33.52510,  55.82472,
     VERTEX,   31.97656,  33.43879,  56.78082,
     VERTEX,   31.61815,  32.93777,  57.51712,
     VERTEX,   31.03371,  32.21342,  57.75236,
     VERTEX,   30.44646,  31.54242,  57.39670,
     VERTEX,   30.08071,  31.18106,  56.58599,
     VERTEX,   30.07618,  31.26738,  55.62989,
     VERTEX,   30.43458,  31.76839,  54.89360,
     VERTEX,   31.01903,  32.49274,  54.65835,
     VERTEX,   31.60628,  33.16375,  55.01401,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.02637,  32.35308,  56.20536,
                       
     VERTEX,   31.60628,  33.16375,  55.01401,
     VERTEX,   31.97202,  33.52510,  55.82472,
     VERTEX,   31.97656,  33.43879,  56.78082,
     VERTEX,   31.61815,  32.93777,  57.51712,
     VERTEX,   31.03371,  32.21342,  57.75236,
     VERTEX,   30.44646,  31.54242,  57.39670,
     VERTEX,   30.08071,  31.18106,  56.58599,
     VERTEX,   30.07618,  31.26738,  55.62989,
     VERTEX,   30.43458,  31.76839,  54.89360,
     VERTEX,   31.01903,  32.49274,  54.65835,
     VERTEX,   31.60628,  33.16375,  55.01401,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  31.02637,  32.35308,  56.20536,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.02585,  41.04387,  48.67210,
                       
     VERTEX,   27.26073,  43.58001,  47.40200,
     VERTEX,   27.57808,  44.20022,  48.06247,
     VERTEX,   27.67857,  44.34623,  49.00597,
     VERTEX,   27.52380,  43.96225,  49.87211,
     VERTEX,   27.17289,  43.19495,  50.33007,
     VERTEX,   26.75988,  42.33742,  50.20491,
     VERTEX,   26.44252,  41.71721,  49.54444,
     VERTEX,   26.34203,  41.57121,  48.60094,
     VERTEX,   26.49680,  41.95518,  47.73480,
     VERTEX,   26.84771,  42.72248,  47.27685,
     VERTEX,   27.26073,  43.58001,  47.40200,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.01030,  42.95871,  48.80346,
                       
     VERTEX,   27.26073,  43.58001,  47.40200,
     VERTEX,   27.57808,  44.20022,  48.06247,
     VERTEX,   27.67857,  44.34623,  49.00597,
     VERTEX,   27.52380,  43.96225,  49.87211,
     VERTEX,   27.17289,  43.19495,  50.33007,
     VERTEX,   26.75988,  42.33742,  50.20491,
     VERTEX,   26.44252,  41.71721,  49.54444,
     VERTEX,   26.34203,  41.57121,  48.60094,
     VERTEX,   26.49680,  41.95518,  47.73480,
     VERTEX,   26.84771,  42.72248,  47.27685,
     VERTEX,   27.26073,  43.58001,  47.40200,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.01030,  42.95871,  48.80346,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.07952,  40.08456,  42.79584,
                       
     VERTEX,   28.56742,  42.85514,  41.59949,
     VERTEX,   28.90673,  43.42030,  42.29738,
     VERTEX,   28.99714,  43.51033,  43.24887,
     VERTEX,   28.80410,  43.09083,  44.09051,
     VERTEX,   28.40136,  42.32204,  44.50083,
     VERTEX,   27.94274,  41.49762,  44.32310,
     VERTEX,   27.60343,  40.93245,  43.62520,
     VERTEX,   27.51302,  40.84242,  42.67372,
     VERTEX,   27.70606,  41.26192,  41.83208,
     VERTEX,   28.10880,  42.03071,  41.42176,
     VERTEX,   28.56742,  42.85514,  41.59949,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.25508,  42.17638,  42.96129,
                       
     VERTEX,   28.56742,  42.85514,  41.59949,
     VERTEX,   28.90673,  43.42030,  42.29738,
     VERTEX,   28.99714,  43.51033,  43.24887,
     VERTEX,   28.80410,  43.09083,  44.09051,
     VERTEX,   28.40136,  42.32204,  44.50083,
     VERTEX,   27.94274,  41.49762,  44.32310,
     VERTEX,   27.60343,  40.93245,  43.62520,
     VERTEX,   27.51302,  40.84242,  42.67372,
     VERTEX,   27.70606,  41.26192,  41.83208,
     VERTEX,   28.10880,  42.03071,  41.42176,
     VERTEX,   28.56742,  42.85514,  41.59949,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  28.25508,  42.17638,  42.96129,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00002_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    4.82800, -71.01700,  51.16800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   19.12200, -75.65200,  45.45200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   17.60300, -72.70100,  40.44700,   0.80000,
                       
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
                       
     SPHERE,   22.27400, -42.36000, 123.38600,   0.80000,
                       
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
