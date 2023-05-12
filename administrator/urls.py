
from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from administrator import views

administrator_patterns = [
    path('admin_main', views.admin_main,name="admin_main"),
    #flujo usuarios
    path('users_main', views.users_main,name="users_main"),
    path('new_user/',views.new_user, name='new_user'),
    path('new_proveedor/',views.new_proveedor, name='new_proveedor' ),
    path('user_block/<user_id>/',views.user_block, name='user_block'),
    path('user_activate/<user_id>',views.user_activate, name='user_activate'),
    path('user_delete/<user_id>',views.user_delete, name='user_delete'),
    path('edit_user/<user_id>/',views.edit_user, name='edit_user'),
    path('list_main/<group_id>/',views.list_main, name='list_main'),     
    path('list_user_active/<group_id>/',views.list_user_active, name='list_user_active'),     
    path('list_user_active/<group_id>/<page>/',views.list_user_active, name='list_user_active'),     
    path('list_user_block/<group_id>/',views.list_user_block, name='list_user_block'),     
    path('list_user_block/<group_id>/<page>/',views.list_user_block, name='list_user_block'), 

    #flujo proveedores
    
    path('pro_block/<user_id>/',views.pro_block, name='pro_block'),
    path('pro_activate/<user_id>',views.pro_activate, name='pro_activate'),
    path('pro_delete/<user_id>',views.pro_delete, name='pro_delete'),
    path('edit_user_pro/<user_id>/',views.edit_user_pro, name='edit_user_pro'),
    path('list_prov/<group_id>/',views.list_prov, name='list_prov'),     
    path('list_prov_acti/<group_id>/',views.list_prov_active, name='list_prov_acti'),     
    path('list_prov_acti/<group_id>/<page>/',views.list_prov_active, name='list_prov_acti'),     
    path('list_pro_block/<group_id>/',views.list_pro_block, name='list_pro_block'),     
    path('list_pro_block/<group_id>/<page>/',views.list_pro_block, name='list_pro_block'), 

 
   
  
  
    path('masiva_usuarios/',views.masiva_usuarios,name="masiva_usuarios"),
    path('carga_masiva_save_user/',views.carga_masiva_save_user,name="carga_masiva_save_user"),
    path('import_file_user/',views.import_file_user,name="import_file_user"), 

    path('masiva_proveedores/',views.masiva_proveedores,name="masiva_proveedores"),
    path('carga_masiva_save_prov/',views.carga_masiva_save_prov,name="carga_masiva_save_prov"),
    path('import_file_prov/',views.import_file_user,name="import_file_prov"), 

    #BORRAR
    path('ejemplo_query_set/',views.ejemplo_query_set, name='ejemplo_query_set'),  
    ]  
