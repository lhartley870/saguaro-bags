# Testing

## Validators

### CSS
[The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used for testing the css code for the site. The following results show that no errors have been found:
* [base.css file](readme-documents/validation-results/clear-results/css/clear-result-base-css.png)
* [profile.css file](readme-documents/validation-results/clear-results/css/clear-result-profile-css.png)
* [products.css file](readme-documents/validation-results/clear-results/css/clear-result-products-css.png)
* [home.css file](readme-documents/validation-results/clear-results/css/clear-result-home-css.png)
* [checkout.css file](readme-documents/validation-results/clear-results/css/clear-result-checkout-css.png)
* [basket.css file](readme-documents/validation-results/clear-results/css/clear-result-basket-css.png)

### JavaScript
[The JSHint Validator](https://jshint.com/) was used for testing the javascript code for the site. For the JavaScript contained within script tags in html files, this was extracted and run throgh the JSHint validator. The following results show that no errors have been found:
* [base.js file](readme-documents/validation-results/clear-results/js/clear-result-base-js.png)
* [title logo js in base.html](readme-documents/validation-results/clear-results/js/clear-result-base-title-logo-script-js.png)
* [countryfield.js file](readme-documents/validation-results/clear-results/js/clear-result-countryfield-js.png)
* [js in quantity_input_script.html](readme-documents/validation-results/clear-results/js/clear-result-quantity-input-script-js.png)
* [js in add_bag.html and edit_bag.html script tags](readme-documents/validation-results/clear-results/js/clear-result-add-edit-bag-script-js.png)
* [scroll to top button js in bags.html script tag](readme-documents/validation-results/clear-results/js/clear-result-scroll-top-js.png)
* [js for sorting functionality in bags.html script tag](readme-documents/validation-results/clear-results/js/clear-result-sorting-js.png)
* [js in the script tag in basket.html](readme-documents/validation-results/clear-results/js/clear-result-basket-js.png)

An error was found in the toast JS in base.html with the error being that bootstrap is an undefined variable. However, this code was taken from the Bootstrap documentation and thus relies on the bootstrap framework variable:
* [toast js in base.html](readme-documents/validation-results/errors/js/result-base-toast-script-js.png)
Errors were found in the Mailchimp JS in base.html. However, this code was provided directly by Mailchimp:
* [mailchimp js in base.html](readme-documents/validation-results/errors/js/result-base-mailchimp-script-js.png)
An error was found in the stripe_elements.js file with the error being that Stripe is an undefined variable. However, as with bootstrap, this code relies upon Stripe:
* [stripe_elements.js](readme-documents/validation-results/errors/js/result-stripe-elements-js.png)

### Python
[The PEP8 Online Validator Service](http://pep8online.com/) was used for testing the python code for the application. The following results show that no errors have been found: 

* [custom_storages.py file result](readme-documents/validation-results/clear-results/python/clear-result-custom-storages.png)
* [settings.py file result](readme-documents/validation-results/clear-results/python/clear-result-settings.png)
* [project urls.py file result](readme-documents/validation-results/clear-results/python/clear-result-project-urls.png)

* **Home app**
* [urls.py file result](readme-documents/validation-results/clear-results/python/clear-result-home-urls.png)
* [views.py file result](readme-documents/validation-results/clear-results/python/clear-result-home-views.png)

* **Profiles app**
* [forms.py file result](readme-documents/validation-results/clear-results/python/clear-result-profiles-forms.png)
* [models.py file result](readme-documents/validation-results/clear-results/python/clear-result-profiles-models.png)
* [urls.py file result](readme-documents/validation-results/clear-results/python/clear-result-profiles-urls.png)
* [views.py file result](readme-documents/validation-results/clear-results/python/clear-result-profiles-views.png)

* **Products app**
* [admin.py file result](readme-documents/validation-results/clear-results/python/clear-result-products-admin.png)
* [forms.py file result](readme-documents/validation-results/clear-results/python/clear-result-products-forms.png)
* [models.py file result](readme-documents/validation-results/clear-results/python/clear-result-products-models.png)
* [urls.py file result](readme-documents/validation-results/clear-results/python/clear-result-products-urls.png)
* [views.py file result](readme-documents/validation-results/clear-results/python/clear-result-products-views.png)
* [widgets.py file result](readme-documents/validation-results/clear-results/python/clear-result-products-widgets.png)

* **Checkout app**
* [__init__.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-init.png)
* [admin.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-admin.png)
* [apps.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-apps.png)
* [forms.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-forms.png)
* [models.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-models.png)
* [signals.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-signals.png)
* [urls.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-urls.png)
* [views.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-views.png)
* [webhook_handler.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-webhook-handler.png)
* [webhooks.py file result](readme-documents/validation-results/clear-results/python/clear-result-checkout-webhooks.png)

* **Basket app**
* [contexts.py file result](readme-documents/validation-results/clear-results/python/clear-result-basket-contexts.png)
* [urls.py file result](readme-documents/validation-results/clear-results/python/clear-result-basket-urls.png)
* [views.py file result](readme-documents/validation-results/clear-results/python/clear-result-basket-views.png)
* [bag_tools.py file result](readme-documents/validation-results/clear-results/python/clear-result-bag-tools.png)

* [urls.py file in booking app result](readme-documents/validation-results/clear-result-booking-urls.png)
* [views.py file result](readme-documents/validation-results/clear-result-views.png)
* [urls.py file in nightgarden project result](readme-documents/validation-results/clear-result-nightgarden-urls.png)

Initially when the project was run through the validator an error was raised in relation to the products app models.py file as shown:
+ [products app models.py file initial result](readme-documents/validation-results/errors/python/error-result-products-models.png).

The error was *'line break before binary operator'*. This error also appeared for the checkout app models.py file. This error was resolved by moving the applicable line break to after the binary operator in both cases.

## Manual Testing

### Browser Testing

The manual testing of the website was carried out on the following devices:

1. Mobile phone (Apple iPhone 11 with a device viewport size of 414px by 896px)
2. Tablet (Apple iPad mini with a device viewport size of 768px by 1024px)
3. Laptop (Apple MacBook Pro with a device viewport size of 1440px by 900px)
4. A large monitor (Asus monitor with a device viewport size of 1920px by 1080px) connected to the MacBook Pro

The website was tested on the following browsers on all of the above devices:

1. [Google Chrome](https://www.google.co.uk/chrome/?brand=FHFK&gclid=EAIaIQobChMI3b-xi9y38QIVBrTtCh2I1g3AEAAYASAAEgJN5vD_BwE&gclsrc=aw.ds)
2. [Microsoft Edge](https://www.microsoft.com/en-us/edge)
3. [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
4. [Safari](https://www.apple.com/uk/safari/) 

The site was created using the Chrome browser and Chrome DevTools and was fully tested in that environment as it was being developed. The site was then further tested after deployment on all of the above devices and browsers.

### Manual Tests

The manual testing results can be found [here](). They largely detail manual testing of the user stories. A few test items not directly related to a particular user story are also detailed at the end of the document.

## Contrast Checker Testing

The foreground text colours and their background colours were tested using the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). The following combinations were tested and all received at least a WCAG AA pass. The results are as follows: 

* 

## Fixed Bugs


## Unfixed Bugs

    