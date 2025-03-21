// node.js自带一个crypto包，但是有局限性，一般不用

cryptoJS = require('crypto-js')

const data = 'Hello World!'

// 生成MD5
const data_MD5 = cryptoJS.MD5(data).toString();
console.log(data_MD5);