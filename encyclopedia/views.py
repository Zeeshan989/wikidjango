from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import markdown
import os

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
                filename = f"{title}.md"
                file_path = os.path.join("entries", filename)   # Replace "path/to/save" with your desired file directory
                with open(file_path, "w") as file:
                    file.write(desc)
                return redirect('index')

            
        else:
            return render(request, "encyclopedia/newpage.html")
   

  
    