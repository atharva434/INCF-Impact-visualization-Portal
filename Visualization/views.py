from django.shortcuts import render
from .url_retriever import impact,calculator
from .retrievalqna import chat,ingest
# Create your views here.
from .models import Organization,Project

def home(request):
    organization=Organization.objects.all()
    # urls=list(organization.values_list("impact", flat = True))
    # ingest(urls)
    
    return render(request,"home.html")

def homepage(request):
    organizations=Organization.objects.all()
    # urls=list(organizations.values_list("url", flat = True))
    # ingest(urls)
    return render(request,"newpage.html",{"organization":organizations})

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
    return render(request,"home.html",{"name":org_name})



responses={}

def chatbot(request):
    global responses
    if request.method=="POST":
        query=request.POST["query"]
        organization=Organization.objects.all()
        # urls=list(organization.values_list("url", flat = True))
        answer=chat(query)
        for i in answer["source_documents"]:
            source=i.metadata["source"]
            break
        answer["source"]=source

        responses[query]=answer
        print(responses[query])
       

        return render(request,"chatbot.html",{"responses":responses,"source":source})
    responses={}
    return render(request,"chatbot.html")

def total_impact(request):
    organization=Organization.objects.all()
    urls=list(organization.values_list("impact", flat = True))
    answer=calculator(urls)

def detail(request,id):
    project=Project.objects.filter(organization=id)
    organization=Organization.objects.get(id=id)
    print(organization.impact)
    return render(request,"orgpage.html",{"projects":project,"organization":organization})

def add(request,id):
    if request.method=="POST":
        title=request.POST["name"]
        url=request.POST["url"]
        org=Organization.objects.get(id=id)
        org_name=org.name


    return render(request,"projectform.html",{"id":id})




