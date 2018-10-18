from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
	now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
	return HttpResponse("Curent server time is {}".format(now))

def sort_integers(request):
	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Integer sorted successfully'
	}
	return HttpResponse(
		json.dumps(data, indent=4), 
		content_type='application/json'
	)


def say_hi(request, name, age):
	if age < 12:
		message = "Lo siento {}, eres menor".format(name)
	else:
		message = "Hola {}".format(name)

	return HttpResponse(message)