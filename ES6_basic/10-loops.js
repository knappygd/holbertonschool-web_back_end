export default function appendToEachArrayValue(array, appendString) {
  let arr = [];

  for (let v of array) {
    arr.push(appendString + v);
  }

  return arr;
}
