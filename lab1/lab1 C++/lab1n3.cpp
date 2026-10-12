#include <iostream>

using namespace std;
int main(){
    double length, width;
    //cout << "Введите длину площадки в метрах: ";
    cin >> length;
    //cout << "Введите ширину площадки в метрах: ";
    cin >> width;
    cout << "Площадь: " << (length * width) << endl;
    cout << "Периметр: " << (length + width) * 2;
    return 0;
}