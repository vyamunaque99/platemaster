from django.shortcuts import render

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
                num_placa=splitted_text[3],
                num_serie=splitted_text[4],
                num_vin=splitted_text[5],
                num_motor=splitted_text[6],
                color=splitted_text[7],
                marca=splitted_text[8],
                modelo=splitted_text[9],
                placa_vigente=splitted_text[10],
                placa_anterior=splitted_text[11],
                estado=splitted_text[12],
                anotaciones=splitted_text[13],
                sede=splitted_text[14],
                anio_modelo=splitted_text[15],
                propietarios=''.join(splitted_text[16:])
            )
            data_entry_vehiculo.save()
            form = DataEntryVehiculoForm()
            context = {"form": form}
            return render(request, "data-entry-vehiculo.html", context)
    else:
        form = DataEntryVehiculoForm()
        context = {"form": form}
        return render(request, "data-entry-vehiculo.html", context)