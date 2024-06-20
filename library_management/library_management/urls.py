from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.info(
        titulo="Gerenciamento de Biblioteca API",
        versao_default='v1',
        descricao="Documentação da API do sistema de Gerenciamento de Biblioteca",
        termos_de_servico="https://www.google.com/policies/terms/",
        contato=openapi.Contact(email="contato@biblioteca.local"),
        licenca=openapi.License(name="Licença BSD")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
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
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # As duas linas abaixo configuram a rota para exibir a documentação quando acessadas pela URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]