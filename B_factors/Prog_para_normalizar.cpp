#include <iostream>
#include <cstdlib>
#include <math.h>
#include "fstream"
#include "string"
#include<iomanip>//para manipular el setw
using namespace std;

int main(){

//Maximos
//hay 14 maximos, desde 7 hasta 20
ifstream miFichero("max.csv");
int nm=14;
double M[nm][2];
for(int i=0;i<nm;i++)
        for(int j=0;j<2;j++)
                miFichero>>M[i][j];
miFichero.close();
//A continuacion se define la matriz de matrices A
//Con dimensiones
//14 es el numero de distancias de corte, por cada distancia de corte:
// 4 tablas para Ca, Ca+Gal, Ca+Gal+Na, Ca+Na, por c/u de las 4 tablas:
//    el numero de residuos y 4 columnas con el # de residuo, , , ,
double A[14][4][2028][4]; 
////////////////////////////////////////////////////////////////////////con solo Ca
ifstream FichCa[nm];
int m=1012, n=4; //1012 con solo Ca
FichCa[0].open("b_factor_Ca_7.csv");
FichCa[1].open("b_factor_Ca_8.csv");
FichCa[2].open("b_factor_Ca_9.csv");
FichCa[3].open("b_factor_Ca_10.csv");
FichCa[4].open("b_factor_Ca_11.csv");
FichCa[5].open("b_factor_Ca_12.csv");
FichCa[6].open("b_factor_Ca_13.csv");
FichCa[7].open("b_factor_Ca_14.csv");
FichCa[8].open("b_factor_Ca_15.csv");
FichCa[9].open("b_factor_Ca_16.csv");
FichCa[10].open("b_factor_Ca_17.csv");
FichCa[11].open("b_factor_Ca_18.csv");
FichCa[12].open("b_factor_Ca_19.csv");
FichCa[13].open("b_factor_Ca_20.csv");
//////Entrada de datos

//Es como un cin miFichero>>A[i][j];
for(int k=0;k<nm;k++){
for(int i=0;i<m;i++){
	for(int j=0;j<4;j++)
		FichCa[k]>>A[0][0][i][j];
	}
FichCa[k].close();
}
////////////////////////////////////////////////////////////////////////Ca mas Gal
int m2=1036;//1036 con Ca+Gal debido a que se incluyen los atomos de la Gal
ifstream FichCaGal[nm];
FichCaGal[0].open("b_factor_Ca_7_Gal_7.csv");
FichCaGal[1].open("b_factor_Ca_8_Gal_8.csv");
FichCaGal[2].open("b_factor_Ca_9_Gal_9.csv");
FichCaGal[3].open("b_factor_Ca_10_Gal_10.csv");
FichCaGal[4].open("b_factor_Ca_11_Gal_11.csv");
FichCaGal[5].open("b_factor_Ca_12_Gal_12.csv");
FichCaGal[6].open("b_factor_Ca_13_Gal_13.csv");
FichCaGal[7].open("b_factor_Ca_14_Gal_14.csv");
FichCaGal[8].open("b_factor_Ca_15_Gal_15.csv");
FichCaGal[9].open("b_factor_Ca_16_Gal_16.csv");
FichCaGal[10].open("b_factor_Ca_17_Gal_17.csv");
FichCaGal[11].open("b_factor_Ca_18_Gal_18.csv");
FichCaGal[12].open("b_factor_Ca_19_Gal_19.csv");
FichCaGal[13].open("b_factor_Ca_20_Gal_20.csv");

for(int k=0;k<nm;k++){
for(int i=0;i<m2;i++){
	for(int j=0;j<4;j++)
		FichCaGal[k]>>A[0][1][i][j];
	}
FichCaGal[k].close();
}

////////////////////////////////////////////////////////////////////////Ca mas Gal mas Na

int m3=1038;//1038 con Ca+Gal+Na
ifstream FichCaNaGal[nm];
FichCaNaGal[0].open("b_factor_Ca_7_Na_7_Gal_7.csv");
FichCaNaGal[1].open("b_factor_Ca_8_Na_8_Gal_8.csv");
FichCaNaGal[2].open("b_factor_Ca_9_Na_9_Gal_9.csv");
FichCaNaGal[3].open("b_factor_Ca_10_Na_10_Gal_10.csv");
FichCaNaGal[4].open("b_factor_Ca_11_Na_11_Gal_11.csv");
FichCaNaGal[5].open("b_factor_Ca_12_Na_12_Gal_12.csv");
FichCaNaGal[6].open("b_factor_Ca_13_Na_13_Gal_13.csv");
FichCaNaGal[7].open("b_factor_Ca_14_Na_14_Gal_14.csv");
FichCaNaGal[8].open("b_factor_Ca_15_Na_15_Gal_15.csv");
FichCaNaGal[9].open("b_factor_Ca_16_Na_16_Gal_16.csv");
FichCaNaGal[10].open("b_factor_Ca_17_Na_17_Gal_17.csv");
FichCaNaGal[11].open("b_factor_Ca_18_Na_18_Gal_18.csv");
FichCaNaGal[12].open("b_factor_Ca_19_Na_19_Gal_19.csv");
FichCaNaGal[13].open("b_factor_Ca_20_Na_20_Gal_20.csv");

for(int k=0;k<nm;k++){
for(int i=0;i<m2;i++){
	for(int j=0;j<4;j++)
		FichCaNaGal[k]>>A[0][2][i][j];
	}
FichCaNaGal[k].close();
}

////////////////////////////////////////////////////////////////////////Ca mas Na

int m4=1014;//1014 con Ca+Na
ifstream FichCaNa[nm];
FichCaNa[0].open("b_factor_Ca_7_Na_7.csv");
FichCaNa[1].open("b_factor_Ca_8_Na_8.csv");
FichCaNa[2].open("b_factor_Ca_9_Na_9.csv");
FichCaNa[3].open("b_factor_Ca_10_Na_10.csv");
FichCaNa[4].open("b_factor_Ca_11_Na_11.csv");
FichCaNa[5].open("b_factor_Ca_12_Na_12.csv");
FichCaNa[6].open("b_factor_Ca_13_Na_13.csv");
FichCaNa[7].open("b_factor_Ca_14_Na_14.csv");
FichCaNa[8].open("b_factor_Ca_15_Na_15.csv");
FichCaNa[9].open("b_factor_Ca_16_Na_16.csv");
FichCaNa[10].open("b_factor_Ca_17_Na_17.csv");
FichCaNa[11].open("b_factor_Ca_18_Na_18.csv");
FichCaNa[12].open("b_factor_Ca_19_Na_19.csv");
FichCaNa[13].open("b_factor_Ca_20_Na_20.csv");
for(int k=0;k<nm;k++){
for(int i=0;i<m2;i++){
	for(int j=0;j<4;j++)
		FichCaNa[k]>>A[0][3][i][j];
	}
FichCaNa[k].close();
}
///////////////////////////////////////////////////////////////////////////////////


//Enviar informacion a un archivo plano de salida
//off file stream
//se llamara miFichsal[14] con tamano 14 (de 7 hasta 14)
//es decir no es un solo archivo sino son 14 archivos por cada rc
ofstream miFichsal[14];
miFichsal[0].open("n7.csv");
miFichsal[1].open("n8.csv");
miFichsal[2].open("n9.csv");
miFichsal[3].open("n10.csv");
miFichsal[4].open("n11.csv");
miFichsal[5].open("n12.csv");
miFichsal[6].open("n13.csv");
miFichsal[7].open("n14.csv");
miFichsal[8].open("n15.csv");
miFichsal[9].open("n16.csv");
miFichsal[10].open("n17.csv");
miFichsal[11].open("n18.csv");
miFichsal[12].open("n19.csv");
miFichsal[13].open("n20.csv");
//setw(): reserva para cada dato 10 lugares 
/*
Se guardan todos los datos de la cadena A; n=530
A[0][0][i][0] numero de residuo
A[0][j][i][3] factor b experimental para el residuo i, 
con los sustratos j (0 para Ca, 1 para CaGal, 2 para CaGalNa, 3para CaNa)
con distancia de corte r_0
Indice k: r_k=7,8,...14
*/
for(int k=0;k<14;k++){
	for(int i=0;i<543;i++){ 
		miFichsal[k]<<setw(10)<<A[k][0][i][0];
			for(int j=0;j<4;j++)
				miFichsal[k]<<"\t"<<setw(10)<<A[k][j][i][3]/M[k][1];
		miFichsal[k]<<endl;
}
miFichsal[k].close();
}
//print
/*for(int i=0;i<m;i++){
	std::cout<<A[0][0][i][0]<<"\t\t"<<A[0][0][i][1]<<endl;
}*/
system("Pause");
return 0;
}
