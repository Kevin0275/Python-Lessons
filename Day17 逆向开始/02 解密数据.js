// 直接拿取我们想要的JS代码
// function b(t) {
//     var e = h.a.enc.Utf8.parse(r["e"])
//         , n = h.a.enc.Utf8.parse(r["i"])
//         , a = h.a.AES.decrypt(t, e, {
//             iv: n,
//             mode: h.a.mode.CBC,
//             padding: h.a.pad.Pkcs7
//         }
//     );
//     return a.toString(h.a.enc.Utf8)
// }

// 但是我们知道 h.a完全没有被定义，但是他好像只需要执行两个函数：
// h.a.enc.Utf8.parse()
// h.a.AES.decrypt
// 所以直接替换

const cryptoJS = require('crypto-js')
function b(t) {
    var e = cryptoJS.enc.Utf8.parse(r["e"])
        , n = cryptoJS.enc.Utf8.parse(r["i"])
        , a = cryptoJS.AES.decrypt(t, e, {
            iv: n,
            mode: cryptoJS.mode.CBC,
            padding: cryptoJS.pad.Pkcs7
        }
    );
    return a.toString(cryptoJS.enc.Utf8)
}

// 这里的 r 会显示undefined，当然，因为key和iv是写死的，所以直接自己替换了就行了

// 到这里，我们已经构建了应该的 JS 解密代码，所以接下来我们应该考虑和python联动，因为我们的数据是通过python爬取的
// 所以，我们转回python，用到第三方库，execjs