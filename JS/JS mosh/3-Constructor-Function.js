//Camel Notaion: oneTwoThree
//Pascal Notation: OneTwoThree


function createCircle(radius) {
    return {
        radius,
        draw() {
            console.log('draw');
        }
    };
}

//Constructor Function
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}

const Circle = new Circle(1);
const x = {};