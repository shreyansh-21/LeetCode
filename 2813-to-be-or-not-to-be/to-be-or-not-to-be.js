/**
 * @param {string} val
 * @return {Object}
 */
// The expect function takes an input val and returns an object containing two methods: toBe and notToBe. These methods take another value as an argument and perform strict equality or inequality checks.

var expect = function(val) {
    return {
        toBe: function(otherVal) {
            if (val === otherVal) return true;
            else throw new Error("Not Equal");
        },
        notToBe: function(otherVal) {
            if (val !== otherVal) return true;
            else throw new Error("Equal");
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */