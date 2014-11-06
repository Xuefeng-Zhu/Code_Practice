class MyClass {

    public static void balanced_brackets(String s) {
        // Write your code here
        // To print results to the standard output please use System.out.println
        // Example: System.out.println("Hello world!");
        int count = 0;
        for (char c : s.toCharArray()){
            if (c == '('){
                count += 1;
            }
            else{
                count -= 1;
                if (count < 0){
                    System.out.println("Unbalanced");
                    System.exit(0);
                }
            }
        }
        
        System.out.println(count == 0 ? "Balanced" : "Unbalanced");
    }
}