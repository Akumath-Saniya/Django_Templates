from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def login_view(request):
    return render(request, "login.html")


def tenth(request):
    return render(request, "tenth.html")


# ===== INTER =====

def inter(request):
    return render(request, "inter.html")


def inter_groups(request, year):
    return render(request, "inter_groups.html", {"year": year})


def subjects(request, year, group):

    data = {
        "mpc": ["Mathematics", "Physics", "Chemistry", "English"],
        "bipc": ["Botany", "Zoology", "Chemistry", "English"],
        "cec": ["Civics", "Economics", "Commerce", "English"],
        "mec": ["Mathematics", "Economics", "Commerce", "English"],
    }

    return render(request, "subjects.html", {
        "year": year,
        "group": group.upper(),
        "subjects": data.get(group.lower(), [])
    })


# ===== BTECH =====

def btech1(request):
    return render(request, "btech1.html")


def content(request):
    return render(request, "content.html")
