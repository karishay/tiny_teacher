var objectFunction = "[object Function]",
    toString = Object.prototype.toString,
    isFunction;


if (typeof(/./) === "function" || (typeof(Uint8Array) !== "undefined" && typeof(Uint8Array) !== "function")) {
    isFunction = function isFunction(obj) {
        return toString.call(obj) === objectFunction;
    };
} else {
    isFunction = function isFunction(obj) {
        return typeof(obj) === "function" || false;
    };
}


module.exports = isFunction;
