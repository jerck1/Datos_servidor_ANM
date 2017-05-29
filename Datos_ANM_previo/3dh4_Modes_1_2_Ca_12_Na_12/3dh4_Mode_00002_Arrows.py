from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.42897, -77.72475,  46.54327,
                       
     VERTEX,    9.84328, -74.07214,  47.25016,
     VERTEX,   10.42359, -73.93303,  48.00215,
     VERTEX,   10.66091, -74.26358,  48.87164,
     VERTEX,   10.46461, -74.93753,  49.52651,
     VERTEX,    9.90966, -75.69746,  49.71663,
     VERTEX,    9.20803, -76.25309,  49.36936,
     VERTEX,    8.62773, -76.39220,  48.61737,
     VERTEX,    8.39040, -76.06165,  47.74788,
     VERTEX,    8.58671, -75.38770,  47.09301,
     VERTEX,    9.14166, -74.62777,  46.90289,
     VERTEX,    9.84328, -74.07214,  47.25016,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.52566, -75.16261,  48.30976,
                       
     VERTEX,    9.84328, -74.07214,  47.25016,
     VERTEX,   10.42359, -73.93303,  48.00215,
     VERTEX,   10.66091, -74.26358,  48.87164,
     VERTEX,   10.46461, -74.93753,  49.52651,
     VERTEX,    9.90966, -75.69746,  49.71663,
     VERTEX,    9.20803, -76.25309,  49.36936,
     VERTEX,    8.62773, -76.39220,  48.61737,
     VERTEX,    8.39040, -76.06165,  47.74788,
     VERTEX,    8.58671, -75.38770,  47.09301,
     VERTEX,    9.14166, -74.62777,  46.90289,
     VERTEX,    9.84328, -74.07214,  47.25016,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,   9.52566, -75.16261,  48.30976,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.18716, -74.27612,  51.41197,
                       
     VERTEX,   12.12476, -70.89565,  51.93900,
     VERTEX,   12.70125, -70.79898,  52.70052,
     VERTEX,   12.91460, -71.16030,  53.56396,
     VERTEX,   12.68332, -71.84161,  54.19951,
     VERTEX,   12.09574, -72.58266,  54.36443,
     VERTEX,   11.37631, -73.10040,  53.99570,
     VERTEX,   10.79982, -73.19708,  53.23418,
     VERTEX,   10.58647, -72.83576,  52.37074,
     VERTEX,   10.81776, -72.15445,  51.73518,
     VERTEX,   11.40533, -71.41340,  51.57027,
     VERTEX,   12.12476, -70.89565,  51.93900,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.75054, -71.99803,  52.96735,
                       
     VERTEX,   12.12476, -70.89565,  51.93900,
     VERTEX,   12.70125, -70.79898,  52.70052,
     VERTEX,   12.91460, -71.16030,  53.56396,
     VERTEX,   12.68332, -71.84161,  54.19951,
     VERTEX,   12.09574, -72.58266,  54.36443,
     VERTEX,   11.37631, -73.10040,  53.99570,
     VERTEX,   10.79982, -73.19708,  53.23418,
     VERTEX,   10.58647, -72.83576,  52.37074,
     VERTEX,   10.81776, -72.15445,  51.73518,
     VERTEX,   11.40533, -71.41340,  51.57027,
     VERTEX,   12.12476, -70.89565,  51.93900,
                       
     END,              
                       
     CYLINDER,    7.80800, -68.31200,  55.48400,  11.75054, -71.99803,  52.96735,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.32314, -77.95156,  41.82236,
                       
     VERTEX,   24.37738, -76.57722,  41.80134,
     VERTEX,   24.75127, -75.83179,  42.27689,
     VERTEX,   25.14706, -75.56054,  43.10837,
     VERTEX,   25.41359, -75.86707,  43.97820,
     VERTEX,   25.44903, -76.63431,  44.55413,
     VERTEX,   25.23986, -77.56918,  44.61617,
     VERTEX,   24.86597, -78.31462,  44.14063,
     VERTEX,   24.47017, -78.58587,  43.30915,
     VERTEX,   24.20366, -78.27934,  42.43932,
     VERTEX,   24.16821, -77.51210,  41.86339,
     VERTEX,   24.37738, -76.57722,  41.80134,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.80862, -77.07320,  43.20876,
                       
     VERTEX,   24.37738, -76.57722,  41.80134,
     VERTEX,   24.75127, -75.83179,  42.27689,
     VERTEX,   25.14706, -75.56054,  43.10837,
     VERTEX,   25.41359, -75.86707,  43.97820,
     VERTEX,   25.44903, -76.63431,  44.55413,
     VERTEX,   25.23986, -77.56918,  44.61617,
     VERTEX,   24.86597, -78.31462,  44.14063,
     VERTEX,   24.47017, -78.58587,  43.30915,
     VERTEX,   24.20366, -78.27934,  42.43932,
     VERTEX,   24.16821, -77.51210,  41.86339,
     VERTEX,   24.37738, -76.57722,  41.80134,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  24.80862, -77.07320,  43.20876,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.37776, -75.06604,  36.87761,
                       
     VERTEX,   22.60190, -73.62968,  36.84501,
     VERTEX,   22.99620, -72.90290,  37.33278,
     VERTEX,   23.40192, -72.65731,  38.16745,
     VERTEX,   23.66409, -72.98672,  39.03021,
     VERTEX,   23.68257, -73.76530,  39.59152,
     VERTEX,   23.45030, -74.69567,  39.63697,
     VERTEX,   23.05600, -75.42245,  39.14920,
     VERTEX,   22.65028, -75.66804,  38.31453,
     VERTEX,   22.38811, -75.33863,  37.45177,
     VERTEX,   22.36963, -74.56004,  36.89046,
     VERTEX,   22.60190, -73.62968,  36.84501,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.02610, -74.16267,  38.24099,
                       
     VERTEX,   22.60190, -73.62968,  36.84501,
     VERTEX,   22.99620, -72.90290,  37.33278,
     VERTEX,   23.40192, -72.65731,  38.16745,
     VERTEX,   23.66409, -72.98672,  39.03021,
     VERTEX,   23.68257, -73.76530,  39.59152,
     VERTEX,   23.45030, -74.69567,  39.63697,
     VERTEX,   23.05600, -75.42245,  39.14920,
     VERTEX,   22.65028, -75.66804,  38.31453,
     VERTEX,   22.38811, -75.33863,  37.45177,
     VERTEX,   22.36963, -74.56004,  36.89046,
     VERTEX,   22.60190, -73.62968,  36.84501,
                       
     END,              
                       
     CYLINDER,   17.60300, -72.70100,  40.44700,  23.02610, -74.16267,  38.24099,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.43796, -19.04285,  90.62904,
                       
     VERTEX,   36.85793, -19.35001,  91.03847,
     VERTEX,   36.85006, -18.46794,  90.65967,
     VERTEX,   36.68623, -17.96933,  89.85583,
     VERTEX,   36.42901, -18.04464,  88.93401,
     VERTEX,   36.17666, -18.66509,  88.24628,
     VERTEX,   36.02555, -19.59370,  88.05537,
     VERTEX,   36.03342, -20.47577,  88.43417,
     VERTEX,   36.19725, -20.97438,  89.23800,
     VERTEX,   36.45447, -20.89908,  90.15983,
     VERTEX,   36.70683, -20.27862,  90.84755,
     VERTEX,   36.85793, -19.35001,  91.03847,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.44174, -19.47186,  89.54691,
                       
     VERTEX,   36.85793, -19.35001,  91.03847,
     VERTEX,   36.85006, -18.46794,  90.65967,
     VERTEX,   36.68623, -17.96933,  89.85583,
     VERTEX,   36.42901, -18.04464,  88.93401,
     VERTEX,   36.17666, -18.66509,  88.24628,
     VERTEX,   36.02555, -19.59370,  88.05537,
     VERTEX,   36.03342, -20.47577,  88.43417,
     VERTEX,   36.19725, -20.97438,  89.23800,
     VERTEX,   36.45447, -20.89908,  90.15983,
     VERTEX,   36.70683, -20.27862,  90.84755,
     VERTEX,   36.85793, -19.35001,  91.03847,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  36.44174, -19.47186,  89.54691,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   85.18886, -56.91290,  93.38654,
                       
     VERTEX,   82.75661, -63.98801,  92.18529,
     VERTEX,   82.15993, -63.60760,  91.53654,
     VERTEX,   81.33228, -63.13385,  91.42629,
     VERTEX,   80.58981, -62.74770,  91.89664,
     VERTEX,   80.21611, -62.59665,  92.76792,
     VERTEX,   80.35392, -62.73840,  93.70734,
     VERTEX,   80.95061, -63.11880,  94.35608,
     VERTEX,   81.77826, -63.59256,  94.46633,
     VERTEX,   82.52073, -63.97871,  93.99599,
     VERTEX,   82.89443, -64.12975,  93.12471,
     VERTEX,   82.75661, -63.98801,  92.18529,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   81.55527, -63.36320,  92.94631,
                       
     VERTEX,   82.75661, -63.98801,  92.18529,
     VERTEX,   82.15993, -63.60760,  91.53654,
     VERTEX,   81.33228, -63.13385,  91.42629,
     VERTEX,   80.58981, -62.74770,  91.89664,
     VERTEX,   80.21611, -62.59665,  92.76792,
     VERTEX,   80.35392, -62.73840,  93.70734,
     VERTEX,   80.95061, -63.11880,  94.35608,
     VERTEX,   81.77826, -63.59256,  94.46633,
     VERTEX,   82.52073, -63.97871,  93.99599,
     VERTEX,   82.89443, -64.12975,  93.12471,
     VERTEX,   82.75661, -63.98801,  92.18529,
                       
     END,              
                       
     CYLINDER,   75.67600, -73.80000,  92.23400,  81.55527, -63.36320,  92.94631,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   79.56280, -55.42826,  91.18224,
                       
     VERTEX,   77.78928, -61.59970,  90.01289,
     VERTEX,   77.19959, -61.23026,  89.35154,
     VERTEX,   76.36629, -60.77108,  89.22367,
     VERTEX,   75.60764, -60.39755,  89.67814,
     VERTEX,   75.21345, -60.25235,  90.54134,
     VERTEX,   75.33427, -60.39093,  91.48357,
     VERTEX,   75.92394, -60.76037,  92.14493,
     VERTEX,   76.75726, -61.21955,  92.27280,
     VERTEX,   77.51589, -61.59308,  91.81833,
     VERTEX,   77.91010, -61.73829,  90.95512,
     VERTEX,   77.78928, -61.59970,  90.01289,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.56177, -60.99532,  90.74824,
                       
     VERTEX,   77.78928, -61.59970,  90.01289,
     VERTEX,   77.19959, -61.23026,  89.35154,
     VERTEX,   76.36629, -60.77108,  89.22367,
     VERTEX,   75.60764, -60.39755,  89.67814,
     VERTEX,   75.21345, -60.25235,  90.54134,
     VERTEX,   75.33427, -60.39093,  91.48357,
     VERTEX,   75.92394, -60.76037,  92.14493,
     VERTEX,   76.75726, -61.21955,  92.27280,
     VERTEX,   77.51589, -61.59308,  91.81833,
     VERTEX,   77.91010, -61.73829,  90.95512,
     VERTEX,   77.78928, -61.59970,  90.01289,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.56177, -60.99532,  90.74824,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.41209, -74.01594,  91.25115,
                       
     VERTEX,   73.23573, -78.83559,  90.57948,
     VERTEX,   72.68298, -78.10599,  90.29008,
     VERTEX,   72.17340, -77.35044,  90.59187,
     VERTEX,   71.90163, -76.85754,  91.36956,
     VERTEX,   71.97148, -76.81556,  92.32610,
     VERTEX,   72.35628, -77.24054,  93.09612,
     VERTEX,   72.90903, -77.97014,  93.38550,
     VERTEX,   73.41862, -78.72569,  93.08371,
     VERTEX,   73.69038, -79.21858,  92.30603,
     VERTEX,   73.62053, -79.26056,  91.34949,
     VERTEX,   73.23573, -78.83559,  90.57948,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   72.79601, -78.03806,  91.83779,
                       
     VERTEX,   73.23573, -78.83559,  90.57948,
     VERTEX,   72.68298, -78.10599,  90.29008,
     VERTEX,   72.17340, -77.35044,  90.59187,
     VERTEX,   71.90163, -76.85754,  91.36956,
     VERTEX,   71.97148, -76.81556,  92.32610,
     VERTEX,   72.35628, -77.24054,  93.09612,
     VERTEX,   72.90903, -77.97014,  93.38550,
     VERTEX,   73.41862, -78.72569,  93.08371,
     VERTEX,   73.69038, -79.21858,  92.30603,
     VERTEX,   73.62053, -79.26056,  91.34949,
     VERTEX,   73.23573, -78.83559,  90.57948,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  72.79601, -78.03806,  91.83779,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.38808, -77.52886,  95.60651,
                       
     VERTEX,   70.94795, -81.66301,  95.05711,
     VERTEX,   70.45016, -80.86890,  94.84930,
     VERTEX,   70.04015, -80.08788,  95.22813,
     VERTEX,   69.87451, -79.61829,  96.04889,
     VERTEX,   70.01653, -79.63950,  96.99809,
     VERTEX,   70.41194, -80.14339,  97.71317,
     VERTEX,   70.90973, -80.93752,  97.92098,
     VERTEX,   71.31975, -81.71853,  97.54216,
     VERTEX,   71.48538, -82.18811,  96.72139,
     VERTEX,   71.34337, -82.16691,  95.77219,
     VERTEX,   70.94795, -81.66301,  95.05711,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   70.67995, -80.90321,  96.38514,
                       
     VERTEX,   70.94795, -81.66301,  95.05711,
     VERTEX,   70.45016, -80.86890,  94.84930,
     VERTEX,   70.04015, -80.08788,  95.22813,
     VERTEX,   69.87451, -79.61829,  96.04889,
     VERTEX,   70.01653, -79.63950,  96.99809,
     VERTEX,   70.41194, -80.14339,  97.71317,
     VERTEX,   70.90973, -80.93752,  97.92098,
     VERTEX,   71.31975, -81.71853,  97.54216,
     VERTEX,   71.48538, -82.18811,  96.72139,
     VERTEX,   71.34337, -82.16691,  95.77219,
     VERTEX,   70.94795, -81.66301,  95.05711,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  70.67995, -80.90321,  96.38514,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.26084, -55.15295, 121.11671,
                       
     VERTEX,   16.96710, -51.12469, 122.93169,
     VERTEX,   16.29429, -50.69226, 123.46266,
     VERTEX,   15.54174, -50.09719, 123.42864,
     VERTEX,   14.99689, -49.56679, 122.84263,
     VERTEX,   14.86787, -49.30364, 121.92846,
     VERTEX,   15.20395, -49.40826, 121.03532,
     VERTEX,   15.87676, -49.84069, 120.50435,
     VERTEX,   16.62931, -50.43576, 120.53837,
     VERTEX,   17.17416, -50.96616, 121.12438,
     VERTEX,   17.30318, -51.22932, 122.03855,
     VERTEX,   16.96710, -51.12469, 122.93169,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.08553, -50.26648, 121.98351,
                       
     VERTEX,   16.96710, -51.12469, 122.93169,
     VERTEX,   16.29429, -50.69226, 123.46266,
     VERTEX,   15.54174, -50.09719, 123.42864,
     VERTEX,   14.99689, -49.56679, 122.84263,
     VERTEX,   14.86787, -49.30364, 121.92846,
     VERTEX,   15.20395, -49.40826, 121.03532,
     VERTEX,   15.87676, -49.84069, 120.50435,
     VERTEX,   16.62931, -50.43576, 120.53837,
     VERTEX,   17.17416, -50.96616, 121.12438,
     VERTEX,   17.30318, -51.22932, 122.03855,
     VERTEX,   16.96710, -51.12469, 122.93169,
                       
     END,              
                       
     CYLINDER,   22.27400, -42.36000, 123.38600,  16.08553, -50.26648, 121.98351,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.07176,  37.46539,  97.23283,
                       
     VERTEX,  -29.96844,  32.06824,  95.26923,
     VERTEX,  -30.52917,  32.56814,  94.67149,
     VERTEX,  -31.33058,  33.09368,  94.61546,
     VERTEX,  -32.06657,  33.44413,  95.12252,
     VERTEX,  -32.45600,  33.48563,  95.99900,
     VERTEX,  -32.35013,  33.20232,  96.91011,
     VERTEX,  -31.78940,  32.70242,  97.50784,
     VERTEX,  -30.98799,  32.17688,  97.56388,
     VERTEX,  -30.25201,  31.82643,  97.05682,
     VERTEX,  -29.86257,  31.78493,  96.18034,
     VERTEX,  -29.96844,  32.06824,  95.26923,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.15928,  32.63528,  96.08967,
                       
     VERTEX,  -29.96844,  32.06824,  95.26923,
     VERTEX,  -30.52917,  32.56814,  94.67149,
     VERTEX,  -31.33058,  33.09368,  94.61546,
     VERTEX,  -32.06657,  33.44413,  95.12252,
     VERTEX,  -32.45600,  33.48563,  95.99900,
     VERTEX,  -32.35013,  33.20232,  96.91011,
     VERTEX,  -31.78940,  32.70242,  97.50784,
     VERTEX,  -30.98799,  32.17688,  97.56388,
     VERTEX,  -30.25201,  31.82643,  97.05682,
     VERTEX,  -29.86257,  31.78493,  96.18034,
     VERTEX,  -29.96844,  32.06824,  95.26923,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.15928,  32.63528,  96.08967,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.05701,  32.57563,  89.48031,
                       
     VERTEX,  -27.23119,  27.81352,  87.71990,
     VERTEX,  -27.78363,  28.27996,  87.08836,
     VERTEX,  -28.60139,  28.77246,  86.98684,
     VERTEX,  -29.37214,  29.10289,  87.45414,
     VERTEX,  -29.80146,  29.14504,  88.31175,
     VERTEX,  -29.72538,  28.88282,  89.23211,
     VERTEX,  -29.17295,  28.41637,  89.86366,
     VERTEX,  -28.35518,  27.92388,  89.96516,
     VERTEX,  -27.58443,  27.59345,  89.49787,
     VERTEX,  -27.15511,  27.55130,  88.64025,
     VERTEX,  -27.23119,  27.81352,  87.71990,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.47829,  28.34817,  88.47601,
                       
     VERTEX,  -27.23119,  27.81352,  87.71990,
     VERTEX,  -27.78363,  28.27996,  87.08836,
     VERTEX,  -28.60139,  28.77246,  86.98684,
     VERTEX,  -29.37214,  29.10289,  87.45414,
     VERTEX,  -29.80146,  29.14504,  88.31175,
     VERTEX,  -29.72538,  28.88282,  89.23211,
     VERTEX,  -29.17295,  28.41637,  89.86366,
     VERTEX,  -28.35518,  27.92388,  89.96516,
     VERTEX,  -27.58443,  27.59345,  89.49787,
     VERTEX,  -27.15511,  27.55130,  88.64025,
     VERTEX,  -27.23119,  27.81352,  87.71990,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.47829,  28.34817,  88.47601,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.05943,  34.05102,  88.13834,
                       
     VERTEX,  -21.81968,  29.91285,  86.27693,
     VERTEX,  -22.38091,  30.49545,  85.76002,
     VERTEX,  -23.13500,  31.08791,  85.80412,
     VERTEX,  -23.79391,  31.46393,  86.39237,
     VERTEX,  -24.10596,  31.47988,  87.30010,
     VERTEX,  -23.95195,  31.12967,  88.18057,
     VERTEX,  -23.39072,  30.54708,  88.69749,
     VERTEX,  -22.63664,  29.95462,  88.65340,
     VERTEX,  -21.97773,  29.57860,  88.06514,
     VERTEX,  -21.66568,  29.56264,  87.15741,
     VERTEX,  -21.81968,  29.91285,  86.27693,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -22.88582,  30.52126,  87.22875,
                       
     VERTEX,  -21.81968,  29.91285,  86.27693,
     VERTEX,  -22.38091,  30.49545,  85.76002,
     VERTEX,  -23.13500,  31.08791,  85.80412,
     VERTEX,  -23.79391,  31.46393,  86.39237,
     VERTEX,  -24.10596,  31.47988,  87.30010,
     VERTEX,  -23.95195,  31.12967,  88.18057,
     VERTEX,  -23.39072,  30.54708,  88.69749,
     VERTEX,  -22.63664,  29.95462,  88.65340,
     VERTEX,  -21.97773,  29.57860,  88.06514,
     VERTEX,  -21.66568,  29.56264,  87.15741,
     VERTEX,  -21.81968,  29.91285,  86.27693,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -22.88582,  30.52126,  87.22875,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.08439,  41.47910,  97.97996,
                       
     VERTEX,  -16.67285,  37.74953,  95.86469,
     VERTEX,  -17.17005,  38.51707,  95.57269,
     VERTEX,  -17.74519,  39.22752,  95.86610,
     VERTEX,  -18.17859,  39.60949,  96.63282,
     VERTEX,  -18.30470,  39.51709,  97.58000,
     VERTEX,  -18.07535,  38.98561,  98.34586,
     VERTEX,  -17.57815,  38.21806,  98.63785,
     VERTEX,  -17.00301,  37.50761,  98.34444,
     VERTEX,  -16.56961,  37.12565,  97.57772,
     VERTEX,  -16.44350,  37.21805,  96.63054,
     VERTEX,  -16.67285,  37.74953,  95.86469,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.37410,  38.36757,  97.10527,
                       
     VERTEX,  -16.67285,  37.74953,  95.86469,
     VERTEX,  -17.17005,  38.51707,  95.57269,
     VERTEX,  -17.74519,  39.22752,  95.86610,
     VERTEX,  -18.17859,  39.60949,  96.63282,
     VERTEX,  -18.30470,  39.51709,  97.58000,
     VERTEX,  -18.07535,  38.98561,  98.34586,
     VERTEX,  -17.57815,  38.21806,  98.63785,
     VERTEX,  -17.00301,  37.50761,  98.34444,
     VERTEX,  -16.56961,  37.12565,  97.57772,
     VERTEX,  -16.44350,  37.21805,  96.63054,
     VERTEX,  -16.67285,  37.74953,  95.86469,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -17.37410,  38.36757,  97.10527,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -14.75688,  39.40094, 103.46484,
                       
     VERTEX,  -18.04984,  35.55192, 101.37025,
     VERTEX,  -18.56446,  36.29183, 101.03963,
     VERTEX,  -19.17402,  36.98882, 101.29311,
     VERTEX,  -19.64569,  37.37666, 102.03385,
     VERTEX,  -19.79930,  37.30721, 102.97894,
     VERTEX,  -19.57620,  36.80701, 103.76736,
     VERTEX,  -19.06158,  36.06710, 104.09798,
     VERTEX,  -18.45203,  35.37011, 103.84451,
     VERTEX,  -17.98036,  34.98227, 103.10377,
     VERTEX,  -17.82674,  35.05171, 102.15868,
     VERTEX,  -18.04984,  35.55192, 101.37025,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -18.81302,  36.17947, 102.56881,
                       
     VERTEX,  -18.04984,  35.55192, 101.37025,
     VERTEX,  -18.56446,  36.29183, 101.03963,
     VERTEX,  -19.17402,  36.98882, 101.29311,
     VERTEX,  -19.64569,  37.37666, 102.03385,
     VERTEX,  -19.79930,  37.30721, 102.97894,
     VERTEX,  -19.57620,  36.80701, 103.76736,
     VERTEX,  -19.06158,  36.06710, 104.09798,
     VERTEX,  -18.45203,  35.37011, 103.84451,
     VERTEX,  -17.98036,  34.98227, 103.10377,
     VERTEX,  -17.82674,  35.05171, 102.15868,
     VERTEX,  -18.04984,  35.55192, 101.37025,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -18.81302,  36.17947, 102.56881,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   43.19364,  30.12681,  51.12720,
                       
     VERTEX,   40.72731,  34.47854,  50.51725,
     VERTEX,   41.07656,  34.69229,  51.38555,
     VERTEX,   40.99730,  34.50155,  52.32306,
     VERTEX,   40.51980,  33.97918,  52.97170,
     VERTEX,   39.82646,  33.32471,  53.08370,
     VERTEX,   39.18210,  32.78812,  52.61629,
     VERTEX,   38.83286,  32.57437,  51.74799,
     VERTEX,   38.91212,  32.76511,  50.81047,
     VERTEX,   39.38961,  33.28748,  50.16183,
     VERTEX,   40.08295,  33.94195,  50.04984,
     VERTEX,   40.72731,  34.47854,  50.51725,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.95470,  33.63333,  51.56677,
                       
     VERTEX,   40.72731,  34.47854,  50.51725,
     VERTEX,   41.07656,  34.69229,  51.38555,
     VERTEX,   40.99730,  34.50155,  52.32306,
     VERTEX,   40.51980,  33.97918,  52.97170,
     VERTEX,   39.82646,  33.32471,  53.08370,
     VERTEX,   39.18210,  32.78812,  52.61629,
     VERTEX,   38.83286,  32.57437,  51.74799,
     VERTEX,   38.91212,  32.76511,  50.81047,
     VERTEX,   39.38961,  33.28748,  50.16183,
     VERTEX,   40.08295,  33.94195,  50.04984,
     VERTEX,   40.72731,  34.47854,  50.51725,
                       
     END,              
                       
     CYLINDER,   34.71400,  39.30700,  52.27800,  39.95470,  33.63333,  51.56677,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   38.92647,  27.02455,  54.01431,
                       
     VERTEX,   36.95748,  30.92243,  53.34589,
     VERTEX,   37.30075,  31.12729,  54.21870,
     VERTEX,   37.21008,  30.93243,  55.15434,
     VERTEX,   36.72010,  30.41229,  55.79541,
     VERTEX,   36.01796,  29.76555,  55.89706,
     VERTEX,   35.37187,  29.23923,  55.42045,
     VERTEX,   35.02860,  29.03438,  54.54764,
     VERTEX,   35.11927,  29.22923,  53.61200,
     VERTEX,   35.60925,  29.74937,  52.97093,
     VERTEX,   36.31139,  30.39612,  52.86928,
     VERTEX,   36.95748,  30.92243,  53.34589,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.16467,  30.08083,  54.38317,
                       
     VERTEX,   36.95748,  30.92243,  53.34589,
     VERTEX,   37.30075,  31.12729,  54.21870,
     VERTEX,   37.21008,  30.93243,  55.15434,
     VERTEX,   36.72010,  30.41229,  55.79541,
     VERTEX,   36.01796,  29.76555,  55.89706,
     VERTEX,   35.37187,  29.23923,  55.42045,
     VERTEX,   35.02860,  29.03438,  54.54764,
     VERTEX,   35.11927,  29.22923,  53.61200,
     VERTEX,   35.60925,  29.74937,  52.97093,
     VERTEX,   36.31139,  30.39612,  52.86928,
     VERTEX,   36.95748,  30.92243,  53.34589,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  36.16467,  30.08083,  54.38317,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.81628,  30.12804,  56.05894,
                       
     VERTEX,   31.43911,  33.35135,  55.06628,
     VERTEX,   31.80128,  33.72407,  55.87344,
     VERTEX,   31.80573,  33.64778,  56.83039,
     VERTEX,   31.45074,  33.15162,  57.57162,
     VERTEX,   30.87192,  32.42511,  57.81399,
     VERTEX,   30.29035,  31.74575,  57.46494,
     VERTEX,   29.92817,  31.37303,  56.65777,
     VERTEX,   29.92373,  31.44931,  55.70082,
     VERTEX,   30.27871,  31.94547,  54.95959,
     VERTEX,   30.85754,  32.67198,  54.71722,
     VERTEX,   31.43911,  33.35135,  55.06628,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.86473,  32.54855,  56.26561,
                       
     VERTEX,   31.43911,  33.35135,  55.06628,
     VERTEX,   31.80128,  33.72407,  55.87344,
     VERTEX,   31.80573,  33.64778,  56.83039,
     VERTEX,   31.45074,  33.15162,  57.57162,
     VERTEX,   30.87192,  32.42511,  57.81399,
     VERTEX,   30.29035,  31.74575,  57.46494,
     VERTEX,   29.92817,  31.37303,  56.65777,
     VERTEX,   29.92373,  31.44931,  55.70082,
     VERTEX,   30.27871,  31.94547,  54.95959,
     VERTEX,   30.85754,  32.67198,  54.71722,
     VERTEX,   31.43911,  33.35135,  55.06628,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  30.86473,  32.54855,  56.26561,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.66819,  41.39269,  48.95837,
                       
     VERTEX,   27.05324,  43.76649,  47.56886,
     VERTEX,   27.35091,  44.40653,  48.21951,
     VERTEX,   27.43404,  44.57590,  49.16079,
     VERTEX,   27.27089,  44.20990,  50.03315,
     VERTEX,   26.92377,  43.44834,  50.50340,
     VERTEX,   26.52527,  42.58210,  50.39191,
     VERTEX,   26.22761,  41.94206,  49.74126,
     VERTEX,   26.14447,  41.77269,  48.79998,
     VERTEX,   26.30762,  42.13869,  47.92761,
     VERTEX,   26.65474,  42.90025,  47.45736,
     VERTEX,   27.05324,  43.76649,  47.56886,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.78926,  43.17430,  48.98038,
                       
     VERTEX,   27.05324,  43.76649,  47.56886,
     VERTEX,   27.35091,  44.40653,  48.21951,
     VERTEX,   27.43404,  44.57590,  49.16079,
     VERTEX,   27.27089,  44.20990,  50.03315,
     VERTEX,   26.92377,  43.44834,  50.50340,
     VERTEX,   26.52527,  42.58210,  50.39191,
     VERTEX,   26.22761,  41.94206,  49.74126,
     VERTEX,   26.14447,  41.77269,  48.79998,
     VERTEX,   26.30762,  42.13869,  47.92761,
     VERTEX,   26.65474,  42.90025,  47.45736,
     VERTEX,   27.05324,  43.76649,  47.56886,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  26.78926,  43.17430,  48.98038,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.59964,  40.51833,  43.07271,
                       
     VERTEX,   28.28054,  43.09579,  41.75951,
     VERTEX,   28.60188,  43.68189,  42.44859,
     VERTEX,   28.67747,  43.79533,  43.39886,
     VERTEX,   28.47844,  43.39279,  44.24736,
     VERTEX,   28.08081,  42.62801,  44.66998,
     VERTEX,   27.63646,  41.79313,  44.50530,
     VERTEX,   27.31512,  41.20702,  43.81622,
     VERTEX,   27.23953,  41.09358,  42.86595,
     VERTEX,   27.43856,  41.49613,  42.01746,
     VERTEX,   27.83619,  42.26090,  41.59483,
     VERTEX,   28.28054,  43.09579,  41.75951,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.95850,  42.44446,  43.13241,
                       
     VERTEX,   28.28054,  43.09579,  41.75951,
     VERTEX,   28.60188,  43.68189,  42.44859,
     VERTEX,   28.67747,  43.79533,  43.39886,
     VERTEX,   28.47844,  43.39279,  44.24736,
     VERTEX,   28.08081,  42.62801,  44.66998,
     VERTEX,   27.63646,  41.79313,  44.50530,
     VERTEX,   27.31512,  41.20702,  43.81622,
     VERTEX,   27.23953,  41.09358,  42.86595,
     VERTEX,   27.43856,  41.49613,  42.01746,
     VERTEX,   27.83619,  42.26090,  41.59483,
     VERTEX,   28.28054,  43.09579,  41.75951,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  27.95850,  42.44446,  43.13241,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
       ]               
                       
cmd.load_cgo( obj, 'Mode_00002_Arrows') 
                       
obj = [                
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    4.82800, -71.01700,  51.16800,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,    7.80800, -68.31200,  55.48400,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   19.12200, -75.65200,  45.45200,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   17.60300, -72.70100,  40.44700,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   42.92000, -20.16600,  87.79600,   0.80000,
                       
     COLOR,   1.000,  1.000,  1.000,
                       
     SPHERE,   75.67600, -73.80000,  92.23400,   0.80000,
                       
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
                       
     SPHERE,   34.71400,  39.30700,  52.27800,   0.80000,
                       
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