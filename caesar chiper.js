let str = "Hlw I am Raima123";
let key = 3;
let res = "";

for (let ch of str) {
    if (ch >= 'a' && ch <= 'z') {
        ch = String.fromCharCode(
            ((ch.charCodeAt(0) - 'a'.charCodeAt(0) + key) % 26) + 'a'.charCodeAt(0)
        );
    } 
    else if (ch >= 'A' && ch <= 'Z') {
        ch = String.fromCharCode(
            ((ch.charCodeAt(0) - 'A'.charCodeAt(0) + key) % 26) + 'A'.charCodeAt(0)
        );
    } 
    else if (ch >= '0' && ch <= '9') {
        ch = String.fromCharCode(
            ((ch.charCodeAt(0) - '0'.charCodeAt(0) + key) % 10) + '0'.charCodeAt(0)
        );
    }
    
    res += ch; 
}

console.log(res);
