// Determine whether an integer is a palindrome. Do this without extra space.
#include <stdio.h>
#include <stdlib.h>

int reverse(int x){
	int result = 0;
	while (x > 0){
		result = result * 10 + x % 10;
		x /= 10;
	}
	return result;
}

int main(){
	char temp[32];
	gets(temp);
	int num = atoi(temp);
	if (reverse(num) == num){
		printf("The number you entered is palidrome\n");
	}
	else{
		printf("The number you enters is not palidrome\n");
	}
}