from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import FiltersForm, QuickApplyForm
from django.db.models import Q
from applications.models import Application

# Create your views here.
def jobsList(request):
    query = request.GET.get("q", "").strip()
    jobs = Job.objects.all()
    if query: 
        jobs=jobs.filter(description__contains=query)


    template = "jobs/jobsList.html"

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        template = "jobs/jobsResults.html"

    form = FiltersForm(request.GET or None)
    form2 = QuickApplyForm(request.POST or None)

    if form.is_valid():
        titleSearch = form.cleaned_data["title"]
        print("hello2")
        locationSearch = form.cleaned_data["location"]
        skillsSearch = form.cleaned_data["skills"]
        onSite = form.cleaned_data["onSite"]
        remote = form.cleaned_data["remote"]
        minimumSalary = form.cleaned_data["minSalary"]
        maximumSalary = form.cleaned_data["maxSalary"]
        visaSponsorship = form.cleaned_data["visaSponsorship"]
        if titleSearch:
            terms = [term.strip() for term in titleSearch.split(",") if term.strip()]

            query = Q()

            for term in terms:
                query |= Q(title__contains=term)

            jobs = jobs.filter(query)
        if locationSearch:
            terms = [term.strip() for term in locationSearch.split(",") if term.strip()]

            query = Q()

            for term in terms:
                query |= Q(location__contains=term)

            jobs = jobs.filter(query)
        if skillsSearch:
            terms = [term.strip() for term in skillsSearch.split(",") if term.strip()]
            matchingJobs = []
            for job in jobs:
                json_values = job.skills or []
                if any(
                    term in str(value).lower()
                    for value in json_values
                    for term in terms
                ):
                    matchingJobs.append(job)
            jobs = matchingJobs
        if onSite == False:
            jobs = jobs.filter(onSite=False)
        if remote == False:
            jobs = jobs.filter(onSite=True)
        if minimumSalary:
            jobs = jobs.filter(maxSalary__gte=minimumSalary)
        if maximumSalary:
            jobs = jobs.filter(minSalary__lte=maximumSalary )
        if visaSponsorship:
            jobs = jobs.filter(visaSponsorship=True)
    else:
        print(form.errors)

    if form2.is_valid():
        note = form2.cleaned_data["note"]
        jobId = request.POST.get("job_id")
        job = get_object_or_404(Job, id=jobId)
        #applicant, job, note, status
        Application.objects.create(
            applicant=request.user.applicantProfile,
            job=job,
            note=note
        )

    return render(request, template, {'jobs': jobs, 'form': form, 'form2': form2})


    #if request.headers.get("x-requested-with") == "XMLHttpRequest":
    #    return render(
    #        request,
    #        "jobs/jobsList.html",
    #        {"jobs": jobs}
    #    )

    #return render(
    #    request,
    #    "jobs/jobsList.html",
    #    {
    #        "jobs": jobs,
    #        "query": query,
    #    }
    #)
