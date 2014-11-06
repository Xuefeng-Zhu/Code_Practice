class MyClass {

    public static void find_missing_number(Integer[] v) {
        // Write your code here
        // To print results to the standard output please use System.out.println
        // Example: System.out.println("Hello world!");
        int n = v.length + 1;
        int total = (1 + n) * n / 2;
        for (int i : v){
            total -= i;
        }
        System.out.println(total);
    }
}