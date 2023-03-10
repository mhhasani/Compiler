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
                if (symbol == 'a') current_state = 1;
                if (symbol == 'b') current_state = 2;
                break;
            case 1:
                if (symbol == 'a') current_state = 0;
                if (symbol == 'b') current_state = 5;
                break;
            case 2:
                if (symbol == 'b') current_state = 3;
                break;
            case 3:
                if (symbol == 'b') current_state = 4;
                break;
            case 4:
                if (symbol == 'b') current_state = 3;
                break;
            case 5:
                if (symbol == 'b') current_state = 6;
                break;
            case 6:
                if (symbol == 'b') current_state = 5;
                break;
        }
    }
    if (
        current_state == 0 ||
        current_state == 3 ||
        current_state == 5 
    ) {
        cout << "The string is accepted" << endl;
    } else {
        cout << "The string is not accepted" << endl;
    }
    return 0;
}