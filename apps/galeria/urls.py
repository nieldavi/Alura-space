from apps.galeria.views import (buscar, deletar_imagem, editar_imagem, imagem,
                                index, nova_imagem)
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
]