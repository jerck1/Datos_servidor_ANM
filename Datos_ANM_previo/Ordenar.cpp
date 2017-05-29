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


//a:numero de residuos, Nrc numero de cutoffs, unk numero de residuos desconocidos
const int a=545-47, Nrc=8, unk=47;
int s=5+1;//Numero de maximos( debe sumarse 1)que desea ver en la tabla
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
				  temp2 = bfac[k][l][i][0];
				  bfac[k][l][i][0] = bfac[k][l][j][0];
				  bfac[k][l][j][0] = temp2;
				}
	   }
}
}
char* ptetabla(int j){
char* p="\\multicolumn{2}{c}{Con solo C$\\alpha$}\\\\\\hline";
char* q="\\multicolumn{2}{c}{C$\\alpha$ $+$ Gal}\\\\\\hline";
char* r="\\multicolumn{2}{c}{C$\\alpha$ $+$ Gal $+$ Na}\\\\\\hline";
char* t="\\multicolumn{2}{c}{C$\\alpha$ $+$ Na}\\\\\\hline";
 switch(j){
	case 0: return (char *) p;
	case 1: return (char *) q;
	case 2: return (char *)r;
	case 3: return (char *)t;

}
}
int main () {
//A continuacion se define la matriz de matrices A
//Con dimensiones
//14 es el numero de distancias de corte. Por cada distancia de corte:
// 4 tablas para Ca, Ca+Gal, Ca+Gal+Na, Ca+Na, por c/u de las 4 tablas:
//    el numero de residuos y 4 columnas con el # de residuo, , , ,
double A[Nrc][4][2028][4];
int nm=8;
////////////////////////////////////////////////////////////////////////con solo Ca
ifstream FichCa[nm];
int m=1980, n=4; //1012 con solo Ca
FichCa[0].open("b_factor_Ca_7.csv");
FichCa[1].open("b_factor_Ca_8.csv");
FichCa[2].open("b_factor_Ca_9.csv");
FichCa[3].open("b_factor_Ca_10.csv");
FichCa[4].open("b_factor_Ca_11.csv");
FichCa[5].open("b_factor_Ca_12.csv");
FichCa[6].open("b_factor_Ca_13.csv");
FichCa[7].open("b_factor_Ca_14.csv");

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
int m2=2028;//1036 con Ca+Gal debido a que se incluyen los atomos de la Gal
ifstream FichCaGal[nm];
FichCaGal[0].open("b_factor_Ca_7_Gal_7.csv");
FichCaGal[1].open("b_factor_Ca_8_Gal_8.csv");
FichCaGal[2].open("b_factor_Ca_9_Gal_9.csv");
FichCaGal[3].open("b_factor_Ca_10_Gal_10.csv");
FichCaGal[4].open("b_factor_Ca_11_Gal_11.csv");
FichCaGal[5].open("b_factor_Ca_12_Gal_12.csv");
FichCaGal[6].open("b_factor_Ca_13_Gal_13.csv");
FichCaGal[7].open("b_factor_Ca_14_Gal_14.csv");

for(int k=0;k<nm;k++){
for(int i=0;i<m2;i++){
	for(int j=0;j<4;j++)
		FichCaGal[k]>>A[k][1][i][j];
	}
FichCaGal[k].close();
}

////////////////////////////////////////////////////////////////////////Ca mas Gal mas Na

int m3=2032;//1038 con Ca+Gal+Na
ifstream FichCaNaGal[nm];
FichCaNaGal[0].open("b_factor_Ca_7_Na_7_Gal_7.csv");
FichCaNaGal[1].open("b_factor_Ca_8_Na_8_Gal_8.csv");
FichCaNaGal[2].open("b_factor_Ca_9_Na_9_Gal_9.csv");
FichCaNaGal[3].open("b_factor_Ca_10_Na_10_Gal_10.csv");
FichCaNaGal[4].open("b_factor_Ca_11_Na_11_Gal_11.csv");
FichCaNaGal[5].open("b_factor_Ca_12_Na_12_Gal_12.csv");
FichCaNaGal[6].open("b_factor_Ca_13_Na_13_Gal_13.csv");
FichCaNaGal[7].open("b_factor_Ca_14_Na_14_Gal_14.csv");

for(int k=0;k<nm;k++){
for(int i=0;i<m3;i++){
	for(int j=0;j<4;j++)
		FichCaNaGal[k]>>A[k][2][i][j];
	}
FichCaNaGal[k].close();
}
for(int i=0;i<Nrc;i++){
	for(int j=0;j<4;j++){
		for(int k=0;k<10;k++)
			cout<<A[i][j][k][3]<<" ";
cout<<endl;
}
cout<<endl;
}
////////////////////////////////////////////////////////////////////////Ca mas Na

int m4=1984;//1014 con Ca+Na
ifstream FichCaNa[nm];
FichCaNa[0].open("b_factor_Ca_7_Na_7.csv");
FichCaNa[1].open("b_factor_Ca_8_Na_8.csv");
FichCaNa[2].open("b_factor_Ca_9_Na_9.csv");
FichCaNa[3].open("b_factor_Ca_10_Na_10.csv");
FichCaNa[4].open("b_factor_Ca_11_Na_11.csv");
FichCaNa[5].open("b_factor_Ca_12_Na_12.csv");
FichCaNa[6].open("b_factor_Ca_13_Na_13.csv");
FichCaNa[7].open("b_factor_Ca_14_Na_14.csv");

for(int k=0;k<nm;k++){
for(int i=0;i<m4;i++){
	for(int j=0;j<4;j++)
		FichCaNa[k]>>A[k][3][i][j];
	}
FichCaNa[k].close();
}

///////////////////////////////////////////////////////////////////////////////////


//En bfac se guardan los factores b:
// 	4 tablas para Ca, Ca+Gal, Ca+Gal+Na, Ca+Na, por c/u de las 4 tablas:
//	el numero de residuos(cadena A) y 2 columnas con el # de residuo y el factor b teorico
//En bmax se guardan los factores b maximos con su numero de residuo
double bfac[Nrc][4][a][2], bmax[Nrc][2];
for(int i=0;i<Nrc;i++)
	for(int j=0;j<4;j++)
		for(int k=0;k<a;k++){
			bfac[i][j][k][0]=A[i][j][k][0];
			bfac[i][j][k][1]=A[i][j][k][3];
}

////////////////7//////////7/
//aqui llamamamos a la funcion que ordena
sort_matrix(bfac,a);
////////////////////////////7
//Llamamos a los maximos para normalizar
ifstream max;
max.open("max.csv");
for(int i=0;i<Nrc;i++){
	for(int j=0;j<2;j++)
		max>>bmax[i][j];
	}
max.close();
//Enviar info a dos archivos planos (.tex)
//off file stream
ofstream lista_max;
lista_max.open("lista_max.tex");
///////////"10 primeros máximos"
//No se usa la primera fila porque este no es un maximo, error en el programa
for(int k=1;k<Nrc;k++){
	lista_max<<"\\begin{tabular}[c]{|c|c|}"<<endl;
	lista_max<<"\\multicolumn{2}{c}{$R_c=$"<<k+7<<"$\\AA$"<<"}\\\\\\hline"<<endl;
	lista_max<<"\\textbf{Residuo}&\\textbf{Factor B}\\\\\\hline"<<endl;
		for(int j=0;j<4;j++){
			lista_max<<ptetabla(j)<<endl;
			for(int i=1;i<s;i++)
				lista_max<<setw(10)<<bfac[k][j][i][0]+unk<<"&"<<setw(10)<<bfac[k][j][i][1]/bmax[k][1]<<"\\\\"<<endl;
			lista_max<<"\\hline"<<endl;		
		}
	lista_max<<"\\end{tabular}"<<endl;
}
lista_max.close();
ofstream lista_min;
//////////"10 minimos"
//En el segundo for se agrega la primera fila olvidada arriba, que corresponde al minimo
lista_min.open("lista_min.tex");
for(int k=1;k<Nrc;k++){
	lista_min<<"\\begin{tabular}[c]{|c|c|}"<<endl;
	lista_min<<"\\multicolumn{2}{c}{$R_c=$"<<k+7<<"$\\AA$"<<"}\\\\\\hline"<<endl;
	lista_min<<"\\textbf{Residuo}&\\textbf{Factor B}\\\\\\hline"<<endl;
		for(int j=0;j<4;j++){
			lista_min<<ptetabla(j)<<endl;
			for(int i=a-s+2;i<a;i++)
				lista_min<<setw(10)<<bfac[k][j][i][0]+unk<<"&"<<setw(10)<<bfac[k][j][i][1]/bmax[k][1]<<"\\\\"<<endl;
			lista_min<<setw(10)<<bfac[k][j][0][0]+unk<<"&"<<setw(10)<<bfac[k][j][0][1]/bmax[k][1]<<"\\\\\\hline"<<endl;
		}
	lista_min<<"\\end{tabular}"<<endl;
}
lista_min.close();
return 0;
}
