#include <iostream>
#include <cstdlib>
#include <math.h>
#include "fstream"
#include "string"
#include<iomanip>//para manipular el setw
using namespace std;

int main(){

//Maximos
ifstream miFichero("max.csv");
double M[8][2];
for(int i=0;i<8;i++)
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
int m=1012, n=4; //1012 con solo Ca
ifstream miFichero1("b_factor_7.csv");
ifstream miFichero2("b_factor_8.csv");
ifstream miFichero3("b_factor_9.csv");
ifstream miFichero4("b_factor_10.csv");
ifstream miFichero5("b_factor_11.csv");
ifstream miFichero6("b_factor_12.csv");
ifstream miFichero7("b_factor_13.csv");
ifstream miFichero8("b_factor_14.csv");
ifstream miFichero9("b_factor_15.csv");
ifstream miFichero10("b_factor_16.csv");
ifstream miFichero110("b_factor_17.csv");
ifstream miFichero120("b_factor_18.csv");
ifstream miFichero130("b_factor_19.csv");
ifstream miFichero14("b_factor_20.csv");
//////Entrada de datos

//Es como un cin miFichero>>A[i][j];
for(int i=0;i<m;i++){
	for(int j=0;j<4;j++)
		miFichero1>>A[0][0][i][j];
	}
//Se cierra el archivo porque sino se puede danar
miFichero1.close();
for(int i=0;i<m;i++){
	for(int j=0;j<4;j++)
	miFichero2>>A[1][0][i][j];
	}
miFichero2.close();
for(int i=0;i<m;i++){
	for(int j=0;j<4;j++)
	miFichero3>>A[2][0][i][j];
	}
miFichero3.close();
for(int i=0;i<m;i++){
	for(int j=0;j<4;j++)
	miFichero4>>A[3][0][i][j];
	}
//Se cierra el archivo porque sino se puede danar
miFichero4.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
 	miFichero5>>A[4][0][i][j];
	}
miFichero5.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero6>>A[5][0][i][j];
	 }
miFichero6.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero7>>A[6][0][i][j];
	}
miFichero7.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero8>>A[7][0][i][j];
	}
miFichero8.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero9>>A[8][0][i][j];
	}
miFichero9.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero10>>A[9][0][i][j];
	}
miFichero10.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero110>>A[10][0][i][j];
	}
miFichero110.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero120>>A[11][0][i][j];
	}
miFichero120.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero130>>A[12][0][i][j];
	}
miFichero130.close();
for(int i=0;i<m;i++){
for(int j=0;j<4;j++)
	miFichero14>>A[13][0][i][j];
	}
miFichero14.close();

////////////////////////////////////////////////////////////////////////Ca mas Gal

int m2=1036;//1036 con Ca+Gal debido a que se incluyen los atomos de la Gal
ifstream miFichero11("b_factor_Ca_7_Gal_7.csv");
ifstream miFichero21("b_factor_Ca_8_Gal_8.csv");
ifstream miFichero31("b_factor_Ca_9_Gal_9.csv");
ifstream miFichero41("b_factor_Ca_10_Gal_10.csv");
ifstream miFichero51("b_factor_Ca_11_Gal_11.csv");
ifstream miFichero61("b_factor_Ca_12_Gal_12.csv");
ifstream miFichero71("b_factor_Ca_13_Gal_13.csv");
ifstream miFichero81("b_factor_Ca_14_Gal_14.csv");
ifstream miFichero91("b_factor_Ca_15_Gal_15.csv");
ifstream miFichero101("b_factor_Ca_16_Gal_16.csv");
ifstream miFichero111("b_factor_Ca_17_Gal_17.csv");
ifstream miFichero121("b_factor_Ca_18_Gal_18.csv");
ifstream miFichero131("b_factor_Ca_19_Gal_19.csv");
ifstream miFichero141("b_factor_Ca_20_Gal_20.csv");

for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero11>>A[0][1][i][j];
	}
//Se cierra el archivo porque sino se puede danar
miFichero11.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero21>>A[1][1][i][j];
}
miFichero21.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero31>>A[2][1][i][j];
}
miFichero31.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero41>>A[3][1][i][j];
}
//Se cierra el archivo porque sino se puede danar
miFichero41.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
 	miFichero51>>A[4][1][i][j];
}
miFichero51.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero61>>A[5][1][i][j];
}
miFichero61.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero71>>A[6][1][i][j];
}
miFichero71.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero81>>A[7][1][i][j];
}
miFichero81.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero91>>A[8][1][i][j];
}
miFichero91.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero101>>A[9][1][i][j];
}
miFichero101.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero111>>A[10][1][i][j];
}
miFichero111.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero121>>A[11][1][i][j];
}
miFichero121.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero131>>A[12][1][i][j];
}
miFichero131.close();
for(int i=0;i<m2;i++){
for(int j=0;j<4;j++)
	miFichero141>>A[13][1][i][j];
}
miFichero141.close();

