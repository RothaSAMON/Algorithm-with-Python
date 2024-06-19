// string primitive
//check type: string: 
const message = 'hi';
console.log(typeof(message));

// string object (added "new" operator cuz it a constructor function)
//check type: object: 
const another = new String('hii');
console.log(typeof(another))

let str = "Array: ";
let arr = [1, 2, 3];
console.log(str.concat(arr)); // "Array: 1,2,3"


let str2 = "Object: ";
let obj = {key: "value"};
console.log(str2.concat(obj)); // "Object: [object Object]" type: String


let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combinedArr = arr1.concat(arr2);
console.log(combinedArr); // [1, 2, 3, 4, 5, 6] type: object



let str3 = "Hello, World!";
console.log(str3.lastIndexOf("W")); // 8 it will return -1 if it not in there



let str4 = "Hello, World!";
console.log(str4.indexOf("H")); // 0



let str5 = "Hello, World!";
let newStr = str5.replace("World", "HAHA"); //first string is the place and second is the new string
console.log(newStr); // "Hello, JavaScript!" 


let str6 = "Hello, World!";
console.log(str6.search("World")); // 7


let str7 = "Hello, World!";
console.log(str7.slice(5)); // "Hello"
console.log(str7.slice(-6, -1)); // "World"



let str8 = "Hello, World!";
let arr8 = str8.split(", ");
console.log(arr8); // ["Hello", "World!"] //tye: object




let str9 = "Hello, World!";
console.log(str9.substring(0, 5)); // "Hello"
console.log(str9); //Hello, World! the origin string stay still




let str10 = "Hello!";
console.log(str10.repeat(20)); // "Hello!Hello!Hello!"



