# Testing

## Validators

### HTML
[The W3C Markup Validation Service](https://validator.w3.org/) was used for testing the html code for the site. As this project uses Django templates, the html was tested by visiting each page of the site, right clicking, selecting 'View page source' and copying and pasting the code shown into the validator. Validation has only been carried out for pages created by the developer and the django allauth templates customised by the developer. The following results show that no errors have been found: 
* [Home page html](readme-documents/validation-results/clear-results/html/clear-result-home-pg-html.png)
* [All Bags page html](readme-documents/validation-results/clear-results/html/clear-result-all-bags-pg-html.png)
* [All Bags page displaying all styles with the style badges at the top](readme-documents/validation-results/clear-results/html/clear-result-all-styles-html.png)
* [All Bags page displaying all special offers with the Sale and Free Charm badges at the top](readme-documents/validation-results/clear-results/html/clear-result-all-special-offers-html.png)
* [All Bags page search results where some results have been found](readme-documents/validation-results/clear-results/html/clear-result-positive-search-result-html.png)
* [All Bags page search results where no results were found](readme-documents/validation-results/clear-results/html/clear-result-no-search-results-html.png)
* [Bag Detail page showing a bag with a charm option but not on sale](readme-documents/validation-results/clear-results/html/clear-result-bag-detail-charm-no-sale-html.png)
* [Bag Detail page showing a bag with no charm option and not on sale](readme-documents/validation-results/clear-results/html/clear-result-bag-detail-no-charm-no-sale-html.png)
* [Bag Detail page showing a bag on sale and with a charm option](readme-documents/validation-results/clear-results/html/clear-result-bag-detail-sale-and-charm-html.png)
* [Bag Detail page showing a bag on sale but with no charm option](readme-documents/validation-results/clear-results/html/clear-result-bag-detail-sale-no-charm-html.png)
* [Signup page](readme-documents/validation-results/clear-results/html/clear-result-signup-html.png)
* [Verify email address page](readme-documents/validation-results/clear-results/html/clear-result-verify-email-address-html.png)
* [Confirm email address page](readme-documents/validation-results/clear-results/html/clear-result-confirm-email-html.png)
* [Login page after confirming email as part of signup with toast](readme-documents/validation-results/clear-results/html/clear-result-login-after-confirming-email-with-toast-html.png)
* [Login page](readme-documents/validation-results/clear-results/html/clear-result-login-html.png)
* [Login page displaying allauth error message](readme-documents/validation-results/clear-results/html/clear-result-login-with-allauth-error-html.png)
* [Logout page](readme-documents/validation-results/clear-results/html/clear-result-logout-html.png)
* [Password reset page](readme-documents/validation-results/clear-results/html/clear-result-password-reset-html.png)
* [Page confirming password reset email sent](readme-documents/validation-results/clear-results/html/clear-result-confirm-password-reset-email-sent-html.png)
* [Change password page](readme-documents/validation-results/clear-results/html/clear-result-change-password-html.png)
* [Password now changed page](readme-documents/validation-results/clear-results/html/clear-result-password-now-changed-html.png)
* [Add a bag page](readme-documents/validation-results/clear-results/html/clear-result-add-bag-html.png)
* [Bag detail page for new bag added with success toast](readme-documents/validation-results/clear-results/html/clear-result-bag-detail-add-bag-success-toast-html.png)
* [Edit a bag page](readme-documents/validation-results/clear-results/html/clear-result-edit-bag-html.png)
* [Bag detail page for edited bag with success toast](readme-documents/validation-results/clear-results/html/clear-result-bag-detail-edit-bag-success-toast-html.png)
* [All bags page with deleted bag success toast](readme-documents/validation-results/clear-results/html/clear-result-all-bags-delete-bag-success-toast-html.png)
* [Privacy page](readme-documents/validation-results/clear-results/html/clear-result-privacy-pg-html.png)
* [404 error page](readme-documents/validation-results/clear-results/html/clear-result-404-error-html.png)
* [500 error page](readme-documents/validation-results/clear-results/html/clear-result-500-error-html.png)
* [Basket page](readme-documents/validation-results/clear-results/html/clear-result-basket-pg-html.png)
* [My Profile page](readme-documents/validation-results/clear-results/html/clear-result-my-profile-pg-html.png)
* [Checkout page for registered user](readme-documents/validation-results/clear-results/html/clear-result-checkout-pg-registered-user-html.png)
* [Checkout success page for registered user](readme-documents/validation-results/clear-results/html/clear-result-checkout-success-registered-user-html.png)
* [Checkout page for a non-registered user](readme-documents/validation-results/clear-results/html/clear-result-checkout-pg-not-registered-user-html.png)
* [Checkout success page for a non-registered user](readme-documents/validation-results/clear-results/html/clear-result-checkout-success-not-registered-user-html.png)
* [Checkout success page navigated to as order history from the My Profile page](readme-documents/validation-results/clear-results/html/clear-result-checkout-success-history-html.png)


Initially there were errors with the home page which are shown in the following results:
* [Initial home page html error part 1](readme-documents/validation-results/errors/html/home-html-error-part-1.png)
* [Initial home page html error part 2](readme-documents/validation-results/errors/html/home-html-error-part-2.png)

The *'duplicate ids'* error was addressed by changing the id names. The *'type attribute being unnnessary for JavaScript resources'* error was addressed by removing the attribute from all script tags in html files. The *'element li not allowed as child of element div in this context'* was resolved by wrapping the mobile top header li elements in a ul element instead and adjusting the styling accordingly.  

There were also initially errors with the privacy page which are shown in the following results:
* [Initial privacy page errors](readme-documents/validation-results/errors/html/privacy-html-error.png)

One error related to the mailchimp logo image not having an alt tag. This was resolved by adding one.
The section lacks heading was resolved by adding a heading of 'Introduction'.

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
* [js in the script tag in 500.html](readme-documents/validation-results/clear-results/js/clear-result-500-error-pg-js.png)

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

The manual testing results can be found [here](readme-documents/manual-testing-results/manual-tests.pdf). They largely detail manual testing of the user stories. A few test items not directly related to a particular user story are also detailed at the end of the document.

## Contrast Checker Testing

The foreground text colours and their background colours were tested using the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). The following combinations were tested and all received at least a WCAG AA pass. The results are as follows: 

