const circle = {
    radius: 1,
    draw() {
        console.log('draw');
    }
}

for (let key in circle)
    console.log(key, circle[key]);

//If we display for of loop in here it will error:
//cus it can be use with iterables such as array and maps. NOTE: Obj is not iterables

// for (let key of circle)
//     console.log(key);

for (let key of Object.keys(circle))
    console.log(key);