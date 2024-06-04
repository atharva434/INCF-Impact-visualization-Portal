from django.shortcuts import render,redirect
from .url_retriever import impact,calculator,clean_with_llm
from .retrievalqna import chat,ingest,ingest_documents,fill_db
# Create your views here.
from django.contrib import messages
from django import template
from .models import Organization,Project
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


register = template.Library()
@register.filter
def modulo(num, val):
    return num % val == 0

def adminpage(request):
    organization=Organization.objects.all()
    # urls=list(organization.values_list("impact", flat = True))
    # ingest(urls)
    return render(request,"adminpage.html")

def homepage(request):
    organizations=Organization.objects.all()
    # urls=list(organizations.values_list("url", flat = True))
    # ingest(urls)
    urls=list(organizations.values_list("impact", flat = True))
    impact=calculator(urls)
    print(type(impact))
    return render(request,"homepage.html",{"organization":organizations,"impact":impact})

def organization(request):
    print("ji")
    org_name=request.POST["name"]
    url=request.POST["url"]
    impact_params,project_type=impact(url)
    if project_type=="disease":
        organization=Organization(name=org_name,url=url,impact=impact_params["impact"],impact_json=impact_params)
        organization.save()
    else:
        organization=Organization(name=org_name,url=url,aim=impact_params["aim"],use=impact_params["use"],impact=impact_params["impact"])
        organization.save()
    ingest(url)
    return render(request,"adminpage.html",{"name":org_name})



responses={}

@csrf_exempt  # This decorator is to bypass CSRF token for demonstration. It's better to handle CSRF in AJAX calls properly.
def chatbot(request):
    global responses
    if request.method == "POST":
        query = request.POST.get("query")
        organization = Organization.objects.all()
        # Assume chat() function and everything else works as intended
        answer = chat(query)
        for i in answer["source_documents"]:
            source = i.metadata["source"]
            break
        answer["source"] = source
        responses[query] = answer

        # If AJAX request, return JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"query": query, "answer": answer['answer'], "source": source})
        
        return render(request, "chatbot.html", {"responses": responses, "source": source})
    
    responses = {}
    return render(request, "chatbot.html")

def total_impact(request):
    organization=Organization.objects.all()
    urls=list(organization.values_list("impact", flat = True))
    answer=calculator(urls)

def detail(request,id):
    project=Project.objects.filter(organization=id)
    organization=Organization.objects.get(id=id)
    organization.name=organization.name.upper()
    print(organization.impact)
    impact=clean_with_llm(organization.impact,organization.name)
    return render(request,"orgpage.html",{"projects":project,"organization":organization,"impact":impact})

def add(request,id):
    if request.method=="POST":
        title=request.POST["name"]
        # url=request.POST["url"]
        org=Organization.objects.get(id=id)
        org_name=org.name
        d=fill_db(title)
        my_instance = Project(**d)
        my_instance.title=title
        my_instance.organization=org
        my_instance.save()
        return redirect("homepage")
    return render(request,"projectform.html",{"id":id})


def get_qa_model(request):
    global qa_model
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testpdf='.'+filePathName
    # loader = PyPDFLoader(testpdf)
    # pages = loader.load_and_split()
    ingest_documents(testpdf)
    messages.success(request, 'File uploaded successfully.')
    print("Success")
    return redirect("homepage")

def upload(request):
    return render(request,"upload_pdf.html")