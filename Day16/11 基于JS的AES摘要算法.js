// 准备使用 AES--128

const cryptoJS = require('crypto-js')

const data = 'Hello World!'

// KEY IV
var key = cryptoJS.enc.Utf8.parse('0123456789abcdef')
var iv = cryptoJS.enc.Utf8.parse('1234567890abcdef')

var encrypted_data = cryptoJS.AES.encrypt(data, key, {
    iv: iv,
    mode: cryptoJS.mode.CBC,
    padding: cryptoJS.pad.Pkcs7
})
var encrypted_data_text = encrypted_data.toString()
console.log(encrypted_data_text)