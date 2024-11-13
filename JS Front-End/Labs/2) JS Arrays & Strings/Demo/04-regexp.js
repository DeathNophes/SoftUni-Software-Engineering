const text = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Illo reiciendis reprehenderit nobis nam modi deserunt aliquam, sed dicta assumenda deleniti suscipit. Sint dolor iste modi id quaerat, perspiciatis voluptas nam vel?';

// Regular expression litral
const pattern = /[A-z][a-z]+/g;

// RegExp class
const pattern2 = new RegExp('[A-z][a-z]+', 'g');

// ---- REGEX METHODS ----
// Test
const result = pattern.test(text);
console.log(result);

// Exec
const execResult = pattern.exec(text);
console.log(execResult);

// ---- STRING METHODS ----
// Match
console.log('Match ---');
const matchResult = text.match(pattern);
console.log(matchResult);

// Match All
console.log('MatchAll ---');
const matchAllResult = text.match(pattern);
console.log(matchAllResult);

// Replace
const replacedText = text.replace(pattern, '****');
console.log(replacedText);

// Split
const input = 'first.second/third|forth';
const words = input.split(/[\.\/|]/g);
console.log(words);