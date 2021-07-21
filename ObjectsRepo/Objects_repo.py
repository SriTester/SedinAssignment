class objects_repo:

    username = "//div[@id='login_button_container']//input[@placeholder='Username']"
    password ="//div[@id='login_button_container']//input[@placeholder='Password']"
    submit ="//div[@id='login_button_container']//input[@type='submit']"
    product_add ="//div[@class='inventory_item']//div//following-sibling::div//div//div[text()='{0}']/parent::a/parent::div/parent::div//div//button"
    Cart_Value ="//div[@class='shopping_cart_container']"
    Product_Cart_Added ="//div[@class='inventory_item_name']"
    Product_Particular_Name ="//div[@class='inventory_item_label']//div[text()='{0}']"
    Products_list ="//div[@class='inventory_item']//div[@class='inventory_item_name']"
    Cart_Check_Product_Check="//div[@class='cart_item']//div[text()='{0}']"
    Cart_Checkout_Button="//div[@class='cart_footer']//button[text()='Checkout']"
    Error_Message ="//h3[contains(text(),'Epic sadface: Username and password do not match a')]"
    Product_Prices ="//div[@class='inventory_item_price']"
    Products_details_price="//div[@class='inventory_details_price']"
    Back_to_products ="//div[@class='header_secondary_container']//div//button"

