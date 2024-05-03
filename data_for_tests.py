# ответы на запросы

# ответ на post создание пользователя
answr_post_register_user_ok_status_code = 200
answr_post_register_user_ok_success = True

# ответ на post создание пользователя, который уже зарегистрирован
answr_post_register_user_same_data_status_code = 403
answr_post_register_user_same_data_success = False
answr_post_register_user_same_data_message = 'User already exists'

# ответ на post создание пользователя, который уже зарегистрирован
answr_post_register_user_without_data_status_code = 403
answr_post_register_user_without_data_success = False
answr_post_register_user_without_data_message = 'Email, password and name are required fields'

# ответ на post логина пользователя
answr_post_login_user_ok_status_code = 200
answr_post_login_user_ok_success = True

# ответ на post логина пользователя с неверными логином и паролем
answr_post_login_user_with_incorrect_data_status_code = 401
answr_post_login_user_with_incorrect_data_success = False
answr_post_login_user_with_incorrect_data_message = 'email or password are incorrect'

# ответ на putch изменения данных пользователя с авторизацией
answr_patch_update_user_ok_status_code = 200
answr_patch_update_user_ok_success = True

# ответ на putch изменения данных пользователя с авторизацией
answr_patch_update_user_without_auth_status_code = 401
answr_patch_update_user_without_auth_success = False
answr_patch_update_user_without_auth_message = 'You should be authorised'

# ответ на putch изменения почты пользователя на уже существующую
answr_patch_update_user_with_same_email_status_code = 403
answr_patch_update_user_with_same_email_success = False
answr_patch_update_user_with_same_email_message = 'User with such email already exists'

# ответ на post создания заказа
answr_post_create_order_ok_status_code = 200
answr_post_create_order_ok_success = True

# ответ на post создания заказа без ингредиентов с авторизацией
answr_post_create_order_without_ingredients_status_code = 400
answr_post_create_order_without_ingredients_success = False
answr_post_create_order_without_ingredients_message = 'Ingredient ids must be provided'

# ответ на post создания заказа с неверными хэшами ингредиентов с авторизацией
answr_post_create_order_with_badhash_ingredients_status_code = 500

# ответ на post создания заказа без авторизации
answr_post_create_order_without_auth_status_code = 200
answr_post_create_order_without_auth_success = True

# ответ на get получение заказов пользователя
answr_get_orders_user_status_code = 200
answr_get_orders_user_success = True

# ответ на get получение заказов пользователя без авторизации
answr_get_orders_user_without_auth_status_code = 401
answr_get_orders_user_without_auth_success = False
answr_get_orders_user_without_auth_message = 'You should be authorised'
