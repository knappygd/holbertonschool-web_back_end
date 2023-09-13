export default function appendToEachArrayValue(array, appendString) {
  const arr = [];

  for (const v of array) {
    arr.push(appendString + v);
  }

  return arr;
}
