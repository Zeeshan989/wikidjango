from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import markdown
import os
from .forms import content
import random
from django.urls import reverse




from . import util


def index(request):
    sublist=[]
    if request.method == 'POST':
        ent=util.list_entries()
        search = request.POST.get('q','')  # Assuming you have a form field named 'q'
        if search in ent:
            return redirect('title', title=search)
        for e in ent:
            temp=e
            if search in e:
                sublist.append(temp)

        
        return render(request, "encyclopedia/search.html",{
            "search":sublist
        })
    
    else:
        entries = util.list_entries()
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })

def title(request, title):
    li = util.list_entries()
    if title in li:
        html_content = markdown.markdown(util.get_entry(title))
        context = {
            'markdown_content': html_content,
            'title': title  # Add the 'title' variable to the context
        }
        return render(request, "encyclopedia/title.html", context)
    else:
        return HttpResponse("Not Found")
    
def newpage(request):
        if request.method == 'POST':
            title = request.POST.get('title','') 
            desc= request.POST.get('markdown-content','') 
            if title in util.list_entries():
                return HttpResponse("This Title already exists !")
            else:
                util.save_entry(title,desc)
                return redirect('index')

            
        else:
            return render(request, "encyclopedia/newpage.html")
        

def editpage(request,title):
    tits = util.get_entry(title)
    if request.method =='POST':
        form = content(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data['cont']
            util.save_entry(title, new_content)
            return redirect('index')     
    else:
        initial_data = {'cont':tits}
        form = content(initial=initial_data)
        return render(request, 'encyclopedia/editpage.html', {'form': form})
    
def randpage(request):
    randomtitle=random.choice(util.list_entries())
    url = reverse('title', kwargs={'title':randomtitle})
    return redirect(url)
       

    

   

  
    