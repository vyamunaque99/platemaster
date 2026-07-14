from django.shortcuts import render
from django.db import IntegrityError

from .forms import DataEntryVehiculoForm
from .ocr import extraer_texto_imagen
from .models import DataEntryVehiculo
# Create your views here.
def data_entry_vehiculo_view(request):
    if request.method == "POST":
        form = DataEntryVehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['de_image']
            texto = extraer_texto_imagen(file)
            splitted_text = texto.split("\n")
            splitted_text = [x for x in splitted_text if x != '']
            data_entry_vehiculo=DataEntryVehiculo(
                num_placa=splitted_text[0],
                num_serie=splitted_text[1],
                num_vin=splitted_text[2],
                num_motor=splitted_text[3],
                color=splitted_text[4],
                marca=splitted_text[5],
                modelo=splitted_text[6],
                placa_vigente=splitted_text[7],
                placa_anterior=splitted_text[8],
                estado=splitted_text[9],
                anotaciones=splitted_text[10],
                sede=splitted_text[11],
                anio_modelo=splitted_text[12],
                propietarios=';'.join(splitted_text[13:])
            )
            text=''
            state=''
            try:
                data_entry_vehiculo.save()
                text='Registro guardado exitosamente'
                state='success'
            except IntegrityError:
                # Handle the duplicate key/uniqueness failure here
                text='Este vehiculo ya esta registrado'
                state='error'
            form = DataEntryVehiculoForm()
            context = {"form": form, "text": text, "state": state}
            return render(request, "data-entry-vehiculo.html", context)
    else:
        form = DataEntryVehiculoForm()
        context = {"form": form}
        return render(request, "data-entry-vehiculo.html", context)