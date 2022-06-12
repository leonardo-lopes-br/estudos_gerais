#include <iostream>
#include <stack>
using namespace std;

int main(){

	stack <string> cartas;
	
	
	cartas.push("Rei de Copas");
	cartas.push("Rei de Espadas");
	cartas.push("Rei de Ouros");
	cartas.push("Rei de Paus");
	
	if (cartas.empty()){
		cout << "Pilha vazia\n";
	}else{
		cout << "Pilha com cartas\n";
	}
	
	while (!cartas.empty()){
		cartas.pop();
	}
	
	cout << "Tamanho da pilha: " << cartas.size() << "\n";
	cartas.pop();
	cout << "Tamanho da pilha: " << cartas.size() << "\n";
	
	cout << "Carta do topo: " << cartas.top() << "\n";

	
	return 0;
}
