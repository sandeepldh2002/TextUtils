# I have create this views file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello World</h1> <br> <a href="https://melodic-bhardwaj-2002.netlify.app/">Restautrent website </a>''')

# def about(request):
#     return HttpResponse("hello about page")

def index(request):
    docs = {'name' : 'sandeep', 'place' : 'Mars'}
    return render(request, 'index.html', docs)
    # return HttpResponse("hello World")

def analyze(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    #get the text from index.html se
    djtext = request.GET.get('text', 'default')
    djremovepunc = request.GET.get('removepunc', 'off')
    print(djremovepunc)
    print(djtext) #analyse the text
    # analyzed=djtext
    if djremovepunc == "on":
        punctuation = '''!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char 
        params={'purpose' : 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyzer.html', params)
    else:
        return HttpResponse("<h1>ERROR: Please Tick the Checkbox</h1>")

# def capfirst(request):
#     return HttpResponse("cap first")

# def newline(request):
#     return HttpResponse("newline <a href='/'>Go to Homepage</a>")

# def spaceremove(request):
#     return HttpResponse("space remove")

# def lineremove(request):
#     return HttpResponse("lineremove")