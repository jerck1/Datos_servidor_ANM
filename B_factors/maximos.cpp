#include <iostream>
#include <cstdlib>
#include <math.h>
#include "fstream"
#include "string"
#include<iomanip>//para manipular el setw
using namespace std;


int ImpMat(int m, int n, double xy[][4]){
 for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)
            cout<<xy[i][j]<<"\t";
        cout<<endl;
}
}
//Maximo de una lista
#include <algorithm>    // std::min_element, std::max_element

bool myfn(double i, double j) { return i<j; }

struct myclass {
  bool operator() (double i,double j) { return i<j; }
} myobj;

void trans(int m, int n, double A[][4],double At[][546]){

     for(int i=0;i<m;i++)

             for(int j=0;j<n;j++)

                     At[j][i]=A[i][j];
}
void trans2(int m, int n, double A[][4],double At[][546]){

     for(int i=0;i<m;i++)

             for(int j=0;j<n;j++)

                     At[j][i]=A[i][j];
}
void trans3(int m, int n, double A[][4],double At[][546]){

     for(int i=0;i<m;i++)

             for(int j=0;j<n;j++)

                     At[j][i]=A[i][j];
}
void trans4(int m, int n, double A[][4],double At[][546]){

     for(int i=0;i<m;i++)

             for(int j=0;j<n;j++)

                     At[j][i]=A[i][j];
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main(){

//Acepta el formato plano csv
//input file stream "ifstream": Crea un archivo de entrada de solo lectura
//miFichero("ruta")
//donde se guardan los maximos en el orden: [Ca,CaGal,CaGalNa,CaNa], las filas son las distancias de corte(cuenta a partir de la 7ma fila)
//21 filas por ir desde 7 hasta 20, las primeras 7 estaran vacias 
double C[21][4];
////////////////////////////////////////////////////////////////////////con solo Ca
int m=546, n=4; //546 con solo Ca, 4 columnas del csv en la columna 3 (contando desde 0) estan los factores b teoricos
//Los .csv son los archivos de entrada, en A[m][n] se guardan los valores encontrados en cada csv
ifstream miFichero1("b_factor_7.csv");
double A7[m][4];
double A7t[n][546];
ifstream miFichero2("b_factor_8.csv");
double A8[m][4];
double A8t[n][546];
ifstream miFichero3("b_factor_9.csv");
double A9[m][4];
double A9t[n][546];
ifstream miFichero4("b_factor_10.csv");
double A10[m][4];
double A10t[n][546];
ifstream miFichero5("b_factor_11.csv");
double A11[m][4];
double A11t[n][546];
ifstream miFichero6("b_factor_12.csv");
double A12[m][4];
double A12t[n][546];
ifstream miFichero7("b_factor_13.csv");
double A13[m][4];
double A13t[n][546];
ifstream miFichero8("b_factor_14.csv");
double A14[m][4];
double A14t[n][546];
ifstream miFichero9("b_factor_15.csv");
double A15[m][4];
double A15t[n][546];
ifstream miFichero10("b_factor_16.csv");
double A16[m][4];
double A16t[n][546];
ifstream miFichero110("b_factor_17.csv");
double A17[m][4];
double A17t[n][546];
ifstream miFichero120("b_factor_18.csv");
double A18[m][4];
double A18t[n][546];
ifstream miFichero130("b_factor_19.csv");
double A19[m][4];
double A19t[n][546];
ifstream miFichero14("b_factor_20.csv");
double A20[m][4];
double A20t[n][546];

//////Entrada de datos

//Es como un cin miFichero>>A[i][j];
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero1>>A7[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero1.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero2>>A8[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero2.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero3>>A9[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero3.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero4>>A10[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero4.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero5>>A11[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero5.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero6>>A12[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero6.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero7>>A13[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero7.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero8>>A14[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero8.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero9>>A15[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero9.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero10>>A16[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero10.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero110>>A17[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero110.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero120>>A18[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero120.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero130>>A19[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero130.close();
for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
                miFichero14>>A20[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero14.close();

trans(m,n,A7,A7t);
trans(m,n,A8,A8t);
trans(m,n,A9,A9t);
trans(m,n,A10,A10t);
trans(m,n,A11,A11t);
trans(m,n,A12,A12t);
trans(m,n,A13,A13t);
trans(m,n,A14,A14t);
trans(m,n,A15,A15t);
trans(m,n,A16,A16t);
trans(m,n,A17,A17t);
trans(m,n,A18,A18t);
trans(m,n,A19,A19t);
trans(m,n,A20,A20t);
////Esto es para escoger los valores maximo y minimo
C[7][0]=*std::max_element(A7t[3],A7t[3]+546);
C[8][0]=*std::max_element(A8t[3],A8t[3]+546);
C[9][0]=*std::max_element(A9t[3],A9t[3]+546);
C[10][0]=*std::max_element(A10t[3],A10t[3]+546);
C[11][0]=*std::max_element(A11t[3],A11t[3]+546);
C[12][0]=*std::max_element(A12t[3],A12t[3]+546);
C[13][0]=*std::max_element(A13t[3],A13t[3]+546);
C[14][0]=*std::max_element(A14t[3],A14t[3]+546);
C[15][0]=*std::max_element(A15t[3],A15t[3]+546);
C[16][0]=*std::max_element(A16t[3],A16t[3]+546);
C[17][0]=*std::max_element(A17t[3],A17t[3]+546);
C[18][0]=*std::max_element(A18t[3],A18t[3]+546);
C[19][0]=*std::max_element(A19t[3],A19t[3]+546);
C[20][0]=*std::max_element(A20t[3],A20t[3]+546);
//Enviar info a un archivo plano
std::cout << "The largest b-factor for rc=7 and Ca is (Units of SD) " <<C[7][0]<< '\n';

////////////////////////////////////////////////////////////////////////Ca mas Gal

int m2=546;//546 con Ca+Gal
ifstream miFichero11("b_factor_Ca_7_Gal_7.csv");
double A7g[m2][4];
double A7tg[n][546];
ifstream miFichero21("b_factor_Ca_8_Gal_8.csv");
double A8g[m2][4];
double A8tg[n][546];
ifstream miFichero31("b_factor_Ca_9_Gal_9.csv");
double A9g[m2][4];
double A9tg[n][546];
ifstream miFichero41("b_factor_Ca_10_Gal_10.csv");
double A10g[m2][4];
double A10tg[n][546];
ifstream miFichero51("b_factor_Ca_11_Gal_11.csv");
double A11g[m2][4];
double A11tg[n][546];
ifstream miFichero61("b_factor_Ca_12_Gal_12.csv");
double A12g[m2][4];
double A12tg[n][546];
ifstream miFichero71("b_factor_Ca_13_Gal_13.csv");
double A13g[m2][4];
double A13tg[n][546];
ifstream miFichero81("b_factor_Ca_14_Gal_14.csv");
double A14g[m2][4];
double A14tg[n][546];
ifstream miFichero91("b_factor_Ca_15_Gal_15.csv");
double A15g[m2][4];
double A15tg[n][546];
ifstream miFichero101("b_factor_Ca_16_Gal_16.csv");
double A16g[m2][4];
double A16tg[n][546];
ifstream miFichero111("b_factor_Ca_17_Gal_17.csv");
double A17g[m2][4];
double A17tg[n][546];
ifstream miFichero121("b_factor_Ca_18_Gal_18.csv");
double A18g[m2][4];
double A18tg[n][546];
ifstream miFichero131("b_factor_Ca_19_Gal_19.csv");
double A19g[m2][4];
double A19tg[n][546];
ifstream miFichero141("b_factor_Ca_20_Gal_20.csv");
double A20g[m2][4];
double A20tg[n][546];

for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero11>>A7g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero11.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero21>>A8g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero21.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero31>>A9g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero31.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero41>>A10g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero41.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero51>>A11g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero51.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero61>>A12g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero61.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero71>>A13g[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero71.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero81>>A14g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero81.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero91>>A15g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero91.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero101>>A16g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero101.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero111>>A17g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero111.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero121>>A18g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero121.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero131>>A19g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero131.close();
for(int i=0;i<m2;i++)
        for(int j=0;j<n;j++)
                miFichero141>>A20g[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero141.close();
//Otra transpuesta
trans2(m,n,A7g,A7tg);
trans2(m,n,A8g,A8tg);
trans2(m,n,A9g,A9tg);
trans2(m,n,A10g,A10tg);
trans2(m,n,A11g,A11tg);
trans2(m,n,A12g,A12tg);
trans2(m,n,A13g,A13tg);
trans2(m,n,A14g,A14tg);
trans2(m,n,A15g,A15tg);
trans2(m,n,A16g,A16tg);
trans2(m,n,A17g,A17tg);
trans2(m,n,A18g,A18tg);
trans2(m,n,A19g,A19tg);
trans2(m,n,A20g,A20tg);


////Esto es para escoger los valores maximo y minimo
C[7][1]=*std::max_element(A7tg[3],A7tg[3]+546);
C[8][1]=*std::max_element(A8tg[3],A8tg[3]+546);
C[9][1]=*std::max_element(A9tg[3],A9tg[3]+546);
C[10][1]=*std::max_element(A10tg[3],A10tg[3]+546);
C[11][1]=*std::max_element(A11tg[3],A11tg[3]+546);
C[12][1]=*std::max_element(A12tg[3],A12tg[3]+546);
C[13][1]=*std::max_element(A13tg[3],A13tg[3]+546);
C[14][1]=*std::max_element(A14tg[3],A14tg[3]+546);
C[15][1]=*std::max_element(A15tg[3],A15tg[3]+546);
C[16][1]=*std::max_element(A16tg[3],A16tg[3]+546);
C[17][1]=*std::max_element(A17tg[3],A17tg[3]+546);
C[18][1]=*std::max_element(A18tg[3],A18tg[3]+546);
C[19][1]=*std::max_element(A19tg[3],A19tg[3]+546);
C[20][1]=*std::max_element(A20tg[3],A20tg[3]+546);
std::cout << "The largest b-factor (Units of SD) for rc=7 and Ca+Gal is  " <<C[7][1]<< '\n';

////////////////////////////////////////////////////////////////////////Ca mas Gal mas Na

int m3=546;//546 con Ca+Gal+Na
ifstream miFichero12("b_factor_Ca_7_Na_7_Gal_7.csv");
double A7gn[m3][4];
double A7tgn[n][546];
ifstream miFichero22("b_factor_Ca_8_Na_8_Gal_8.csv");
double A8gn[m3][4];
double A8tgn[n][546];
ifstream miFichero32("b_factor_Ca_9_Na_9_Gal_9.csv");
double A9gn[m3][4];
double A9tgn[n][546];
ifstream miFichero42("b_factor_Ca_10_Na_10_Gal_10.csv");
double A10gn[m3][4];
double A10tgn[n][546];
ifstream miFichero52("b_factor_Ca_11_Na_11_Gal_11.csv");
double A11gn[m3][4];
double A11tgn[n][546];
ifstream miFichero62("b_factor_Ca_12_Na_12_Gal_12.csv");
double A12gn[m3][4];
double A12tgn[n][546];
ifstream miFichero72("b_factor_Ca_13_Na_13_Gal_13.csv");
double A13gn[m3][4];
double A13tgn[n][546];
ifstream miFichero82("b_factor_Ca_14_Na_14_Gal_14.csv");
double A14gn[m3][4];
double A14tgn[n][546];
ifstream miFichero92("b_factor_Ca_15_Na_15_Gal_15.csv");
double A15gn[m3][4];
double A15tgn[n][546];
ifstream miFichero102("b_factor_Ca_16_Na_16_Gal_16.csv");
double A16gn[m3][4];
double A16tgn[n][546];
ifstream miFichero112("b_factor_Ca_17_Na_17_Gal_17.csv");
double A17gn[m3][4];
double A17tgn[n][546];
ifstream miFichero122("b_factor_Ca_18_Na_18_Gal_18.csv");
double A18gn[m3][4];
double A18tgn[n][546];
ifstream miFichero132("b_factor_Ca_19_Na_19_Gal_19.csv");
double A19gn[m3][4];
double A19tgn[n][546];
ifstream miFichero142("b_factor_Ca_20_Na_20_Gal_20.csv");
double A20gn[m3][4];
double A20tgn[n][546];

//el de R_c=7 se cambia por no tener todos sus valores definidos para Residuo>546
for(int i=0;i<546;i++)//Ojo con este
        for(int j=0;j<n;j++)
                miFichero12>>A7gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero12.close();
for(int i=546;i<m3;i++)
        for(int j=0;j<n;j++)
                A7gn[i][j]=0;
//
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero22>>A8gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero22.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero32>>A9gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero32.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero42>>A10gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero42.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero52>>A11gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero52.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero62>>A12gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero62.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero72>>A13gn[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero72.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero82>>A14gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero82.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero92>>A15gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero92.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero102>>A16gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero102.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero112>>A17gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero112.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero122>>A18gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero122.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero132>>A19gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero132.close();
for(int i=0;i<m3;i++)
        for(int j=0;j<n;j++)
                miFichero142>>A20gn[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero142.close();

trans3(m,n,A7gn,A7tgn);
trans3(m,n,A8gn,A8tgn);
trans3(m,n,A9gn,A9tgn);
trans3(m,n,A10gn,A10tgn);
trans3(m,n,A11gn,A11tgn);
trans3(m,n,A12gn,A12tgn);
trans3(m,n,A13gn,A13tgn);
trans3(m,n,A14gn,A14tgn);
trans3(m,n,A15gn,A15tgn);
trans3(m,n,A16gn,A16tgn);
trans3(m,n,A17gn,A17tgn);
trans3(m,n,A18gn,A18tgn);
trans3(m,n,A19gn,A19tgn);
trans3(m,n,A20gn,A20tgn);


////Esto es para escoger los valores maximo y minimo
C[7][2]=*std::max_element(A7tgn[3],A7tgn[3]+546);
C[8][2]=*std::max_element(A8tgn[3],A8tgn[3]+546);
C[9][2]=*std::max_element(A9tgn[3],A9tgn[3]+546);
C[10][2]=*std::max_element(A10tgn[3],A10tgn[3]+546);
C[11][2]=*std::max_element(A11tgn[3],A11tgn[3]+546);
C[12][2]=*std::max_element(A12tgn[3],A12tgn[3]+546);
C[13][2]=*std::max_element(A13tgn[3],A13tgn[3]+546);
C[14][2]=*std::max_element(A14tgn[3],A14tgn[3]+546);
C[15][2]=*std::max_element(A15tgn[3],A15tgn[3]+546);
C[16][2]=*std::max_element(A16tgn[3],A16tgn[3]+546);
C[17][2]=*std::max_element(A17tgn[3],A17tgn[3]+546);
C[18][2]=*std::max_element(A18tgn[3],A18tgn[3]+546);
C[19][2]=*std::max_element(A19tgn[3],A19tgn[3]+546);
C[20][2]=*std::max_element(A20tgn[3],A20tgn[3]+546);
std::cout << "The largest b-factor (Units of SD) for rc=7 is  Ca+Gal+Na" <<C[7][2]<< '\n';

////////////////////////////////////////////////////////////////////////Ca mas Na

int m4=546;//546 con Ca+Na
ifstream miFichero13("b_factor_CA_7_Na_7.csv");
double A7n[m4][4];
double A7tn[n][546];
ifstream miFichero23("b_factor_CA_8_Na_8.csv");
double A8n[m4][4];
double A8tn[n][546];
ifstream miFichero33("b_factor_CA_9_Na_9.csv");
double A9n[m4][4];
double A9tn[n][546];
ifstream miFichero43("b_factor_CA_10_Na_10.csv");
double A10n[m4][4];
double A10tn[n][546];
ifstream miFichero53("b_factor_CA_11_Na_11.csv");
double A11n[m4][4];
double A11tn[n][546];
ifstream miFichero63("b_factor_CA_12_Na_12.csv");
double A12n[m4][4];
double A12tn[n][546];
ifstream miFichero73("b_factor_CA_13_Na_13.csv");
double A13n[m4][4];
double A13tn[n][546];
ifstream miFichero83("b_factor_CA_14_Na_14.csv");
double A14n[m4][4];
double A14tn[n][546];
ifstream miFichero93("b_factor_CA_15_Na_15.csv");
double A15n[m4][4];
double A15tn[n][546];
ifstream miFichero103("b_factor_CA_16_Na_16.csv");
double A16n[m4][4];
double A16tn[n][546];
ifstream miFichero113("b_factor_CA_17_Na_17.csv");
double A17n[m4][4];
double A17tn[n][546];
ifstream miFichero123("b_factor_CA_18_Na_18.csv");
double A18n[m4][4];
double A18tn[n][546];
ifstream miFichero133("b_factor_CA_19_Na_19.csv");
double A19n[m4][4];
double A19tn[n][546];
ifstream miFichero143("b_factor_CA_20_Na_20.csv");
double A20n[m4][4];
double A20tn[n][546];

for(int i=0;i<m2;i++)//Ojo con este
        for(int j=0;j<n;j++)
                miFichero13>>A7n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero13.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero23>>A8n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero23.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero33>>A9n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero33.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero43>>A10n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero43.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero53>>A11n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero53.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero63>>A12n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero63.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero73>>A13n[i][j];
//Se cierra el archivo porque sino se puede danar
miFichero73.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero83>>A14n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero83.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero93>>A15n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero93.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero103>>A16n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero103.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero113>>A17n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero113.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero123>>A18n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero123.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero133>>A19n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero133.close();
for(int i=0;i<m4;i++)
        for(int j=0;j<n;j++)
                miFichero143>>A20n[i][j];
//Se cierra el archivo porque sino, se puede danar
miFichero143.close();

trans4(m,n,A7n,A7tn);
trans4(m,n,A8n,A8tn);
trans4(m,n,A9n,A9tn);
trans4(m,n,A10n,A10tn);
trans4(m,n,A11n,A11tn);
trans4(m,n,A12n,A12tn);
trans4(m,n,A13n,A13tn);
trans4(m,n,A14n,A14tn);
trans4(m,n,A15n,A15tn);
trans4(m,n,A16n,A16tn);
trans4(m,n,A17n,A17tn);
trans4(m,n,A18n,A18tn);
trans4(m,n,A19n,A19tn);
trans4(m,n,A20n,A20tn);


////Esto es para escoger los valores maximo y minimo
C[7][3]=*std::max_element(A7tn[3],A7tn[3]+546);
C[8][3]=*std::max_element(A8tn[3],A8tn[3]+546);
C[9][3]=*std::max_element(A9tn[3],A9tn[3]+546);
C[10][3]=*std::max_element(A10tn[3],A10tn[3]+546);
C[11][3]=*std::max_element(A11tn[3],A11tn[3]+546);
C[12][3]=*std::max_element(A12tn[3],A12tn[3]+546);
C[13][3]=*std::max_element(A13tn[3],A13tn[3]+546);
C[14][3]=*std::max_element(A14tn[3],A14tn[3]+546);
C[15][3]=*std::max_element(A15tn[3],A15tn[3]+546);
C[16][3]=*std::max_element(A16tn[3],A16tn[3]+546);
C[17][3]=*std::max_element(A17tn[3],A17tn[3]+546);
C[18][3]=*std::max_element(A18tn[3],A18tn[3]+546);
C[19][3]=*std::max_element(A19tn[3],A19tn[3]+546);
C[20][3]=*std::max_element(A20tn[3],A20tn[3]+546);
std::cout << "The largest b-factor (Units of SD) for rc=7 and Ca+Na is  " <<C[7][3]<< '\n';

///////////////////////////////////////////////////////////////////////////////////

//Enviar info a un archivo plano
//off file stream
ofstream miFichsal;
//miFichero2.open : Lo crea y lo abre
miFichsal.open("max.csv");
//setw(): reserva para cada dato 10 lugares 
//Columnas de salida: Rc(A)    &&  Max b-factor
for(int i=7;i<21;i++){
	miFichsal<<setw(10)<<i<<" ";
	miFichsal<<setw(10)<<*std::max_element(C[i],C[i]+4);
	miFichsal<<endl;
        }
miFichsal.close();

system("Pause");
return 0;
}
