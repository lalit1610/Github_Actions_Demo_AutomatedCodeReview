// Poor naming and style issues
function calc(x,y,z) {
  var a=x+y;  // No spaces, unclear naming
  var b=a*z;
  return b;
}

// Security issue
function evaluateUserInput(input) {
  return eval(input);  // NEVER use eval with user input!
}

// Performance issue
function findInArray(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {  // O(n²) when O(n) is sufficient
      if (arr[j] === target) {
        return j;
      }
    }
  }
  return -1;
}
