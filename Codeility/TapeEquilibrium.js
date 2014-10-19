function solution(A) {
    // write your code in JavaScript (ECMA-262, 5th edition)
    var result = Number.MAX_VALUE;
    var p0 = 0;
    var p1 = 0;
    for (var i in A){
        p1 += A[i];    
    }
    for (var i = 0; i < A.length - 1; i++){
        p0 += A[i];
        p1 -= A[i];
        result = Math.min(result, Math.abs(p0-p1));
    }
    return result;
}