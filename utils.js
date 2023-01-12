export function randint(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}

export function randomchoice(a, b) {
    return Math.random() > 0.5 ? a : b;
}

export function calculate_gcd(x, y) {
    while (y) {
        var t = y;
        y = x % y;
        x = t;
    }
    return x;
}

export function intParser(z) {
    if (z > 0) {
        return `+${z}`;
    } else if (z < 0) {
        return `-${abs(z)}`;
    } else {
        return '';
    }
}
