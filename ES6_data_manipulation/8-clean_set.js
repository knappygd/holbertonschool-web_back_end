export default function cleanSet(set, startString) {
  if (startString === '') return '';
  let ret = '';
  for (const i of set) if (i.startsWith(startString)) ret += i.replace(startString, '-');
  return ret.substring(1);
}
