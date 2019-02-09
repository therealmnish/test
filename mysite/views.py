from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on' and fullcaps == 'on' and extraspaceremover == 'on' and newlineremover=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for index, char in enumerate(djtext):
            if char not in punctuations and not (djtext[index] == " " and djtext[index + 1] == " ") and char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and fullcaps == 'on' and extraspaceremover == 'on' :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for index, char in enumerate(djtext):
            if char not in punctuations and not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char.upper()

        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif removepunc == 'on' and newlineremover=='on' and fullcaps=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations and char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
    elif removepunc == 'on' and fullcaps == 'on' and newlineremover=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations and char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on' and extraspaceremover == 'on' and newlineremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " ") and char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and extraspaceremover == 'on' and newlineremover=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for index, char in enumerate(djtext):
            if char not in punctuations and not (djtext[index] == " " and djtext[index + 1] == " ") and char!='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on' and newlineremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and newlineremover=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations and char!='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == 'on' and newlineremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " ") and char!='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on' and extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " ") :
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and fullcaps == 'on' and newlineremover=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for index, char in enumerate(djtext):
            if char not in punctuations and  char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and fullcaps == 'on' and extraspaceremover == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for index, char in enumerate(djtext):
            if char not in punctuations and not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations , Changed to Uppercase & Remove Extraspace ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc =='on' and fullcaps =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations & Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")



