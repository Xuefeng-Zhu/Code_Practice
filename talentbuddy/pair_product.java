class MyClass {

    public static void max_prod(Integer[] v) {
        // Write your code here
        // To print results to the standard output please use System.out.println
        // Example: System.out.println("Hello world!");
        int max = 0;
        int max3 = 0;
        for (int i : v){
            if (i % 3 == 0 && i > max3){
                max3 = i;
            }
            else{
                if (i > max){
                    max = i;
                }
            }
        }
        System.out.println(max * max3);
        
    }
}