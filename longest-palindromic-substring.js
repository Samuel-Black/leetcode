// 5. Longest Palindromic Substring

/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
  const sLength = s.length;
  if (sLength === 0) {
    return "";
  }
  if (sLength === 1) {
    return s;
  }

  let minstart = 0, maxlen = 0;

  let i = 0;
  while (i < sLength) {
    if (sLength - i < maxlen / 2) {
    break;
    }

    let l = i, r = i;

    // Find the center of the palindrome
    while (r < sLength - 1 && s[r] === s[r + 1]) {
    r++;
    }

    // Update the next starting point
    i = r + 1;

    // Expand around the center to find the longest palindrome
    while (l > 0 && r < sLength - 1 && s[l - 1] === s[r + 1]) {
    l--;
    r++;
    }

    const newlen = r - l + 1;
    if (newlen > maxlen) {
    maxlen = newlen;
    minstart = l;
    }
  }

  return s.substring(minstart, minstart + maxlen);
}

console.log(longestPalindrome("aaaa"));
