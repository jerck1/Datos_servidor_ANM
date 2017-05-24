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
double A[8][4][2028][4];
////////////////////////////////////////////////////////////////////////con solo Ca
int m=1980, n=4; //1980 con solo Ca
ifstream miFichero1("b_factor_7.csv");
ifstream miFichero2("b_factor_8.csv");
ifstream miFichero3("b_factor_9.csv");
ifstream miFichero4("b_factor_10.csv");
ifstream miFichero5("b_factor_11.csv");
ifstream miFichero6("b_factor_12.csv");
ifstream miFichero7("b_factor_13.csv");
ifstream miFichero8("b_factor_14.csv");

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

////////////////////////////////////////////////////////////////////////Ca mas Gal

int m2=2028;//2028 con Ca+Gal
ifstream miFichero11("b_factor_Ca_7_Gal_7.csv");
ifstream miFichero21("b_factor_Ca_8_Gal_8.csv");
ifstream miFichero31("b_factor_Ca_9_Gal_9.csv");
ifstream miFichero41("b_factor_Ca_10_Gal_10.csv");
ifstream miFichero51("b_factor_Ca_11_Gal_11.csv");
ifstream miFichero61("b_factor_Ca_12_Gal_12.csv");

ifstream miFichero71("b_factor_Ca_13_Gal_13.csv");

ifstream miFichero81("b_factor_Ca_14_Gal_14.csv");


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

////////////////////////////////////////////////////////////////////////Ca mas Gal mas Na

int m3=2032;//2032 con Ca+Gal+Na
ifstream miFichero12("b_factor_Ca_7_Na_7_Gal_7.csv");
ifstream miFichero22("b_factor_Ca_8_Na_8_Gal_8.csv");
ifstream miFichero32("b_factor_Ca_9_Na_9_Gal_9.csv");
ifstream miFichero42("b_factor_Ca_10_Na_10_Gal_10.csv");
ifstream miFichero52("b_factor_Ca_11_Na_11_Gal_11.csv");
ifstream miFichero62("b_factor_Ca_12_Na_12_Gal_12.csv");
ifstream miFichero72("b_factor_Ca_13_Na_13_Gal_13.csv");
ifstream miFichero82("b_factor_Ca_14_Na_14_Gal_14.csv");
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

////////////////////////////////////////////////////////////////////////Ca mas Na

int m4=1984;//1984 con Ca+Na
ifstream miFichero13("b_factor_CA_7_Na_7.csv");

ifstream miFichero23("b_factor_CA_8_Na_8.csv");
ifstream miFichero33("b_factor_CA_9_Na_9.csv");
ifstream miFichero43("b_factor_CA_10_Na_10.csv");
ifstream miFichero53("b_factor_CA_11_Na_11.csv");
ifstream miFichero63("b_factor_CA_12_Na_12.csv");
ifstream miFichero73("b_factor_CA_13_Na_13.csv");
ifstream miFichero83("b_factor_CA_14_Na_14.csv");

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

///////////////////////////////////////////////////////////////////////////////////


//Enviar info a un archivo plano
//off file stream
ofstream miFichsal[8];
miFichsal[0].open("n7.csv");
miFichsal[1].open("n8.csv");
miFichsal[2].open("n9.csv");
miFichsal[3].open("n10.csv");
miFichsal[4].open("n11.csv");
miFichsal[5].open("n12.csv");
miFichsal[6].open("n13.csv");
miFichsal[7].open("n14.csv");
//setw(): reserva para cada dato 10 lugares 
/*
Se guardan todos los datos de la cadena A; n=530
A[0][0][i][0] numero de residuo
A[0][j][i][3] factor b experimental para el residuo i, 
con los sustratos j (0 para Ca, 1 para CaGal, 2 para CaGalNa, 3para CaNa)
con distancia de corte r_0
Indice k: r_k=7,8,...14
*/
for(int k=0;k<8;k++){
	for(int i=0;i<530;i++){ 
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
