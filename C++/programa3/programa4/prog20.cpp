#include <iostream>
using namespace std;

void imp(string txt = "Leonardo");

int main(){

	imp("Marcela");

	return 0;
}

void imp(string txt){
	cout << "\n" << txt << "\n";
}