#include <iostream>
#include <string>

using namespace std;
int main(){
    string station_name = "Ocean";
    int active_sensors = 18;
    float average_temperature = 21.6;
    bool is_online = true;

    cout << station_name << "class 'str'>" << endl;
    cout << active_sensors << " <class 'int'>" << endl;
    cout << average_temperature << " <class 'float'>" << endl;
    cout << boolalpha << is_online << " <class 'bool'>" << endl;
    return 0;
}