* The Spanish Viridian colour (#00855D) was tested against the white colour (#FFFFFF):
    * [results](readme-documents/colour-contrast-results/contrast-spanish-veridian-against-white.png) 
* The white colour (#FFFFFF) was tested against the Spanish Viridian colour (#00855D):
    * [results](readme-documents/colour-contrast-results/contrast-white-against-spanish-veridian.png) 
* The Mexican pink colour (#E4117A) was tested against the white colour (#FFFFFF):
    * [results](readme-documents/colour-contrast-results/contrast-mexican-pink-against-white.png) 
* The white colour (#FFFFFF) was tested against the Mexican pink colour (#E4117A):
    * [results](readme-documents/colour-contrast-results/contrast-white-against-mexican-pink.png) 
* The Toolbox colour (#6C6EC4) was tested against the white colour (#FFFFFF):
    * [results](readme-documents/colour-contrast-results/contrast-toolbox-against-white.png) 
* The white colour (#FFFFFF) was tested against the Toolbox colour (#6C6EC4):
    * [results](readme-documents/colour-contrast-results/contrast-white-against-toolbox.png) 
* The Rusty Red colour (#DC3545) used by Bootstrap for errors was tested against white (#FFFFFF):
    * [results](readme-documents/colour-contrast-results/contrast-rusty-red-against-white.png) 
* The allauth error messages of Antique Ruby (#842029) were tested against their background of Pale Pink (#F8D7DA):
    * [results](readme-documents/colour-contrast-results/contrast-antique-ruby-against-pale-pink.png) 
* The Space Cadet link colour (#1F2551) was tested against the white background colour (#FFFFFF) and each of the text colours:
    * [results for body text colour Spanish Viridian](readme-documents/colour-contrast-results/contrast-link-colour-against-spanish-viridian-body.png)
    * [results for body text colour Mexican Pink](readme-documents/colour-contrast-results/contrast-link-colour-against-mexican-pink-body.png)
    * [results for body text colour Toolbox](readme-documents/colour-contrast-results/contrast-link-colour-against-toolbox-body.png)

## Fixed Bugs
1. Initially, clicking on the basket in the hover/focus state (when it has turned into a purple trolley) was not actually taking the user to the basket page, so the link was broken. This was because the whole i element was being added and removed with JavaScript in a separate javascript file linked to base.html via a script tag. This issue was resolved by leaving the i element in the html page and just changing its class in the JavaScript file to change it from a basket to a trolley when being hovered over/focussed on and back to a basket when not being hovered over/focussed on.
2. Similarly, the Saguaro Bags title logo being added on medium sized screens via JavaScript was also not taking the user to the home page when clicked on, so the link was broken. This was resolved by putting the relevant JavaScript in a script tag at the bottom of base.html instead of in a separate JavaScript file linked to base.html in a script tag.
3. For some reason the top and bottom right corners of the quantity incrementer (+) button were not rounded on the shopping basket page even though, for example, on the bag detail page where the same incrementer button was used with the same styling, this issue did not arise. This was fixed by adding css to make those corners rounded on the shopping basket page.
4. Initially, in the products app forms.py file, I tried to return the cleaned data for the clean methods in the check_form_entry_unique mixin method. However, I realised that the cleaned data has to be returned in each individual clean method itself rather than in a mixin method that the clean method uses, in order to work.

## Unfixed Bugs
1. In the deployed application, when a registered user is presented with a checkbox to choose whether or not they want their delivery information to be saved to their profile on the checkout page, their delivery information is always saved to their profile, even when the checkbox is not checked. This issue does not arise in the development environment. I have spoken to a Code Institute tutor (Sean Murphy), being as the code used is based upon code used in the Code Institute Boutique Ado walkthrough project, and he has advised that this is a bug in Boutique Ado and there seems to be no known cause or solution.
2. On the basket page, there is a bug in relation to the quantity inputs. The incrementer plus and minus buttons work as expected on all screen sizes, namely that the user can use the buttons to adjust the quantity to between 0 and 99 (inclusive). If the quantity is decremented to 0, the minus button is disabled and the user cannot click to a negative number and if the quantity is incremented to 99, the plus button is disabled and the user cannot increment to 100 and beyond. It is expected that most users would use the plus and minus buttons to change the quantity of an item. The bug relates to the user typing in a quantity or using the inbuilt input up and down arrows to adjust the quantity. The bug does not appear on the basket page for mobile screens, only on medium screens of 768px wide and larger. The expected behaviour that is present on the basket page on mobile screens is that if the user types in 0 or a negative number, the minus button will be disabled and if the user types in a number above 0 the minus button will be enabled. Similarly, if the user types in a number of 99 or larger, the plus button should be disabled and if they type a number below 99, the plus button should be enabled. However, there seems to be no change event firing if the user types in a number or uses the up/down arrows so that e.g. if the user were to decrement to 0 using the minus button and then type in 1, the minus button is not enabled, it remains disabled. As a side note, it is expected that users can manually type in or use the up/down arrows to enter a negative value, a value over 99 or a blank value on the basket page. These eventualities are dealt with by the python code and an appropriate error message toast being displayed to the user. 
    