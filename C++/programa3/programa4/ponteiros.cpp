#include <iostream>
using namespace std;

int main(){

	string veiculo = "Carro";
	string *pv;
	pv = &veiculo; // Ponteiro PV recebe o endereço da variável veiculo
	cout << pv << "\n" << &veiculo << "\n";
	
	*pv = "Moto"; // No endereço apontado por *pv adicione o valor "Moto"
	
	cout << veiculo << "\n" << *pv;

	return 0;
}
