class Cat {
    examCount = 0; // initialize property
    #internalValue = 'Secret'; // private property
    static value = 'Some static value';
    static #staticPrivate = 'Value that is private and static' // static private property

    constructor(name, breed, age) {
        this.name = name;
        this.breed = breed;
        this.age = age;
    }

    makeSound() {
        console.log(`${this.name} - Meow...`);
    }

    recordExam() {
        console.log(`${this.name} has been examined.`);
        this.examCount++;
    }

    static hasVaccines(cat) {
        return cat.examCount > 0;
    }

    // getter property
    get internalValue() {
        return this.#internalValue;
    }

    set internalValue(value) {
        this.#internalValue = value;
    }
}

const zuza = new Cat('Zuza', 'British Shorthair', 8);

console.log(zuza);

console.log(zuza.internalValue);
zuza.internalValue = 'Updated internal value';
console.log(zuza.internalValue);


zuza.makeSound();
zuza.recordExam();

console.log(zuza.examCount);
console.log(zuza);
console.log(typeof zuza);

console.log('Is Zuza vaccinated? ->', Cat.hasVaccines(zuza) );

/// ------------

function createCat(name, breed, age) {
    return {
        name,
        breed,
        age,
    }
}

const aria = createCat('Aria', 'British Shorthair', 1);

console.log(aria);