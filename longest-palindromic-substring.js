// 5. Longest Palindromic Substring

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {

  for (let i = 0; i < s.length; i++) {
    
  }

  // let longestPalindrome = "";
  // let longestPalindromeLength = 0;
  // for (let i = 1; i < s.length; i++) {
  //   let leftChar = s?.[i - 1];
  //   let rightChar = s?.[i + 1];
  //   let iterationCount = 2;
    

  //   if (
  //     longestPalindromeLength < 2 &&
  //     leftChar !== rightChar
  //   ) {
  //     if (s[i] === leftChar) {
  //       longestPalindromeLength = 2;
  //       longestPalindrome = leftChar + s[i];
  //       continue;
  //     }
  //     if (s[i] === rightChar) {
  //       longestPalindromeLength = 2;
  //       longestPalindrome = s[i] + rightChar;
  //       continue;
  //     }
  //   }

  //   let currentPalindromeLength = 1;
  //   let currentLongestPalindrome = s[i];
  //   let tempI = -1;
  //   while (leftChar === rightChar && leftChar != null && rightChar != null) {
  //     currentPalindromeLength += 2;
  //     longestPalindrome = leftChar + currentLongestPalindrome + rightChar;
  //     leftChar = s?.[i - iterationCount];
  //     rightChar = s?.[i + iterationCount];
  //     iterationCount++;
  //     tempI = (i + iterationCount) - 1;
  //   }
  //   if (tempI !== -1) {
  //     i = tempI;
  //   }

  //   if (currentPalindromeLength > 1 && currentPalindromeLength > longestPalindromeLength) {
  //     longestPalindromeLength = currentPalindromeLength;
  //   }
  // }
  // return longestPalindromeLength === 0 ? s[0] : longestPalindrome;
};

console.log(longestPalindrome("aaaa"));


// longestPalSubstring(String str){
//   // Getting length of the input string
//   int n = str.length();

//   // All substrings of length 1 are palindromes
//   int maxLength = 1, start = 0;

//   // Checking all the substrings
//   for (int i = 0; i < n; i++) {
//       for (int j = i; j < n; j++) {
//           int flag = 1;

//           // Checking for a palindromic subtring
//           for (int k = 0; k < (j - i + 1) / 2; k++)
//               if (str.charAt(i + k) != str.charAt(j - k))
//                   flag = 0;

//           // If substring is palindromic
//           if (flag!=0 && (j - i + 1) > maxLength) {
//               start = i;
//               maxLength = j - i + 1;
//           }
//       }
//   }

//   // Printing the longest Palindromic substring
//   System.out.print("The Longest Palindromic Substring is: ");
//   printSubstring(str, start, start + maxLength - 1);
// }


// var searchPalindrome = function(s, ) {

// };
