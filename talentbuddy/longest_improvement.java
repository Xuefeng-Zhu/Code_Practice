class MyClass {

    public static void longest_improvement(Integer[] grades) {
        // Write your code here
        // To print results to the standard output please use System.out.println
        // Example: System.out.println("Hello world!");
        int result = 0;
        int prev = 0;
        int count = 0;
        for (int grade : grades){
            if (grade < prev){
                if (count > result){
                    result = count;
                }
                count = 0;
            }
            prev = grade;
            count += 1;
        }
        
        System.out.println(result);
    }
}