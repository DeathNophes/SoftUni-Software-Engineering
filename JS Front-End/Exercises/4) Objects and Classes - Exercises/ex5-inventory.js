function heroRegister (input) {
   let heroes = [];

   for (let line of input) {
       const [name, level, items] = line.split(' / ')
       const thisHero = {
           'name': name,
           'level': level,
           'items': items
       }
       heroes.push(thisHero)
   }

   const sortedHeroes = heroes.sort((a, b) => a.level - b.level);

   for (let hero of sortedHeroes) {
       console.log(`Hero: ${hero.name}`);
       console.log(`level => ${hero.level}`);
       if (hero.items.length > 0) {
           console.log(`items => ${hero.items}`)
       }
   }
}
