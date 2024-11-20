


function cutAllPoints(s: string): [string, string][] {
    // Cut the string at each index and build a zipped array of the cut strings
    const zipped: [string, string][] = [];
    for (let i = 1; i <= s.length; i++) {
        zipped.push([s.slice(0, i), s.slice(i)]);
    }
    return zipped
}

function sumOfAllSubstrings(s: string): number {
    // Cut the string at each index
    const zipped = cutAllPoints(s);
    let sum = 0;

    for (let i = 0; i < zipped.length; i++) {
        const [left, right] = zipped[i];
        if (right.length === 0) {
            sum += parseInt(left);
        } else {
            const rightSum = sumOfAllSubstrings(right);
            const leftSum = ((right.length - 1) * (right.length) / 2 + 1) * parseInt(left);
            sum += leftSum + rightSum;
        }
    }

    return sum;
}

console.log(sumOfAllSubstrings("123")); // 169