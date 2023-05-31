import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from Web.Laliga.models import Liga



def upload_excel(request):
    
    if request.method == 'POST':
        excel_file = request.FILES['Datos']
        df = pd.read_csv(excel_file)

        # Eliminar todos los objetos Person existentes en la base de datos
        Liga.objects.all().delete()
        
        for index, row in df.iterrows():
            deportes = Liga(
                temporada=row['temporada'],
                fecha=row['fecha'],
                equipo_local=row['nombre_equipo_local'],
                equipo_visitante=row['nombre_equipo_visitante'],
                goles_local=row['goles_local'],
                goles_visitante=row['goles_visitante'],
                ganador=row['ganador']
            )
            
            deportes.save()

        # Obtener los datos guardados en la base de datos
        sports = Liga.objects.all()

        return render(request, 'screen2.html', {'sports': sports})

    return render(request, 'screen.html')
