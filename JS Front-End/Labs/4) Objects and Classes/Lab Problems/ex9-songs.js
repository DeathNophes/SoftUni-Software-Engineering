function songAlbum (array) {
    const numberOfSongs = array.shift(); // First element is the number of songs
    const typeToPrint = array.pop() // Last element is the type to print or "all"

    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let songs = [];
    for (let i = 0; i < numberOfSongs; i++) {
        const [type, name, time] = array[i].split('_')
        songs.push(new Song(type, name, time))
    }

    for (let obj of songs) {
        if (typeToPrint === 'all') {
            console.log(obj.name)
        }
        else if (typeToPrint === obj.typeList) {
            console.log(obj.name)
        }
    }
}
