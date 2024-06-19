/*
Javascript dynamic: which is mean once you create them you can always add new properties
or methods, or remove existing ones.
*/


//In this "const" we can change the value and it will error.
const circle = {
    radius: 1
};
//Here is added the properties from the object
circle.color = 'yellow'
circle.drawssss = function() {}

//Here is delete the properties from the object
delete circle.color;
delete circle.drawssss;

console.log(circle);