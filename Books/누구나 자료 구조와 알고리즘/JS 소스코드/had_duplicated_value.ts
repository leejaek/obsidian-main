const input_array = [1, 4, 3, 5]

function hasDuplicatedValue(input_array) {
  for (let i = 0; i < input_array.length; i++) {
    for (let j = 0; j < input_array.length; j++) {
      if (i != j && input_array[i] === input_array[j]) {
        return true;
      }
    }
  }
  return false;
}

function hasDuplicatedValue2(input_array) {
  let temp_array = [];
  for (let i = 0; i < input_array.length; i++) {
    if(temp_array[input_array[i]] === 1) {
      return true;
    } else {
      temp_array[input_array[i]] = 1;
    }
  }
  return false;
}

console.log(hasDuplicatedValue(input_array));
console.log(hasDuplicatedValue2(input_array));