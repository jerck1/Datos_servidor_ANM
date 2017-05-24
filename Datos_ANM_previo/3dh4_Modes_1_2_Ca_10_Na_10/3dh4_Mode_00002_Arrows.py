from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.38038, -77.25737,  46.52237,
                       
     VERTEX,    9.73035, -73.78423,  47.21489,
     VERTEX,   10.32593, -73.60845,  47.94700,
     VERTEX,   10.60436, -73.91598,  48.81274,
     VERTEX,   10.45930, -74.58934,  49.48143,
     VERTEX,    9.94614, -75.37135,  49.69764,
     VERTEX,    9.26091, -75.96329,  49.37880,
     VERTEX,    8.66533, -76.13906,  48.64669,
     VERTEX,    8.38690, -75.83154,  47.78094,
     VERTEX,    8.53196, -75.15817,  47.11226,
     VERTEX,    9.04511, -74.37617,  46.89605,
     VERTEX,    9.73035, -73.78423,  47.21489,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.49563, -74.87376,  48.29684,
                       
     VERTEX,    9.73035, -73.78423,  47.21489,
     VERTEX,   10.32593, -73.60845,  47.94700,
     VERTEX,   10.60436, -73.91598,  48.81274,
     VERTEX,   10.45930, -74.58934,  49.48143,
     VERTEX,    9.94614, -75.37135,  49.69764,
     VERTEX,    9.26091, -75.96329,  49.37880,
     VERTEX,    8.66533, -76.13906,  48.64669,
     VERTEX,    8.38690, -75.83154,  47.78094,
     VERTEX,    8.53196, -75.15817,  47.11226,
     VERTEX,    9.04511, -74.37617,  46.89605,
     VERTEX,    9.73035, -73.78423,  47.21489,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,   9.49563, -74.87376,  48.29684,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.33133, -77.25690,  41.48979,
                       
     VERTEX,   24.27116, -76.27865,  41.59430,
     VERTEX,   24.58945, -75.47280,  42.00770,
     VERTEX,   24.99339, -75.11427,  42.80135,
     VERTEX,   25.32869, -75.34000,  43.67211,
     VERTEX,   25.46727, -76.06377,  44.28738,
     VERTEX,   25.35620, -77.00912,  44.41214,
     VERTEX,   25.03791, -77.81497,  43.99874,
     VERTEX,   24.63396, -78.17351,  43.20508,
     VERTEX,   24.29867, -77.94778,  42.33432,
     VERTEX,   24.16009, -77.22400,  41.71906,
     VERTEX,   24.27116, -76.27865,  41.59430,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.81368, -76.64388,  43.00322,
                       
     VERTEX,   24.27116, -76.27865,  41.59430,
     VERTEX,   24.58945, -75.47280,  42.00770,
     VERTEX,   24.99339, -75.11427,  42.80135,
     VERTEX,   25.32869, -75.34000,  43.67211,
     VERTEX,   25.46727, -76.06377,  44.28738,
     VERTEX,   25.35620, -77.00912,  44.41214,
     VERTEX,   25.03791, -77.81497,  43.99874,
     VERTEX,   24.63396, -78.17351,  43.20508,
     VERTEX,   24.29867, -77.94778,  42.33432,
     VERTEX,   24.16009, -77.22400,  41.71906,
     VERTEX,   24.27116, -76.27865,  41.59430,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  24.81368, -76.64388,  43.00322,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.28188, -74.17529,  37.03687,
                       
     VERTEX,   26.28087, -73.82905,  36.98813,
     VERTEX,   26.46845, -72.94622,  37.31528,
     VERTEX,   26.80366, -72.45126,  38.06644,
     VERTEX,   27.15845, -72.53322,  38.95471,
     VERTEX,   27.39730, -73.16080,  39.64078,
     VERTEX,   27.42898, -74.09428,  39.86260,
     VERTEX,   27.24140, -74.97711,  39.53545,
     VERTEX,   26.90619, -75.47207,  38.78428,
     VERTEX,   26.55140, -75.39011,  37.89602,
     VERTEX,   26.31255, -74.76253,  37.20995,
     VERTEX,   26.28087, -73.82905,  36.98813,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.85492, -73.96166,  38.42537,
                       
     VERTEX,   26.28087, -73.82905,  36.98813,
     VERTEX,   26.46845, -72.94622,  37.31528,
     VERTEX,   26.80366, -72.45126,  38.06644,
     VERTEX,   27.15845, -72.53322,  38.95471,
     VERTEX,   27.39730, -73.16080,  39.64078,
     VERTEX,   27.42898, -74.09428,  39.86260,
     VERTEX,   27.24140, -74.97711,  39.53545,
     VERTEX,   26.90619, -75.47207,  38.78428,
     VERTEX,   26.55140, -75.39011,  37.89602,
     VERTEX,   26.31255, -74.76253,  37.20995,
     VERTEX,   26.28087, -73.82905,  36.98813,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  26.85492, -73.96166,  38.42537,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.92282, -18.98827,  91.43483,
                       
     VERTEX,   36.62093, -19.32506,  91.51203,
     VERTEX,   36.59236, -18.44075,  91.13949,
     VERTEX,   36.38465, -17.93741,  90.34885,
     VERTEX,   36.07714, -18.00729,  89.44212,
     VERTEX,   35.78729, -18.62370,  88.76564,
     VERTEX,   35.62581, -19.55119,  88.57780,
     VERTEX,   35.65438, -20.43549,  88.95035,
     VERTEX,   35.86208, -20.93884,  89.74098,
     VERTEX,   36.16959, -20.86896,  90.64771,
     VERTEX,   36.45944, -20.25255,  91.32419,
     VERTEX,   36.62093, -19.32506,  91.51203,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.12337, -19.43812,  90.04491,
                       
     VERTEX,   36.62093, -19.32506,  91.51203,
     VERTEX,   36.59236, -18.44075,  91.13949,
     VERTEX,   36.38465, -17.93741,  90.34885,
     VERTEX,   36.07714, -18.00729,  89.44212,
     VERTEX,   35.78729, -18.62370,  88.76564,
     VERTEX,   35.62581, -19.55119,  88.57780,
     VERTEX,   35.65438, -20.43549,  88.95035,
     VERTEX,   35.86208, -20.93884,  89.74098,
     VERTEX,   36.16959, -20.86896,  90.64771,
     VERTEX,   36.45944, -20.25255,  91.32419,
     VERTEX,   36.62093, -19.32506,  91.51203,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  36.12337, -19.43812,  90.04491,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.91503, -18.18011,  84.02710,
                       
     VERTEX,   32.26639, -18.23711,  84.32514,
     VERTEX,   32.19304, -17.32864,  84.02363,
     VERTEX,   31.97467, -16.77574,  83.26983,
     VERTEX,   31.69469, -16.78959,  82.35167,
     VERTEX,   31.46003, -17.36490,  81.61986,
     VERTEX,   31.36034, -18.28193,  81.35391,
     VERTEX,   31.43368, -19.19040,  81.65543,
     VERTEX,   31.65206, -19.74330,  82.40923,
     VERTEX,   31.93204, -19.72945,  83.32738,
     VERTEX,   32.16669, -19.15413,  84.05920,
     VERTEX,   32.26639, -18.23711,  84.32514,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.81336, -18.25952,  82.83952,
                       
     VERTEX,   32.26639, -18.23711,  84.32514,
     VERTEX,   32.19304, -17.32864,  84.02363,
     VERTEX,   31.97467, -16.77574,  83.26983,
     VERTEX,   31.69469, -16.78959,  82.35167,
     VERTEX,   31.46003, -17.36490,  81.61986,
     VERTEX,   31.36034, -18.28193,  81.35391,
     VERTEX,   31.43368, -19.19040,  81.65543,
     VERTEX,   31.65206, -19.74330,  82.40923,
     VERTEX,   31.93204, -19.72945,  83.32738,
     VERTEX,   32.16669, -19.15413,  84.05920,
     VERTEX,   32.26639, -18.23711,  84.32514,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  31.81336, -18.25952,  82.83952,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   86.31799, -60.13285,  93.92662,
                       
     VERTEX,   83.22875, -67.04197,  93.55701,
     VERTEX,   82.57967, -66.65343,  92.96597,
     VERTEX,   81.78208, -66.12032,  92.93085,
     VERTEX,   81.14063, -65.64626,  93.46507,
     VERTEX,   80.90032, -65.41233,  94.36459,
     VERTEX,   81.15295, -65.50787,  95.28581,
     VERTEX,   81.80203, -65.89641,  95.87686,
     VERTEX,   82.59963, -66.42952,  95.91197,
     VERTEX,   83.24109, -66.90358,  95.37775,
     VERTEX,   83.48139, -67.13751,  94.47823,
     VERTEX,   83.22875, -67.04197,  93.55701,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   82.19086, -66.27493,  94.42141,
                       
     VERTEX,   83.22875, -67.04197,  93.55701,
     VERTEX,   82.57967, -66.65343,  92.96597,
     VERTEX,   81.78208, -66.12032,  92.93085,
     VERTEX,   81.14063, -65.64626,  93.46507,
     VERTEX,   80.90032, -65.41233,  94.36459,
     VERTEX,   81.15295, -65.50787,  95.28581,
     VERTEX,   81.80203, -65.89641,  95.87686,
     VERTEX,   82.59963, -66.42952,  95.91197,
     VERTEX,   83.24109, -66.90358,  95.37775,
     VERTEX,   83.48139, -67.13751,  94.47823,
     VERTEX,   83.22875, -67.04197,  93.55701,
                       
     END,              
                       
     CYLINDER,   75.51300, -76.21300,  95.22200,  82.19086, -66.27493,  94.42141,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   79.81275, -55.19206,  89.31977,
                       
     VERTEX,   77.89610, -61.53165,  88.85206,
     VERTEX,   77.26971, -61.22106,  88.19421,
     VERTEX,   76.43192, -60.76847,  88.07224,
     VERTEX,   75.70273, -60.34678,  88.53275,
     VERTEX,   75.36067, -60.11704,  89.39982,
     VERTEX,   75.53640, -60.16701,  90.34227,
     VERTEX,   76.16280, -60.47761,  91.00012,
     VERTEX,   77.00058, -60.93019,  91.12209,
     VERTEX,   77.72977, -61.35189,  90.66159,
     VERTEX,   78.07182, -61.58163,  89.79452,
     VERTEX,   77.89610, -61.53165,  88.85206,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.71625, -60.84933,  89.59717,
                       
     VERTEX,   77.89610, -61.53165,  88.85206,
     VERTEX,   77.26971, -61.22106,  88.19421,
     VERTEX,   76.43192, -60.76847,  88.07224,
     VERTEX,   75.70273, -60.34678,  88.53275,
     VERTEX,   75.36067, -60.11704,  89.39982,
     VERTEX,   75.53640, -60.16701,  90.34227,
     VERTEX,   76.16280, -60.47761,  91.00012,
     VERTEX,   77.00058, -60.93019,  91.12209,
     VERTEX,   77.72977, -61.35189,  90.66159,
     VERTEX,   78.07182, -61.58163,  89.79452,
     VERTEX,   77.89610, -61.53165,  88.85206,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.71625, -60.84933,  89.59717,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.77095, -74.07486,  89.33081,
                       
     VERTEX,   73.33002, -78.93729,  89.39762,
     VERTEX,   72.76325, -78.21206,  89.12483,
     VERTEX,   72.29370, -77.43428,  89.43497,
     VERTEX,   72.10073, -76.90104,  90.20958,
     VERTEX,   72.25805, -76.81601,  91.15278,
     VERTEX,   72.70557, -77.21167,  91.90430,
     VERTEX,   73.27234, -77.93690,  92.17709,
     VERTEX,   73.74189, -78.71468,  91.86694,
     VERTEX,   73.93486, -79.24792,  91.09234,
     VERTEX,   73.77754, -79.33295,  90.14914,
     VERTEX,   73.33002, -78.93729,  89.39762,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   73.01779, -78.07448,  90.65096,
                       
     VERTEX,   73.33002, -78.93729,  89.39762,
     VERTEX,   72.76325, -78.21206,  89.12483,
     VERTEX,   72.29370, -77.43428,  89.43497,
     VERTEX,   72.10073, -76.90104,  90.20958,
     VERTEX,   72.25805, -76.81601,  91.15278,
     VERTEX,   72.70557, -77.21167,  91.90430,
     VERTEX,   73.27234, -77.93690,  92.17709,
     VERTEX,   73.74189, -78.71468,  91.86694,
     VERTEX,   73.93486, -79.24792,  91.09234,
     VERTEX,   73.77754, -79.33295,  90.14914,
     VERTEX,   73.33002, -78.93729,  89.39762,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  73.01779, -78.07448,  90.65096,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.94852, -77.68309,  93.68248,
                       
     VERTEX,   71.13956, -81.80472,  93.87315,
     VERTEX,   70.64407, -81.00302,  93.69049,
     VERTEX,   70.29458, -80.19961,  94.08289,
     VERTEX,   70.22459, -79.70135,  94.90047,
     VERTEX,   70.46084, -79.69857,  95.83095,
     VERTEX,   70.91308, -80.19233,  96.51891,
     VERTEX,   71.40858, -80.99403,  96.70156,
     VERTEX,   71.75806, -81.79744,  96.30916,
     VERTEX,   71.82805, -82.29569,  95.49158,
     VERTEX,   71.59180, -82.29848,  94.56110,
     VERTEX,   71.13956, -81.80472,  93.87315,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   71.02632, -80.99852,  95.19602,
                       
     VERTEX,   71.13956, -81.80472,  93.87315,
     VERTEX,   70.64407, -81.00302,  93.69049,
     VERTEX,   70.29458, -80.19961,  94.08289,
     VERTEX,   70.22459, -79.70135,  94.90047,
     VERTEX,   70.46084, -79.69857,  95.83095,
     VERTEX,   70.91308, -80.19233,  96.51891,
     VERTEX,   71.40858, -80.99403,  96.70156,
     VERTEX,   71.75806, -81.79744,  96.30916,
     VERTEX,   71.82805, -82.29569,  95.49158,
     VERTEX,   71.59180, -82.29848,  94.56110,
     VERTEX,   71.13956, -81.80472,  93.87315,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  71.02632, -80.99852,  95.19602,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.60919, -56.30304, 121.94926,
                       
     VERTEX,   18.00168, -51.73436, 123.31480,
     VERTEX,   17.34988, -51.39283, 123.93134,
     VERTEX,   16.53344, -50.89257, 124.00040,
     VERTEX,   15.86421, -50.42467, 123.49561,
     VERTEX,   15.59782, -50.16785, 122.60979,
     VERTEX,   15.83602, -50.22020, 121.68129,
     VERTEX,   16.48782, -50.56172, 121.06476,
     VERTEX,   17.30426, -51.06198, 120.99570,
     VERTEX,   17.97349, -51.52988, 121.50047,
     VERTEX,   18.23988, -51.78671, 122.38630,
     VERTEX,   18.00168, -51.73436, 123.31480,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.91885, -50.97728, 122.49805,
                       
     VERTEX,   18.00168, -51.73436, 123.31480,
     VERTEX,   17.34988, -51.39283, 123.93134,
     VERTEX,   16.53344, -50.89257, 124.00040,
     VERTEX,   15.86421, -50.42467, 123.49561,
     VERTEX,   15.59782, -50.16785, 122.60979,
     VERTEX,   15.83602, -50.22020, 121.68129,
     VERTEX,   16.48782, -50.56172, 121.06476,
     VERTEX,   17.30426, -51.06198, 120.99570,
     VERTEX,   17.97349, -51.52988, 121.50047,
     VERTEX,   18.23988, -51.78671, 122.38630,
     VERTEX,   18.00168, -51.73436, 123.31480,
                       
     END,              
                       
     CYLINDER,   22.27400, -42.36000, 123.38600,  16.91885, -50.97728, 122.49805,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.83669,  38.05591,  95.83597,
                       
     VERTEX,  -30.40424,  32.41151,  94.47890,
     VERTEX,  -30.98478,  32.81109,  93.82706,
     VERTEX,  -31.81255,  33.28293,  93.70969,
     VERTEX,  -32.57137,  33.64679,  94.17165,
     VERTEX,  -32.97139,  33.76369,  95.03647,
     VERTEX,  -32.85983,  33.58898,  95.97382,
     VERTEX,  -32.27929,  33.18939,  96.62567,
     VERTEX,  -31.45152,  32.71756,  96.74303,
     VERTEX,  -30.69270,  32.35370,  96.28107,
     VERTEX,  -30.29268,  32.23680,  95.41626,
     VERTEX,  -30.40424,  32.41151,  94.47890,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.63203,  33.00024,  95.22636,
                       
     VERTEX,  -30.40424,  32.41151,  94.47890,
     VERTEX,  -30.98478,  32.81109,  93.82706,
     VERTEX,  -31.81255,  33.28293,  93.70969,
     VERTEX,  -32.57137,  33.64679,  94.17165,
     VERTEX,  -32.97139,  33.76369,  95.03647,
     VERTEX,  -32.85983,  33.58898,  95.97382,
     VERTEX,  -32.27929,  33.18939,  96.62567,
     VERTEX,  -31.45152,  32.71756,  96.74303,
     VERTEX,  -30.69270,  32.35370,  96.28107,
     VERTEX,  -30.29268,  32.23680,  95.41626,
     VERTEX,  -30.40424,  32.41151,  94.47890,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.63203,  33.00024,  95.22636,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.59944,  33.19044,  88.36412,
                       
     VERTEX,  -27.53171,  28.18097,  87.10036,
     VERTEX,  -28.09814,  28.55028,  86.41891,
     VERTEX,  -28.93782,  28.98753,  86.25971,
     VERTEX,  -29.73003,  29.32570,  86.68356,
     VERTEX,  -30.17216,  29.43563,  87.52856,
     VERTEX,  -30.09534,  29.27533,  88.47196,
     VERTEX,  -29.52891,  28.90602,  89.15341,
     VERTEX,  -28.68923,  28.46876,  89.31261,
     VERTEX,  -27.89703,  28.13059,  88.88876,
     VERTEX,  -27.45489,  28.02066,  88.04375,
     VERTEX,  -27.53171,  28.18097,  87.10036,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.81353,  28.72815,  87.78616,
                       
     VERTEX,  -27.53171,  28.18097,  87.10036,
     VERTEX,  -28.09814,  28.55028,  86.41891,
     VERTEX,  -28.93782,  28.98753,  86.25971,
     VERTEX,  -29.73003,  29.32570,  86.68356,
     VERTEX,  -30.17216,  29.43563,  87.52856,
     VERTEX,  -30.09534,  29.27533,  88.47196,
     VERTEX,  -29.52891,  28.90602,  89.15341,
     VERTEX,  -28.68923,  28.46876,  89.31261,
     VERTEX,  -27.89703,  28.13059,  88.88876,
     VERTEX,  -27.45489,  28.02066,  88.04375,
     VERTEX,  -27.53171,  28.18097,  87.10036,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.81353,  28.72815,  87.78616,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.48255,  34.63253,  87.04437,
                       
     VERTEX,  -22.05950,  30.22525,  85.65828,
     VERTEX,  -22.65249,  30.72105,  85.08893,
     VERTEX,  -23.43449,  31.27780,  85.07867,
     VERTEX,  -24.10679,  31.68286,  85.63142,
     VERTEX,  -24.41261,  31.78151,  86.53605,
     VERTEX,  -24.23513,  31.53606,  87.44701,
     VERTEX,  -23.64214,  31.04027,  88.01636,
     VERTEX,  -22.86015,  30.48351,  88.02661,
     VERTEX,  -22.18784,  30.07845,  87.47386,
     VERTEX,  -21.88202,  29.97980,  86.56924,
     VERTEX,  -22.05950,  30.22525,  85.65828,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -23.14732,  30.88066,  86.55264,
                       
     VERTEX,  -22.05950,  30.22525,  85.65828,
     VERTEX,  -22.65249,  30.72105,  85.08893,
     VERTEX,  -23.43449,  31.27780,  85.07867,
     VERTEX,  -24.10679,  31.68286,  85.63142,
     VERTEX,  -24.41261,  31.78151,  86.53605,
     VERTEX,  -24.23513,  31.53606,  87.44701,
     VERTEX,  -23.64214,  31.04027,  88.01636,
     VERTEX,  -22.86015,  30.48351,  88.02661,
     VERTEX,  -22.18784,  30.07845,  87.47386,
     VERTEX,  -21.88202,  29.97980,  86.56924,
     VERTEX,  -22.05950,  30.22525,  85.65828,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -23.14732,  30.88066,  86.55264,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.87958,  42.16167,  96.76055,
                       
     VERTEX,  -17.14688,  38.08329,  95.16941,
     VERTEX,  -17.69918,  38.78002,  94.80729,
     VERTEX,  -18.31503,  39.48034,  95.03506,
     VERTEX,  -18.75920,  39.91675,  95.76572,
     VERTEX,  -18.86203,  39.92255,  96.72018,
     VERTEX,  -18.58424,  39.49554,  97.53387,
     VERTEX,  -18.03194,  38.79881,  97.89599,
     VERTEX,  -17.41608,  38.09849,  97.66821,
     VERTEX,  -16.97191,  37.66208,  96.93756,
     VERTEX,  -16.86908,  37.65628,  95.98310,
     VERTEX,  -17.14688,  38.08329,  95.16941,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.86556,  38.78941,  96.35164,
                       
     VERTEX,  -17.14688,  38.08329,  95.16941,
     VERTEX,  -17.69918,  38.78002,  94.80729,
     VERTEX,  -18.31503,  39.48034,  95.03506,
     VERTEX,  -18.75920,  39.91675,  95.76572,
     VERTEX,  -18.86203,  39.92255,  96.72018,
     VERTEX,  -18.58424,  39.49554,  97.53387,
     VERTEX,  -18.03194,  38.79881,  97.89599,
     VERTEX,  -17.41608,  38.09849,  97.66821,
     VERTEX,  -16.97191,  37.66208,  96.93756,
     VERTEX,  -16.86908,  37.65628,  95.98310,
     VERTEX,  -17.14688,  38.08329,  95.16941,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -17.86556,  38.78941,  96.35164,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -15.63817,  40.21421, 102.25238,
                       
     VERTEX,  -18.55246,  35.97170, 100.69710,
     VERTEX,  -19.12380,  36.62387, 100.28497,
     VERTEX,  -19.78448,  37.29827, 100.45898,
     VERTEX,  -20.28214,  37.73732, 101.15264,
     VERTEX,  -20.42669,  37.77330, 102.10101,
     VERTEX,  -20.16292,  37.39248, 102.94185,
     VERTEX,  -19.59158,  36.74031, 103.35397,
     VERTEX,  -18.93090,  36.06591, 103.17996,
     VERTEX,  -18.43324,  35.62686, 102.48630,
     VERTEX,  -18.28868,  35.59088, 101.53793,
     VERTEX,  -18.55246,  35.97170, 100.69710,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.35769,  36.68209, 101.81947,
                       
     VERTEX,  -18.55246,  35.97170, 100.69710,
     VERTEX,  -19.12380,  36.62387, 100.28497,
     VERTEX,  -19.78448,  37.29827, 100.45898,
     VERTEX,  -20.28214,  37.73732, 101.15264,
     VERTEX,  -20.42669,  37.77330, 102.10101,
     VERTEX,  -20.16292,  37.39248, 102.94185,
     VERTEX,  -19.59158,  36.74031, 103.35397,
     VERTEX,  -18.93090,  36.06591, 103.17996,
     VERTEX,  -18.43324,  35.62686, 102.48630,
     VERTEX,  -18.28868,  35.59088, 101.53793,
     VERTEX,  -18.55246,  35.97170, 100.69710,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.35769,  36.68209, 101.81947,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   43.93526,  31.06489,  47.80400,
                       
     VERTEX,   40.96679,  35.69890,  47.12605,
     VERTEX,   41.31679,  35.94921,  47.98421,
     VERTEX,   41.25112,  35.78485,  48.92776,
     VERTEX,   40.79487,  35.26860,  49.59628,
     VERTEX,   40.12231,  34.59764,  49.73442,
     VERTEX,   39.49034,  34.02827,  49.28942,
     VERTEX,   39.14034,  33.77796,  48.43126,
     VERTEX,   39.20601,  33.94232,  47.48772,
     VERTEX,   39.66225,  34.45857,  46.81920,
     VERTEX,   40.33482,  35.12952,  46.68105,
     VERTEX,   40.96679,  35.69890,  47.12605,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.22856,  34.86359,  48.20774,
                       
     VERTEX,   40.96679,  35.69890,  47.12605,
     VERTEX,   41.31679,  35.94921,  47.98421,
     VERTEX,   41.25112,  35.78485,  48.92776,
     VERTEX,   40.79487,  35.26860,  49.59628,
     VERTEX,   40.12231,  34.59764,  49.73442,
     VERTEX,   39.49034,  34.02827,  49.28942,
     VERTEX,   39.14034,  33.77796,  48.43126,
     VERTEX,   39.20601,  33.94232,  47.48772,
     VERTEX,   39.66225,  34.45857,  46.81920,
     VERTEX,   40.33482,  35.12952,  46.68105,
     VERTEX,   40.96679,  35.69890,  47.12605,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  40.22856,  34.86359,  48.20774,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.71959,  26.00885,  54.11272,
                       
     VERTEX,   37.47258,  30.27977,  53.41408,
     VERTEX,   37.80231,  30.48883,  54.29110,
     VERTEX,   37.69376,  30.30227,  55.22652,
     VERTEX,   37.18838,  29.79135,  55.86304,
     VERTEX,   36.47921,  29.15123,  55.95753,
     VERTEX,   35.83713,  28.62642,  55.47390,
     VERTEX,   35.50739,  28.41736,  54.59688,
     VERTEX,   35.61594,  28.60392,  53.66146,
     VERTEX,   36.12133,  29.11484,  53.02494,
     VERTEX,   36.83049,  29.75496,  52.93045,
     VERTEX,   37.47258,  30.27977,  53.41408,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.65485,  29.45309,  54.44399,
                       
     VERTEX,   37.47258,  30.27977,  53.41408,
     VERTEX,   37.80231,  30.48883,  54.29110,
     VERTEX,   37.69376,  30.30227,  55.22652,
     VERTEX,   37.18838,  29.79135,  55.86304,
     VERTEX,   36.47921,  29.15123,  55.95753,
     VERTEX,   35.83713,  28.62642,  55.47390,
     VERTEX,   35.50739,  28.41736,  54.59688,
     VERTEX,   35.61594,  28.60392,  53.66146,
     VERTEX,   36.12133,  29.11484,  53.02494,
     VERTEX,   36.83049,  29.75496,  52.93045,
     VERTEX,   37.47258,  30.27977,  53.41408,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  36.65485,  29.45309,  54.44399,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   34.63647,  29.28867,  55.98619,
                       
     VERTEX,   31.96383,  32.83672,  55.03281,
     VERTEX,   32.32504,  33.19741,  55.84586,
     VERTEX,   32.32207,  33.11209,  56.80206,
     VERTEX,   31.95608,  32.61338,  57.53617,
     VERTEX,   31.36684,  31.89175,  57.76780,
     VERTEX,   30.77943,  31.22284,  57.40847,
     VERTEX,   30.41823,  30.86216,  56.59542,
     VERTEX,   30.42119,  30.94747,  55.63923,
     VERTEX,   30.78718,  31.44619,  54.90511,
     VERTEX,   31.37642,  32.16782,  54.67348,
     VERTEX,   31.96383,  32.83672,  55.03281,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.37163,  32.02979,  56.22064,
                       
     VERTEX,   31.96383,  32.83672,  55.03281,
     VERTEX,   32.32504,  33.19741,  55.84586,
     VERTEX,   32.32207,  33.11209,  56.80206,
     VERTEX,   31.95608,  32.61338,  57.53617,
     VERTEX,   31.36684,  31.89175,  57.76780,
     VERTEX,   30.77943,  31.22284,  57.40847,
     VERTEX,   30.41823,  30.86216,  56.59542,
     VERTEX,   30.42119,  30.94747,  55.63923,
     VERTEX,   30.78718,  31.44619,  54.90511,
     VERTEX,   31.37642,  32.16782,  54.67348,
     VERTEX,   31.96383,  32.83672,  55.03281,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  31.37163,  32.02979,  56.22064,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.75965,  40.54902,  48.56480,
                       
     VERTEX,   27.71919,  43.28854,  47.34305,
     VERTEX,   28.04404,  43.89717,  48.01061,
     VERTEX,   28.14727,  44.03053,  48.95568,
     VERTEX,   27.98944,  43.63766,  49.81728,
     VERTEX,   27.63083,  42.86865,  50.26630,
     VERTEX,   27.20843,  42.01722,  50.13124,
     VERTEX,   26.88358,  41.40859,  49.46368,
     VERTEX,   26.78035,  41.27523,  48.51861,
     VERTEX,   26.93818,  41.66809,  47.65701,
     VERTEX,   27.29679,  42.43710,  47.20798,
     VERTEX,   27.71919,  43.28854,  47.34305,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.46381,  42.65288,  48.73714,
                       
     VERTEX,   27.71919,  43.28854,  47.34305,
     VERTEX,   28.04404,  43.89717,  48.01061,
     VERTEX,   28.14727,  44.03053,  48.95568,
     VERTEX,   27.98944,  43.63766,  49.81728,
     VERTEX,   27.63083,  42.86865,  50.26630,
     VERTEX,   27.20843,  42.01722,  50.13124,
     VERTEX,   26.88358,  41.40859,  49.46368,
     VERTEX,   26.78035,  41.27523,  48.51861,
     VERTEX,   26.93818,  41.66809,  47.65701,
     VERTEX,   27.29679,  42.43710,  47.20798,
     VERTEX,   27.71919,  43.28854,  47.34305,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.46381,  42.65288,  48.73714,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.86183,  39.53006,  42.71467,
                       
     VERTEX,   29.05888,  42.52254,  41.55626,
     VERTEX,   29.40261,  43.07778,  42.25994,
     VERTEX,   29.49270,  43.15781,  43.21235,
     VERTEX,   29.29474,  42.73207,  44.04970,
     VERTEX,   28.88434,  41.96317,  44.45215,
     VERTEX,   28.41827,  41.14481,  44.26598,
     VERTEX,   28.07454,  40.58957,  43.56231,
     VERTEX,   27.98444,  40.50954,  42.60990,
     VERTEX,   28.18240,  40.93528,  41.77255,
     VERTEX,   28.59280,  41.70418,  41.37010,
     VERTEX,   29.05888,  42.52254,  41.55626,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.73857,  41.83368,  42.91113,
                       
     VERTEX,   29.05888,  42.52254,  41.55626,
     VERTEX,   29.40261,  43.07778,  42.25994,
     VERTEX,   29.49270,  43.15781,  43.21235,
     VERTEX,   29.29474,  42.73207,  44.04970,
     VERTEX,   28.88434,  41.96317,  44.45215,
     VERTEX,   28.41827,  41.14481,  44.26598,
     VERTEX,   28.07454,  40.58957,  43.56231,
     VERTEX,   27.98444,  40.50954,  42.60990,
     VERTEX,   28.18240,  40.93528,  41.77255,
     VERTEX,   28.59280,  41.70418,  41.37010,
     VERTEX,   29.05888,  42.52254,  41.55626,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  28.73857,  41.83368,  42.91113,   0.80000,
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
