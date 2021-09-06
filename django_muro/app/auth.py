from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .models import User

    

def login(request):
    
    if request.method == "POST":
        print(request.POST)
        us = User.objects.filter(email=request.POST['email'])
        if us:
            log_user = us[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):

                us = {
                    "id" : log_user.id,
                    "name": f"{log_user}",
                    "email": log_user.email,
                    "role": log_user.role
                }
                # variable de sesion
                request.session['user'] = us
                messages.success(request, "Logueado correctamente.")
                print('variable de sesion', us)
                print(us["name"])
                print(request.POST['email'])
                return redirect("/muro/")
            else:
                messages.error(request, "Password o Email  incorrectos.")
        else:
            messages.error(request, "Email o password incorrectos.")

        return redirect("/login")
    else:
        if 'user' in request.session:
            messages.warning(request,"Ya estás registrado o logeado.")
    
            return redirect('/muro/')
        else:

            # new = User.objects.last()
            #  request.session['user'] = {
            #     "id" : new.id,
            #     "name": f"{usuario_nuevo.name}",
            #     "email": usuario_nuevo.email
            # # }
            return render(request, 'login.html')


def registro(request):
    if request.method == "POST":

        errors = User.objects.validador_basico(request.POST)
        # print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                # print("DESDE EL FOR: ",key, value)
            
            request.session['register_name'] =  request.POST['name']
            request.session['register_email'] =  request.POST['email']

        else:
            request.session['register_name'] = ""
            request.session['register_email'] = ""

            password_encryp = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 

            usuario_nuevo = User.objects.create(
                name = request.POST['name'],
                email=request.POST['email'],
                password=password_encryp,
                role=request.POST['role']
            )

            messages.success(request, "El usuario fue agregado con exito.")
            

            request.session['user'] = {
                "id" : usuario_nuevo.id,
                "name": f"{usuario_nuevo.name}",
                "email": usuario_nuevo.email
            }
            return redirect("/muro/")

        return redirect("/registro")
    else:
        if 'user' in request.session:
            messages.warning(request,"Ya estás registrado o logeado.")
            return redirect('/muro/')

        else:   
            context ={} 
            return render(request, 'registro.html',context)


def logout(request):
    if 'user' in request.session:
        del request.session['user']
        # del request.session['usuario']
    
    return redirect("/login")