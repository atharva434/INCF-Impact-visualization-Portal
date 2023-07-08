from django.shortcuts import render
from .url_retriever import impact
# Create your views here.
from .models import Organization

def home(request):
    return render(request,"home.html")


def organization(request):
    print("ji")
    org_name=request.POST["name"]
    url=request.POST["url"]
    impact_params,project_type=impact(url)
    if project_type=="disease":
        organization=Organization(name=org_name,url=url,impact=impact_params)
        organization.save()
    else:
        organization=Organization(name=org_name,url=url,aim=impact_params["aim"],use=impact_params["use"],impact=impact_params["impact"])
        organization.save()

    return render(request,"home.html",{"name":org_name})

