// Literals
const singleQuoteLiteral = 'text';
const doubleQuoteLiteral = "text";
const templateLiteral = `Some longer ${singleQuoteLiteral}`;

console.log(templateLiteral);

// Escaping
const quoteText = 'quote: "Fancy quote"';
const singleQuoteText = "K'vo staa?";
const escapeCharacters = 'quote: \'Some Fancy Quote\'';

console.log(escapeCharacters);

// Concatenation operator
const firstString = 'We are bob.';
const secondString = 'We are legion.'
const greet = firstString + ' ' + secondString;
console.log(greet);

// concatenation method
console.log(firstString.concat(' ' + secondString));

// indexOf
const text = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Illo reiciendis reprehenderit nobis nam modi deserunt aliquam, sed dicta assumenda deleniti suscipit. Sint dolor iste modi id quaerat, perspiciatis voluptas nam vel?';
const firstDolorIndex = text.indexOf('dolor');
const lastDolorIndex = text.lastIndexOf('dolor');
console.log(firstDolorIndex, lastDolorIndex);

// substring
const subText = text.substring(0, firstDolorIndex);
console.log(text);
console.log(subText);

// replace
const replaceDolorText = text.replaceAll('dolor', '$$$');
console.log(replaceDolorText);

// split
const loremArr = text.split(' ');
const sentences = text.split('. ');
console.log(sentences);

// includes 
const hasDolor = text.includes('dolor');
console.log(hasDolor);

// repeat
console.log('Ho '.repeat(3));
console.log('Tra' + 'la'.repeat(2));

// trim
const stringWithSpacing = '     some  text  here     ';
console.log(stringWithSpacing);
console.log(stringWithSpacing.trimEnd());
console.log(stringWithSpacing.trimStart());
console.log(stringWithSpacing.trim().replaceAll('  ', ' '));

// startWith endswith
console.log(text.startsWith('Lorem'));
console.log(text.endsWith('Ipsum'));

// padStart padEnd
const number = 10;
const binaryString = number.toString(2);
console.log(binaryString);
console.log(binaryString.padStart(8, '0'));

const decimalNumber = 0.011;
console.log(decimalNumber.toString().padEnd(8, '0'));