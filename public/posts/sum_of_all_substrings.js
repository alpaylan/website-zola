function cutAllPoints(s) {
    // Cut the string at each index and build a zipped array of the cut strings
    var zipped = [];
    for (var i = 1; i <= s.length; i++) {
        zipped.push([s.slice(0, i), s.slice(i)]);
    }
    return zipped;
}
function sumOfAllSubstrings(s) {
    // Cut the string at each index
    var zipped = cutAllPoints(s);
    var sum = 0;
    for (var i = 0; i < zipped.length; i++) {
        var _a = zipped[i], left = _a[0], right = _a[1];
        if (right.length === 0) {
            sum += parseInt(left);
        }
        else {
            var rightSum = sumOfAllSubstrings(right);
            var leftSum = ((right.length - 1) * (right.length) / 2 + 1) * parseInt(left);
            sum += leftSum + rightSum;
        }
    }
    return sum;
}
console.log(sumOfAllSubstrings("123")); // 169
