#include <iostream>
using namespace std;

/* 99521199  it is a multi-line comment
this type of comment is used to describe the code
and it is not executed by the compiler.
i want to convert this to a single line comment */

void printHello() {
    cout << "Hello" << endl;
    if (true) {
/* 99521199  hi */
        cout << "World" << endl;
    }
}

/* 99521199  it is a multi-line comment
this type of comment is used to describe the code
and it is not executed by the compiler.
i want to convert this to a single line comment*/

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

// 99521199  it is a multi-line comment
// 99521199  this type of comment is used to describe the code
// 99521199  and it is not executed by the compiler.
// 99521199  i want to convert this to a single line comment*/