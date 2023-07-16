let x = prompt('tamanho da piramide: ')
let piramide = ''
for (let i = 1; i <= x; i++) {
   for (let ii = 1; ii <= i; ii++) {
       piramide += i.toString()
   }
   piramide += '\n'
}
console.log(piramide)