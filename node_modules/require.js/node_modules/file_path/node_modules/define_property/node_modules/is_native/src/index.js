var isFunction = require("is_function");


var reHostCtor = /^\[object .+?Constructor\]$/,

    functionToString = Function.prototype.toString,

    reNative = RegExp("^" +
        functionToString.call(toString)
        .replace(/[.*+?^${}()|[\]\/\\]/g, "\\$&")
        .replace(/toString|(function).*?(?=\\\()| for .+?(?=\\\])/g, "$1.*?") + "$"
    ),

    isHostObject = (function() {
        try {
            String({
                "toString": 0
            } + "");
        } catch (e) {
            return function isHostObject() {
                return false;
            };
        }

        return function isHostObject(value) {
            return !isFunction(value.toString) && typeof(value + "") === "string";
        };
    }());


module.exports = function isNative(obj) {
    return obj && (
        isFunction(obj) ?
        reNative.test(functionToString.call(obj)) : (
            typeof(obj) === "object" && (
                (isHostObject(obj) ? reNative : reHostCtor).test(obj) || false
            )
        )
    ) || false;
};
