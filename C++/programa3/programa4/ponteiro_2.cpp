#include <iostream>
using namespace std;

int main(){

	int *p;
	int vetor[10];
	
	p = &vetor[0]; // p = vetor;
	cout << p << "\n";
	
	*p = 10; //vetor[0] recebe 10
	cout << vetor[0];
	

	

	return 0;
}
