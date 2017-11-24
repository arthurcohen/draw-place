from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from binascii import a2b_base64
from place.models import canvas as p5canvas


# Create your views here.
def home(request):
    return render(request, 'place/index.html')


def canvas(request):
    name = request.META['PATH_INFO'].rsplit('/', 1)[-1]
    # print(p5canvas)
    c = None
    try:
        c = p5canvas.objects.get(name=str(name))
        return render(request, 'place/canvas.html', {'name': c.name, 'dataurl': c.urlimage})
    except:
        c = p5canvas.objects.create(name=str(name))

    return render(request, 'place/canvas.html', {'name': name})


def saveCanvas(request):
    try:
        name = request.POST['name']

        print(name)
        c = p5canvas.objects.get(name=str(name))

        c.urlimage = request.POST['image']

        binary_data = a2b_base64(request.POST['image'])
        fd = open('place/static/place/images/'+name+'.png', 'wb')
        fd.write(binary_data)
        fd.close()
        c.file = 'place/static/place/images/'+name+'.png'
        c.save()
    except Exception as e:
        print(e)
    # return HttpResponse("Do something")
    return render(request, 'place/index.html')


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
