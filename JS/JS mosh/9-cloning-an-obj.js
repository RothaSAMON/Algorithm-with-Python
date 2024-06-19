
const circle = {
    radius: 1,
    draw() {
        console.log('draw');
    }
};

// const another = {};
// for (let key in circle)
//     another[key] = circle[key];


//there is the modern & simpler way to clone object
const another2 = { ...circle };

const another = Object.assign({}, circle);


console.log(another);
console.log(another2);