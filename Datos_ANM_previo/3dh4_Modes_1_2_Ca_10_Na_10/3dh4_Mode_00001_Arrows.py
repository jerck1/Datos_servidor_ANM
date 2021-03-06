from pymol.cgo import *
from pymol import cmd  
import math            
                       
obj = [                
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   40.57469, -45.63512,  30.31647,
                       
     VERTEX,   36.29984, -49.94567,  30.13283,
     VERTEX,   35.71487, -49.24590,  29.83329,
     VERTEX,   35.21183, -48.47926,  30.11756,
     VERTEX,   34.98285, -47.93859,  30.87706,
     VERTEX,   35.11539, -47.83041,  31.82170,
     VERTEX,   35.55883, -48.19604,  32.59064,
     VERTEX,   36.14380, -48.89582,  32.89018,
     VERTEX,   36.64684, -49.66246,  32.60591,
     VERTEX,   36.87583, -50.20313,  31.84640,
     VERTEX,   36.74328, -50.31130,  30.90177,
     VERTEX,   36.29984, -49.94567,  30.13283,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   35.92934, -49.07086,  31.36173,
                       
     VERTEX,   36.29984, -49.94567,  30.13283,
     VERTEX,   35.71487, -49.24590,  29.83329,
     VERTEX,   35.21183, -48.47926,  30.11756,
     VERTEX,   34.98285, -47.93859,  30.87706,
     VERTEX,   35.11539, -47.83041,  31.82170,
     VERTEX,   35.55883, -48.19604,  32.59064,
     VERTEX,   36.14380, -48.89582,  32.89018,
     VERTEX,   36.64684, -49.66246,  32.60591,
     VERTEX,   36.87583, -50.20313,  31.84640,
     VERTEX,   36.74328, -50.31130,  30.90177,
     VERTEX,   36.29984, -49.94567,  30.13283,
                       
     END,              
                       
     CYLINDER,   28.41300, -54.63000,  33.05300,  35.92934, -49.07086,  31.36173,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   15.24069, -66.22636,  35.63441,
                       
     VERTEX,   10.85439, -69.13683,  39.16179,
     VERTEX,   10.34752, -68.32681,  39.06921,
     VERTEX,   10.26840, -67.42075,  39.37641,
     VERTEX,   10.64724, -66.76470,  39.96606,
     VERTEX,   11.33934, -66.60927,  40.61293,
     VERTEX,   12.08034, -67.01382,  41.06993,
     VERTEX,   12.58721, -67.82383,  41.16251,
     VERTEX,   12.66633, -68.72990,  40.85530,
     VERTEX,   12.28749, -69.38595,  40.26566,
     VERTEX,   11.59539, -69.54137,  39.61879,
     VERTEX,   10.85439, -69.13683,  39.16179,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.46736, -68.07533,  40.11586,
                       
     VERTEX,   10.85439, -69.13683,  39.16179,
     VERTEX,   10.34752, -68.32681,  39.06921,
     VERTEX,   10.26840, -67.42075,  39.37641,
     VERTEX,   10.64724, -66.76470,  39.96606,
     VERTEX,   11.33934, -66.60927,  40.61293,
     VERTEX,   12.08034, -67.01382,  41.06993,
     VERTEX,   12.58721, -67.82383,  41.16251,
     VERTEX,   12.66633, -68.72990,  40.85530,
     VERTEX,   12.28749, -69.38595,  40.26566,
     VERTEX,   11.59539, -69.54137,  39.61879,
     VERTEX,   10.85439, -69.13683,  39.16179,
                       
     END,              
                       
     CYLINDER,    5.36200, -71.06700,  47.36700,  11.46736, -68.07533,  40.11586,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   29.72294, -69.62730,  36.19154,
                       
     VERTEX,   25.34284, -72.99937,  38.65326,
     VERTEX,   24.77662, -72.23955,  38.49940,
     VERTEX,   24.55307, -71.36093,  38.81510,
     VERTEX,   24.75758, -70.69913,  39.47977,
     VERTEX,   25.31203, -70.50691,  40.23953,
     VERTEX,   26.00464, -70.85770,  40.80418,
     VERTEX,   26.57086, -71.61752,  40.95805,
     VERTEX,   26.79441, -72.49613,  40.64235,
     VERTEX,   26.58991, -73.15794,  39.97768,
     VERTEX,   26.03546, -73.35016,  39.21791,
     VERTEX,   25.34284, -72.99937,  38.65326,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   25.67374, -71.92854,  39.72872,
                       
     VERTEX,   25.34284, -72.99937,  38.65326,
     VERTEX,   24.77662, -72.23955,  38.49940,
     VERTEX,   24.55307, -71.36093,  38.81510,
     VERTEX,   24.75758, -70.69913,  39.47977,
     VERTEX,   25.31203, -70.50691,  40.23953,
     VERTEX,   26.00464, -70.85770,  40.80418,
     VERTEX,   26.57086, -71.61752,  40.95805,
     VERTEX,   26.79441, -72.49613,  40.64235,
     VERTEX,   26.58991, -73.15794,  39.97768,
     VERTEX,   26.03546, -73.35016,  39.21791,
     VERTEX,   25.34284, -72.99937,  38.65326,
                       
     END,              
                       
     CYLINDER,   19.12200, -75.65200,  45.45200,  25.67374, -71.92854,  39.72872,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   36.54641, -61.64093,  27.80102,
                       
     VERTEX,   31.67478, -65.88702,  29.30463,
     VERTEX,   31.07586, -65.17376,  29.07190,
     VERTEX,   30.69706, -64.34656,  29.37823,
     VERTEX,   30.68306, -63.72137,  30.10662,
     VERTEX,   31.03921, -63.53700,  30.97884,
     VERTEX,   31.62947, -63.86388,  31.66173,
     VERTEX,   32.22838, -64.57713,  31.89446,
     VERTEX,   32.60719, -65.40434,  31.58813,
     VERTEX,   32.62119, -66.02953,  30.85974,
     VERTEX,   32.26504, -66.21390,  29.98752,
     VERTEX,   31.67478, -65.88702,  29.30463,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.65212, -64.87545,  30.48318,
                       
     VERTEX,   31.67478, -65.88702,  29.30463,
     VERTEX,   31.07586, -65.17376,  29.07190,
     VERTEX,   30.69706, -64.34656,  29.37823,
     VERTEX,   30.68306, -63.72137,  30.10662,
     VERTEX,   31.03921, -63.53700,  30.97884,
     VERTEX,   31.62947, -63.86388,  31.66173,
     VERTEX,   32.22838, -64.57713,  31.89446,
     VERTEX,   32.60719, -65.40434,  31.58813,
     VERTEX,   32.62119, -66.02953,  30.85974,
     VERTEX,   32.26504, -66.21390,  29.98752,
     VERTEX,   31.67478, -65.88702,  29.30463,
                       
     END,              
                       
     CYLINDER,   23.73300, -70.10900,  34.82300,  31.65212, -64.87545,  30.48318,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   23.39227, -46.40860,  28.24779,
                       
     VERTEX,   18.90881, -50.40763,  29.56721,
     VERTEX,   18.30819, -49.69598,  29.33397,
     VERTEX,   17.92890, -48.86847,  29.63888,
     VERTEX,   17.91581, -48.24119,  30.36548,
     VERTEX,   18.27394, -48.05373,  31.23623,
     VERTEX,   18.86648, -48.37771,  31.91854,
     VERTEX,   19.46710, -49.08936,  32.15178,
     VERTEX,   19.84639, -49.91687,  31.84687,
     VERTEX,   19.85947, -50.54415,  31.12027,
     VERTEX,   19.50135, -50.73161,  30.24952,
     VERTEX,   18.90881, -50.40763,  29.56721,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   18.88764, -49.39267,  30.74287,
                       
     VERTEX,   18.90881, -50.40763,  29.56721,
     VERTEX,   18.30819, -49.69598,  29.33397,
     VERTEX,   17.92890, -48.86847,  29.63888,
     VERTEX,   17.91581, -48.24119,  30.36548,
     VERTEX,   18.27394, -48.05373,  31.23623,
     VERTEX,   18.86648, -48.37771,  31.91854,
     VERTEX,   19.46710, -49.08936,  32.15178,
     VERTEX,   19.84639, -49.91687,  31.84687,
     VERTEX,   19.85947, -50.54415,  31.12027,
     VERTEX,   19.50135, -50.73161,  30.24952,
     VERTEX,   18.90881, -50.40763,  29.56721,
                       
     END,              
                       
     CYLINDER,   11.59900, -54.22100,  34.78000,  18.88764, -49.39267,  30.74287,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   46.50725, -43.87194, 124.78544,
                       
     VERTEX,   51.08414, -40.93833, 122.50708,
     VERTEX,   50.65479, -40.15407, 122.85663,
     VERTEX,   49.92975, -39.53971, 122.72066,
     VERTEX,   49.18596, -39.32993, 122.15112,
     VERTEX,   48.70754, -39.60485, 121.36555,
     VERTEX,   48.67721, -40.25946, 120.66400,
     VERTEX,   49.10657, -41.04372, 120.31445,
     VERTEX,   49.83161, -41.65808, 120.45042,
     VERTEX,   50.57539, -41.86786, 121.01996,
     VERTEX,   51.05382, -41.59294, 121.80553,
     VERTEX,   51.08414, -40.93833, 122.50708,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   49.88068, -40.59890, 121.58554,
                       
     VERTEX,   51.08414, -40.93833, 122.50708,
     VERTEX,   50.65479, -40.15407, 122.85663,
     VERTEX,   49.92975, -39.53971, 122.72066,
     VERTEX,   49.18596, -39.32993, 122.15112,
     VERTEX,   48.70754, -39.60485, 121.36555,
     VERTEX,   48.67721, -40.25946, 120.66400,
     VERTEX,   49.10657, -41.04372, 120.31445,
     VERTEX,   49.83161, -41.65808, 120.45042,
     VERTEX,   50.57539, -41.86786, 121.01996,
     VERTEX,   51.05382, -41.59294, 121.80553,
     VERTEX,   51.08414, -40.93833, 122.50708,
                       
     END,              
                       
     CYLINDER,   55.33900, -35.30300, 116.40800,  49.88068, -40.59890, 121.58554,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   28.94965, -68.22402, 123.01487,
                       
     VERTEX,   34.15356, -65.33253, 124.44035,
     VERTEX,   33.58559, -64.63442, 124.77448,
     VERTEX,   33.01868, -63.90401, 124.51617,
     VERTEX,   32.66938, -63.42031, 123.76410,
     VERTEX,   32.67110, -63.36806, 122.80553,
     VERTEX,   33.02320, -63.76723, 122.00659,
     VERTEX,   33.59117, -64.46535, 121.67246,
     VERTEX,   34.15808, -65.19575, 121.93077,
     VERTEX,   34.50738, -65.67946, 122.68285,
     VERTEX,   34.50566, -65.73170, 123.64142,
     VERTEX,   34.15356, -65.33253, 124.44035,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   33.58838, -64.54988, 123.22347,
                       
     VERTEX,   34.15356, -65.33253, 124.44035,
     VERTEX,   33.58559, -64.63442, 124.77448,
     VERTEX,   33.01868, -63.90401, 124.51617,
     VERTEX,   32.66938, -63.42031, 123.76410,
     VERTEX,   32.67110, -63.36806, 122.80553,
     VERTEX,   33.02320, -63.76723, 122.00659,
     VERTEX,   33.59117, -64.46535, 121.67246,
     VERTEX,   34.15808, -65.19575, 121.93077,
     VERTEX,   34.50738, -65.67946, 122.68285,
     VERTEX,   34.50566, -65.73170, 123.64142,
     VERTEX,   34.15356, -65.33253, 124.44035,
                       
     END,              
                       
     CYLINDER,   41.09400, -58.60500, 123.56100,  33.58838, -64.54988, 123.22347,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   26.93719, -63.76567, 124.61053,
                       
     VERTEX,   32.22612, -60.78252, 125.84778,
     VERTEX,   31.66438, -60.08120, 126.18570,
     VERTEX,   31.08759, -59.35732, 125.93092,
     VERTEX,   30.71606, -58.88738, 125.18077,
     VERTEX,   30.69172, -58.85088, 124.22177,
     VERTEX,   31.02385, -59.26177, 123.42023,
     VERTEX,   31.58560, -59.96309, 123.08232,
     VERTEX,   32.16239, -60.68697, 123.33709,
     VERTEX,   32.53391, -61.15691, 124.08724,
     VERTEX,   32.55826, -61.19341, 125.04624,
     VERTEX,   32.22612, -60.78252, 125.84778,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   31.62499, -60.02215, 124.63401,
                       
     VERTEX,   32.22612, -60.78252, 125.84778,
     VERTEX,   31.66438, -60.08120, 126.18570,
     VERTEX,   31.08759, -59.35732, 125.93092,
     VERTEX,   30.71606, -58.88738, 125.18077,
     VERTEX,   30.69172, -58.85088, 124.22177,
     VERTEX,   31.02385, -59.26177, 123.42023,
     VERTEX,   31.58560, -59.96309, 123.08232,
     VERTEX,   32.16239, -60.68697, 123.33709,
     VERTEX,   32.53391, -61.15691, 124.08724,
     VERTEX,   32.55826, -61.19341, 125.04624,
     VERTEX,   32.22612, -60.78252, 125.84778,
                       
     END,              
                       
     CYLINDER,   39.21000, -53.96500, 124.67200,  31.62499, -60.02215, 124.63401,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.07610, -54.23134, 126.29630,
                       
     VERTEX,   21.58435, -51.10342, 127.75844,
     VERTEX,   21.01582, -50.40542, 128.09187,
     VERTEX,   20.45029, -49.67417, 127.83295,
     VERTEX,   20.10377, -49.18898, 127.08054,
     VERTEX,   20.10862, -49.13517, 126.12206,
     VERTEX,   20.46299, -49.53329, 125.32362,
     VERTEX,   21.03152, -50.23128, 124.99017,
     VERTEX,   21.59705, -50.96253, 125.24911,
     VERTEX,   21.94357, -51.44773, 126.00151,
     VERTEX,   21.93872, -51.50154, 126.95999,
     VERTEX,   21.58435, -51.10342, 127.75844,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.02367, -50.31835, 126.54103,
                       
     VERTEX,   21.58435, -51.10342, 127.75844,
     VERTEX,   21.01582, -50.40542, 128.09187,
     VERTEX,   20.45029, -49.67417, 127.83295,
     VERTEX,   20.10377, -49.18898, 127.08054,
     VERTEX,   20.10862, -49.13517, 126.12206,
     VERTEX,   20.46299, -49.53329, 125.32362,
     VERTEX,   21.03152, -50.23128, 124.99017,
     VERTEX,   21.59705, -50.96253, 125.24911,
     VERTEX,   21.94357, -51.44773, 126.00151,
     VERTEX,   21.93872, -51.50154, 126.95999,
     VERTEX,   21.58435, -51.10342, 127.75844,
                       
     END,              
                       
     CYLINDER,   29.02900, -43.98700, 126.93700,  21.02367, -50.31835, 126.54103,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.73259, -59.46022, 122.59155,
                       
     VERTEX,   21.88237, -56.66653, 124.62700,
     VERTEX,   21.29326, -55.98069, 124.94975,
     VERTEX,   20.75644, -55.23012, 124.68507,
     VERTEX,   20.47696, -54.70150, 123.93403,
     VERTEX,   20.56157, -54.59676, 122.98352,
     VERTEX,   20.97795, -54.95589, 122.19659,
     VERTEX,   21.56706, -55.64174, 121.87384,
     VERTEX,   22.10388, -56.39231, 122.13853,
     VERTEX,   22.38336, -56.92093, 122.88956,
     VERTEX,   22.29875, -57.02567, 123.84008,
     VERTEX,   21.88237, -56.66653, 124.62700,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.43016, -55.81121, 123.41180,
                       
     VERTEX,   21.88237, -56.66653, 124.62700,
     VERTEX,   21.29326, -55.98069, 124.94975,
     VERTEX,   20.75644, -55.23012, 124.68507,
     VERTEX,   20.47696, -54.70150, 123.93403,
     VERTEX,   20.56157, -54.59676, 122.98352,
     VERTEX,   20.97795, -54.95589, 122.19659,
     VERTEX,   21.56706, -55.64174, 121.87384,
     VERTEX,   22.10388, -56.39231, 122.13853,
     VERTEX,   22.38336, -56.92093, 122.88956,
     VERTEX,   22.29875, -57.02567, 123.84008,
     VERTEX,   21.88237, -56.66653, 124.62700,
                       
     END,              
                       
     CYLINDER,   29.03100, -49.90700, 124.73900,  21.43016, -55.81121, 123.41180,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.07287,  10.37122, 112.62232,
                       
     VERTEX,    7.39502,   6.81243, 111.01092,
     VERTEX,    6.89079,   7.58423, 110.74319,
     VERTEX,    6.36540,   8.31944, 111.06728,
     VERTEX,    6.01953,   8.73724, 111.85938,
     VERTEX,    5.98529,   8.67804, 112.81694,
     VERTEX,    6.27576,   8.16445, 113.57420,
     VERTEX,    6.77999,   7.39264, 113.84193,
     VERTEX,    7.30538,   6.65743, 113.51785,
     VERTEX,    7.65125,   6.23964, 112.72575,
     VERTEX,    7.68549,   6.29884, 111.76819,
     VERTEX,    7.39502,   6.81243, 111.01092,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.83539,   7.48844, 112.29256,
                       
     VERTEX,    7.39502,   6.81243, 111.01092,
     VERTEX,    6.89079,   7.58423, 110.74319,
     VERTEX,    6.36540,   8.31944, 111.06728,
     VERTEX,    6.01953,   8.73724, 111.85938,
     VERTEX,    5.98529,   8.67804, 112.81694,
     VERTEX,    6.27576,   8.16445, 113.57420,
     VERTEX,    6.77999,   7.39264, 113.84193,
     VERTEX,    7.30538,   6.65743, 113.51785,
     VERTEX,    7.65125,   6.23964, 112.72575,
     VERTEX,    7.68549,   6.29884, 111.76819,
     VERTEX,    7.39502,   6.81243, 111.01092,
                       
     END,              
                       
     CYLINDER,   -0.02100,   2.82400, 111.75900,   6.83539,   7.48844, 112.29256,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    9.74111,   3.93015, 114.33990,
                       
     VERTEX,    6.00836,   0.48911, 112.09445,
     VERTEX,    5.54049,   1.29067, 111.84910,
     VERTEX,    4.99927,   2.00821, 112.18648,
     VERTEX,    4.59143,   2.36764, 112.97772,
     VERTEX,    4.47275,   2.23169, 113.92061,
     VERTEX,    4.68856,   1.65227, 114.65498,
     VERTEX,    5.15644,   0.85071, 114.90034,
     VERTEX,    5.69766,   0.13318, 114.56296,
     VERTEX,    6.10550,  -0.22626, 113.77171,
     VERTEX,    6.22417,  -0.09030, 112.82883,
     VERTEX,    6.00836,   0.48911, 112.09445,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    5.34846,   1.07069, 113.37472,
                       
     VERTEX,    6.00836,   0.48911, 112.09445,
     VERTEX,    5.54049,   1.29067, 111.84910,
     VERTEX,    4.99927,   2.00821, 112.18648,
     VERTEX,    4.59143,   2.36764, 112.97772,
     VERTEX,    4.47275,   2.23169, 113.92061,
     VERTEX,    4.68856,   1.65227, 114.65498,
     VERTEX,    5.15644,   0.85071, 114.90034,
     VERTEX,    5.69766,   0.13318, 114.56296,
     VERTEX,    6.10550,  -0.22626, 113.77171,
     VERTEX,    6.22417,  -0.09030, 112.82883,
     VERTEX,    6.00836,   0.48911, 112.09445,
                       
     END,              
                       
     CYLINDER,   -1.75900,  -3.55600, 111.81300,   5.34846,   1.07069, 113.37472,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   11.57190,  -0.55166, 113.87315,
                       
     VERTEX,    7.90439,  -4.03603, 111.42228,
     VERTEX,    7.43908,  -3.23558, 111.16859,
     VERTEX,    6.87820,  -2.52729, 111.49316,
     VERTEX,    6.43599,  -2.18172, 112.27203,
     VERTEX,    6.28135,  -2.33086, 113.20768,
     VERTEX,    6.47336,  -2.91774, 113.94273,
     VERTEX,    6.93867,  -3.71820, 114.19643,
     VERTEX,    7.49955,  -4.42648, 113.87185,
     VERTEX,    7.94176,  -4.77205, 113.09299,
     VERTEX,    8.09640,  -4.62292, 112.15733,
     VERTEX,    7.90439,  -4.03603, 111.42228,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.18888,  -3.47689, 112.68251,
                       
     VERTEX,    7.90439,  -4.03603, 111.42228,
     VERTEX,    7.43908,  -3.23558, 111.16859,
     VERTEX,    6.87820,  -2.52729, 111.49316,
     VERTEX,    6.43599,  -2.18172, 112.27203,
     VERTEX,    6.28135,  -2.33086, 113.20768,
     VERTEX,    6.47336,  -2.91774, 113.94273,
     VERTEX,    6.93867,  -3.71820, 114.19643,
     VERTEX,    7.49955,  -4.42648, 113.87185,
     VERTEX,    7.94176,  -4.77205, 113.09299,
     VERTEX,    8.09640,  -4.62292, 112.15733,
     VERTEX,    7.90439,  -4.03603, 111.42228,
                       
     END,              
                       
     CYLINDER,    0.09700,  -8.21000, 110.75600,   7.18888,  -3.47689, 112.68251,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   20.56793, -10.51096, 111.29076,
                       
     VERTEX,   17.41329, -14.03305, 108.95790,
     VERTEX,   16.92398, -13.26417, 108.65626,
     VERTEX,   16.32409, -12.56765, 108.93302,
     VERTEX,   15.84275, -12.20955, 109.68247,
     VERTEX,   15.66383, -12.32666, 110.61835,
     VERTEX,   15.85566, -12.87423, 111.38319,
     VERTEX,   16.34497, -13.64311, 111.68483,
     VERTEX,   16.94486, -14.33963, 111.40807,
     VERTEX,   17.42620, -14.69772, 110.65862,
     VERTEX,   17.60512, -14.58062, 109.72273,
     VERTEX,   17.41329, -14.03305, 108.95790,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   16.63447, -13.45364, 110.17054,
                       
     VERTEX,   17.41329, -14.03305, 108.95790,
     VERTEX,   16.92398, -13.26417, 108.65626,
     VERTEX,   16.32409, -12.56765, 108.93302,
     VERTEX,   15.84275, -12.20955, 109.68247,
     VERTEX,   15.66383, -12.32666, 110.61835,
     VERTEX,   15.85566, -12.87423, 111.38319,
     VERTEX,   16.34497, -13.64311, 111.68483,
     VERTEX,   16.94486, -14.33963, 111.40807,
     VERTEX,   17.42620, -14.69772, 110.65862,
     VERTEX,   17.60512, -14.58062, 109.72273,
     VERTEX,   17.41329, -14.03305, 108.95790,
                       
     END,              
                       
     CYLINDER,   10.27000, -18.21500, 108.35800,  16.63447, -13.45364, 110.17054,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   21.47880,  -3.97257, 110.30142,
                       
     VERTEX,   17.82342,  -7.67538, 108.54247,
     VERTEX,   17.31483,  -6.91303, 108.25654,
     VERTEX,   16.76402,  -6.18820, 108.56123,
     VERTEX,   16.38137,  -5.77776, 109.34015,
     VERTEX,   16.31306,  -5.83848, 110.29579,
     VERTEX,   16.58517,  -6.34717, 111.06313,
     VERTEX,   17.09377,  -7.10952, 111.34905,
     VERTEX,   17.64458,  -7.83434, 111.04436,
     VERTEX,   18.02722,  -8.24478, 110.26543,
     VERTEX,   18.09553,  -8.18406, 109.30980,
     VERTEX,   17.82342,  -7.67538, 108.54247,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   17.20430,  -7.01127, 109.80280,
                       
     VERTEX,   17.82342,  -7.67538, 108.54247,
     VERTEX,   17.31483,  -6.91303, 108.25654,
     VERTEX,   16.76402,  -6.18820, 108.56123,
     VERTEX,   16.38137,  -5.77776, 109.34015,
     VERTEX,   16.31306,  -5.83848, 110.29579,
     VERTEX,   16.58517,  -6.34717, 111.06313,
     VERTEX,   17.09377,  -7.10952, 111.34905,
     VERTEX,   17.64458,  -7.83434, 111.04436,
     VERTEX,   18.02722,  -8.24478, 110.26543,
     VERTEX,   18.09553,  -8.18406, 109.30980,
     VERTEX,   17.82342,  -7.67538, 108.54247,
                       
     END,              
                       
     CYLINDER,   10.28800, -11.92800, 108.99600,  17.20430,  -7.01127, 109.80280,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   -2.78761,  26.60369,  20.82151,
                       
     VERTEX,    2.23000,  28.06484,  25.08264,
     VERTEX,    1.82410,  28.93177,  25.15519,
     VERTEX,    1.71291,  29.77672,  24.71327,
     VERTEX,    1.93891,  30.27695,  23.92567,
     VERTEX,    2.41576,  30.24137,  23.09324,
     VERTEX,    2.96134,  29.68359,  22.53394,
     VERTEX,    3.36724,  28.81665,  22.46139,
     VERTEX,    3.47843,  27.97170,  22.90331,
     VERTEX,    3.25243,  27.47148,  23.69090,
     VERTEX,    2.77558,  27.50705,  24.52333,
     VERTEX,    2.23000,  28.06484,  25.08264,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    2.59567,  28.87421,  23.80829,
                       
     VERTEX,    2.23000,  28.06484,  25.08264,
     VERTEX,    1.82410,  28.93177,  25.15519,
     VERTEX,    1.71291,  29.77672,  24.71327,
     VERTEX,    1.93891,  30.27695,  23.92567,
     VERTEX,    2.41576,  30.24137,  23.09324,
     VERTEX,    2.96134,  29.68359,  22.53394,
     VERTEX,    3.36724,  28.81665,  22.46139,
     VERTEX,    3.47843,  27.97170,  22.90331,
     VERTEX,    3.25243,  27.47148,  23.69090,
     VERTEX,    2.77558,  27.50705,  24.52333,
     VERTEX,    2.23000,  28.06484,  25.08264,
                       
     END,              
                       
     CYLINDER,   11.30600,  32.54800,  28.64100,   2.59567,  28.87421,  23.80829,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   22.68518,  44.11849,  33.99746,
                       
     VERTEX,   26.07177,  43.62491,  40.61497,
     VERTEX,   26.67503,  44.29564,  40.28664,
     VERTEX,   27.43881,  44.44518,  39.72462,
     VERTEX,   28.07138,  44.01641,  39.14358,
     VERTEX,   28.33112,  43.17311,  38.76545,
     VERTEX,   28.11881,  42.23739,  38.73468,
     VERTEX,   27.51555,  41.56666,  39.06301,
     VERTEX,   26.75177,  41.41712,  39.62503,
     VERTEX,   26.11920,  41.84589,  40.20608,
     VERTEX,   25.85946,  42.68919,  40.58420,
     VERTEX,   26.07177,  43.62491,  40.61497,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   27.09529,  42.93115,  39.67483,
                       
     VERTEX,   26.07177,  43.62491,  40.61497,
     VERTEX,   26.67503,  44.29564,  40.28664,
     VERTEX,   27.43881,  44.44518,  39.72462,
     VERTEX,   28.07138,  44.01641,  39.14358,
     VERTEX,   28.33112,  43.17311,  38.76545,
     VERTEX,   28.11881,  42.23739,  38.73468,
     VERTEX,   27.51555,  41.56666,  39.06301,
     VERTEX,   26.75177,  41.41712,  39.62503,
     VERTEX,   26.11920,  41.84589,  40.20608,
     VERTEX,   25.85946,  42.68919,  40.58420,
     VERTEX,   26.07177,  43.62491,  40.61497,
                       
     END,              
                       
     CYLINDER,   34.23100,  41.01000,  48.86100,  27.09529,  42.93115,  39.67483,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    7.96162,  46.28436,  36.27154,
                       
     VERTEX,   11.65007,  46.24568,  42.22935,
     VERTEX,   11.88956,  47.14898,  42.00960,
     VERTEX,   12.45993,  47.68885,  41.45750,
     VERTEX,   13.14332,  47.65908,  40.78393,
     VERTEX,   13.67870,  47.07104,  40.24618,
     VERTEX,   13.86157,  46.14935,  40.04964,
     VERTEX,   13.62208,  45.24604,  40.26939,
     VERTEX,   13.05171,  44.70617,  40.82148,
     VERTEX,   12.36832,  44.73594,  41.49505,
     VERTEX,   11.83294,  45.32398,  42.03281,
     VERTEX,   11.65007,  46.24568,  42.22935,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   12.75582,  46.19751,  41.13949,
                       
     VERTEX,   11.65007,  46.24568,  42.22935,
     VERTEX,   11.88956,  47.14898,  42.00960,
     VERTEX,   12.45993,  47.68885,  41.45750,
     VERTEX,   13.14332,  47.65908,  40.78393,
     VERTEX,   13.67870,  47.07104,  40.24618,
     VERTEX,   13.86157,  46.14935,  40.04964,
     VERTEX,   13.62208,  45.24604,  40.26939,
     VERTEX,   13.05171,  44.70617,  40.82148,
     VERTEX,   12.36832,  44.73594,  41.49505,
     VERTEX,   11.83294,  45.32398,  42.03281,
     VERTEX,   11.65007,  46.24568,  42.22935,
                       
     END,              
                       
     CYLINDER,   20.51300,  46.05700,  49.01600,  12.75582,  46.19751,  41.13949,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    0.84136,  42.43451,  25.29145,
                       
     VERTEX,    5.80798,  43.16993,  30.96664,
     VERTEX,    5.66429,  44.11591,  30.88861,
     VERTEX,    5.89032,  44.89621,  30.37711,
     VERTEX,    6.39972,  45.21281,  29.62753,
     VERTEX,    6.99793,  44.94476,  28.92617,
     VERTEX,    7.45644,  44.19446,  28.54094,
     VERTEX,    7.60013,  43.24849,  28.61897,
     VERTEX,    7.37410,  42.46817,  29.13047,
     VERTEX,    6.86470,  42.15158,  29.88005,
     VERTEX,    6.26649,  42.41962,  30.58141,
     VERTEX,    5.80798,  43.16993,  30.96664,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,    6.63221,  43.68219,  29.75379,
                       
     VERTEX,    5.80798,  43.16993,  30.96664,
     VERTEX,    5.66429,  44.11591,  30.88861,
     VERTEX,    5.89032,  44.89621,  30.37711,
     VERTEX,    6.39972,  45.21281,  29.62753,
     VERTEX,    6.99793,  44.94476,  28.92617,
     VERTEX,    7.45644,  44.19446,  28.54094,
     VERTEX,    7.60013,  43.24849,  28.61897,
     VERTEX,    7.37410,  42.46817,  29.13047,
     VERTEX,    6.86470,  42.15158,  29.88005,
     VERTEX,    6.26649,  42.41962,  30.58141,
     VERTEX,    5.80798,  43.16993,  30.96664,
                       
     END,              
                       
     CYLINDER,   16.00200,  45.70100,  36.97400,   6.63221,  43.68219,  29.75379,   0.80000,
                 1.000,  1.000,  1.000,  1.000,  1.000,  1.000,
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   14.49147,  29.01690,  18.89790,
                       
     VERTEX,   18.77744,  29.47931,  24.39585,
     VERTEX,   18.70649,  30.43052,  24.28735,
     VERTEX,   19.01129,  31.17779,  23.76747,
     VERTEX,   19.57542,  31.43569,  23.03478,
     VERTEX,   20.18341,  31.10572,  22.36914,
     VERTEX,   20.60302,  30.31391,  22.02481,
     VERTEX,   20.67397,  29.36270,  22.13332,
     VERTEX,   20.36917,  28.61543,  22.65320,
     VERTEX,   19.80504,  28.35752,  23.38589,
     VERTEX,   19.19705,  28.68750,  24.05153,
     VERTEX,   18.77744,  29.47931,  24.39585,
                       
     END,              
                       
     BEGIN,  TRIANGLE_FAN, 
     COLOR,   1.000,  1.000,  1.000,
                       
     VERTEX,   19.69023,  29.89661,  23.21033,
                       
     VERTEX,   18.77744,  29.47931,  24.39585,
     VERTEX,   18.70649,  30.43052,  24.28735,
     VERTEX,   19.01129,  31.17779,  23.76747,
     VERTEX,   19.57542,  31.43569,  23.03478,
     VERTEX,   20.18341,  31.10572,  22.36914,
     VERTEX,   20.60302,  30.31391,  22.02481,
     VERTEX,   20.67397,  29.36270,  22.13332,
     VERTEX,   20.36917,  28.61543,  22.65320,
     VERTEX,   19.80504,  28.35752,  23.38589,
     VERTEX,   19.19705,  28.68750,  24.05153,
     VERTEX,   18.77744,  29.47931,  24.39585,
                       
     END,              
                       
     CYLINDER,   28.10200,  31.32000,  30.18800,  19.69023,  29.89661,  23.21033,   0.80000,
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
