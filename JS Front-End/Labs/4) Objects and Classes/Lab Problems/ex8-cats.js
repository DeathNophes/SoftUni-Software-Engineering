function catCreator (input) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        meow () {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    let cats = [];
    for (let pair of input) {
        const [name, age] = pair.split(' ');
        cats.push(new Cat(name, age));
    }

    for (const obj of cats) {
        obj.meow()
    }
}
