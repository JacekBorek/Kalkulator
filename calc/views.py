from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'calc/index.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'substract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error! Division by zero'
        else:
            result = 'Invalid operation'
        return render(request, 'calc/result.html', {'result': result})
