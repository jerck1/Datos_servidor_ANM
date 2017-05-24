// sort algorithm example
#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <cstdlib>
#include <math.h>
#include "fstream"
#include "string"
#include<iomanip>//para manipular el setw
using namespace std;

//bubble sort

const int a=546, Nrc=14;
void sort_matrix(double bfac[Nrc][4][a][2], int arraySize){
//2 for externos para los indices # del residuo y si es Ca, Ca+Gal,...
//2 for internos ordenan un array
double temp, temp2;
for(int k = 0; k < Nrc; k++)
for(int l = 0; l < 4; l++)
for(int i = 0; i < arraySize; i++)
{
	  for(int j = 1; j < arraySize-1; j++)
	  {
			   if(bfac[k][l][j][1] < bfac[k][l][i][1])
			   {
				  temp = bfac[k][l][i][1] ;
				  bfac[k][l][i][1] = bfac[k][l][j][1];
				  bfac[k][l][j][1] = temp;
				  temp2 = bfac[k][l][i][0] ;
				  bfac[k][l][i][0] = bfac[k][l][j][0];
				  bfac[k][l][j][0] = temp2;
				}
	   }
}
}

int main () {
//A continuacion se define la matriz de matrices A
//Con dimensiones
//14 es el numero de distancias de corte. Por cada distancia de corte:
// 4 tablas para Ca, Ca+Gal, Ca+Gal+Na, Ca+Na, por c/u de las 4 tablas:
//    el numero de residuos y 4 columnas con el # de residuo, , , ,
double A[Nrc][4][1038][4];
//En B se almacenan los factores b de los sustratos y los ligandos
double B[Nrc][4][26][4];
int nm=14;
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
		FichCa[k]>>A[k][0][i][j];
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

int i1;
for(int k=0;k<nm;k++){
	i1=0;
	while(i1<m2){
		if(i1<517){
			for(int j=0;j<4;j++)
				FichCaGal[k]>>A[k][1][i1][j];
		}else{
			while(i1<529){
			for(int j=0;j<4;j++)
			FichCaGal[k]>>B[k][1][i1-517][j];
			i1++;
			}
			for(int j=0;j<4;j++)
				FichCaGal[k]>>A[k][1][i1-12][j];
		}
		i1++;
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

int i2;
for(int k=0;k<nm;k++){
	i2=0;
	while(i2<m3){
		if(i2<517){
			for(int j=0;j<4;j++)
				FichCaNaGal[k]>>A[k][2][i2][j];
		}else{
			while(i2<530){
			for(int j=0;j<4;j++)
			FichCaNaGal[k]>>B[k][2][i2-517][j];
			i2++;
			}
			for(int j=0;j<4;j++)
				FichCaNaGal[k]>>A[k][2][i2-13][j];
		}
		i2++;
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

int i3;
for(int k=0;k<nm;k++){
	i3=0;
	while(i3<m4){
		if(i3<517){
			for(int j=0;j<4;j++)
				FichCaNa[k]>>A[k][3][i3][j];
		}else{
			while(i3<518){
			for(int j=0;j<4;j++)
			FichCaNa[k]>>B[k][3][i3-517][j];
			i3++;
			}
			for(int j=0;j<4;j++){
				FichCaNa[k]>>A[k][3][i3-1][j];
			}
		}
		i3++;
	}
FichCaNa[k].close();
}

///////////////////////////////////////////////////////////////////////////////////


//En bfac se guardan los factores b:
// 	4 tablas para Ca, Ca+Gal, Ca+Gal+Na, Ca+Na, por c/u de las 4 tablas:
//	el numero de residuos(cadena A) y 2 columnas con el # de residuo y el factor b teorico
//En bord se guardan los factores b ordenados con su numero de residuo
double bfac[Nrc][4][a][2], bord[a];
//double bfac[a], bord[a];
for(int i=0;i<14;i++)
	for(int j=0;j<4;j++)
		for(int k=0;k<a;k++){
			bfac[i][j][k][0]=A[i][j][k][0];
			bfac[i][j][k][1]=A[i][j][k][3];
}
sort_matrix(bfac,a);
cout<<"Maximos"<<endl;
for(int i=0;i<10;i++)
cout<<bfac[2][0][i][0]<<" "<<bfac[2][0][i][1]<<endl;
cout<<"Minimos"<<endl;
for(int i=540;i<546;i++)
cout<<bfac[2][0][i][0]<<" "<<bfac[2][0][i][1]<<endl;

return 0;
}
