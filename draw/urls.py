from django.urls import path
from.import views
app_name="draw"
urlpatterns=[
    path("",views.home,name='home'),
    path("sign/",views.sign,name='sign'),
    path("login/",views.login,name='login'),
    path("dashbord/",views.dashbord,name="dashbord"),
    path("viewdrawings/",views.viewdrawings,name="viewdrawings"),
    path("adddrawings/",views.adddrawings,name="adddrawings"),
    path('slogin/',views.Slogin,name='slogin'),
    path('deletedraw/<int:did>',views.deletedraw,name='deletedraw'),
    path('update/<int:did>',views.update,name='update'),
    path('views/',views.view,name="view"),
    path('about/',views.about,name="about"),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('removefromcart/<int:drawings_id>',views.removefromcart,name='removefromcart'),
    path('payment/',views.payment,name='payment'),
    path('card/',views.card,name='card'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup')
]