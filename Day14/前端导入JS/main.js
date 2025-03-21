// 如果在前端，这个是主程序，然后我们需要浏览器来调用 JS 文件

import math from './math.js'

console.log(math.add(1,2))
console.log(math.mul(4,2))

// 直接执行是报错的，因为直接执行默认用node.js执行
// 用 HTML 直接自己执行
