from django import forms
from .models import Producto, Categoria, proveedor



class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta: 
        model = Categoria
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta: 
        model = proveedor
        exclude= ['um', 'fm','uc','fc']
        widget={'descripcion':forms.TextInput()}
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })