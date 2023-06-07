
//------------------------------------------------------------- LOAD PDF FILE FROM RECAP PROJECT HTML PAGE
function htmlIntoPDF() {
    var pdf = new jsPDF('p', 'pt', 'letter');
    // source can be HTML-formatted string, or a reference
    // to an actual DOM element from which the text will be scraped.
    source = $('#content')[0];

    // we support special element handlers. Register them with jQuery-style 
    // ID selector for either ID or node name. ("#iAmID", "div", "span" etc.)
    // There is no support for any other type of selectors 
    // (class, of compound) at this time.
    specialElementHandlers = {
        // element with id of "bypass" - jQuery style selector
        '#bypassme': function (element, renderer) {
            // true = "handled elsewhere, bypass text extraction"
            return true
        }
    };
    margins = {
        top: 80,
        bottom: 60,
        left: 40,
        width: 522
    };
    // all coords and widths are in jsPDF instance's declared units
    // 'inches' in this case
    pdf.fromHTML(
        source, // HTML string or DOM elem ref.
        margins.left, // x coord
        margins.top, { // y coord
            'width': margins.width, // max width of content on PDF
            'elementHandlers': specialElementHandlers
        },

        function (dispose) {
            // dispose: object with X, Y of the last line add to the PDF 
            //          this allow the insertion of new lines after html
            pdf.save('recap_project.pdf');
        }, margins
    );
}


//------------------------------------------------------------- VISUALIZE PASSWORD
function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}


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


//text description

document.getElementById("zone-survol").addEventListener("mouseover", function() {
    document.getElementById("texte-cache").style.display = "block";
 });
 
 document.getElementById("zone-survol").addEventListener("mouseout", function() {
    document.getElementById("texte-cache").style.display = "none";
 });
 