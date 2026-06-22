// Write a Python program that processes a given string "HeLLo" and performs XOR operation on each character. 

// For each character in the string, the program must:
// 1. Convert the character into its ASCII value.
// 2. Represent the ASCII value in binary and hexadecimal format.
// 3. Perform XOR operations with the key value 127.
// 4. Convert the resulting value (XOR) back into character and binary representation.

// Display the output in a well-formatted table, showing:
// Character
// ASCII value
// Binary representation
// XOR result (decimal and binary)



function convertBin(c) { return c.toString(2); }
function convertHex(c) { return c.toString(16); }

function transformXOR(text, key) {
    console.log("Char".padEnd(6) + "ASCII".padEnd(8) + "XOR(dec)".padEnd(10) + "XOR(char)".padEnd(10) + "XOR(bin)".padEnd(12));
    console.log("-".repeat(46));

    for (let i = 0; i < text.length; i++) {
        let ch = text.charAt(i);
        let asciiVal = text.charCodeAt(i);

        let xorVal = asciiVal ^ key;
        let xorChar = String.fromCharCode(xorVal);
        let xorBin = convertBin(xorVal);

        console.log(
            ch.padEnd(6) + 
            String(asciiVal).padEnd(8) + 
            String(xorVal).padEnd(10) + 
            xorChar.padEnd(10) + 
            xorBin.padEnd(12)
        );
    }
}

transformXOR("kowshik", 127);