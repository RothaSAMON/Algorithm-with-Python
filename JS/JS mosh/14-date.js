const now = new Date();
const date1 = new Date('May 11 2018 09:00');
const date2 = new Date(2018, 11, 11, 9); // year, month (0-based), day, hour

now.setFullYear(2017);

console.log("Now:", now.toDateString());
console.log("Date1:", date1.toDateString());
console.log("Date2:", date2.toDateString());


let str8 = "Hello, World!";
let arr8 = str8.split(",");
console.log(arr8); // ["Hello", "World!"] //tye: object
