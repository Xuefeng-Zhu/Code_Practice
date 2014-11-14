import java.util.StringUtils;
class MyClass {

    public static void sort_students(Integer[] numbers) {
        // Write your code here
        // To print results to the standard output please use System.out.println
        // Example: System.out.println("Hello world!");
        boolean change = false;
        do{
            change = false;
            for (int i = 1; i < numbers.length; i++){
            if (numbers[i] < numbers[i-1]){
                int temp = numbers[i];
                numbers[i] = numbers[i-1];
                numbers[i-1] = temp;
                change = true;
            } 
            }
        }while (change);
        
        System.out.println(StringUtils.join(numbers, " "));
    }
}