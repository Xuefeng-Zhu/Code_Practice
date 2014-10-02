function stringToLong(s){
	var result = 0;
	for (var i in s){
		result = result * 10 + parseInt(i);
	}
	return result;
}

function test(){
	var i = stringToLong("1234");
	if (i == 1234){
		console.log("success");
	}
	else{
		console.log("success");
	}
}

test();