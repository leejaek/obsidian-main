const input_array = [1, 3, 4, 6, 8, 9, 11, 12, 43, 98]

const input_value = 11;

console.log(input_array[1])

function binary_search(array: number[], value: number) {
  let last = array.length - 1
  let first = 0
  
  while (first <= last) {
  	let middle = Math.round((last + first) / 2);
    let middle_value = array[middle];
    if (middle_value === value) {
      return middle;
    } else if (middle_value > value) {
      last = middle;
    } else if (middle_value < value) {
      first = middle;
      break;
    }
  }
  return null;
}

binary_search(input_array, input_value);