////////////////////////////////////////////////////////////////////////Ca mas Gal mas Na

int m3=1038;//2032 con Ca+Gal+Na
ifstream miFichero12("b_factor_Ca_7_Na_7_Gal_7.csv");
ifstream miFichero22("b_factor_Ca_8_Na_8_Gal_8.csv");
ifstream miFichero32("b_factor_Ca_9_Na_9_Gal_9.csv");
ifstream miFichero42("b_factor_Ca_10_Na_10_Gal_10.csv");
ifstream miFichero52("b_factor_Ca_11_Na_11_Gal_11.csv");
ifstream miFichero62("b_factor_Ca_12_Na_12_Gal_12.csv");
ifstream miFichero72("b_factor_Ca_13_Na_13_Gal_13.csv");
ifstream miFichero82("b_factor_Ca_14_Na_14_Gal_14.csv");
ifstream miFichero92("b_factor_Ca_15_Na_15_Gal_15.csv");
ifstream miFichero102("b_factor_Ca_16_Na_16_Gal_16.csv");
ifstream miFichero112("b_factor_Ca_17_Na_17_Gal_17.csv");
ifstream miFichero122("b_factor_Ca_18_Na_18_Gal_18.csv");
ifstream miFichero132("b_factor_Ca_19_Na_19_Gal_19.csv");
ifstream miFichero142("b_factor_Ca_20_Na_20_Gal_20.csv");

for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero12>>A[0][2][i][j];
}
//Se cierra el archivo porque sino se puede danar
miFichero12.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero22>>A[1][2][i][j];
}
miFichero22.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero32>>A[2][2][i][j];
}
miFichero32.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero42>>A[3][2][i][j];
}
//Se cierra el archivo porque sino se puede danar
miFichero42.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
 	miFichero52>>A[4][2][i][j];
}
miFichero52.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero62>>A[5][2][i][j];
}
miFichero62.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero72>>A[6][2][i][j];
}
miFichero72.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero82>>A[7][2][i][j];
}
miFichero82.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero82>>A[8][2][i][j];
}
miFichero92.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero92>>A[9][2][i][j];
}
miFichero102.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero102>>A[10][2][i][j];
}
miFichero112.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero112>>A[11][2][i][j];
}
miFichero122.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero132>>A[12][2][i][j];
}
miFichero132.close();
for(int i=0;i<m3;i++){
for(int j=0;j<4;j++)
	miFichero142>>A[13][2][i][j];
}
miFichero142.close();

////////////////////////////////////////////////////////////////////////Ca mas Na

int m4=1014;//1014 con Ca+Na
ifstream miFichero13("b_factor_CA_7_Na_7.csv");

ifstream miFichero23("b_factor_CA_8_Na_8.csv");
ifstream miFichero33("b_factor_CA_9_Na_9.csv");
ifstream miFichero43("b_factor_CA_10_Na_10.csv");
ifstream miFichero53("b_factor_CA_11_Na_11.csv");
ifstream miFichero63("b_factor_CA_12_Na_12.csv");
ifstream miFichero73("b_factor_CA_13_Na_13.csv");
ifstream miFichero83("b_factor_CA_14_Na_14.csv");
ifstream miFichero93("b_factor_CA_15_Na_15.csv");
ifstream miFichero103("b_factor_CA_16_Na_16.csv");
ifstream miFichero113("b_factor_CA_17_Na_17.csv");
ifstream miFichero123("b_factor_CA_18_Na_18.csv");
ifstream miFichero133("b_factor_CA_19_Na_19.csv");
ifstream miFichero143("b_factor_CA_20_Na_20.csv");
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero13>>A[0][3][i][j];
}
//Se cierra el archivo porque sino se puede danar
miFichero13.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero23>>A[1][3][i][j];
}
miFichero23.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero33>>A[2][3][i][j];
}
miFichero33.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero43>>A[3][3][i][j];
}
//Se cierra el archivo porque sino se puede danar
miFichero43.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
 	miFichero53>>A[4][3][i][j];
}
miFichero53.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero63>>A[5][3][i][j];
}
miFichero63.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero73>>A[6][3][i][j];
}
miFichero73.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero83>>A[7][3][i][j];
}
miFichero83.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero93>>A[8][3][i][j];
}
miFichero93.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero103>>A[9][3][i][j];
}
miFichero103.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero113>>A[10][3][i][j];
}
miFichero113.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero123>>A[11][3][i][j];
}
miFichero123.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero133>>A[12][3][i][j];
}
miFichero133.close();
for(int i=0;i<m4;i++){
for(int j=0;j<4;j++)
	miFichero143>>A[13][3][i][j];
}
miFichero143.close();
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
