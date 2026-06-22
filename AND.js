function convertBin(c) { return c.toString(2); }

function transformAND(text, key) {
    console.log("Char".padEnd(6) + "ASCII".padEnd(8) + "AND(dec)".padEnd(10) + "AND(char)".padEnd(10) + "AND(bin)".padEnd(12));
    console.log("-".repeat(46));

    for (let i = 0; i < text.length; i++) {
        let ch = text.charAt(i);
        let asciiVal = text.charCodeAt(i);

        let andVal = asciiVal & key;
        let andChar = String.fromCharCode(andVal);
        let andBin = convertBin(andVal);

        console.log(
            ch.padEnd(6) + 
            String(asciiVal).padEnd(8) + 
            String(andVal).padEnd(10) + 
            andChar.padEnd(10) + 
            andBin.padEnd(12)
        );
    }
}

transformAND("kowshik", 127);