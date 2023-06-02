
// IF USERNAME/biogem => APPLICATION APEAR
const username = document.querySelector('#username');
const application = document.querySelector('#application');
const laboratories = document.querySelector('#laboratories');
const clinical_service = document.querySelector('#clinical_service');
laboratories.style.display = 'none';
application.style.display = 'none';
clinical_service.style.display = 'none';


username.addEventListener('change', event => {
  if (event.target.value == 'Laboratoire diagnostic St Louis') {
    application.style.display = 'block';
    laboratories.style.display = 'block';
    clinical_service.style.display = 'none';
  } else if (event.target.value == 'Service clinique St Louis') {
    clinical_service.style.display = 'block';
    application.style.display = 'none';
    laboratories.style.display = 'none';
  } else if (event.target.value == 'None'){
    application.style.display = 'none';
    laboratories.style.display = 'none';
    clinical_service.style.display = 'none';
  }
});

// IF LABORATORIES == AUTRE
const if_no_laboratory = document.querySelector('#if_no_laboratory')
if_no_laboratory.style.display = 'none'

laboratories.addEventListener('change', event => {
    if (event.target.value == 'Autre') {
        if_no_laboratory.style.display = 'block';
    } else {
        if_no_laboratory.style.display = 'none';
    }
})

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
    if (event.target.value == 'Yes') {
        access_data.style.display = 'block';
    } else if (event.target.value == 'No') {
        access_data.style.display = 'none';
    }
});

// IF reg req are AVAILABLE, THEN PRECISE
const regulatory_requirements = document.querySelector('#regulatory_requirements');
const if_regulatory_requirements = document.querySelector('#if_regulatory_requirements');
if_regulatory_requirements.style.display = 'none';

regulatory_requirements.addEventListener('change', event => {
    if (event.target.value == 'Yes') {
        if_regulatory_requirements.style.display = 'block';
    } else if (event.target.value == 'No') {
        if_regulatory_requirements.style.display = 'none';
    }
});

// IF very urgency, THEN PRECISE
const urgency_of_request = document.querySelector('#urgency_of_request');
const if_urgency = document.querySelector('#if_urgency');
if_urgency.style.display = 'none';

urgency_of_request.addEventListener('change', event => {
    if (event.target.value == 'Very urgent') {
        if_urgency.style.display = 'block';
    } else {
        if_urgency.style.display = 'none';

    }
});


