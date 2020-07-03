from django.shortcuts import render
from .models import Details
from coordinator.models import Companies


def companyForm(request):
    
    companyName = request.POST.get('companyName', "")
    companyWebsite = request.POST.get('companyWebsite', "")
    companyHR = request.POST.get('companyHR', "")
    companyAddress = request.POST.get('companyAddress', "")
    companyEmail = request.POST.get('companyEmail', "")
    companyPhone = str(request.POST.get('companyPhone', ""))
    companyMobile = str(request.POST.get('companyMobile', ""))
    sector = ','.join(request.POST.getlist('sector'))+":"+str(request.POST.get('sector-text-input')) if "other" in request.POST.getlist('sector') else ','.join(request.POST.getlist('sector'))
    category = ','.join(request.POST.getlist('category'))+":"+str(request.POST.get('category-text-input')) if "other" in request.POST.getlist('category') else ','.join(request.POST.getlist('category'))
    typeOfOffer = ','.join(request.POST.getlist('typeOfOffer'))
    job_designation = request.POST.get('job_designation', "")
    work_location = request.POST.get('work_location', "")
    relevant_info = request.POST.get('relevant_info', "")
    joining_date = request.POST.get('joining_date', "")
    cgpa = str(request.POST.get('cgpa', ""))
    percent = str(request.POST.get('percent', ""))
    ssc = str(request.POST.get('ssc', ""))
    fittness = request.POST.get('fittness', "")
    age = str(request.POST.get('age', ""))
    oths = str(request.POST.get('oths', ""))
    selectionProcess = ','.join(request.POST.getlist('selectionProcess'))+":"+str(request.POST.get('selectionProcess-text-input')) if "other" in request.POST.getlist('selectionProcess') else ','.join(request.POST.getlist('selectionProcess'))
    noRounds = str(request.POST.get('noRounds', ""))

    branchesAllowed = ','.join(request.POST.getlist('branchAllowed'))

    btechSalary = "basic: "+str(request.POST.get('btech-basic', ""))+" hra: "+str(request.POST.get('btech-hra', ""))+" gross: "+str(request.POST.get('btech-gross', ""))+" others: "+str(request.POST.get('btech-others', ""))+" ctc: "+str(request.POST.get('btech-ctc', ""))
    mtechSalary = str(request.POST.get('mtech-basic', ""))+" "+str(request.POST.get('mtech-hra', ""))+" "+str(request.POST.get('mtech-gross', ""))+" "+str(request.POST.get('mtech-others', ""))+" "+str(request.POST.get('mtech-ctc', ""))
    otherPGSalary = str(request.POST.get('other-pg-basic', ""))+" "+str(request.POST.get('other-pg-hra', ""))+" "+str(request.POST.get('other-pg-gross', ""))+" "+str(request.POST.get('other-pg-others', ""))+" "+str(request.POST.get('other-pg-ctc', ""))
    phDSalary = str(request.POST.get('phd-basic', ""))+" "+str(request.POST.get('phd-hra', ""))+" "+str(request.POST.get('phd-gross', ""))+" "+str(request.POST.get('phd-others', ""))+" "+str(request.POST.get('phd-ctc', ""))
    serviceAgreement = ','.join(request.POST.getlist('service-agreement'))+":"+str(request.POST.get('service-agreement-text-input'))if "yes" in request.POST.getlist('service-agreement') else ','.join(request.POST.getlist('service-agreement'))
    trainingPeriod = ','.join(request.POST.getlist('training-period'))+":"+str(request.POST.get('training-period-text-input'))if "yes" in request.POST.getlist('training-period') else ','.join(request.POST.getlist('training-period'))
    stipendBtech = str(request.POST.get('stipend-btech-monthly', ""))+" "+str(request.POST.get('stipend-btech-others', ""))+" "+str(request.POST.get('stipend-btech-total', ""))
    stipendMtech = str(request.POST.get('stipend-mtech-monthly', ""))+" "+str(request.POST.get('stipend-mtech-others', ""))+" "+str(request.POST.get('stipend-mtech-total', ""))
    stipendPG = str(request.POST.get('stipend-otherpg-monthly', ""))+" "+str(request.POST.get('stipend-otherpg-others', ""))+" "+str(request.POST.get('stipend-otherpg-total', ""))
    durationUG = str(request.POST.get('stipend-ugproject-duration', ""))
    durationPG = str(request.POST.get('stipend-pgproject-duration', ""))
    minOffers = str(request.POST.get('min-offers', ""))

    saveDetails = Details(
        name = companyName,
        websiteLink = companyWebsite,
        hrDetails = companyHR,
        address = companyAddress,
        emailId = companyEmail,
        phoneNumber = companyPhone,
        mobileNumber = companyMobile,
        sector = sector,
        category = category,
        jobDesignation = job_designation,
        jobType = typeOfOffer,
        workLocation = work_location,
        otherInfo = relevant_info,
        tentativeDOJ = joining_date,
        roundsDetails = selectionProcess,
        numberOfRounds = noRounds,
        salaryDetails_btech = btechSalary,
        salaryDetails_mtech = mtechSalary,
        salaryDetails_otherPG = otherPGSalary,
        salaryDetails_PhD = phDSalary,

        trainingPeriod = trainingPeriod,
        stipulatedBond = serviceAgreement,

        stipendDetails_BTech = stipendBtech,
        stipendDetails_MTech = stipendMtech,
        stipendDetails_OtherPG = stipendPG,
        minOffers = minOffers,

        duration_UG = durationUG,
        duration_PG = durationPG
    )
    # print(saveDetails)
    saveDetails.save()

    saveCompanyStatus = Companies(
        companyID = saveDetails,
        CGPA = cgpa,
        branchesAllowed = branchesAllowed,
        status = 'Accepted',
        name = companyName
    )

    saveCompanyStatus.save()
    return render(request, 'company/cpnf.html', {})