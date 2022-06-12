#include <iostream>
using namespace std;

void fatorial();

int main(){

	cout << "\nDigite o numero para saber o valor de seu fatorial: \n";
	fatorial();

	return 0;
}

void fatorial(){
	
	int num, mult = 1;
	cin >> num;
	for (num; num > 0; num--){
		mult *= num;
	}
	cout << "O valor do fatorial eh: " << mult;
}