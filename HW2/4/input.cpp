#include <iostream>

using namespace std;

void printHello() {
    cout << "Hello" << endl;
    if (true) {
        cout << "World" << endl;
    }
}

int main() {
    int x = 10;

    if (x > 5) {
        cout << "x is greater than 5" << endl;
    }

    for (int i = 0; i < 5; i++) {
        cout << "i = " << i << endl;
        cout << "x = " << x << endl;
        cout << "x + i = " << x + i << endl;
    }

    return 0;
}
