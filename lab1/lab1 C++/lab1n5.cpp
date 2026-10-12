//Пользователь последовательно вводит расстояние в километрах, расход топлива в литрах
//на 100 километров и стоимость одного литра топлива
//Вычислить необходимое количество топлива и его полную стоимость
//Оба результата вывести с двумя цифрами после десятичной точки


#include <iostream>
#include <iomanip>

using namespace std;
int main(){
    double rasstoyanie_kilometr, rashod_topliva, stoimost_litr, trebyemoe_toplivo;
    cin >> rasstoyanie_kilometr >> rashod_topliva >> stoimost_litr;
    trebyemoe_toplivo = ((rasstoyanie_kilometr * rashod_topliva) / 100);
    cout << fixed << setprecision(2);
    cout << "Топливо: " << trebyemoe_toplivo << " л" << endl;
    cout << "Стоимость: " << (trebyemoe_toplivo * stoimost_litr) << " руб";
    return 0;
}