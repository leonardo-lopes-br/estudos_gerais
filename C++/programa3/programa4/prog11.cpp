#include <iostream>
using namespace std;

int main(){
	

	/* switch(expressao){
		
		case const1:
			comandos;
			break;
		case const2:
			comandos;
			break;
		default:
			comandos;
	}
	*/
	
	int val;
	
	cout << "Selecione uma cor:\n";
	cout << "[1] Verde\n[2] Amarelo\n[3] Vermelho\n\n";
	cout << "Numero da cor: ";
	cin >> val;
	
	switch(val){
		
		case 1:
			cout << "\nSiga em frente!\n";
			break;
		case 2:
			cout << "\nAtencao!\n";
			break;
		case 3:
			cout << "\nPare e espere!\n";
			break;
			
	}

	return 0;
}
