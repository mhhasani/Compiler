#include <stdio.h>

struct person {
    char name[20];
    int age;
};

struct MyStruct {
    int a;
    int b;
    int c;
};

int main() {
    struct person john;
    john.age = 30;
    printf("John is %d years old\n", john.age);
    return 0;
}
