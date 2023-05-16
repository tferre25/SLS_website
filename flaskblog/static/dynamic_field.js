
// IF USERNAME/biogem => APPLICATION APEAR
const username = document.querySelector('#username');
const application = document.querySelector('#application');
application.style.display = 'none';

username.addEventListener('change', event => {
  if (event.target.value == 'BioGem') {
    application.style.display = 'block';
  } else if (event.target.value == 'Another_DMU') {
    application.style.display = 'none';
  }
});

// IF APPLICATION/RESEARCH ==> 4 FIELD APEAR 
const organism = document.querySelector('#organism');
const principal_investigator = document.querySelector('#principal_investigator');
const promotor = document.querySelector('#promotor');

application.addEventListener('change', event => {
    if (event.target.value == 'For_diagnosis') {
        organism.style.display = 'none';
        principal_investigator.style.display = 'none';
        promotor.style.display = 'none';
    } else if (event.target.value == 'For_research') {
        organism.style.display = 'block';
        principal_investigator.style.display = 'block';
        promotor.style.display = 'block';
    }
})

// IF DATA IS AVAILABLE, THEN PRECISE
const data_available = document.querySelector('#data_available');
const access_data = document.querySelector('#access_data');
access_data.style.display = 'none';

data_available.addEventListener('change', event => {
    if (event.target.value == '1') {
        access_data.style.display = 'block';
    } else if (event.target.value == '0') {
        access_data.style.display = 'none';
    }
});

// IF reg req are AVAILABLE, THEN PRECISE
const regulatory_requirements = document.querySelector('#regulatory_requirements');
const if_regulatory_requirements = document.querySelector('#if_regulatory_requirements');
if_regulatory_requirements.style.display = 'none';

regulatory_requirements.addEventListener('change', event => {
    if (event.target.value == '1') {
        if_regulatory_requirements.style.display = 'block';
    } else if (event.target.value == '0') {
        if_regulatory_requirements.style.display = 'none';
    }
});

// IF very urgency, THEN PRECISE
const urgency_of_request = document.querySelector('#urgency_of_request');
const if_urgency = document.querySelector('#if_urgency');
if_urgency.style.display = 'none';

urgency_of_request.addEventListener('change', event => {
    if (event.target.value == 'vu') {
        if_urgency.style.display = 'block';
    } else {
        if_urgency.style.display = 'none';

    }
});


