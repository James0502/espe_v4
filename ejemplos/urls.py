from django.urls import path
from ejemplos import views #importará los métodos que generemos en nuestra app
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProveedorView, ProveedorNew, ProveedorEdit
ejemplos_urlpatterns = [
    path('ejemplos_main/',views.ejemplos_main,name="ejemplos_main"),
    path('proveedor_main/',views.proveedor_main,name="proveedor_main"),
    path('agregar_producto/',views.agregar_producto,name="agregar_producto"),
    path('listar_producto/',views.listar_producto,name="listar_producto"),
    path('actualizar_producto/<id>/',views.actualizar_producto,name="actualizar_producto"),
    path('eliminar_producto/<id>/',views.eliminar_producto,name="eliminar_producto"),

    path('agregar_categoria/',views.agregar_categoria,name="agregar_categoria"),
    path('listar_categoria/',views.listar_categoria,name="listar_categoria"),
    path('modificar_categoria/<id>/',views.modificar_categoria,name="modificar_categoria"),
    path('eliminar_categoria/<id>/',views.eliminar_categoria,name="eliminar_categoria"),

    path('carga_masiva_categoria/',views.carga_masiva_categoria,name="carga_masiva_categoria"),
    path('categoria_carga_masiva_save/',views.categoria_carga_masiva_save,name="categoria_carga_masiva_save"),
    path('import_file_categoria/',views.import_file_categoria,name="import_file_categoria"),


    path('ejemplos_habilidad_add/',views.ejemplos_habilidad_add,name="ejemplos_habilidad_add"),
    path('ejemplos_habilidad_save/',views.ejemplos_habilidad_save,name="ejemplos_habilidad_save"),
    path('ejemplos_habilidad_ver/<habilidad_id>/',views.ejemplos_habilidad_ver,name="ejemplos_habilidad_ver"),
    path('ejemplos_list_habilidades/',views.ejemplos_list_habilidades,name="ejemplos_list_habilidades"),

    path('ejemplos_carga_masiva/',views.ejemplos_carga_masiva,name="ejemplos_carga_masiva"),
    path('ejemplos_carga_masiva_save/',views.ejemplos_carga_masiva_save,name="ejemplos_carga_masiva_save"),
    path('import_file/',views.import_file,name="import_file"),

    #path('agregar_proveedor/',views.agregar_proveedor,name="agregar_proveedor"),
    #path('proveedor_main/',views.proveedor_main,name="proveedor_main"),
    


    #endPoints
    path('ejemplos_habilidad_add_rest/', views.ejemplos_habilidad_add_rest),  
     path('ejemplos_habilidad_list_rest/', views.ejemplos_habilidad_list_rest),  
     path('ejemplos_habilidad_get_element_rest/', views.ejemplos_habilidad_get_element_rest),  
     path('ejemplos_habilidad_update_element_rest/', views.ejemplos_habilidad_update_element_rest), 
     path('ejemplos_habilidad_del_element_rest/', views.ejemplos_habilidad_del_element_rest), 
     path('ejemplos_habilidad_list_date_rest/', views.ejemplos_habilidad_list_date_rest), 
     path('ejemplos_habilidad_list_range_date_rest/', views.ejemplos_habilidad_list_range_date_rest), 
     path('ejemplos_habilidad_list_contains/', views.ejemplos_habilidad_list_contains), 

     path("product_list_rest/",views.product_list_rest),
     path("product_edit_rest/",views.product_edit_rest),

    path('proveedores/',ProveedorView.as_view(), name="proveedor_list"),
    path('proveedores/new',ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>',ProveedorEdit.as_view(), name="proveedor_edit"),

    path('proveedor_form/',views.proveedor_form,name="proveedor_form"),
    path('proveedor_list/',views.proveedor_list,name="proveedor_list")


    
    ]

    