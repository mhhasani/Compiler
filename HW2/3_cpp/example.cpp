class A {
    void f() { cout << "A::f()" << endl; }
};

class B
{
public:
    B() { cout << "B" << endl; }
    ~B() { cout << "~B" << endl; }
};

class C
{
public:
    C() { cout << "C" << endl; }
    ~C() { cout << "~C" << endl; }
};
// C() class

int main()
{
    A a;
    B b;
    C c;
    return 0;
}