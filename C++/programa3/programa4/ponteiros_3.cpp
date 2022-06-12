#include <iostream>
using namespace std;

void somar(float *var, float valor);
void iniVetor(float *v);

int main(){

	float num = 0;
	float vetor[5];
	
	somar(&num,15);
	iniVetor(vetor); //vetor n precisa do endereço (&)
	
	cout << num << "\n\n";
	
	for (int i = 0; i<5; i++){
		cout << vetor[i] << "\n";
	}

	return 0;
}

void somar(float *var, float valor){
	*var += valor; 
}

void iniVetor(float *v){
	v[0] = 0;
	v[1] = 0;
	v[2] = 0;
	v[3] = 0;
	v[4] = 0;
}
// sem o ponteiro, a função somar nao atribui valor pro num, pois a função está fora do scopo principal, então não somaria 