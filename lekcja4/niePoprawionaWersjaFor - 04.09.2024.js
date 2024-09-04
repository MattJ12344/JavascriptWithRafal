
console.log("
// Wersja 1 TO SAMO
for (let i
=
0; i < 5; i++) {
console.log("i=
+ i);
}
console.log("
// Wersja 2 TO SAMO
for (let i
=
0; i < 5; i
=
i+1) {
console.log("i=
+ i);
}
console.log("
// Wersja 3 TO SAMO
for (let i = 0; i < sth(); i = sth2(i)) {
console.log("i=
+ i);
}
function sth() {
return 5;
}
function sth2(i: number) {
}
return i + 1;
console.log("
// Wersja 4 TO SAMO
let i
=
0;
for(; i < 5;) {
}
console.log("i=
i++
console.log("
+ i);
// for (ZINCIJALIZUJ; BOOLEAN; ZWIĘKSZ/ZMNIEJSZ) {
// }
===