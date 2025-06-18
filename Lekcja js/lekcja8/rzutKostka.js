function rzutKostka(){

    const numRzutu = document.getElementById("numRzutu").value;
    const rzutResult = document.getElementById("rzutResult");
    const rzutObraz = document.getElementById("rzutObraz");
    const values = [];
    const images = [];

    for (let i = 0; i < numRzutu; i++){
        const value = Math.floor(Math.random() * 6) + 1;
        values.push(value);
        images.push(` <img src="rzut_Obrazy/${value}.png"> Rzut ${value} ` );
    }

    rzutResult.textContent = `rzut: ${values.join(', ')}`;
    rzutObraz.innerHTML =  images.join('');

}