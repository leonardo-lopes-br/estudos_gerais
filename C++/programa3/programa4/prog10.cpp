#include <iostream>
using namespace std;

int main(){

	int n1,n2,nota;
	string res;
	
	cout << "Digite a primeira nota: ";
	cin >> n1;
	cout << "\n\nDigite a segunda nota: ";
	cin >> n2;
	
	nota = n1 + n2;
	
	// primeira maneira de usar um operador ternario (mais leve que o if, usado em casos bem simples)
	//(nota >= 60) ? res = "APROVADO" : res = "REPROVADO";
	//cout << res;
	//segunda maneira:
	res = (nota >= 60) ? "Aprovado\n" : "Reprovado\n";
	cout << "\nSituacao do aluno: " << res;

	return 0;
}
