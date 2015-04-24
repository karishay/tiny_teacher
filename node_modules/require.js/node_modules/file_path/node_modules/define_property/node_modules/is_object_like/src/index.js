module.exports = function isObjectLike(obj) {
    return (obj && typeof(obj) === "object") || false;
};
