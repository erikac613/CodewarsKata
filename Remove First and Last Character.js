function removeChar(str){
  var makeArr = str.split('');
  makeArr.pop();
  makeArr.shift();
  var newSt = makeArr.join('');
  return newSt;
};
