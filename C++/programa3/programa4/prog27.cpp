#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main(){

	float pi = M_PI;
	int num = 15;
	
	printf("Valor de pi: %.2f \n",pi); // o f é porque a variavel é do tipo float, o .2 é quantas casas decimais de aproximação terá a variavel
	printf("Valor de NUM: %07d \n",num); // o d é porque a variavel é do tipo inteira, o 07 significa preencher o numero zero, sete vezes antes do 5
	
	cout << "\nO valor de Num em decimal: " << num << "\n";
	cout << "\nO valor de Num em hexadecimal: " << hex << num << "\n"; // colocando o hex antes da variavel, ela é convertida em hexadecimal
	
	return 0;
}
