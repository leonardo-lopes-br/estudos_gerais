#include <iostream>
using namespace std;

int main(){

	int n1,n2,res;
	char opc;
	
	inicio:
	
	cout << "Digite o valor da primeira nota (0 a 100): ";
	cin >> n1;
	cout << "Digite o valor da segunda nota (0 a 100): ";
	cin >> n2;
	
	res = (n1 + n2)/2;
	
	if(res >= 60){
		cout << "APROVADO\n";
	}
	else{
		if(res <50){
			cout << "REPROVADO\n";
		}
		else{
			cout << "RECUPERACAO\n";
		}
	}
	
	cout << "Deseja digitar outras notas?[s/n]\n R: ";
	cin >> opc;
		
	if(opc == 's' or opc == 'S'){
		goto inicio;
		
	}
	
	
	
	return 0;
}
