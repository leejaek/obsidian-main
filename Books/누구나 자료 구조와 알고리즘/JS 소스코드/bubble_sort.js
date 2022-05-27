const input_array = [42, 23, 1, 11, 49, 32, 2, 6]

function bubble_sort(input_array: number[]) {
  let last_index = input_array.length

  while (last_index >= 1) {
    let point_1 = 0
  	let point_2 = point_1 + 1
    last_index -= 1

    while (point_2 <= last_index) {
    	if (input_array[point_1] > input_array[point_2]) {
        [input_array[point_1], input_array[point_2]] = [input_array[point_2], input_array[point_1]];
      } else {
        point_1 += 1
        point_2 = point_1 + 1
      }
    }
  }

  return input_array
}

console.log(bubble_sort(input_array));
