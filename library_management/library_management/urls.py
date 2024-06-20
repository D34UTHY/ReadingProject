from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# Define a lista padrão de URL para a aplicação
urlpatterns = [
    # URL padrão para acessar a interface de administração do Django
    path('admin/', admin.site.urls),
    # Inclui as URLs definidas no aplicativo 'api'. A base URL para essas rotas será 'api/'
    path('api/', include('api.urls')),
    # Obtenção de um novo token JWT, sendo TokenObtainPerView uma view fornecida pelo Django Framework atrelado ao jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Atualiza o token JWT utilizando outra view fornecida pelo mesmo pacote
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]