//------------------------------------------------------------- DIAPO CONTACT
let compteur = 0; // permet de connaitre l'image dans lequelle on se trouve
let timer, elements, slides, slideWidth;
const parentElement = document.getElementById('user');

window.onload = () => {
    // on recupere le diapo
    const diapo = document.querySelector(".diapo");
    elements = document.querySelector(".elements");
    // on clone la 1ere image
    if (parentElement !== null) {
        let firstImage = elements.firstElementChild.cloneNode(true);
        // on injeste le clone a la fin du diapo
        elements.appendChild(firstImage);
        slides = Array.from(elements.children);
        // on recup la largeur d'une slide
        slideWidth = diapo.getBoundingClientRect().width;
        // on recupere les fleches
        let next = document.querySelector("#nav-droite");
        // on gere le clic
        next.addEventListener("click", slideNext);
    } else {
        console.error("user element does not exist.");
    }
}

function slideNext(){
    // incrementer le compteur
    compteur++;
    elements.style.transition = "1s linear";
    let decal = -slideWidth * compteur;
    elements.style.transform = `translateX(${decal}px)`;

    // on attend la fin de la transition et on rebobine de facon cachee
    setTimeout(function(){
        if(compteur >= slides.length-1){
            compteur = 0;
            elements.style.transition= 'unset';
            elements.style.transform ="translateX(0)";
        }
    }, 1000)
     
}