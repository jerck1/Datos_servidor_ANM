set terminal png transparent truecolor
set output "grafica_7_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n7.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n7.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n7.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n7.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_8_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n8.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n8.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n8.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n8.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_9_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n9.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n9.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n9.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n9.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_10_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n10.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n10.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n10.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n10.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_11_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n11.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n11.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n11.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n11.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_12_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n12.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n12.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n12.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n12.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_13_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n13.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n13.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n13.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n13.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"

set terminal png transparent truecolor
set output "grafica_14_A_n.png"
set size 5/5., 3/3.
set xlabel "# Residue"
set ylabel "Mean Square Fluctuation"
set xlabel font ",18"
set ylabel font ",18"

plot [0:543] [0:1.1] "n14.csv" using 1:2 with lines lt rgb 'red' title "C alpha", "n14.csv" using 1:3 with lines lt rgb 'blue' title "C alpha+Gal", "n14.csv" using 1:5 with lines lt rgb 'green' title "C alpha+Na", "n14.csv" using 1:4 with lines lt rgb 'black' title "C alpha+Gal+Na"


