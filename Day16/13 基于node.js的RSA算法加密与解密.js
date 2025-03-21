// 获取库
const rsa = require('node-rsa')

// 创建公钥和私钥
const key = new rsa({b: 1024})
// 指定key的长度

const publicKey = key.exportKey('publicKey')
console.log(publicKey)

const privateKey = key.exportKey('privateKey')
console.log(privateKey)

var message = 'hello world'

// 加密
encrypted_message = key.encrypt(message, 'base64');
console.log(encrypted_message)

// 解密
decrypted_message = key.decrypt(encrypted_message, 'utf8');


