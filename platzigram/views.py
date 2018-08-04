from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
	now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
	return HttpResponse("Curent server time is {}".format(now))

def sort_integers(request):
	numbers = (request.GET['numbers']).split(',')
	numbers = list(map(int, numbers))
	numbers_or = sorted(numbers)
	a = json.dumps(numbers_or)
	import pdb; pdb.set_trace()
	# return JsonResponse({'Numeros': a})
	return HttpResponse(map(int, numbers))

def say_hi(request, name, age):
	if age < 12:
		message = "Lo siento {}, eres menor".format(name)
	else:
		message = "Hola {}".format(name)

	return HttpResponse(message)