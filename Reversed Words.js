function reverseWords(str){
  var splt = str.split(" ");
  var rev = splt.reverse();
  var newStr = rev.join(" ");
  return newStr;
}
