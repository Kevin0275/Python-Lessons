const add = (x, y) => x + y;
const mul = (x, y) => x * y;

// JS 需要限制出口，也就是哪些函数可以被调用（必须有！）
export default {
    add,
    mul
};
