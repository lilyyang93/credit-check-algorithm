//'5541808923795240' => "The number is valid!"
exports.creditCheck = function(str) {
    let num = str.split('').reverse().map(Number)
    let num2 = []
    let num3 = []
    let product
    for (let n in num) {
        if (n % 2 === 0) {
            num2.push(num[n])
        } else {
            num2.push(num[n]*2)
        }
    }
    for (let n of num2) {
        if (n > 9) {
            digits = n.toString().split('').map(Number)
            product = digits.reduce((x,y) => x+y)
            num3.push(product)
        } else {
            num3.push(n)
        }
    }
    return num3.reduce((x,y) => x+y) % 10 === 0 ? 'The number is valid!' : 'The number is invalid!'
    
}


