#include <iostream>
#include <cmath>

using namespace std;
int main(){
    int a, b, c;
    a = 7;
    b = 4;
    c = 3;
    cout << "Результат: " << (a + b) * pow(c, 2) - (a / b) + (a % b);
    return 0;
}