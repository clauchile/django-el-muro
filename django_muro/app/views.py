from app.models import Comment, Message, User
from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt, time
from .decorators import login_required




def index(request):
    print(request.session)
    # if 'user' in request.session:
    #         messages.warning(request,"Ya estás logeado.")
    return redirect("/login/")
# @login_required
def muro(request):

    if request.method == 'GET':
        # cuenta = Message.objects.filter(id = request.session['user']['id']).annotate(count_messages = Count('id'))
        cuenta = Message.objects.filter(user__id = request.session['user']['id']).count()
        fil = Comment.objects.filter(user__id = request.session['user']['id'])
        # prueba = time(fil['created_at'].minute)
        # prueba =fil['created_at']
        # print('campo fil', fil)
        context = {
            'saludo': 'Hola',
            'mensaje_list': Message.objects.order_by('mensaje'),
            'comentario_list':Comment.objects.order_by('comentario'),
            'id_delete': fil,
            'cuenta': cuenta
            # 'comentario_list': Comment.objects.filter(id= val),
            }
        
        return render(request, 'muro.html', context)

    else:

        if not request.POST['mensaje']:
            messages.warning(request, "Debe escribir algo")

            return redirect( '/muro/' )    
        # print(request.session.usuario.name)
        else:
            print(request.POST)

            # print(nombre_sesion)
            # val = request.POST.get('')
            usuario = User.objects.get(id = request.session['user']['id'])
            # c = request.POST['comment']
            nuevo_Mensaje = Message.objects.create(
                    mensaje = request.POST['mensaje'],
                    user = usuario
            )
            print(nuevo_Mensaje)
            messages.success(request,"Mensaje publicado")
            return redirect( '/muro/' )

def comentario(request,val):

    if request.method == 'GET':
        
        context = {
            'saludo': 'Hola',
            # 'mensaje_list': Message.objects.filter(user__id = request.session['user']['id']),
            # 'comentario_list': Comment.objects.filter(id= val),
            'comentario_list': Comment.objects.all(),
            'mensaje_list': Message.objects.all(),
            'cuenta': Message.objects.filter(user__id = request.session['user']['id']).count()
            }
        
        return render(request, 'muro.html', context)

    else:
        if not request.POST['comentario']:
            messages.warning(request, "Debe escribir algo")
        # print(request.session.usuario.name)

        else:
            print(request.POST)
            # print(request.POST)
            # print(nombre_sesion)
            # val = request.POST.get('')
            usuario = User.objects.get(id = request.session['user']['id'])
            msg = Message.objects.get(id = request.POST['msgnum'])
            # c = request.POST['comment']
            nuevo_Comentario = Comment.objects.create(
                    comentario = request.POST['comentario'],
                    message = msg,
                    user = usuario,
            )
            print(nuevo_Comentario)
            messages.success(request,"comentario publicado")
        return redirect( f'/muro/{val}/' )


            # datos = request.POST[]

def delete(request,num):

    dato = Comment.objects.get(id=num)

    dato.delete()
    messages.success(request, f" el comentario ha sido borrado con exito")
    return redirect(f'/muro')

def mensaje_delete(request,num):

    # hora = Message.objects.all()
    # for h in hora:
    #     tiempo_transcurrido = time.time.now() - h.created_at
    #     if tiempo_transcurrido > timedelta(days=2):
    #         pass

        dato = Message.objects.get(id=num)

        dato.delete()
        messages.success(request,f" el mensaje ha sido borrado con exito")
        return redirect(f'/muro')



