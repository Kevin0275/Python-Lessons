var counter = (function (){
    var n = 0;
    function c(){
        n++;
        console.log('次数', n)
    }
    return c
})()

// counter()
// counter()
// counter()
counter()


