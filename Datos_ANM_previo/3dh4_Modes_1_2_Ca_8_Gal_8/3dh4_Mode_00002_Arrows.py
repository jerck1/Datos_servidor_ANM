from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   13.20734, -76.84161,  45.43795,
                       
     VERTEX,   10.00000, -73.53241,  46.51452,
     VERTEX,   10.63868, -73.26956,  47.18130,
     VERTEX,   11.03597, -73.52132,  48.01819,
     VERTEX,   11.04012, -74.19151,  48.70552,
     VERTEX,   10.64955, -75.02415,  48.98075,
     VERTEX,   10.01343, -75.70121,  48.73876,
     VERTEX,    9.37476, -75.96406,  48.07197,
     VERTEX,    8.97747, -75.71230,  47.23508,
     VERTEX,    8.97332, -75.04211,  46.54776,
     VERTEX,    9.36389, -74.20946,  46.27253,
     VERTEX,   10.00000, -73.53241,  46.51452,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   10.00672, -74.61681,  47.62664,
                       
     VERTEX,   10.00000, -73.53241,  46.51452,
     VERTEX,   10.63868, -73.26956,  47.18130,
     VERTEX,   11.03597, -73.52132,  48.01819,
     VERTEX,   11.04012, -74.19151,  48.70552,
     VERTEX,   10.64955, -75.02415,  48.98075,
     VERTEX,   10.01343, -75.70121,  48.73876,
     VERTEX,    9.37476, -75.96406,  48.07197,
     VERTEX,    8.97747, -75.71230,  47.23508,
     VERTEX,    8.97332, -75.04211,  46.54776,
     VERTEX,    9.36389, -74.20946,  46.27253,
     VERTEX,   10.00000, -73.53241,  46.51452,
                       
     END,              
                       
     CYLINDER,    4.82800, -71.01700,  51.16800,  10.00672, -74.61681,  47.62664,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.35033, -76.14605,  40.32942,
                       
     VERTEX,   24.75376, -75.84900,  40.89850,
     VERTEX,   24.94916, -74.95975,  41.20290,
     VERTEX,   25.33337, -74.45155,  41.92103,
     VERTEX,   25.75962, -74.51851,  42.77860,
     VERTEX,   26.06511, -75.13506,  43.44804,
     VERTEX,   26.13315, -76.06568,  43.67365,
     VERTEX,   25.93775, -76.95493,  43.36925,
     VERTEX,   25.55354, -77.46313,  42.65111,
     VERTEX,   25.12729, -77.39617,  41.79354,
     VERTEX,   24.82180, -76.77962,  41.12411,
     VERTEX,   24.75376, -75.84900,  40.89850,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.44345, -75.95734,  42.28607,
                       
     VERTEX,   24.75376, -75.84900,  40.89850,
     VERTEX,   24.94916, -74.95975,  41.20290,
     VERTEX,   25.33337, -74.45155,  41.92103,
     VERTEX,   25.75962, -74.51851,  42.77860,
     VERTEX,   26.06511, -75.13506,  43.44804,
     VERTEX,   26.13315, -76.06568,  43.67365,
     VERTEX,   25.93775, -76.95493,  43.36925,
     VERTEX,   25.55354, -77.46313,  42.65111,
     VERTEX,   25.12729, -77.39617,  41.79354,
     VERTEX,   24.82180, -76.77962,  41.12411,
     VERTEX,   24.75376, -75.84900,  40.89850,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.44345, -75.95734,  42.28607,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.26303, -72.81232,  35.98794,
                       
     VERTEX,   26.81598, -73.29683,  36.37538,
     VERTEX,   26.83487, -72.35834,  36.57655,
     VERTEX,   27.09305, -71.71050,  37.23630,
     VERTEX,   27.49189, -71.60078,  38.10260,
     VERTEX,   27.87905, -72.07108,  38.84458,
     VERTEX,   28.10665, -72.94176,  39.17881,
     VERTEX,   28.08775, -73.88026,  38.97763,
     VERTEX,   27.82957, -74.52809,  38.31789,
     VERTEX,   27.43074, -74.63782,  37.45158,
     VERTEX,   27.04358, -74.16752,  36.70961,
     VERTEX,   26.81598, -73.29683,  36.37538,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.46131, -73.11930,  37.77709,
                       
     VERTEX,   26.81598, -73.29683,  36.37538,
     VERTEX,   26.83487, -72.35834,  36.57655,
     VERTEX,   27.09305, -71.71050,  37.23630,
     VERTEX,   27.49189, -71.60078,  38.10260,
     VERTEX,   27.87905, -72.07108,  38.84458,
     VERTEX,   28.10665, -72.94176,  39.17881,
     VERTEX,   28.08775, -73.88026,  38.97763,
     VERTEX,   27.82957, -74.52809,  38.31789,
     VERTEX,   27.43074, -74.63782,  37.45158,
     VERTEX,   27.04358, -74.16752,  36.70961,
     VERTEX,   26.81598, -73.29683,  36.37538,
                       
     END,              
                       
     CYLINDER,   21.31000, -73.61600,  40.67200,  27.46131, -73.11930,  37.77709,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.32832, -18.97732,  92.59583,
                       
     VERTEX,   36.35756, -19.33376,  92.19120,
     VERTEX,   36.30003, -18.44527,  91.83221,
     VERTEX,   36.03467, -17.93343,  91.06462,
     VERTEX,   35.66285, -17.99374,  90.18161,
     VERTEX,   35.32659, -18.60318,  89.52045,
     VERTEX,   35.15433, -19.52895,  89.33371,
     VERTEX,   35.21186, -20.41744,  89.69270,
     VERTEX,   35.47722, -20.92928,  90.46029,
     VERTEX,   35.84904, -20.86897,  91.34331,
     VERTEX,   36.18530, -20.25953,  92.00446,
     VERTEX,   36.35756, -19.33376,  92.19120,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.75595, -19.43135,  90.76246,
                       
     VERTEX,   36.35756, -19.33376,  92.19120,
     VERTEX,   36.30003, -18.44527,  91.83221,
     VERTEX,   36.03467, -17.93343,  91.06462,
     VERTEX,   35.66285, -17.99374,  90.18161,
     VERTEX,   35.32659, -18.60318,  89.52045,
     VERTEX,   35.15433, -19.52895,  89.33371,
     VERTEX,   35.21186, -20.41744,  89.69270,
     VERTEX,   35.47722, -20.92928,  90.46029,
     VERTEX,   35.84904, -20.86897,  91.34331,
     VERTEX,   36.18530, -20.25953,  92.00446,
     VERTEX,   36.35756, -19.33376,  92.19120,
                       
     END,              
                       
     CYLINDER,   42.92000, -20.16600,  87.79600,  35.75595, -19.43135,  90.76246,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.04827, -17.95588,  85.25777,
                       
     VERTEX,   31.84562, -18.08248,  85.04537,
     VERTEX,   31.75976, -17.17769,  84.73621,
     VERTEX,   31.48975, -16.63319,  83.99309,
     VERTEX,   31.13875, -16.65695,  83.09988,
     VERTEX,   30.84081, -17.23991,  82.39774,
     VERTEX,   30.70974, -18.15939,  82.15488,
     VERTEX,   30.79560, -19.06417,  82.46405,
     VERTEX,   31.06560, -19.60868,  83.20716,
     VERTEX,   31.41661, -19.58491,  84.10037,
     VERTEX,   31.71455, -19.00195,  84.80251,
     VERTEX,   31.84562, -18.08248,  85.04537,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.27768, -18.12093,  83.60013,
                       
     VERTEX,   31.84562, -18.08248,  85.04537,
     VERTEX,   31.75976, -17.17769,  84.73621,
     VERTEX,   31.48975, -16.63319,  83.99309,
     VERTEX,   31.13875, -16.65695,  83.09988,
     VERTEX,   30.84081, -17.23991,  82.39774,
     VERTEX,   30.70974, -18.15939,  82.15488,
     VERTEX,   30.79560, -19.06417,  82.46405,
     VERTEX,   31.06560, -19.60868,  83.20716,
     VERTEX,   31.41661, -19.58491,  84.10037,
     VERTEX,   31.71455, -19.00195,  84.80251,
     VERTEX,   31.84562, -18.08248,  85.04537,
                       
     END,              
                       
     CYLINDER,   38.12100, -18.38800,  80.91800,  31.27768, -18.12093,  83.60013,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   85.81750, -57.42364,  89.79235,
                       
     VERTEX,   83.01238, -64.46157,  89.91366,
     VERTEX,   82.34823, -64.14199,  89.29855,
     VERTEX,   81.52959, -63.64550,  89.22828,
     VERTEX,   80.86917, -63.16176,  89.72971,
     VERTEX,   80.61921, -62.87553,  90.61129,
     VERTEX,   80.87520, -62.89614,  91.53630,
     VERTEX,   81.53935, -63.21572,  92.15141,
     VERTEX,   82.35799, -63.71220,  92.22168,
     VERTEX,   83.01842, -64.19595,  91.72025,
     VERTEX,   83.26837, -64.48219,  90.83867,
     VERTEX,   83.01238, -64.46157,  89.91366,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   81.94379, -63.67886,  90.72498,
                       
     VERTEX,   83.01238, -64.46157,  89.91366,
     VERTEX,   82.34823, -64.14199,  89.29855,
     VERTEX,   81.52959, -63.64550,  89.22828,
     VERTEX,   80.86917, -63.16176,  89.72971,
     VERTEX,   80.61921, -62.87553,  90.61129,
     VERTEX,   80.87520, -62.89614,  91.53630,
     VERTEX,   81.53935, -63.21572,  92.15141,
     VERTEX,   82.35799, -63.71220,  92.22168,
     VERTEX,   83.01842, -64.19595,  91.72025,
     VERTEX,   83.26837, -64.48219,  90.83867,
     VERTEX,   83.01238, -64.46157,  89.91366,
                       
     END,              
                       
     CYLINDER,   75.67600, -73.80000,  92.23400,  81.94379, -63.67886,  90.72498,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   80.05303, -55.25922,  88.05801,
                       
     VERTEX,   77.99711, -61.63440,  88.05731,
     VERTEX,   77.34380, -61.35136,  87.41335,
     VERTEX,   76.50751, -60.89242,  87.30569,
     VERTEX,   75.80767, -60.43288,  87.77542,
     VERTEX,   75.51160, -60.14827,  88.64314,
     VERTEX,   75.73239, -60.14729,  89.57741,
     VERTEX,   76.38570, -60.43033,  90.22136,
     VERTEX,   77.22199, -60.88927,  90.32903,
     VERTEX,   77.92183, -61.34881,  89.85929,
     VERTEX,   78.21790, -61.63342,  88.99158,
     VERTEX,   77.99711, -61.63440,  88.05731,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   76.86475, -60.89085,  88.81736,
                       
     VERTEX,   77.99711, -61.63440,  88.05731,
     VERTEX,   77.34380, -61.35136,  87.41335,
     VERTEX,   76.50751, -60.89242,  87.30569,
     VERTEX,   75.80767, -60.43288,  87.77542,
     VERTEX,   75.51160, -60.14827,  88.64314,
     VERTEX,   75.73239, -60.14729,  89.57741,
     VERTEX,   76.38570, -60.43033,  90.22136,
     VERTEX,   77.22199, -60.88927,  90.32903,
     VERTEX,   77.92183, -61.34881,  89.85929,
     VERTEX,   78.21790, -61.63342,  88.99158,
     VERTEX,   77.99711, -61.63440,  88.05731,
                       
     END,              
                       
     CYLINDER,   71.70600, -70.00300,  90.04600,  76.86475, -60.89085,  88.81736,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   78.99529, -74.29377,  87.51130,
                       
     VERTEX,   73.34317, -79.12632,  88.28633,
     VERTEX,   72.76877, -78.39958,  88.03430,
     VERTEX,   72.34246, -77.60034,  88.35222,
     VERTEX,   72.22706, -77.03388,  89.11864,
     VERTEX,   72.46665, -76.91657,  90.04083,
     VERTEX,   72.96973, -77.29323,  90.76654,
     VERTEX,   73.54412, -78.01997,  91.01857,
     VERTEX,   73.97044, -78.81921,  90.70065,
     VERTEX,   74.08584, -79.38567,  89.93423,
     VERTEX,   73.84624, -79.50298,  89.01204,
     VERTEX,   73.34317, -79.12632,  88.28633,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   73.15645, -78.20978,  89.52644,
                       
     VERTEX,   73.34317, -79.12632,  88.28633,
     VERTEX,   72.76877, -78.39958,  88.03430,
     VERTEX,   72.34246, -77.60034,  88.35222,
     VERTEX,   72.22706, -77.03388,  89.11864,
     VERTEX,   72.46665, -76.91657,  90.04083,
     VERTEX,   72.96973, -77.29323,  90.76654,
     VERTEX,   73.54412, -78.01997,  91.01857,
     VERTEX,   73.97044, -78.81921,  90.70065,
     VERTEX,   74.08584, -79.38567,  89.93423,
     VERTEX,   73.84624, -79.50298,  89.01204,
     VERTEX,   73.34317, -79.12632,  88.28633,
                       
     END,              
                       
     CYLINDER,   63.70900, -84.54600,  92.78700,  73.15645, -78.20978,  89.52644,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   77.19305, -78.10011,  91.87187,
                       
     VERTEX,   71.13667, -82.09261,  92.76872,
     VERTEX,   70.65285, -81.27779,  92.61512,
     VERTEX,   70.36942, -80.45473,  93.01991,
     VERTEX,   70.39462, -79.93784,  93.82848,
     VERTEX,   70.71883, -79.92453,  94.73198,
     VERTEX,   71.21822, -80.41989,  95.38530,
     VERTEX,   71.70203, -81.23472,  95.53890,
     VERTEX,   71.98547, -82.05776,  95.13411,
     VERTEX,   71.96027, -82.57466,  94.32554,
     VERTEX,   71.63605, -82.58797,  93.42204,
     VERTEX,   71.13667, -82.09261,  92.76872,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   71.17744, -81.25625,  94.07701,
                       
     VERTEX,   71.13667, -82.09261,  92.76872,
     VERTEX,   70.65285, -81.27779,  92.61512,
     VERTEX,   70.36942, -80.45473,  93.01991,
     VERTEX,   70.39462, -79.93784,  93.82848,
     VERTEX,   70.71883, -79.92453,  94.73198,
     VERTEX,   71.21822, -80.41989,  95.38530,
     VERTEX,   71.70203, -81.23472,  95.53890,
     VERTEX,   71.98547, -82.05776,  95.13411,
     VERTEX,   71.96027, -82.57466,  94.32554,
     VERTEX,   71.63605, -82.58797,  93.42204,
     VERTEX,   71.13667, -82.09261,  92.76872,
                       
     END,              
                       
     CYLINDER,   61.44400, -86.36300,  97.64500,  71.17744, -81.25625,  94.07701,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   74.59129, -82.04655,  97.92764,
                       
     VERTEX,   68.21142, -84.88902,  98.94433,
     VERTEX,   67.87839, -83.98903,  98.91742,
     VERTEX,   67.78745, -83.17907,  99.42465,
     VERTEX,   67.97333, -82.76849, 100.27229,
     VERTEX,   68.36504, -82.91415, 101.13655,
     VERTEX,   68.81297, -83.56038, 101.68732,
     VERTEX,   69.14600, -84.46036, 101.71423,
     VERTEX,   69.23694, -85.27032, 101.20699,
     VERTEX,   69.05106, -85.68089, 100.35937,
     VERTEX,   68.65934, -85.53525,  99.49510,
     VERTEX,   68.21142, -84.88902,  98.94433,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   68.51219, -84.22469, 100.31583,
                       
     VERTEX,   68.21142, -84.88902,  98.94433,
     VERTEX,   67.87839, -83.98903,  98.91742,
     VERTEX,   67.78745, -83.17907,  99.42465,
     VERTEX,   67.97333, -82.76849, 100.27229,
     VERTEX,   68.36504, -82.91415, 101.13655,
     VERTEX,   68.81297, -83.56038, 101.68732,
     VERTEX,   69.14600, -84.46036, 101.71423,
     VERTEX,   69.23694, -85.27032, 101.20699,
     VERTEX,   69.05106, -85.68089, 100.35937,
     VERTEX,   68.65934, -85.53525,  99.49510,
     VERTEX,   68.21142, -84.88902,  98.94433,
                       
     END,              
                       
     CYLINDER,   58.67600, -87.74900, 104.18000,  68.51219, -84.22469, 100.31583,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -29.16728,  39.01722,  94.80910,
                       
     VERTEX,  -30.57506,  33.00105,  93.90623,
     VERTEX,  -31.16469,  33.31883,  93.21851,
     VERTEX,  -32.01086,  33.74185,  93.05531,
     VERTEX,  -32.79039,  34.10854,  93.47897,
     VERTEX,  -33.20550,  34.27883,  94.32766,
     VERTEX,  -33.09764,  34.18768,  95.27722,
     VERTEX,  -32.50801,  33.86991,  95.96494,
     VERTEX,  -31.66183,  33.44688,  96.12814,
     VERTEX,  -30.88231,  33.08020,  95.70448,
     VERTEX,  -30.46721,  32.90990,  94.85578,
     VERTEX,  -30.57506,  33.00105,  93.90623,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -31.83635,  33.59437,  94.59172,
                       
     VERTEX,  -30.57506,  33.00105,  93.90623,
     VERTEX,  -31.16469,  33.31883,  93.21851,
     VERTEX,  -32.01086,  33.74185,  93.05531,
     VERTEX,  -32.79039,  34.10854,  93.47897,
     VERTEX,  -33.20550,  34.27883,  94.32766,
     VERTEX,  -33.09764,  34.18768,  95.27722,
     VERTEX,  -32.50801,  33.86991,  95.96494,
     VERTEX,  -31.66183,  33.44688,  96.12814,
     VERTEX,  -30.88231,  33.08020,  95.70448,
     VERTEX,  -30.46721,  32.90990,  94.85578,
     VERTEX,  -30.57506,  33.00105,  93.90623,
                       
     END,              
                       
     CYLINDER,  -36.15500,  24.82000,  94.24000, -31.83635,  33.59437,  94.59172,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -26.84096,  34.02114,  87.47798,
                       
     VERTEX,  -27.65351,  28.69186,  86.60890,
     VERTEX,  -28.22666,  28.98204,  85.89554,
     VERTEX,  -29.08099,  29.37135,  85.69514,
     VERTEX,  -29.89017,  29.71108,  86.08425,
     VERTEX,  -30.34513,  29.87146,  86.91425,
     VERTEX,  -30.27208,  29.79124,  87.86810,
     VERTEX,  -29.69893,  29.50105,  88.58146,
     VERTEX,  -28.84460,  29.11174,  88.78186,
     VERTEX,  -28.03542,  28.77201,  88.39275,
     VERTEX,  -27.58046,  28.61163,  87.56275,
     VERTEX,  -27.65351,  28.69186,  86.60890,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -28.96280,  29.24155,  87.23849,
                       
     VERTEX,  -27.65351,  28.69186,  86.60890,
     VERTEX,  -28.22666,  28.98204,  85.89554,
     VERTEX,  -29.08099,  29.37135,  85.69514,
     VERTEX,  -29.89017,  29.71108,  86.08425,
     VERTEX,  -30.34513,  29.87146,  86.91425,
     VERTEX,  -30.27208,  29.79124,  87.86810,
     VERTEX,  -29.69893,  29.50105,  88.58146,
     VERTEX,  -28.84460,  29.11174,  88.78186,
     VERTEX,  -28.03542,  28.77201,  88.39275,
     VERTEX,  -27.58046,  28.61163,  87.56275,
     VERTEX,  -27.65351,  28.69186,  86.60890,
                       
     END,              
                       
     CYLINDER,  -32.39600,  21.50800,  86.85100, -28.96280,  29.24155,  87.23849,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -20.70316,  35.40685,  86.14235,
                       
     VERTEX,  -22.16548,  30.67669,  85.16053,
     VERTEX,  -22.78021,  31.09078,  84.55042,
     VERTEX,  -23.58725,  31.60741,  84.49216,
     VERTEX,  -24.27832,  32.02924,  85.00799,
     VERTEX,  -24.58947,  32.19513,  85.90089,
     VERTEX,  -24.40184,  32.04174,  86.82980,
     VERTEX,  -23.78711,  31.62764,  87.43990,
     VERTEX,  -22.98008,  31.11101,  87.49816,
     VERTEX,  -22.28900,  30.68919,  86.98233,
     VERTEX,  -21.97786,  30.52329,  86.08943,
     VERTEX,  -22.16548,  30.67669,  85.16053,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -23.28366,  31.35921,  85.99516,
                       
     VERTEX,  -22.16548,  30.67669,  85.16053,
     VERTEX,  -22.78021,  31.09078,  84.55042,
     VERTEX,  -23.58725,  31.60741,  84.49216,
     VERTEX,  -24.27832,  32.02924,  85.00799,
     VERTEX,  -24.58947,  32.19513,  85.90089,
     VERTEX,  -24.40184,  32.04174,  86.82980,
     VERTEX,  -23.78711,  31.62764,  87.43990,
     VERTEX,  -22.98008,  31.11101,  87.49816,
     VERTEX,  -22.28900,  30.68919,  86.98233,
     VERTEX,  -21.97786,  30.52329,  86.08943,
     VERTEX,  -22.16548,  30.67669,  85.16053,
                       
     END,              
                       
     CYLINDER,  -27.45900,  24.81000,  85.75700, -23.28366,  31.35921,  85.99516,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -14.17990,  43.16151,  95.64457,
                       
     VERTEX,  -17.30093,  38.62857,  94.54684,
     VERTEX,  -17.90197,  39.24640,  94.12419,
     VERTEX,  -18.56000,  39.92572,  94.28891,
     VERTEX,  -19.02367,  40.40704,  94.97807,
     VERTEX,  -19.11587,  40.50651,  95.92844,
     VERTEX,  -18.80139,  40.18614,  96.77701,
     VERTEX,  -18.20035,  39.56831,  97.19965,
     VERTEX,  -17.54232,  38.88899,  97.03493,
     VERTEX,  -17.07866,  38.40767,  96.34577,
     VERTEX,  -16.98645,  38.30820,  95.39540,
     VERTEX,  -17.30093,  38.62857,  94.54684,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -18.05116,  39.40735,  95.66193,
                       
     VERTEX,  -17.30093,  38.62857,  94.54684,
     VERTEX,  -17.90197,  39.24640,  94.12419,
     VERTEX,  -18.56000,  39.92572,  94.28891,
     VERTEX,  -19.02367,  40.40704,  94.97807,
     VERTEX,  -19.11587,  40.50651,  95.92844,
     VERTEX,  -18.80139,  40.18614,  96.77701,
     VERTEX,  -18.20035,  39.56831,  97.19965,
     VERTEX,  -17.54232,  38.88899,  97.03493,
     VERTEX,  -17.07866,  38.40767,  96.34577,
     VERTEX,  -16.98645,  38.30820,  95.39540,
     VERTEX,  -17.30093,  38.62857,  94.54684,
                       
     END,              
                       
     CYLINDER,  -24.31500,  33.33300,  95.69000, -18.05116,  39.40735,  95.66193,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -16.05466,  41.40028, 101.17386,
                       
     VERTEX,  -18.74858,  36.64640, 100.11802,
     VERTEX,  -19.36592,  37.20048,  99.63481,
     VERTEX,  -20.07843,  37.83655,  99.73146,
     VERTEX,  -20.61397,  38.31165, 100.37106,
     VERTEX,  -20.76797,  38.44431, 101.30930,
     VERTEX,  -20.48161,  38.18385, 102.18780,
     VERTEX,  -19.86428,  37.62977, 102.67101,
     VERTEX,  -19.15176,  36.99370, 102.57435,
     VERTEX,  -18.61623,  36.51860, 101.93475,
     VERTEX,  -18.46222,  36.38594, 100.99652,
     VERTEX,  -18.74858,  36.64640, 100.11802,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,  -19.61510,  37.41512, 101.15291,
                       
     VERTEX,  -18.74858,  36.64640, 100.11802,
     VERTEX,  -19.36592,  37.20048,  99.63481,
     VERTEX,  -20.07843,  37.83655,  99.73146,
     VERTEX,  -20.61397,  38.31165, 100.37106,
     VERTEX,  -20.76797,  38.44431, 101.30930,
     VERTEX,  -20.48161,  38.18385, 102.18780,
     VERTEX,  -19.86428,  37.62977, 102.67101,
     VERTEX,  -19.15176,  36.99370, 102.57435,
     VERTEX,  -18.61623,  36.51860, 101.93475,
     VERTEX,  -18.46222,  36.38594, 100.99652,
     VERTEX,  -18.74858,  36.64640, 100.11802,
                       
     END,              
                       
     CYLINDER,  -25.37600,  30.96700, 101.11900, -19.61510,  37.41512, 101.15291,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   44.61145,  29.84372,  47.16144,
                       
     VERTEX,   41.39992,  34.96926,  46.75953,
     VERTEX,   41.76176,  35.17393,  47.62485,
     VERTEX,   41.69760,  34.97178,  48.56113,
     VERTEX,   41.23193,  34.44001,  49.21074,
     VERTEX,   40.54265,  33.78176,  49.32554,
     VERTEX,   39.89301,  33.24844,  48.86170,
     VERTEX,   39.53117,  33.04378,  47.99638,
     VERTEX,   39.59534,  33.24593,  47.06010,
     VERTEX,   40.06100,  33.77769,  46.41049,
     VERTEX,   40.75029,  34.43595,  46.29568,
     VERTEX,   41.39992,  34.96926,  46.75953,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.64647,  34.10886,  47.81061,
                       
     VERTEX,   41.39992,  34.96926,  46.75953,
     VERTEX,   41.76176,  35.17393,  47.62485,
     VERTEX,   41.69760,  34.97178,  48.56113,
     VERTEX,   41.23193,  34.44001,  49.21074,
     VERTEX,   40.54265,  33.78176,  49.32554,
     VERTEX,   39.89301,  33.24844,  48.86170,
     VERTEX,   39.53117,  33.04378,  47.99638,
     VERTEX,   39.59534,  33.24593,  47.06010,
     VERTEX,   40.06100,  33.77769,  46.41049,
     VERTEX,   40.75029,  34.43595,  46.29568,
     VERTEX,   41.39992,  34.96926,  46.75953,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  40.64647,  34.10886,  47.81061,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.22847,  24.94340,  53.60588,
                       
     VERTEX,   37.80740,  29.63983,  53.13271,
     VERTEX,   38.14415,  29.80436,  54.01653,
     VERTEX,   38.03217,  29.58319,  54.94397,
     VERTEX,   37.51424,  29.06082,  55.56079,
     VERTEX,   36.78817,  28.43676,  55.63138,
     VERTEX,   36.13131,  27.94939,  55.12878,
     VERTEX,   35.79456,  27.78486,  54.24497,
     VERTEX,   35.90654,  28.00602,  53.31752,
     VERTEX,   36.42448,  28.52840,  52.70071,
     VERTEX,   37.15054,  29.15245,  52.63011,
     VERTEX,   37.80740,  29.63983,  53.13271,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.96936,  28.79461,  54.13074,
                       
     VERTEX,   37.80740,  29.63983,  53.13271,
     VERTEX,   38.14415,  29.80436,  54.01653,
     VERTEX,   38.03217,  29.58319,  54.94397,
     VERTEX,   37.51424,  29.06082,  55.56079,
     VERTEX,   36.78817,  28.43676,  55.63138,
     VERTEX,   36.13131,  27.94939,  55.12878,
     VERTEX,   35.79456,  27.78486,  54.24497,
     VERTEX,   35.90654,  28.00602,  53.31752,
     VERTEX,   36.42448,  28.52840,  52.70071,
     VERTEX,   37.15054,  29.15245,  52.63011,
     VERTEX,   37.80740,  29.63983,  53.13271,
                       
     END,              
                       
     CYLINDER,   31.69600,  35.02600,  54.98000,  36.96936,  28.79461,  54.13074,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.13706,  28.36197,  55.34064,
                       
     VERTEX,   32.28344,  32.30862,  54.67072,
     VERTEX,   32.66892,  32.61074,  55.49639,
     VERTEX,   32.67706,  32.47218,  56.44630,
     VERTEX,   32.30474,  31.94589,  57.15763,
     VERTEX,   31.69417,  31.23287,  57.35867,
     VERTEX,   31.07858,  30.60548,  56.97263,
     VERTEX,   30.69309,  30.30336,  56.14696,
     VERTEX,   30.68496,  30.44191,  55.19704,
     VERTEX,   31.05728,  30.96821,  54.48571,
     VERTEX,   31.66784,  31.68123,  54.28468,
     VERTEX,   32.28344,  32.30862,  54.67072,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.68101,  31.45705,  55.82167,
                       
     VERTEX,   32.28344,  32.30862,  54.67072,
     VERTEX,   32.66892,  32.61074,  55.49639,
     VERTEX,   32.67706,  32.47218,  56.44630,
     VERTEX,   32.30474,  31.94589,  57.15763,
     VERTEX,   31.69417,  31.23287,  57.35867,
     VERTEX,   31.07858,  30.60548,  56.97263,
     VERTEX,   30.69309,  30.30336,  56.14696,
     VERTEX,   30.68496,  30.44191,  55.19704,
     VERTEX,   31.05728,  30.96821,  54.48571,
     VERTEX,   31.66784,  31.68123,  54.28468,
     VERTEX,   32.28344,  32.30862,  54.67072,
                       
     END,              
                       
     CYLINDER,   26.08900,  36.46500,  56.60000,  31.68101,  31.45705,  55.82167,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   32.52536,  39.49569,  47.51702,
                       
     VERTEX,   28.16374,  42.72650,  46.73447,
     VERTEX,   28.54637,  43.26848,  47.42834,
     VERTEX,   28.69625,  43.32667,  48.37478,
     VERTEX,   28.55615,  42.87883,  49.21228,
     VERTEX,   28.17957,  42.09603,  49.62095,
     VERTEX,   27.71035,  41.27727,  49.44469,
     VERTEX,   27.32773,  40.73529,  48.75082,
     VERTEX,   27.17785,  40.67710,  47.80438,
     VERTEX,   27.31795,  41.12494,  46.96687,
     VERTEX,   27.69453,  41.90774,  46.55820,
     VERTEX,   28.16374,  42.72650,  46.73447,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.93705,  42.00188,  48.08958,
                       
     VERTEX,   28.16374,  42.72650,  46.73447,
     VERTEX,   28.54637,  43.26848,  47.42834,
     VERTEX,   28.69625,  43.32667,  48.37478,
     VERTEX,   28.55615,  42.87883,  49.21228,
     VERTEX,   28.17957,  42.09603,  49.62095,
     VERTEX,   27.71035,  41.27727,  49.44469,
     VERTEX,   27.32773,  40.73529,  48.75082,
     VERTEX,   27.17785,  40.67710,  47.80438,
     VERTEX,   27.31795,  41.12494,  46.96687,
     VERTEX,   27.69453,  41.90774,  46.55820,
     VERTEX,   28.16374,  42.72650,  46.73447,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  27.93705,  42.00188,  48.08958,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.69267,  38.23976,  41.69132,
                       
     VERTEX,   29.56944,  41.81455,  40.97242,
     VERTEX,   29.96631,  42.29082,  41.70540,
     VERTEX,   30.09037,  42.28787,  42.65735,
     VERTEX,   29.89422,  41.80684,  43.46465,
     VERTEX,   29.45278,  41.03146,  43.81894,
     VERTEX,   28.93468,  40.25790,  43.58490,
     VERTEX,   28.53781,  39.78164,  42.85192,
     VERTEX,   28.41375,  39.78458,  41.89997,
     VERTEX,   28.60990,  40.26561,  41.09267,
     VERTEX,   29.05133,  41.04099,  40.73838,
     VERTEX,   29.56944,  41.81455,  40.97242,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.25206,  41.03623,  42.27866,
                       
     VERTEX,   29.56944,  41.81455,  40.97242,
     VERTEX,   29.96631,  42.29082,  41.70540,
     VERTEX,   30.09037,  42.28787,  42.65735,
     VERTEX,   29.89422,  41.80684,  43.46465,
     VERTEX,   29.45278,  41.03146,  43.81894,
     VERTEX,   28.93468,  40.25790,  43.58490,
     VERTEX,   28.53781,  39.78164,  42.85192,
     VERTEX,   28.41375,  39.78458,  41.89997,
     VERTEX,   28.60990,  40.26561,  41.09267,
     VERTEX,   29.05133,  41.04099,  40.73838,
     VERTEX,   29.56944,  41.81455,  40.97242,
                       
     END,              
                       
     CYLINDER,   22.06700,  45.56100,  43.22900,  29.25206,  41.03623,  42.27866,   0.80000,
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
