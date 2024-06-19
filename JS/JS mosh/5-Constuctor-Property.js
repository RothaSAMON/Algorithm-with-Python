
//Factory Function
function createCircle(radius) {
    return {
        radius,
        draw() {
            console.log('draw');
        }
    };
}
const circle = createCircle(1);


//Constructor Function
function Circle(radius) {
    this.radius = radius;
    this.draw = function(){
        console.log('draww');
    }
}
const another =  new Circle(1);