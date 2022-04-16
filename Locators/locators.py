class Locators():
    # account create objects
    email_textbox_id = "email_create"
    create_button_name = "SubmitCreate"

    # accounts details objects
    firstname_id = "customer_firstname"
    lastname_id = "customer_lastname"
    password_id = "passwd"
    address = "address1"
    city_id = "city"
    state_id = "id_state"
    postcode_id = "postcode"
    mobile = "phone_mobile"
    submit_buttoon_id = "submitAccount"

    # Signout
    signout_class = './/a[@class="logout"]'

    # login
    login_email_textbox_id = "email"
    login_password_textbox_id = "passwd"
    login_button_id = "SubmitLogin"

    #Shopping steps
    go_to_tshirt_link = "http://automationpractice.com/index.php?id_category=5&controller=category"
    filter_button_id = "layered_id_attribute_group_14"
    product_link_text = "Faded Short Sleeve T-shirts"
    add_to_cart_button = "Submit"
    checkout_button_class = './/a[@class="btn btn-default button button-medium"]'
    confirm_Checkout_class = './/a[@class="button btn btn-default standard-checkout button-medium"]'
    confirm_Checkout_next = 'processAddress'
    checkerbox = './/div[@class="checker"]'
    confirm_shipping = "processCarrier"
    payment_class = './/a[@class="cheque"]'
    confirmation_class = './/button[@class="button btn btn-default button-medium"]'
