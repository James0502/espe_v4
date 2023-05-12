import json
import pandas as pd
import xlwt
#nuevas importaciones 30-05-2022
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from registration.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

#fin nuevas importaciones 30-05-2022

from django.db.models import Count, Avg, Q
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ejemplos.models import Habilidad, Heroe, Product, Producto, Categoria, proveedor
from .forms import ProductoForm, CategoriaForm, ProveedorForm
#PRODUCTOS
@login_required
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Producto creado!')
    return render(request, 'ejemplos/agregar.html',data)

    # profile = Profile.objects.get(user_id=request.user.id)
    # if profile.group_id != 1:
    #     messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
    #     return redirect('check_group_main')
    # template_name = 'ejemplos/agregar.html'
    # return render(request,template_name,{'profile':profile})
@login_required
def listar_producto(request):
     productos = Producto.objects.all()
     data={
         'productos': productos
     }
     return render(request, 'ejemplos/listar.html',data)
@login_required
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data ={
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
    messages.add_message(request, messages.INFO, 'Producto actualizado!')
    return render(request, 'ejemplos/modificar.html',data)
@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.add_message(request, messages.INFO, 'Producto eliminado!')
    return redirect(to="listar_producto")

#CATEGORIAS
@login_required
def agregar_categoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Categoria creada!')
    return render(request, 'ejemplos/agregar_categoria.html',data)
    # profile = Profile.objects.get(user_id=request.user.id)
    # if profile.group_id != 1:
    #     messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
    #     return redirect('check_group_main')
    # template_name = 'ejemplos/agregar.html'
    # return render(request,template_name,{'profile':profile})
@login_required
def listar_categoria(request):
     categorias = Categoria.objects.all()
     data={
         'categoria': categorias
     }
     return render(request, 'ejemplos/listar_categoria.html',data)
@login_required
def modificar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    data ={
        'form': CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_categoria")
    messages.add_message(request, messages.INFO, 'Categoria modificada!')
    return render(request, 'ejemplos/modificar_categoria.html',data)
@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.add_message(request, messages.INFO, 'Categoria eliminada!')
    return redirect(to="listar_categoria")





@login_required
def ejemplos_main(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/ejemplos_main.html'
    return render(request,template_name,{'profile':profile})


@login_required
def proveedor_main(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/proveedor_main.html'
    return render(request,template_name,{'profile':profile})

@login_required
def ejemplos_habilidad_add(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/ejemplos_add.html'
    return render(request,template_name,{'profile':profile})

@login_required
def ejemplos_habilidad_save(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nivel = request.POST.get('nivel')        
        if nombre == '' or nivel == '':
            messages.add_message(request, messages.INFO, 'Debes ingresar toda la información')
            return redirect('ejemplos_habilidad_add')
        habilidad_save = Habilidad(
            nombre = nombre,
            nivel = nivel,
            )
        habilidad_save.save()
        messages.add_message(request, messages.INFO, 'Habilidad ingresada con éxito')
        return redirect('ejemplos_list_habilidades')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')
@login_required
def ejemplos_habilidad_ver(request,habilidad_id):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    habildad_data = Habilidad.objects.get(pk=habilidad_id)
    template_name = 'ejemplos/ejemplos_habilidad_ver.html'
    return render(request,template_name,{'profile':profile,'habildad_data':habildad_data})

@login_required
def ejemplos_list_habilidades(request,page=None,search=None):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if page == None:
        page = request.GET.get('page')
    else:
        page = page
    if request.GET.get('page') == None:
        page = page
    else:
        page = request.GET.get('page') 
    if search == None:
        search = request.GET.get('search')
    else:
        search = search
    if request.GET.get('search') == None:
        search = search
    else:
        search = request.GET.get('search') 
    if request.method == 'POST':
        search = request.POST.get('search') 
        page = None
    h_list = []
    if search == None or search == "None":
        h_count = Habilidad.objects.filter(estado='Activo').count()
        h_list_array = Habilidad.objects.filter(estado='Activo').order_by('nivel')
        for h in h_list_array:
            h_list.append({'id':h.id,'nombre':h.nombre,'nivel':h.nivel})
    else:
        h_count = Habilidad.objects.filter(estado='Activo').filter(nombre__icontains=search).count()
        h_list_array = Habilidad.objects.filter(estado='Activo').filter(nombre__icontains=search).order_by('nombre')
        for h in h_list_array:
            h_list.append({'id':h.id,'nombre':h.nombre,'nivel':h.nivel})            
    paginator = Paginator(h_list, 1) 
    h_list_paginate= paginator.get_page(page)   
    template_name = 'ejemplos/ejemplos_list_habilidades.html'
    return render(request,template_name,{'template_name':template_name,'h_list_paginate':h_list_paginate,'paginator':paginator,'page':page})
#########################
#CARGA MASIVA PRODUCTO
@login_required
def ejemplos_carga_masiva(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/ejemplos_carga_masiva.html'
    return render(request,template_name,{'profiles':profiles})

@login_required
def import_file(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="archivo_importacion.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('carga_masiva')
    row_num = 0
    columns = ['Nombre Producto','Precio','Descripcion','Talla','Categoria']
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/MM/yyyy'
    for row in range(1):
        row_num += 1
        for col_num in range(5):
            if col_num == 0:
                ws.write(row_num, col_num, 'ej: producto' , font_style)
            if col_num == 1:                           
                ws.write(row_num, col_num, '10000' , font_style)
            if col_num == 2:                           
                ws.write(row_num, col_num, 'Polera de diseñador...' , font_style)
            if col_num == 3:                           
                ws.write(row_num, col_num, 'xs,s,m,l,xl' , font_style)
            if col_num == 4:                           
                ws.write(row_num, col_num, '1,2,3...' , font_style)
    wb.save(response)
    return response  

@login_required
def ejemplos_carga_masiva_save(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')

    if request.method == 'POST':
        #try:
        print(request.FILES['myfile'])
        data = pd.read_excel(request.FILES['myfile'])
        df = pd.DataFrame(data)
        acc = 0
        for item in df.itertuples():
            #capturamos los datos desde excel
            nombre = str(item[1])            
            precio = int(item[2])
            descripcion = str(item[3])            
            talla = str(item[4])
            categoria_id = str(item[5])
            producto_save = Producto(
                nombre = nombre,            
                precio = precio,
                descripcion = descripcion,            
                talla = talla,
                categoria_id = categoria_id,         
                
                )
            producto_save.save()
        messages.add_message(request, messages.INFO, 'Carga masiva finalizada, se importaron '+str(acc)+' registros')
        return redirect('ejemplos_carga_masiva')    
#####################################
#########################
#CARGA MASIVA CATEGORIA
@login_required
def carga_masiva_categoria(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/carga_masiva_categoria.html'
    return render(request,template_name,{'profiles':profiles})

@login_required
def import_file_categoria(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="archivo_importacion.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('carga_masiva')
    row_num = 0
    columns = ['Nombre Categoria']
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/MM/yyyy'
    for row in range(1):
        row_num += 1
        for col_num in range(1):
            if col_num == 0:
                ws.write(row_num, col_num, 'ej: categoria' , font_style)
    wb.save(response)
    return response  

@login_required
def categoria_carga_masiva_save(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')

    if request.method == 'POST':
        #try:
        print(request.FILES['myfile'])
        data = pd.read_excel(request.FILES['myfile'])
        df = pd.DataFrame(data)
        acc = 0
        for item in df.itertuples():
            #capturamos los datos desde excel
            nombre = str(item[1])            
            categoria_save = Categoria(
                nombre = nombre,                   
                )
            categoria_save.save()
        messages.add_message(request, messages.INFO, 'Carga masiva finalizada, se importaron '+str(acc)+' registros')
        return redirect('carga_masiva_categoria')    
#####################################
#ENDPOINT
#Listar Proveedores Activos
@api_view(['GET'])
def product_list_rest(request, format=None):
    if request.method == 'GET':
        product_list = Product.objects.all().order_by('product_name')
        product_json = []
        for h in product_list:
            product_json.append({
                'product_id':h.id,
                'product_name':h.product_name,
                'product_price': h.product_price,
                'product_image': h.product_image,
                'product_state': h.product_state,
                })
        return Response({'Listado':product_json})
    else:
        return Response({'Msj':"Error método no soportado"})

@api_view(['POST'])
def product_edit_rest(request, format=None):
    if request.method == 'POST':
        product_id = request.data['product_id']
        product_name = request.data['product_name']
        product_price = request.data['product_price']
        product_image = request.data['product_image']
        product_state = request.data['product_state']

        Product.objects.filter(pk=product_id).update(product_name=product_name)
        Product.objects.filter(pk=product_id).update(product_price=product_price)
        Product.objects.filter(pk=product_id).update(product_image=product_image)
        Product.objects.filter(pk=product_id).update(product_state=product_state)

        return Response({'MSJ':'editado'})
    else:
        return Response({'Msj':"Error método no soportado"})

@api_view(['POST'])
def ejemplos_habilidad_add_rest(request, format=None):    
    if request.method == 'POST':
        nombre = request.data['nombre'] 
        nivel = request.data['nivel'] 
        if nombre == '' or nivel == '':
            return Response({'Msj': "Error los datos no pueder estar en blanco"})                         
        habilidad_save = Habilidad(
            nombre = nombre,
            nivel = nivel,
            )
        habilidad_save.save()
        return Response({'Msj': "Habilidad creada"})
    else:
        return Response({'Msj': "Error método no soportado"})

@api_view(['GET'])
def ejemplos_habilidad_list_rest(request, format=None):    
    if request.method == 'GET':
        habilidad_list =  Habilidad.objects.all().order_by('nombre')
        habilidad_json = []
        for h in habilidad_list:
            habilidad_json.append({'habilidad':h.nombre,'nivel':h.nivel,'estado':h.estado})
        return Response({'Listado': habilidad_json})
    else:
        return Response({'Msj': "Error método no soportado"})

@api_view(['POST'])
def ejemplos_habilidad_get_element_rest(request, format=None):    
    if request.method == 'POST':
        habilidad_json = []
        habilidad_id = request.data['habilidad_id']
        habilidad_array =  Habilidad.objects.get(pk=habilidad_id)
        habilidad_json.append(
            {'id':habilidad_array.id,
             'nombre':habilidad_array.nombre,
             'nivel':habilidad_array.nivel,
             'estado':habilidad_array.estado})
        return Response({habilidad_array.nombre:habilidad_json})
    else:
        return Response({'Msj': "Error método no soportado"})

@api_view(['POST'])
def ejemplos_habilidad_update_element_rest(request, format=None):    
    if request.method == 'POST':
        habilidad_id = request.data['habilidad_id']
        nombre = request.data['nombre']
        nivel = request.data['nivel']
        estado = request.data['estado']
        Habilidad.objects.filter(pk=habilidad_id).update(nombre=nombre)
        Habilidad.objects.filter(pk=habilidad_id).update(nivel=nivel)
        Habilidad.objects.filter(pk=habilidad_id).update(estado=estado)
        return Response({'Msj':'Habilidad editada con éxito'})
    else:
        return Response({'Msj': 'Error método no soportado'})

@api_view(['POST'])
def ejemplos_habilidad_del_element_rest(request, format=None):    
    if request.method == 'POST':
        habilidad_id = request.data['habilidad_id']
        Habilidad.objects.filter(pk=habilidad_id).delete()
        return Response({'Msj':'Habilidad eliminada con éxito'})
    else:
        return Response({'Msj': 'Error método no soportado'})

@api_view(['POST'])
def ejemplos_habilidad_list_date_rest(request, format=None):    
    if request.method == 'POST':
        created = request.data['created']
        habilidad_list_count = Habilidad.objects.filter(created=created).count()
        if habilidad_list_count > 0:
            habilidad_list =  Habilidad.objects.filter(created=created).order_by('nombre')
            habilidad_json = []
            for h in habilidad_list:
                habilidad_json.append({'habilidad':h.nombre,'nivel':h.nivel,'estado':h.estado})
            return Response({'Listado': habilidad_json})
        else:
            return Response({'Msj': 'No existen habilidades creadas el '+str(created)})
    else:
        return Response({'Msj': 'Error método no soportado'})

@api_view(['POST'])
def ejemplos_habilidad_list_range_date_rest(request, format=None):    
    if request.method == 'POST':
        initial = request.data['initial']
        final = request.data['final']
        habilidad_list_count = Habilidad.objects.filter(created__range=(initial,final)).count()
        if habilidad_list_count > 0:
            habilidad_list =  Habilidad.objects.filter(created__range=(initial,final)).order_by('nombre')
            habilidad_json = []
            for h in habilidad_list:
                habilidad_json.append({'habilidad':h.nombre,'nivel':h.nivel,'estado':h.estado})
            return Response({'Listado': habilidad_json})
        else:
            return Response({'Msj': 'No existen habilidades creadas entre el '+str(initial)+' al '+str(final)})
    else:
        return Response({'Msj': 'Error método no soportado'})


@api_view(['POST'])
def ejemplos_habilidad_list_contains(request, format=None):    
    if request.method == 'POST':
        search = request.data['search']
        habilidad_list_count = Habilidad.objects.filter(Q(nombre__icontains=search)|Q(estado__icontains=search)).count()
        if habilidad_list_count > 0:
            habilidad_list =  Habilidad.objects.filter(Q(nombre__icontains=search)|Q(estado__icontains=search)).order_by('nombre')
            habilidad_json = []
            for h in habilidad_list:
                habilidad_json.append({'habilidad':h.nombre,'nivel':h.nivel,'estado':h.estado})
            return Response({'Listado': habilidad_json})
        else:
            return Response({'Msj': 'No existen habilidades que concuerden en estado o nombre con la cadena '+str(search)})    
    else:
        return Response({'Msj': 'Error método no soportado'})
    
#Proveedoreees!!
class ProveedorView(LoginRequiredMixin,generic.ListView):
    model = proveedor
    template_name=" ejemplos/proeveedor_list.html"
    context_object_name= 'obj'

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = proveedor
    template_name= 'ejemplos/proveedor_form.html'
    context_object_name='obj'

    def form_valid(self, form):
        form.instance.uc= self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin,generic.UpdateView):
    model= proveedor
    template_name='ejemplos/proveedor_form.html'
    context_object_name='obj'
    form_class=ProveedorForm
    success_url=reverse_lazy("ejemplos:proveedor_list")
    
@login_required
def proveedor_main(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/proveedor_main.html'
    return render(request,template_name,{'profile':profile})

@login_required
def proveedor_form(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/proveedor_form.html'
    return render(request,template_name,{'profile':profile})

@login_required
def proveedor_list(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ejemplos/proveedor_list.html'
    return render(request,template_name,{'profile':profile})


