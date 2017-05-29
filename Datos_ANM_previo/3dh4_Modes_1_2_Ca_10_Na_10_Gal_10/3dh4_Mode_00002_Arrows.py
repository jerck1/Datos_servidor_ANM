from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.35676, -77.22243,  46.48749,
                       
     VERTEX,    9.70933, -73.76005,  47.19457,
     VERTEX,   10.30766, -73.58471,  47.92455,
     VERTEX,   10.59025, -73.89349,  48.78849,
     VERTEX,   10.44915, -74.56847,  49.45640,
     VERTEX,    9.93827, -75.35179,  49.67317,
     VERTEX,    9.25274, -75.94429,  49.35600,
     VERTEX,    8.65441, -76.11963,  48.62603,
     VERTEX,    8.37182, -75.81084,  47.76208,
     VERTEX,    8.51291, -75.13587,  47.09417,
     VERTEX,    9.02380, -74.35254,  46.87740,
     VERTEX,    9.70933, -73.76005,  47.19457,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.48103, -74.85217,  48.27529,
                       
     VERTEX,    9.70933, -73.76005,  47.19457,
     VERTEX,   10.30766, -73.58471,  47.92455,
     VERTEX,   10.59025, -73.89349,  48.78849,
     VERTEX,   10.44915, -74.56847,  49.45640,
     VERTEX,    9.93827, -75.35179,  49.67317,
     VERTEX,    9.25274, -75.94429,  49.35600,
     VERTEX,    8.65441, -76.11963,  48.62603,
     VERTEX,    8.37182, -75.81084,  47.76208,
     VERTEX,    8.51291, -75.13587,  47.09417,
     VERTEX,    9.02380, -74.35254,  46.87740,
     VERTEX,    9.70933, -73.76005,  47.19457,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,   9.48103, -74.85217,  48.27529,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.31656, -77.20652,  41.46845,
                       
     VERTEX,   24.25447, -76.25713,  41.58158,
     VERTEX,   24.56855, -75.44737,  41.99054,
     VERTEX,   24.97278, -75.08275,  42.78127,
     VERTEX,   25.31275, -75.30253,  43.65173,
     VERTEX,   25.45861, -76.02277,  44.26945,
     VERTEX,   25.35464, -76.96837,  44.39848,
     VERTEX,   25.04055, -77.77812,  43.98952,
     VERTEX,   24.63632, -78.14275,  43.19879,
     VERTEX,   24.29635, -77.92296,  42.32833,
     VERTEX,   24.15049, -77.20271,  41.71061,
     VERTEX,   24.25447, -76.25713,  41.58158,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   24.80455, -76.61275,  42.99003,
                       
     VERTEX,   24.25447, -76.25713,  41.58158,
     VERTEX,   24.56855, -75.44737,  41.99054,
     VERTEX,   24.97278, -75.08275,  42.78127,
     VERTEX,   25.31275, -75.30253,  43.65173,
     VERTEX,   25.45861, -76.02277,  44.26945,
     VERTEX,   25.35464, -76.96837,  44.39848,
     VERTEX,   25.04055, -77.77812,  43.98952,
     VERTEX,   24.63632, -78.14275,  43.19879,
     VERTEX,   24.29635, -77.92296,  42.32833,
     VERTEX,   24.15049, -77.20271,  41.71061,
     VERTEX,   24.25447, -76.25713,  41.58158,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  24.80455, -76.61275,  42.99003,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   30.27337, -74.11752,  37.02044,
                       
     VERTEX,   26.27109, -73.80667,  36.97862,
     VERTEX,   26.45170, -72.92036,  37.30023,
     VERTEX,   26.78432, -72.41816,  38.04773,
     VERTEX,   27.14190, -72.49188,  38.93559,
     VERTEX,   27.38786, -73.11337,  39.62469,
     VERTEX,   27.42824, -74.04524,  39.85181,
     VERTEX,   27.24763, -74.93156,  39.53019,
     VERTEX,   26.91501, -75.43376,  38.78270,
     VERTEX,   26.55743, -75.36004,  37.89483,
     VERTEX,   26.31148, -74.73855,  37.20573,
     VERTEX,   26.27109, -73.80667,  36.97862,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.84967, -73.92596,  38.41521,
                       
     VERTEX,   26.27109, -73.80667,  36.97862,
     VERTEX,   26.45170, -72.92036,  37.30023,
     VERTEX,   26.78432, -72.41816,  38.04773,
     VERTEX,   27.14190, -72.49188,  38.93559,
     VERTEX,   27.38786, -73.11337,  39.62469,
     VERTEX,   27.42824, -74.04524,  39.85181,
     VERTEX,   27.24763, -74.93156,  39.53019,
     VERTEX,   26.91501, -75.43376,  38.78270,
     VERTEX,   26.55743, -75.36004,  37.89483,
     VERTEX,   26.31148, -74.73855,  37.20573,
     VERTEX,   26.27109, -73.80667,  36.97862,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  26.84967, -73.92596,  38.41521,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.92616, -18.97892,  91.50027,
                       
     VERTEX,   36.63105, -19.31922,  91.54972,
     VERTEX,   36.60098, -18.43499,  91.17712,
     VERTEX,   36.38927, -17.93172,  90.38750,
     VERTEX,   36.07678, -18.00163,  89.48248,
     VERTEX,   35.78288, -18.61803,  88.80774,
     VERTEX,   35.61982, -19.54547,  88.62101,
     VERTEX,   35.64989, -20.42970,  88.99361,
     VERTEX,   35.86160, -20.93297,  89.78323,
     VERTEX,   36.17409, -20.86306,  90.68826,
     VERTEX,   36.46799, -20.24666,  91.36299,
     VERTEX,   36.63105, -19.31922,  91.54972,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.12543, -19.43234,  90.08537,
                       
     VERTEX,   36.63105, -19.31922,  91.54972,
     VERTEX,   36.60098, -18.43499,  91.17712,
     VERTEX,   36.38927, -17.93172,  90.38750,
     VERTEX,   36.07678, -18.00163,  89.48248,
     VERTEX,   35.78288, -18.61803,  88.80774,
     VERTEX,   35.61982, -19.54547,  88.62101,
     VERTEX,   35.64989, -20.42970,  88.99361,
     VERTEX,   35.86160, -20.93297,  89.78323,
     VERTEX,   36.17409, -20.86306,  90.68826,
     VERTEX,   36.46799, -20.24666,  91.36299,
     VERTEX,   36.63105, -19.31922,  91.54972,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  36.12543, -19.43234,  90.08537,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.92215, -18.15774,  84.09639,
                       
     VERTEX,   32.28037, -18.22106,  84.36497,
     VERTEX,   32.20649, -17.31308,  84.06215,
     VERTEX,   31.98414, -16.76132,  83.30868,
     VERTEX,   31.69823, -16.77654,  82.39236,
     VERTEX,   31.45798, -17.35292,  81.66321,
     VERTEX,   31.35516, -18.27032,  81.39973,
     VERTEX,   31.42904, -19.17830,  81.70256,
     VERTEX,   31.65139, -19.73006,  82.45603,
     VERTEX,   31.93730, -19.71484,  83.37234,
     VERTEX,   32.17754, -19.13845,  84.10149,
     VERTEX,   32.28037, -18.22106,  84.36497,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.81776, -18.24569,  82.88235,
                       
     VERTEX,   32.28037, -18.22106,  84.36497,
     VERTEX,   32.20649, -17.31308,  84.06215,
     VERTEX,   31.98414, -16.76132,  83.30868,
     VERTEX,   31.69823, -16.77654,  82.39236,
     VERTEX,   31.45798, -17.35292,  81.66321,
     VERTEX,   31.35516, -18.27032,  81.39973,
     VERTEX,   31.42904, -19.17830,  81.70256,
     VERTEX,   31.65139, -19.73006,  82.45603,
     VERTEX,   31.93730, -19.71484,  83.37234,
     VERTEX,   32.17754, -19.13845,  84.10149,
     VERTEX,   32.28037, -18.22106,  84.36497,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  31.81776, -18.24569,  82.88235,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   86.33205, -60.15241,  93.80681,
                       
     VERTEX,   83.23266, -67.05923,  93.48184,
     VERTEX,   82.58146, -66.67253,  92.89193,
     VERTEX,   81.78437, -66.13858,  92.85794,
     VERTEX,   81.14587, -65.66132,  93.39287,
     VERTEX,   80.90984, -65.42306,  94.29237,
     VERTEX,   81.16643, -65.51479,  95.21289,
     VERTEX,   81.81763, -65.90149,  95.80280,
     VERTEX,   82.61472, -66.43545,  95.83679,
     VERTEX,   83.25321, -66.91270,  95.30186,
     VERTEX,   83.48925, -67.15096,  94.40236,
     VERTEX,   83.23266, -67.05923,  93.48184,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   82.19955, -66.28701,  94.34737,
                       
     VERTEX,   83.23266, -67.05923,  93.48184,
     VERTEX,   82.58146, -66.67253,  92.89193,
     VERTEX,   81.78437, -66.13858,  92.85794,
     VERTEX,   81.14587, -65.66132,  93.39287,
     VERTEX,   80.90984, -65.42306,  94.29237,
     VERTEX,   81.16643, -65.51479,  95.21289,
     VERTEX,   81.81763, -65.90149,  95.80280,
     VERTEX,   82.61472, -66.43545,  95.83679,
     VERTEX,   83.25321, -66.91270,  95.30186,
     VERTEX,   83.48925, -67.15096,  94.40236,
     VERTEX,   83.23266, -67.05923,  93.48184,
                       
     END,              
                       
     CYLINDER,   75.51300, -76.21300,  95.22200,  82.19955, -66.28701,  94.34737,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   79.82260, -55.19762,  89.22296,
                       
     VERTEX,   77.89922, -61.53942,  88.79151,
     VERTEX,   77.27085, -61.23147,  88.13430,
     VERTEX,   76.43297, -60.77887,  88.01300,
     VERTEX,   75.70562, -60.35450,  88.47395,
     VERTEX,   75.36662, -60.12045,  89.34107,
     VERTEX,   75.54546, -60.16612,  90.28316,
     VERTEX,   76.17383, -60.47407,  90.94037,
     VERTEX,   77.01170, -60.92667,  91.06167,
     VERTEX,   77.73905, -61.35104,  90.60072,
     VERTEX,   78.07806, -61.58509,  89.73360,
     VERTEX,   77.89922, -61.53942,  88.79151,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.72234, -60.85277,  89.53734,
                       
     VERTEX,   77.89922, -61.53942,  88.79151,
     VERTEX,   77.27085, -61.23147,  88.13430,
     VERTEX,   76.43297, -60.77887,  88.01300,
     VERTEX,   75.70562, -60.35450,  88.47395,
     VERTEX,   75.36662, -60.12045,  89.34107,
     VERTEX,   75.54546, -60.16612,  90.28316,
     VERTEX,   76.17383, -60.47407,  90.94037,
     VERTEX,   77.01170, -60.92667,  91.06167,
     VERTEX,   77.73905, -61.35104,  90.60072,
     VERTEX,   78.07806, -61.58509,  89.73360,
     VERTEX,   77.89922, -61.53942,  88.79151,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.72234, -60.85277,  89.53734,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.78102, -74.08636,  89.19709,
                       
     VERTEX,   73.32760, -78.94888,  89.31594,
     VERTEX,   72.75984, -78.22400,  89.04427,
     VERTEX,   72.29299, -77.44473,  89.35473,
     VERTEX,   72.10537, -76.90871,  90.12874,
     VERTEX,   72.26864, -76.82070,  91.07066,
     VERTEX,   72.72044, -77.21431,  91.82069,
     VERTEX,   73.28819, -77.93919,  92.09236,
     VERTEX,   73.75504, -78.71845,  91.78190,
     VERTEX,   73.94267, -79.25447,  91.00789,
     VERTEX,   73.77940, -79.34248,  90.06598,
     VERTEX,   73.32760, -78.94888,  89.31594,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   73.02402, -78.08159,  90.56831,
                       
     VERTEX,   73.32760, -78.94888,  89.31594,
     VERTEX,   72.75984, -78.22400,  89.04427,
     VERTEX,   72.29299, -77.44473,  89.35473,
     VERTEX,   72.10537, -76.90871,  90.12874,
     VERTEX,   72.26864, -76.82070,  91.07066,
     VERTEX,   72.72044, -77.21431,  91.82069,
     VERTEX,   73.28819, -77.93919,  92.09236,
     VERTEX,   73.75504, -78.71845,  91.78190,
     VERTEX,   73.94267, -79.25447,  91.00789,
     VERTEX,   73.77940, -79.34248,  90.06598,
     VERTEX,   73.32760, -78.94888,  89.31594,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  73.02402, -78.08159,  90.56831,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.96360, -77.70911,  93.54523,
                       
     VERTEX,   71.13767, -81.82385,  93.78928,
     VERTEX,   70.64252, -81.02151,  93.60847,
     VERTEX,   70.29753, -80.21655,  94.00166,
     VERTEX,   70.23447, -79.71640,  94.81866,
     VERTEX,   70.47742, -79.71213,  95.74740,
     VERTEX,   70.93360, -80.20535,  96.43313,
     VERTEX,   71.42876, -81.00769,  96.61394,
     VERTEX,   71.77375, -81.81266,  96.22075,
     VERTEX,   71.83681, -82.31281,  95.40375,
     VERTEX,   71.59385, -82.31708,  94.47501,
     VERTEX,   71.13767, -81.82385,  93.78928,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   71.03564, -81.01460,  95.11121,
                       
     VERTEX,   71.13767, -81.82385,  93.78928,
     VERTEX,   70.64252, -81.02151,  93.60847,
     VERTEX,   70.29753, -80.21655,  94.00166,
     VERTEX,   70.23447, -79.71640,  94.81866,
     VERTEX,   70.47742, -79.71213,  95.74740,
     VERTEX,   70.93360, -80.20535,  96.43313,
     VERTEX,   71.42876, -81.00769,  96.61394,
     VERTEX,   71.77375, -81.81266,  96.22075,
     VERTEX,   71.83681, -82.31281,  95.40375,
     VERTEX,   71.59385, -82.31708,  94.47501,
     VERTEX,   71.13767, -81.82385,  93.78928,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  71.03564, -81.01460,  95.11121,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.63614, -56.40985, 121.98623,
                       
     VERTEX,   18.02672, -51.79492, 123.33150,
     VERTEX,   17.37651, -51.45697, 123.95168,
     VERTEX,   16.55787, -50.96100, 124.02535,
     VERTEX,   15.88346, -50.49646, 123.52436,
     VERTEX,   15.61091, -50.24079, 122.64008,
     VERTEX,   15.84430, -50.29165, 121.71028,
     VERTEX,   16.49451, -50.62961, 121.09010,
     VERTEX,   17.31316, -51.12558, 121.01643,
     VERTEX,   17.98756, -51.59011, 121.51742,
     VERTEX,   18.26012, -51.84578, 122.40170,
     VERTEX,   18.02672, -51.79492, 123.33150,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.93551, -51.04329, 122.52089,
                       
     VERTEX,   18.02672, -51.79492, 123.33150,
     VERTEX,   17.37651, -51.45697, 123.95168,
     VERTEX,   16.55787, -50.96100, 124.02535,
     VERTEX,   15.88346, -50.49646, 123.52436,
     VERTEX,   15.61091, -50.24079, 122.64008,
     VERTEX,   15.84430, -50.29165, 121.71028,
     VERTEX,   16.49451, -50.62961, 121.09010,
     VERTEX,   17.31316, -51.12558, 121.01643,
     VERTEX,   17.98756, -51.59011, 121.51742,
     VERTEX,   18.26012, -51.84578, 122.40170,
     VERTEX,   18.02672, -51.79492, 123.33150,
                       
     END,              
                       
     CYLINDER,   22.27400, -42.36000, 123.38600,  16.93551, -51.04329, 122.52089,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.90058,  38.00520,  95.77695,
                       
     VERTEX,  -30.44248,  32.37952,  94.44498,
     VERTEX,  -31.02364,  32.77545,  93.79146,
     VERTEX,  -31.85226,  33.24527,  93.67208,
     VERTEX,  -32.61185,  33.60953,  94.13245,
     VERTEX,  -33.01226,  33.72909,  94.99673,
     VERTEX,  -32.90056,  33.55828,  95.93478,
     VERTEX,  -32.31940,  33.16235,  96.58831,
     VERTEX,  -31.49078,  32.69254,  96.70769,
     VERTEX,  -30.73119,  32.32828,  96.24731,
     VERTEX,  -30.33078,  32.20872,  95.38304,
     VERTEX,  -30.44248,  32.37952,  94.44498,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.67152,  32.96890,  95.18988,
                       
     VERTEX,  -30.44248,  32.37952,  94.44498,
     VERTEX,  -31.02364,  32.77545,  93.79146,
     VERTEX,  -31.85226,  33.24527,  93.67208,
     VERTEX,  -32.61185,  33.60953,  94.13245,
     VERTEX,  -33.01226,  33.72909,  94.99673,
     VERTEX,  -32.90056,  33.55828,  95.93478,
     VERTEX,  -32.31940,  33.16235,  96.58831,
     VERTEX,  -31.49078,  32.69254,  96.70769,
     VERTEX,  -30.73119,  32.32828,  96.24731,
     VERTEX,  -30.33078,  32.20872,  95.38304,
     VERTEX,  -30.44248,  32.37952,  94.44498,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.67152,  32.96890,  95.18988,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.64924,  33.13745,  88.31242,
                       
     VERTEX,  -27.56173,  28.14753,  87.07039,
     VERTEX,  -28.12870,  28.51351,  86.38760,
     VERTEX,  -28.96902,  28.94896,  86.22681,
     VERTEX,  -29.76170,  29.28756,  86.64944,
     VERTEX,  -30.20397,  29.39997,  87.49405,
     VERTEX,  -30.12689,  29.24326,  88.43803,
     VERTEX,  -29.55992,  28.87728,  89.12081,
     VERTEX,  -28.71960,  28.44183,  89.28160,
     VERTEX,  -27.92692,  28.10323,  88.85898,
     VERTEX,  -27.48465,  27.99082,  88.01437,
     VERTEX,  -27.56173,  28.14753,  87.07039,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.84431,  28.69539,  87.75421,
                       
     VERTEX,  -27.56173,  28.14753,  87.07039,
     VERTEX,  -28.12870,  28.51351,  86.38760,
     VERTEX,  -28.96902,  28.94896,  86.22681,
     VERTEX,  -29.76170,  29.28756,  86.64944,
     VERTEX,  -30.20397,  29.39997,  87.49405,
     VERTEX,  -30.12689,  29.24326,  88.43803,
     VERTEX,  -29.55992,  28.87728,  89.12081,
     VERTEX,  -28.71960,  28.44183,  89.28160,
     VERTEX,  -27.92692,  28.10323,  88.85898,
     VERTEX,  -27.48465,  27.99082,  88.01437,
     VERTEX,  -27.56173,  28.14753,  87.07039,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.84431,  28.69539,  87.75421,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.53533,  34.58716,  87.00050,
                       
     VERTEX,  -22.09185,  30.19565,  85.63264,
     VERTEX,  -22.68581,  30.68884,  85.06203,
     VERTEX,  -23.46851,  31.24458,  85.05044,
     VERTEX,  -24.14099,  31.65060,  85.60227,
     VERTEX,  -24.44637,  31.75182,  86.50676,
     VERTEX,  -24.26802,  31.50958,  87.41841,
     VERTEX,  -23.67406,  31.01640,  87.98901,
     VERTEX,  -22.89137,  30.46066,  88.00061,
     VERTEX,  -22.21889,  30.05463,  87.44878,
     VERTEX,  -21.91351,  29.95341,  86.54429,
     VERTEX,  -22.09185,  30.19565,  85.63264,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -23.17994,  30.85262,  86.52552,
                       
     VERTEX,  -22.09185,  30.19565,  85.63264,
     VERTEX,  -22.68581,  30.68884,  85.06203,
     VERTEX,  -23.46851,  31.24458,  85.05044,
     VERTEX,  -24.14099,  31.65060,  85.60227,
     VERTEX,  -24.44637,  31.75182,  86.50676,
     VERTEX,  -24.26802,  31.50958,  87.41841,
     VERTEX,  -23.67406,  31.01640,  87.98901,
     VERTEX,  -22.89137,  30.46066,  88.00061,
     VERTEX,  -22.21889,  30.05463,  87.44878,
     VERTEX,  -21.91351,  29.95341,  86.54429,
     VERTEX,  -22.09185,  30.19565,  85.63264,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -23.17994,  30.85262,  86.52552,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -13.95339,  42.12344,  96.71278,
                       
     VERTEX,  -17.19330,  38.05703,  95.14098,
     VERTEX,  -17.74700,  38.75198,  94.77757,
     VERTEX,  -18.36341,  39.45221,  95.00413,
     VERTEX,  -18.80708,  39.89024,  95.73411,
     VERTEX,  -18.90855,  39.89878,  96.68870,
     VERTEX,  -18.62905,  39.47455,  97.50326,
     VERTEX,  -18.07535,  38.77960,  97.86667,
     VERTEX,  -17.45894,  38.07938,  97.64011,
     VERTEX,  -17.01527,  37.64134,  96.91013,
     VERTEX,  -16.91381,  37.63281,  95.95554,
     VERTEX,  -17.19330,  38.05703,  95.14098,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -17.91118,  38.76579,  96.32211,
                       
     VERTEX,  -17.19330,  38.05703,  95.14098,
     VERTEX,  -17.74700,  38.75198,  94.77757,
     VERTEX,  -18.36341,  39.45221,  95.00413,
     VERTEX,  -18.80708,  39.89024,  95.73411,
     VERTEX,  -18.90855,  39.89878,  96.68870,
     VERTEX,  -18.62905,  39.47455,  97.50326,
     VERTEX,  -18.07535,  38.77960,  97.86667,
     VERTEX,  -17.45894,  38.07938,  97.64011,
     VERTEX,  -17.01527,  37.64134,  96.91013,
     VERTEX,  -16.91381,  37.63281,  95.95554,
     VERTEX,  -17.19330,  38.05703,  95.14098,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -17.91118,  38.76579,  96.32211,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -15.71628,  40.17789, 102.20344,
                       
     VERTEX,  -18.60035,  35.94669, 100.66875,
     VERTEX,  -19.17327,  36.59628, 100.25475,
     VERTEX,  -19.83508,  37.27007, 100.42686,
     VERTEX,  -20.33298,  37.71069, 101.11935,
     VERTEX,  -20.47679,  37.74986, 102.06770,
     VERTEX,  -20.21158,  37.37260, 102.90969,
     VERTEX,  -19.63866,  36.72302, 103.32369,
     VERTEX,  -18.97686,  36.04923, 103.15158,
     VERTEX,  -18.47896,  35.60860, 102.45909,
     VERTEX,  -18.33514,  35.56944, 101.51073,
     VERTEX,  -18.60035,  35.94669, 100.66875,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.40597,  36.65965, 101.78922,
                       
     VERTEX,  -18.60035,  35.94669, 100.66875,
     VERTEX,  -19.17327,  36.59628, 100.25475,
     VERTEX,  -19.83508,  37.27007, 100.42686,
     VERTEX,  -20.33298,  37.71069, 101.11935,
     VERTEX,  -20.47679,  37.74986, 102.06770,
     VERTEX,  -20.21158,  37.37260, 102.90969,
     VERTEX,  -19.63866,  36.72302, 103.32369,
     VERTEX,  -18.97686,  36.04923, 103.15158,
     VERTEX,  -18.47896,  35.60860, 102.45909,
     VERTEX,  -18.33514,  35.56944, 101.51073,
     VERTEX,  -18.60035,  35.94669, 100.66875,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.40597,  36.65965, 101.78922,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   43.93973,  31.04758,  47.82003,
                       
     VERTEX,   40.97155,  35.68722,  47.13657,
     VERTEX,   41.32059,  35.93767,  47.99508,
     VERTEX,   41.25356,  35.77376,  48.93861,
     VERTEX,   40.79608,  35.25811,  49.60675,
     VERTEX,   40.12288,  34.58768,  49.74430,
     VERTEX,   39.49110,  34.01855,  49.29873,
     VERTEX,   39.14206,  33.76810,  48.44021,
     VERTEX,   39.20908,  33.93201,  47.49668,
     VERTEX,   39.66656,  34.44765,  46.82854,
     VERTEX,   40.33977,  35.11809,  46.69099,
     VERTEX,   40.97155,  35.68722,  47.13657,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.23132,  34.85288,  48.21764,
                       
     VERTEX,   40.97155,  35.68722,  47.13657,
     VERTEX,   41.32059,  35.93767,  47.99508,
     VERTEX,   41.25356,  35.77376,  48.93861,
     VERTEX,   40.79608,  35.25811,  49.60675,
     VERTEX,   40.12288,  34.58768,  49.74430,
     VERTEX,   39.49110,  34.01855,  49.29873,
     VERTEX,   39.14206,  33.76810,  48.44021,
     VERTEX,   39.20908,  33.93201,  47.49668,
     VERTEX,   39.66656,  34.44765,  46.82854,
     VERTEX,   40.33977,  35.11809,  46.69099,
     VERTEX,   40.97155,  35.68722,  47.13657,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  40.23132,  34.85288,  48.21764,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   39.70749,  26.00283,  54.13015,
                       
     VERTEX,   37.46785,  30.27475,  53.42600,
     VERTEX,   37.79630,  30.48372,  54.30353,
     VERTEX,   37.68589,  30.29761,  55.23882,
     VERTEX,   37.17881,  29.78750,  55.87463,
     VERTEX,   36.46874,  29.14824,  55.96810,
     VERTEX,   35.82690,  28.62400,  55.48352,
     VERTEX,   35.49845,  28.41502,  54.60600,
     VERTEX,   35.60885,  28.60114,  53.67070,
     VERTEX,   36.11593,  29.11125,  53.03489,
     VERTEX,   36.82600,  29.75051,  52.94143,
     VERTEX,   37.46785,  30.27475,  53.42600,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.64737,  29.44938,  54.45476,
                       
     VERTEX,   37.46785,  30.27475,  53.42600,
     VERTEX,   37.79630,  30.48372,  54.30353,
     VERTEX,   37.68589,  30.29761,  55.23882,
     VERTEX,   37.17881,  29.78750,  55.87463,
     VERTEX,   36.46874,  29.14824,  55.96810,
     VERTEX,   35.82690,  28.62400,  55.48352,
     VERTEX,   35.49845,  28.41502,  54.60600,
     VERTEX,   35.60885,  28.60114,  53.67070,
     VERTEX,   36.11593,  29.11125,  53.03489,
     VERTEX,   36.82600,  29.75051,  52.94143,
     VERTEX,   37.46785,  30.27475,  53.42600,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  36.64737,  29.44938,  54.45476,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   34.62020,  29.28641,  55.98874,
                       
     VERTEX,   31.95569,  32.83550,  55.03547,
     VERTEX,   32.31664,  33.19518,  55.84908,
     VERTEX,   32.31278,  33.10918,  56.80521,
     VERTEX,   31.94559,  32.61036,  57.53866,
     VERTEX,   31.35533,  31.88924,  57.76927,
     VERTEX,   30.76746,  31.22127,  57.40896,
     VERTEX,   30.40651,  30.86160,  56.59536,
     VERTEX,   30.41037,  30.94760,  55.63923,
     VERTEX,   30.77755,  31.44642,  54.90578,
     VERTEX,   31.36781,  32.16754,  54.67516,
     VERTEX,   31.95569,  32.83550,  55.03547,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.36157,  32.02839,  56.22222,
                       
     VERTEX,   31.95569,  32.83550,  55.03547,
     VERTEX,   32.31664,  33.19518,  55.84908,
     VERTEX,   32.31278,  33.10918,  56.80521,
     VERTEX,   31.94559,  32.61036,  57.53866,
     VERTEX,   31.35533,  31.88924,  57.76927,
     VERTEX,   30.76746,  31.22127,  57.40896,
     VERTEX,   30.40651,  30.86160,  56.59536,
     VERTEX,   30.41037,  30.94760,  55.63923,
     VERTEX,   30.77755,  31.44642,  54.90578,
     VERTEX,   31.36781,  32.16754,  54.67516,
     VERTEX,   31.95569,  32.83550,  55.03547,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  31.36157,  32.02839,  56.22222,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.76515,  40.53743,  48.54005,
                       
     VERTEX,   27.72097,  43.28319,  47.32829,
     VERTEX,   28.04720,  43.89066,  47.99624,
     VERTEX,   28.15190,  44.02259,  48.94135,
     VERTEX,   27.99507,  43.62861,  49.80262,
     VERTEX,   27.63661,  42.85920,  50.25107,
     VERTEX,   27.21345,  42.00824,  50.11541,
     VERTEX,   26.88721,  41.40078,  49.44746,
     VERTEX,   26.78252,  41.26884,  48.50235,
     VERTEX,   26.93935,  41.66282,  47.64108,
     VERTEX,   27.29781,  42.43223,  47.19263,
     VERTEX,   27.72097,  43.28319,  47.32829,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.46721,  42.64571,  48.72185,
                       
     VERTEX,   27.72097,  43.28319,  47.32829,
     VERTEX,   28.04720,  43.89066,  47.99624,
     VERTEX,   28.15190,  44.02259,  48.94135,
     VERTEX,   27.99507,  43.62861,  49.80262,
     VERTEX,   27.63661,  42.85920,  50.25107,
     VERTEX,   27.21345,  42.00824,  50.11541,
     VERTEX,   26.88721,  41.40078,  49.44746,
     VERTEX,   26.78252,  41.26884,  48.50235,
     VERTEX,   26.93935,  41.66282,  47.64108,
     VERTEX,   27.29781,  42.43223,  47.19263,
     VERTEX,   27.72097,  43.28319,  47.32829,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.46721,  42.64571,  48.72185,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.88143,  39.50908,  42.69449,
                       
     VERTEX,   29.07015,  42.51118,  41.54442,
     VERTEX,   29.41499,  43.06521,  42.24851,
     VERTEX,   29.50609,  43.14387,  43.20093,
     VERTEX,   29.30865,  42.71713,  44.03790,
     VERTEX,   28.89808,  41.94799,  44.43971,
     VERTEX,   28.43122,  41.13023,  44.25289,
     VERTEX,   28.08638,  40.57620,  43.54880,
     VERTEX,   27.99528,  40.49754,  42.59637,
     VERTEX,   28.19272,  40.92428,  41.75941,
     VERTEX,   28.60329,  41.69342,  41.35760,
     VERTEX,   29.07015,  42.51118,  41.54442,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.75068,  41.82071,  42.89865,
                       
     VERTEX,   29.07015,  42.51118,  41.54442,
     VERTEX,   29.41499,  43.06521,  42.24851,
     VERTEX,   29.50609,  43.14387,  43.20093,
     VERTEX,   29.30865,  42.71713,  44.03790,
     VERTEX,   28.89808,  41.94799,  44.43971,
     VERTEX,   28.43122,  41.13023,  44.25289,
     VERTEX,   28.08638,  40.57620,  43.54880,
     VERTEX,   27.99528,  40.49754,  42.59637,
     VERTEX,   28.19272,  40.92428,  41.75941,
     VERTEX,   28.60329,  41.69342,  41.35760,
     VERTEX,   29.07015,  42.51118,  41.54442,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  28.75068,  41.82071,  42.89865,   0.80000,
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