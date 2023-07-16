var number = Math.floor(Math.random() * 10)
var start = true

while (start) {
     user_number = prompt('Chute um numero:: ')
     if (user_number > number) {
         console.log('Menor!')
     }
     else if (user_number < number) {
         console.log('Maior!')
     }
     else if (user_number == number) {
         console.log('Você ganhou!')
         break
     }
}