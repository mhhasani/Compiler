public class MainClass {

    public static void main(String[] args) {
        ChildClass1 child1 = new ChildClass1();
        child1.publicMethodChildClass1(); // accessible

        ChildClass2 child2 = new ChildClass2();
        // child2.privateMethod(); // not accessible
        child2.publicMethodChildClass2(); // accessible through public method

        ChildClass3 child3 = new ChildClass3();
        // child3.protectedMethod(); // not accessible
        child3.publicMethodChildClass3(); // accessible through public method
    }
}

class ChildClass1 {

    public void publicMethodChildClass1() {
        System.out.println("This method is public.");
    }
}

class ChildClass2 {

    private void privateMethodChildClass2() {
        System.out.println("This method is private.");
    }

    public void publicMethodChildClass2() {
        System.out.println("This method is public and can access privateMethod.");
        privateMethod();
    }
}

class ChildClass3 {

    protected void protectedMethodChildClass3() {
        System.out.println("This method is protected.");
    }

    public void publicMethodChildClass3() {
        System.out.println("This method is public and can access protectedMethod.");
        protectedMethod();
    }
}
