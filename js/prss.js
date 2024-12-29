function repeatArray(arr, count) { 
    let result = []; 
    for (let i = 0; i < count; i++) { 
        result = result.concat(arr); 
    } 
    return result; 
}

class PrSS {
    constructor(array) {
        if (!Array.isArray(array)) {
            throw new TypeError(`Expected list type for PrSS(), not ${typeof array}`);
        }

        this.sequence = array.slice();
        for (let i = 0; i < this.sequence.length; i++) {
            if (typeof this.sequence[i] !== 'number') {
                throw new TypeError(`Expected int type for array[${i}], not ${typeof this.sequence[i]}`);
            }
        }

        if (this.sequence.length === 0) {
            return;
        }

        let last = -1;
        for (const value of this.sequence) {
            if (value > (last + 1)) {
                throw new Error(`Invalid PrSS: ${this.sequence}`);
            }
            last = value;
        }
    }

    toString() {
        return this.sequence.map(item => `(${item})`).join('');
    }

    eval(base = 3) {
        if (this.sequence.length === 0) {
            throw new Error("Cannot evaluate an empty sequence.");
        }

        if (this.sequence[this.sequence.length - 1] === 0) {
            const s = this.sequence.slice(0, -1);
            return new PrSS(s);
        }

        const bad = this.sequence[this.sequence.length - 1];
        let s = [];
        for (let i = this.sequence.length - 2; i >= 0; i--) {
            s.unshift(this.sequence[i]);
            if (this.sequence[i] < bad) {
                const t = this.sequence.slice(0, i);
                return new PrSS(t.concat(repeatArray(s, base + 1));
            }
        }
        return new PrSS(repeatArray(s, base);
    }
}

module.exports = PrSS;
