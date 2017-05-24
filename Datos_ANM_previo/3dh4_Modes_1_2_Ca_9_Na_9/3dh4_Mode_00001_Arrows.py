from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.26320, -45.50504,  30.34395,
                       
     VERTEX,   36.14122, -49.87516,  30.16770,
     VERTEX,   35.54398, -49.19361,  29.85087,
     VERTEX,   35.02039, -48.43446,  30.11762,
     VERTEX,   34.77047, -47.88769,  30.86607,
     VERTEX,   34.88965, -47.76214,  31.81033,
     VERTEX,   35.33244, -48.10577,  32.58973,
     VERTEX,   35.92968, -48.78732,  32.90657,
     VERTEX,   36.45326, -49.54647,  32.63981,
     VERTEX,   36.70319, -50.09324,  31.89137,
     VERTEX,   36.58400, -50.21879,  30.94710,
     VERTEX,   36.14122, -49.87516,  30.16770,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.73683, -48.99047,  31.37872,
                       
     VERTEX,   36.14122, -49.87516,  30.16770,
     VERTEX,   35.54398, -49.19361,  29.85087,
     VERTEX,   35.02039, -48.43446,  30.11762,
     VERTEX,   34.77047, -47.88769,  30.86607,
     VERTEX,   34.88965, -47.76214,  31.81033,
     VERTEX,   35.33244, -48.10577,  32.58973,
     VERTEX,   35.92968, -48.78732,  32.90657,
     VERTEX,   36.45326, -49.54647,  32.63981,
     VERTEX,   36.70319, -50.09324,  31.89137,
     VERTEX,   36.58400, -50.21879,  30.94710,
     VERTEX,   36.14122, -49.87516,  30.16770,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  35.73683, -48.99047,  31.37872,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.01313, -66.05025,  35.82254,
                       
     VERTEX,   10.76710, -69.06480,  39.28700,
     VERTEX,   10.22840, -68.27761,  39.17873,
     VERTEX,   10.10922, -67.37157,  39.47283,
     VERTEX,   10.45509, -66.69276,  40.05695,
     VERTEX,   11.13389, -66.50048,  40.70799,
     VERTEX,   11.88635, -66.86815,  41.17727,
     VERTEX,   12.42505, -67.65535,  41.28554,
     VERTEX,   12.54423, -68.56139,  40.99144,
     VERTEX,   12.19836, -69.24019,  40.40732,
     VERTEX,   11.51956, -69.43248,  39.75628,
     VERTEX,   10.76710, -69.06480,  39.28700,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.32672, -67.96648,  40.23214,
                       
     VERTEX,   10.76710, -69.06480,  39.28700,
     VERTEX,   10.22840, -68.27761,  39.17873,
     VERTEX,   10.10922, -67.37157,  39.47283,
     VERTEX,   10.45509, -66.69276,  40.05695,
     VERTEX,   11.13389, -66.50048,  40.70799,
     VERTEX,   11.88635, -66.86815,  41.17727,
     VERTEX,   12.42505, -67.65535,  41.28554,
     VERTEX,   12.54423, -68.56139,  40.99144,
     VERTEX,   12.19836, -69.24019,  40.40732,
     VERTEX,   11.51956, -69.43248,  39.75628,
     VERTEX,   10.76710, -69.06480,  39.28700,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  11.32672, -67.96648,  40.23214,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.45888, -69.54341,  36.23184,
                       
     VERTEX,   25.21141, -72.97139,  38.69300,
     VERTEX,   24.62509, -72.22955,  38.52715,
     VERTEX,   24.37698, -71.35293,  38.82978,
     VERTEX,   24.56186, -70.67637,  39.48528,
     VERTEX,   25.10909, -70.45828,  40.24328,
     VERTEX,   25.80967, -70.78198,  40.81425,
     VERTEX,   26.39599, -71.52382,  40.98011,
     VERTEX,   26.64410, -72.40044,  40.67748,
     VERTEX,   26.45923, -73.07700,  40.02198,
     VERTEX,   25.91199, -73.29508,  39.26397,
     VERTEX,   25.21141, -72.97139,  38.69300,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.51054, -71.87669,  39.75363,
                       
     VERTEX,   25.21141, -72.97139,  38.69300,
     VERTEX,   24.62509, -72.22955,  38.52715,
     VERTEX,   24.37698, -71.35293,  38.82978,
     VERTEX,   24.56186, -70.67637,  39.48528,
     VERTEX,   25.10909, -70.45828,  40.24328,
     VERTEX,   25.80967, -70.78198,  40.81425,
     VERTEX,   26.39599, -71.52382,  40.98011,
     VERTEX,   26.64410, -72.40044,  40.67748,
     VERTEX,   26.45923, -73.07700,  40.02198,
     VERTEX,   25.91199, -73.29508,  39.26397,
     VERTEX,   25.21141, -72.97139,  38.69300,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.51054, -71.87669,  39.75363,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.21760, -61.53944,  27.82878,
                       
     VERTEX,   31.50364, -65.84136,  29.33772,
     VERTEX,   30.88857, -65.14691,  29.09068,
     VERTEX,   30.48753, -64.32481,  29.38209,
     VERTEX,   30.45370, -63.68908,  30.10063,
     VERTEX,   30.80001, -63.48254,  30.97184,
     VERTEX,   31.39417, -63.78408,  31.66296,
     VERTEX,   32.00925, -64.47853,  31.90999,
     VERTEX,   32.41029, -65.30063,  31.61858,
     VERTEX,   32.44411, -65.93636,  30.90004,
     VERTEX,   32.09781, -66.14291,  30.02883,
     VERTEX,   31.50364, -65.84136,  29.33772,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.44891, -64.81272,  30.50034,
                       
     VERTEX,   31.50364, -65.84136,  29.33772,
     VERTEX,   30.88857, -65.14691,  29.09068,
     VERTEX,   30.48753, -64.32481,  29.38209,
     VERTEX,   30.45370, -63.68908,  30.10063,
     VERTEX,   30.80001, -63.48254,  30.97184,
     VERTEX,   31.39417, -63.78408,  31.66296,
     VERTEX,   32.00925, -64.47853,  31.90999,
     VERTEX,   32.41029, -65.30063,  31.61858,
     VERTEX,   32.44411, -65.93636,  30.90004,
     VERTEX,   32.09781, -66.14291,  30.02883,
     VERTEX,   31.50364, -65.84136,  29.33772,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  31.44891, -64.81272,  30.50034,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.10395, -46.25740,  28.44625,
                       
     VERTEX,   18.77954, -50.32589,  29.70199,
     VERTEX,   18.16270, -49.63451,  29.45081,
     VERTEX,   17.75469, -48.81506,  29.74000,
     VERTEX,   17.71137, -48.18055,  30.45911,
     VERTEX,   18.04929, -47.97333,  31.33345,
     VERTEX,   18.63936, -48.27256,  32.02906,
     VERTEX,   19.25621, -48.96394,  32.28024,
     VERTEX,   19.66421, -49.78339,  31.99105,
     VERTEX,   19.70753, -50.41790,  31.27194,
     VERTEX,   19.36962, -50.62512,  30.39760,
     VERTEX,   18.77954, -50.32589,  29.70199,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.70945, -49.29922,  30.86553,
                       
     VERTEX,   18.77954, -50.32589,  29.70199,
     VERTEX,   18.16270, -49.63451,  29.45081,
     VERTEX,   17.75469, -48.81506,  29.74000,
     VERTEX,   17.71137, -48.18055,  30.45911,
     VERTEX,   18.04929, -47.97333,  31.33345,
     VERTEX,   18.63936, -48.27256,  32.02906,
     VERTEX,   19.25621, -48.96394,  32.28024,
     VERTEX,   19.66421, -49.78339,  31.99105,
     VERTEX,   19.70753, -50.41790,  31.27194,
     VERTEX,   19.36962, -50.62512,  30.39760,
     VERTEX,   18.77954, -50.32589,  29.70199,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,  18.70945, -49.29922,  30.86553,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.49530, -43.97092, 124.83535,
                       
     VERTEX,   51.08009, -40.99970, 122.53349,
     VERTEX,   50.64998, -40.21748, 122.88668,
     VERTEX,   49.92321, -39.60432, 122.75466,
     VERTEX,   49.17736, -39.39442, 122.18787,
     VERTEX,   48.69734, -39.66795, 121.40279,
     VERTEX,   48.66649, -40.32045, 120.69929,
     VERTEX,   49.09660, -41.10266, 120.34610,
     VERTEX,   49.82337, -41.71583, 120.47811,
     VERTEX,   50.56921, -41.92573, 121.04491,
     VERTEX,   51.04924, -41.65219, 121.82999,
     VERTEX,   51.08009, -40.99970, 122.53349,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.87329, -40.66007, 121.61639,
                       
     VERTEX,   51.08009, -40.99970, 122.53349,
     VERTEX,   50.64998, -40.21748, 122.88668,
     VERTEX,   49.92321, -39.60432, 122.75466,
     VERTEX,   49.17736, -39.39442, 122.18787,
     VERTEX,   48.69734, -39.66795, 121.40279,
     VERTEX,   48.66649, -40.32045, 120.69929,
     VERTEX,   49.09660, -41.10266, 120.34610,
     VERTEX,   49.82337, -41.71583, 120.47811,
     VERTEX,   50.56921, -41.92573, 121.04491,
     VERTEX,   51.04924, -41.65219, 121.82999,
     VERTEX,   51.08009, -40.99970, 122.53349,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  49.87329, -40.66007, 121.61639,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.96255, -68.34935, 123.02851,
                       
     VERTEX,   34.17321, -65.41165, 124.44221,
     VERTEX,   33.60203, -64.71915, 124.78249,
     VERTEX,   33.02868, -63.99157, 124.53049,
     VERTEX,   32.67216, -63.50684, 123.78247,
     VERTEX,   32.66865, -63.45010, 122.82416,
     VERTEX,   33.01949, -63.84303, 122.02159,
     VERTEX,   33.59067, -64.53553, 121.68131,
     VERTEX,   34.16402, -65.26311, 121.93331,
     VERTEX,   34.52054, -65.74784, 122.68133,
     VERTEX,   34.52405, -65.80458, 123.63965,
     VERTEX,   34.17321, -65.41165, 124.44221,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.59635, -64.62734, 123.23190,
                       
     VERTEX,   34.17321, -65.41165, 124.44221,
     VERTEX,   33.60203, -64.71915, 124.78249,
     VERTEX,   33.02868, -63.99157, 124.53049,
     VERTEX,   32.67216, -63.50684, 123.78247,
     VERTEX,   32.66865, -63.45010, 122.82416,
     VERTEX,   33.01949, -63.84303, 122.02159,
     VERTEX,   33.59067, -64.53553, 121.68131,
     VERTEX,   34.16402, -65.26311, 121.93331,
     VERTEX,   34.52054, -65.74784, 122.68133,
     VERTEX,   34.52405, -65.80458, 123.63965,
     VERTEX,   34.17321, -65.41165, 124.44221,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  33.59635, -64.62734, 123.23190,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.94858, -63.89619, 124.63486,
                       
     VERTEX,   32.24516, -60.86432, 125.85609,
     VERTEX,   31.68046, -60.16841, 126.20022,
     VERTEX,   31.09726, -59.44744, 125.95185,
     VERTEX,   30.71833, -58.97681, 125.20586,
     VERTEX,   30.68839, -58.93627, 124.24718,
     VERTEX,   31.01890, -59.34131, 123.44200,
     VERTEX,   31.58360, -60.03722, 123.09788,
     VERTEX,   32.16679, -60.75819, 123.34624,
     VERTEX,   32.54573, -61.22882, 124.09225,
     VERTEX,   32.57566, -61.26936, 125.05092,
     VERTEX,   32.24516, -60.86432, 125.85609,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.63203, -60.10281, 124.64905,
                       
     VERTEX,   32.24516, -60.86432, 125.85609,
     VERTEX,   31.68046, -60.16841, 126.20022,
     VERTEX,   31.09726, -59.44744, 125.95185,
     VERTEX,   30.71833, -58.97681, 125.20586,
     VERTEX,   30.68839, -58.93627, 124.24718,
     VERTEX,   31.01890, -59.34131, 123.44200,
     VERTEX,   31.58360, -60.03722, 123.09788,
     VERTEX,   32.16679, -60.75819, 123.34624,
     VERTEX,   32.54573, -61.22882, 124.09225,
     VERTEX,   32.57566, -61.26936, 125.05092,
     VERTEX,   32.24516, -60.86432, 125.85609,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  31.63203, -60.10281, 124.64905,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.20547, -54.26502, 126.29074,
                       
     VERTEX,   21.67401, -51.12698, 127.74870,
     VERTEX,   21.10201, -50.43465, 128.08797,
     VERTEX,   20.53063, -49.70585, 127.83504,
     VERTEX,   20.17811, -49.21896, 127.08653,
     VERTEX,   20.17910, -49.15995, 126.12834,
     VERTEX,   20.53323, -49.55136, 125.32648,
     VERTEX,   21.10523, -50.24369, 124.98721,
     VERTEX,   21.67661, -50.97249, 125.24014,
     VERTEX,   22.02913, -51.45938, 125.98866,
     VERTEX,   22.02814, -51.51839, 126.94684,
     VERTEX,   21.67401, -51.12698, 127.74870,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.10362, -50.33917, 126.53759,
                       
     VERTEX,   21.67401, -51.12698, 127.74870,
     VERTEX,   21.10201, -50.43465, 128.08797,
     VERTEX,   20.53063, -49.70585, 127.83504,
     VERTEX,   20.17811, -49.21896, 127.08653,
     VERTEX,   20.17910, -49.15995, 126.12834,
     VERTEX,   20.53323, -49.55136, 125.32648,
     VERTEX,   21.10523, -50.24369, 124.98721,
     VERTEX,   21.67661, -50.97249, 125.24014,
     VERTEX,   22.02913, -51.45938, 125.98866,
     VERTEX,   22.02814, -51.51839, 126.94684,
     VERTEX,   21.67401, -51.12698, 127.74870,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  21.10362, -50.33917, 126.53759,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.81264, -59.54628, 122.60392,
                       
     VERTEX,   21.94540, -56.72239, 124.62762,
     VERTEX,   21.35213, -56.04338, 124.95714,
     VERTEX,   20.80757, -55.29600, 124.69930,
     VERTEX,   20.51971, -54.76573, 123.95260,
     VERTEX,   20.59852, -54.65512, 123.00226,
     VERTEX,   21.01388, -55.00641, 122.21127,
     VERTEX,   21.60714, -55.68542, 121.88175,
     VERTEX,   22.15171, -56.43280, 122.13960,
     VERTEX,   22.43956, -56.96307, 122.88629,
     VERTEX,   22.36076, -57.07368, 123.83663,
     VERTEX,   21.94540, -56.72239, 124.62762,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.47964, -55.86440, 123.41945,
                       
     VERTEX,   21.94540, -56.72239, 124.62762,
     VERTEX,   21.35213, -56.04338, 124.95714,
     VERTEX,   20.80757, -55.29600, 124.69930,
     VERTEX,   20.51971, -54.76573, 123.95260,
     VERTEX,   20.59852, -54.65512, 123.00226,
     VERTEX,   21.01388, -55.00641, 122.21127,
     VERTEX,   21.60714, -55.68542, 121.88175,
     VERTEX,   22.15171, -56.43280, 122.13960,
     VERTEX,   22.43956, -56.96307, 122.88629,
     VERTEX,   22.36076, -57.07368, 123.83663,
     VERTEX,   21.94540, -56.72239, 124.62762,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  21.47964, -55.86440, 123.41945,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.02810,  10.44907, 112.57037,
                       
     VERTEX,    7.37231,   6.85423, 110.98435,
     VERTEX,    6.86342,   7.62078, 110.71043,
     VERTEX,    6.33326,   8.35516, 111.02857,
     VERTEX,    5.98432,   8.77686, 111.81725,
     VERTEX,    5.94990,   8.72480, 112.77522,
     VERTEX,    6.24313,   8.21888, 113.53657,
     VERTEX,    6.75202,   7.45233, 113.81049,
     VERTEX,    7.28218,   6.71795, 113.49235,
     VERTEX,    7.63112,   6.29625, 112.70367,
     VERTEX,    7.66554,   6.34830, 111.74570,
     VERTEX,    7.37231,   6.85423, 110.98435,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.80772,   7.53655, 112.26046,
                       
     VERTEX,    7.37231,   6.85423, 110.98435,
     VERTEX,    6.86342,   7.62078, 110.71043,
     VERTEX,    6.33326,   8.35516, 111.02857,
     VERTEX,    5.98432,   8.77686, 111.81725,
     VERTEX,    5.94990,   8.72480, 112.77522,
     VERTEX,    6.24313,   8.21888, 113.53657,
     VERTEX,    6.75202,   7.45233, 113.81049,
     VERTEX,    7.28218,   6.71795, 113.49235,
     VERTEX,    7.63112,   6.29625, 112.70367,
     VERTEX,    7.66554,   6.34830, 111.74570,
     VERTEX,    7.37231,   6.85423, 110.98435,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,   6.80772,   7.53655, 112.26046,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.82456,   3.98217, 114.29254,
                       
     VERTEX,    6.05485,   0.51813, 112.06400,
     VERTEX,    5.58611,   1.31916, 111.81857,
     VERTEX,    5.04629,   2.03756, 112.15635,
     VERTEX,    4.64159,   2.39893, 112.94833,
     VERTEX,    4.52660,   2.26524, 113.89199,
     VERTEX,    4.74522,   1.68755, 114.62689,
     VERTEX,    5.21397,   0.88653, 114.87232,
     VERTEX,    5.75378,   0.16813, 114.53454,
     VERTEX,    6.15848,  -0.19325, 113.74256,
     VERTEX,    6.27348,  -0.05956, 112.79890,
     VERTEX,    6.05485,   0.51813, 112.06400,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    5.40004,   1.10284, 113.34544,
                       
     VERTEX,    6.05485,   0.51813, 112.06400,
     VERTEX,    5.58611,   1.31916, 111.81857,
     VERTEX,    5.04629,   2.03756, 112.15635,
     VERTEX,    4.64159,   2.39893, 112.94833,
     VERTEX,    4.52660,   2.26524, 113.89199,
     VERTEX,    4.74522,   1.68755, 114.62689,
     VERTEX,    5.21397,   0.88653, 114.87232,
     VERTEX,    5.75378,   0.16813, 114.53454,
     VERTEX,    6.15848,  -0.19325, 113.74256,
     VERTEX,    6.27348,  -0.05956, 112.79890,
     VERTEX,    6.05485,   0.51813, 112.06400,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,   5.40004,   1.10284, 113.34544,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.68056,  -0.49803, 113.79370,
                       
     VERTEX,    7.96262,  -4.00746, 111.37018,
     VERTEX,    7.49632,  -3.20739, 111.11710,
     VERTEX,    6.93825,  -2.49759, 111.44319,
     VERTEX,    6.50155,  -2.14919, 112.22391,
     VERTEX,    6.35305,  -2.29526, 113.16103,
     VERTEX,    6.54945,  -2.88001, 113.89662,
     VERTEX,    7.01575,  -3.68009, 114.14970,
     VERTEX,    7.57383,  -4.38988, 113.82361,
     VERTEX,    8.01052,  -4.73829, 113.04289,
     VERTEX,    8.15902,  -4.59221, 112.10577,
     VERTEX,    7.96262,  -4.00746, 111.37018,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.25604,  -3.44374, 112.63340,
                       
     VERTEX,    7.96262,  -4.00746, 111.37018,
     VERTEX,    7.49632,  -3.20739, 111.11710,
     VERTEX,    6.93825,  -2.49759, 111.44319,
     VERTEX,    6.50155,  -2.14919, 112.22391,
     VERTEX,    6.35305,  -2.29526, 113.16103,
     VERTEX,    6.54945,  -2.88001, 113.89662,
     VERTEX,    7.01575,  -3.68009, 114.14970,
     VERTEX,    7.57383,  -4.38988, 113.82361,
     VERTEX,    8.01052,  -4.73829, 113.04289,
     VERTEX,    8.15902,  -4.59221, 112.10577,
     VERTEX,    7.96262,  -4.00746, 111.37018,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,   7.25604,  -3.44374, 112.63340,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.66258, -10.14830, 111.24204,
                       
     VERTEX,   17.48453, -13.82077, 108.94185,
     VERTEX,   16.98582, -13.06460, 108.62392,
     VERTEX,   16.37524, -12.37141, 108.88525,
     VERTEX,   15.88603, -12.00598, 109.62601,
     VERTEX,   15.70504, -12.10790, 110.56327,
     VERTEX,   15.90141, -12.63824, 111.33902,
     VERTEX,   16.40012, -13.39441, 111.65695,
     VERTEX,   17.01069, -14.08760, 111.39563,
     VERTEX,   17.49990, -14.45302, 110.65486,
     VERTEX,   17.68089, -14.35111, 109.71760,
     VERTEX,   17.48453, -13.82077, 108.94185,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.69297, -13.22950, 110.14043,
                       
     VERTEX,   17.48453, -13.82077, 108.94185,
     VERTEX,   16.98582, -13.06460, 108.62392,
     VERTEX,   16.37524, -12.37141, 108.88525,
     VERTEX,   15.88603, -12.00598, 109.62601,
     VERTEX,   15.70504, -12.10790, 110.56327,
     VERTEX,   15.90141, -12.63824, 111.33902,
     VERTEX,   16.40012, -13.39441, 111.65695,
     VERTEX,   17.01069, -14.08760, 111.39563,
     VERTEX,   17.49990, -14.45302, 110.65486,
     VERTEX,   17.68089, -14.35111, 109.71760,
     VERTEX,   17.48453, -13.82077, 108.94185,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,  16.69297, -13.22950, 110.14043,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.63100,  -3.66734, 110.31813,
                       
     VERTEX,   17.93189,  -7.49248, 108.56303,
     VERTEX,   17.41717,  -6.73827, 108.26666,
     VERTEX,   16.85707,  -6.01628, 108.56099,
     VERTEX,   16.46553,  -5.60230, 109.33359,
     VERTEX,   16.39210,  -5.65444, 110.28935,
     VERTEX,   16.66483,  -6.15279, 111.06322,
     VERTEX,   17.17954,  -6.90700, 111.35959,
     VERTEX,   17.73964,  -7.62899, 111.06526,
     VERTEX,   18.13119,  -8.04297, 110.29266,
     VERTEX,   18.20462,  -7.99083, 109.33689,
     VERTEX,   17.93189,  -7.49248, 108.56303,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.29836,  -6.82263, 109.81313,
                       
     VERTEX,   17.93189,  -7.49248, 108.56303,
     VERTEX,   17.41717,  -6.73827, 108.26666,
     VERTEX,   16.85707,  -6.01628, 108.56099,
     VERTEX,   16.46553,  -5.60230, 109.33359,
     VERTEX,   16.39210,  -5.65444, 110.28935,
     VERTEX,   16.66483,  -6.15279, 111.06322,
     VERTEX,   17.17954,  -6.90700, 111.35959,
     VERTEX,   17.73964,  -7.62899, 111.06526,
     VERTEX,   18.13119,  -8.04297, 110.29266,
     VERTEX,   18.20462,  -7.99083, 109.33689,
     VERTEX,   17.93189,  -7.49248, 108.56303,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  17.29836,  -6.82263, 109.81313,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -2.81557,  26.72462,  20.80776,
                       
     VERTEX,    2.19837,  28.15169,  25.07758,
     VERTEX,    1.80233,  29.02372,  25.14326,
     VERTEX,    1.70272,  29.86720,  24.69579,
     VERTEX,    1.93759,  30.35993,  23.90607,
     VERTEX,    2.41722,  30.31371,  23.07576,
     VERTEX,    2.95841,  29.74621,  22.52200,
     VERTEX,    3.35445,  28.87418,  22.45632,
     VERTEX,    3.45406,  28.03071,  22.90379,
     VERTEX,    3.21920,  27.53798,  23.69351,
     VERTEX,    2.73956,  27.58419,  24.52382,
     VERTEX,    2.19837,  28.15169,  25.07758,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    2.57839,  28.94895,  23.79979,
                       
     VERTEX,    2.19837,  28.15169,  25.07758,
     VERTEX,    1.80233,  29.02372,  25.14326,
     VERTEX,    1.70272,  29.86720,  24.69579,
     VERTEX,    1.93759,  30.35993,  23.90607,
     VERTEX,    2.41722,  30.31371,  23.07576,
     VERTEX,    2.95841,  29.74621,  22.52200,
     VERTEX,    3.35445,  28.87418,  22.45632,
     VERTEX,    3.45406,  28.03071,  22.90379,
     VERTEX,    3.21920,  27.53798,  23.69351,
     VERTEX,    2.73956,  27.58419,  24.52382,
     VERTEX,    2.19837,  28.15169,  25.07758,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,   2.57839,  28.94895,  23.79979,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.66403,  44.16265,  33.98929,
                       
     VERTEX,   26.06396,  43.65934,  40.61035,
     VERTEX,   26.67041,  44.32621,  40.28003,
     VERTEX,   27.43415,  44.47064,  39.71662,
     VERTEX,   28.06347,  44.03746,  39.13531,
     VERTEX,   28.31799,  43.19213,  38.75816,
     VERTEX,   28.10048,  42.25755,  38.72921,
     VERTEX,   27.49403,  41.59068,  39.05952,
     VERTEX,   26.73028,  41.44625,  39.62294,
     VERTEX,   26.10096,  41.87943,  40.20424,
     VERTEX,   25.84645,  42.72476,  40.58140,
     VERTEX,   26.06396,  43.65934,  40.61035,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.08222,  42.95845,  39.66978,
                       
     VERTEX,   26.06396,  43.65934,  40.61035,
     VERTEX,   26.67041,  44.32621,  40.28003,
     VERTEX,   27.43415,  44.47064,  39.71662,
     VERTEX,   28.06347,  44.03746,  39.13531,
     VERTEX,   28.31799,  43.19213,  38.75816,
     VERTEX,   28.10048,  42.25755,  38.72921,
     VERTEX,   27.49403,  41.59068,  39.05952,
     VERTEX,   26.73028,  41.44625,  39.62294,
     VERTEX,   26.10096,  41.87943,  40.20424,
     VERTEX,   25.84645,  42.72476,  40.58140,
     VERTEX,   26.06396,  43.65934,  40.61035,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  27.08222,  42.95845,  39.66978,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.94623,  46.37775,  36.27463,
                       
     VERTEX,   11.64231,  46.32306,  42.23198,
     VERTEX,   11.89302,  47.22211,  42.00734,
     VERTEX,   12.46966,  47.75184,  41.45193,
     VERTEX,   13.15197,  47.70992,  40.77792,
     VERTEX,   13.67933,  47.11236,  40.24274,
     VERTEX,   13.85031,  46.18741,  40.05082,
     VERTEX,   13.59960,  45.28837,  40.27546,
     VERTEX,   13.02296,  44.75864,  40.83087,
     VERTEX,   12.34065,  44.80056,  41.50488,
     VERTEX,   11.81329,  45.39811,  42.04006,
     VERTEX,   11.64231,  46.32306,  42.23198,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.74631,  46.25524,  41.14140,
                       
     VERTEX,   11.64231,  46.32306,  42.23198,
     VERTEX,   11.89302,  47.22211,  42.00734,
     VERTEX,   12.46966,  47.75184,  41.45193,
     VERTEX,   13.15197,  47.70992,  40.77792,
     VERTEX,   13.67933,  47.11236,  40.24274,
     VERTEX,   13.85031,  46.18741,  40.05082,
     VERTEX,   13.59960,  45.28837,  40.27546,
     VERTEX,   13.02296,  44.75864,  40.83087,
     VERTEX,   12.34065,  44.80056,  41.50488,
     VERTEX,   11.81329,  45.39811,  42.04006,
     VERTEX,   11.64231,  46.32306,  42.23198,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  12.74631,  46.25524,  41.14140,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    0.79650,  42.54676,  25.31894,
                       
     VERTEX,    5.77463,  43.25721,  30.98722,
     VERTEX,    5.64254,  44.20436,  30.90322,
     VERTEX,    5.87788,  44.97857,  30.38667,
     VERTEX,    6.39075,  45.28410,  29.63486,
     VERTEX,    6.98527,  45.00426,  28.93497,
     VERTEX,    7.43434,  44.24594,  28.55434,
     VERTEX,    7.56643,  43.29879,  28.63833,
     VERTEX,    7.33109,  42.52459,  29.15489,
     VERTEX,    6.81821,  42.21906,  29.90669,
     VERTEX,    6.22370,  42.49889,  30.60658,
     VERTEX,    5.77463,  43.25721,  30.98722,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.60448,  43.75158,  29.77077,
                       
     VERTEX,    5.77463,  43.25721,  30.98722,
     VERTEX,    5.64254,  44.20436,  30.90322,
     VERTEX,    5.87788,  44.97857,  30.38667,
     VERTEX,    6.39075,  45.28410,  29.63486,
     VERTEX,    6.98527,  45.00426,  28.93497,
     VERTEX,    7.43434,  44.24594,  28.55434,
     VERTEX,    7.56643,  43.29879,  28.63833,
     VERTEX,    7.33109,  42.52459,  29.15489,
     VERTEX,    6.81821,  42.21906,  29.90669,
     VERTEX,    6.22370,  42.49889,  30.60658,
     VERTEX,    5.77463,  43.25721,  30.98722,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,   6.60448,  43.75158,  29.77077,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.46868,  29.13752,  18.89714,
                       
     VERTEX,   18.75621,  29.57522,  24.39719,
     VERTEX,   18.69918,  30.52660,  24.28215,
     VERTEX,   19.01532,  31.26581,  23.75754,
     VERTEX,   19.58387,  31.51051,  23.02374,
     VERTEX,   20.18767,  31.16722,  22.36102,
     VERTEX,   20.59608,  30.36708,  22.02254,
     VERTEX,   20.65311,  29.41570,  22.13758,
     VERTEX,   20.33697,  28.67649,  22.66220,
     VERTEX,   19.76842,  28.43179,  23.39600,
     VERTEX,   19.16462,  28.77508,  24.05871,
     VERTEX,   18.75621,  29.57522,  24.39719,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.67614,  29.97115,  23.20987,
                       
     VERTEX,   18.75621,  29.57522,  24.39719,
     VERTEX,   18.69918,  30.52660,  24.28215,
     VERTEX,   19.01532,  31.26581,  23.75754,
     VERTEX,   19.58387,  31.51051,  23.02374,
     VERTEX,   20.18767,  31.16722,  22.36102,
     VERTEX,   20.59608,  30.36708,  22.02254,
     VERTEX,   20.65311,  29.41570,  22.13758,
     VERTEX,   20.33697,  28.67649,  22.66220,
     VERTEX,   19.76842,  28.43179,  23.39600,
     VERTEX,   19.16462,  28.77508,  24.05871,
     VERTEX,   18.75621,  29.57522,  24.39719,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  19.67614,  29.97115,  23.20987,   0.80000,
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
