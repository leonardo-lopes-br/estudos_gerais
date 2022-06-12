#include <iostream>
using namespace std;

int main(){

	int num;
	num = 15;
	
	if ((num > 2 and num <7) or (num > 9 and num < 15) or (num > 15 and num < 20)){
		cout << "Valor aceito\n";
		
	}else{
		cout << "Nao aceito\n";
	}

	return 0;
}
