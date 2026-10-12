#include <iostream>
#include <iomanip>

using namespace std;
int main(){
    int total_seconds, hours, minutes, seconds;
    //cout << "Введите продолжительность поездки в секундах: ";
    cin >> total_seconds ;
    hours = total_seconds / 3600;
    minutes = (total_seconds % 3600) / 60;
    seconds = total_seconds % 60;
    cout << setfill('0') << setw(2) << hours << ":" << setw(2) << minutes << ":" << setw(2) << seconds << endl;
    return 0;
}