#include <iostream>
using namespace std;

void texto();
void soma();
int soma2(int n1, int n2);
void tr(string tra[4]);

int main(){
	
	int res;
	string transp[4] = {"carro","moto","barco","aviao"};
	
	soma();
	
	res = soma2(255,542);
	cout << res;
	tr(transp);

	return 0;
}

void texto(){
	cout << "\nLeonardo Foda\n";
}

void soma(){
	int n1,n2 = 0;
	cout << "Primeiro valor: ";
	cin >> n1;
	cout << "\nSegundo valor: ";
	cin >> n2;
	cout << "\nA soma dos valores eh igual a: " << n1+n2 << "\n";
}
	
int soma2(int n1, int n2){
	return n1+n2;
	
}

void tr(string tra[4]){
	for (int i = 0; i<4; i++)
		cout << tra[i] << "\n";
}
