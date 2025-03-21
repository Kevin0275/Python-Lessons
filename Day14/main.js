// 在后端导入 JS 文件：
// var math = require('./math')
//
// console.log(math)   // { add: [Function: add], mul: [Function: mul] }

// 当然，我们可以解构这个返回值，不用一个变量承载

var {add, mul} = require('./math');
console.log(add(1,2))
console.log(mul(3,2))

