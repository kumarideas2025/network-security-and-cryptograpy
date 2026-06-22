function convertBin(c) { return (c >>> 0).toString(2).slice(-8); }

function transformNOT(text) {
    console.log("Char".padEnd(6) + "ASCII".padEnd(8) + "NOT(dec)".padEnd(10) + "NOT(char)".padEnd(10) + "NOT(bin)".padEnd(12));
    console.log("-".repeat(46));

    for (let i = 0; i < text.length; i++) {
        let ch = text.charAt(i);
        let asciiVal = text.charCodeAt(i);

        let notVal = (~asciiVal) & 0xFF;
        let notChar = String.fromCharCode(notVal);
        let notBin = convertBin(notVal);

        console.log(
            ch.padEnd(6) + 
            String(asciiVal).padEnd(8) + 
            String(notVal).padEnd(10) + 
            notChar.padEnd(10) + 
            notBin.padEnd(12)
        );
    }
}

transformNOT("kowshik");