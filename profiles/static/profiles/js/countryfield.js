/* 
Runs the changeTextColour function on page load
and every time the country field in the default delivery
information form is changed.
*/
let countryField = $('#id_default_country');
changeTextColour();
countryField.change(changeTextColour);

/** 
 * Checks the value of the country field in the default delivery
 * information form. If it is blank (ie 'Country' text is showing),
 * set the text colour to green, otherwise set the text colour to purple.
*/
function changeTextColour() {
    let countrySelected = countryField.val();
    if (!countrySelected) {
        if (countryField.hasClass('text-purple')) {
            countryField.removeClass('text-purple');
        }
        countryField.addClass('text-green');
    } else {
        if (countryField.hasClass('text-green')) {
            countryField.removeClass('text-green');
        }
        countryField.addClass('text-purple');
    }
}