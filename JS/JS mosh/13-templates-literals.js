//string primitive
const message = 'This is \n' +
'\'my\' sheeeh';
console.log(message);

//object {}
//boolean true, false
//string '' , ""
//template ``

//with this template style it can make the code more easy to read.
const another =
`This is my
'first' text.`;
console.log(another);

//This is the way we can make it dynamic and we can use the function in it.
const name = 'broo';
const text =
`Hi ${name},

Thank you for joining us with your $${2 + 3}.
And hope you happy with it.

Regards,
Rothaa`;
console.log(text);