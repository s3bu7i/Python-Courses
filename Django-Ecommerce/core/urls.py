from django.urls import path
from django.views import View
from .views import send_contact_email
from django.urls import path
from . import views

from .views import (
    ItemDetailView,
    HomeView,
    LoginView,
    add_to_cart,
    contact_form,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    send_contact_email
)
from core import views
handler404 = 'core.views.custom_404'
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('about/', views.about, name='about'),
    # path('send-contact-email/', send_contact_email, name='send_contact_email'),
    #path('contact/', views.contact_form(), name='index'),
]
