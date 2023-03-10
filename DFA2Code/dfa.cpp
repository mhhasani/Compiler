#include <iostream>
#include <string>
using namespace std;

int main() {
    string input_string;
    cout << "Enter a string: ";
    cin >> input_string;

    int current_state = 0;
    for (char symbol : input_string) {
        switch (current_state) {
            case 0:
                if (symbol == '0') current_state = 1;
                if (symbol == '1') current_state = 2;
                break;
            case 1:
                if (symbol == '0') current_state = 0;
                if (symbol == '1') current_state = 3;
                break;
            case 2:
                if (symbol == '0') current_state = 3;
                if (symbol == '1') current_state = 1;
                break;
            case 3:
                if (symbol == '1') current_state = 4;
                break;
            case 4:
                if (symbol == '0') current_state = 5;
                break;
            case 5:
                if (symbol == '0') current_state = 6;
                if (symbol == '1') current_state = 2;
                break;
            case 6:
                break;
        }
    }
    if (
        current_state == 5 
    ) {
        cout << "The string is accepted" << endl;
    } else {
        cout << "The string is not accepted" << endl;
    }
    return 0;
}