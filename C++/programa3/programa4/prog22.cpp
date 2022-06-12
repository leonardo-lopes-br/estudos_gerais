#include <iostream>
using namespace std;

int main(){

	enum armas{fuzil = 100, revolver = 8, rifle = 12, escopeta = 10};
	armas armaSel;
	
	armaSel = rifle;
	cout << armaSel;

	return 0;
}
