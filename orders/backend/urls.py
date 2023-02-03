from django.urls import path, include

from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from .views import RegisterAccount, ConfirmAccount, LoginAccount, AccountDetails, ContactView, \
    PartnerUpdate, PartnerState , LoginAccount, CategoryView,   \
    ShopView, ProductInfoView, BasketView, ContactView, OrderView, PartnerOrders


app_name = 'backend'
urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'), #работает
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),  #выдает ложное
    path('user/login', LoginAccount.as_view(), name='user-login'),  #работает
    path('user/details', AccountDetails.as_view(), name='user-details'),    #Работает
    path('user/contact', ContactView.as_view(), name='user-contact'),   #Работает
    path('user/password_reset', reset_password_request_token, name='password-reset'),   #Шевелится, проверить через почту
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'), #Страница не найдена

    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),  #Работает
    path('partner/state', PartnerState.as_view(), name='partner-state'),  #Работает
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),  #Работает

    path('shops', ShopView.as_view(), name='shops'),  #Работает
    path('categories', CategoryView.as_view(), name='categories'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]