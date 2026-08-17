from django.shortcuts import render
from .models import Patient
from ai.predict import predict_brain_tumor
from django.shortcuts import redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import date
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test


def doctor_required(user):

    return user.is_superuser


def home(request):

    return render(request, "index.html")


def brain_analysis(request):

    if request.method == "POST":

        uploaded_image = request.FILES.get("image")

        print("Uploaded image:", uploaded_image)

        if not uploaded_image:

            return render(
                request,
                "brain.html",
                {
                    "error": "Please select an MRI image."
                }
            )

        patient = Patient.objects.create(
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            contact=request.POST.get("contact"),
            email=request.POST.get("email"),
            username=request.POST.get("username"),
            mri_image=uploaded_image,
        )

        prediction, confidence = predict_brain_tumor(
            patient.mri_image.path
        )

        labels = {
            "glioma": "Glioma Tumor",
            "meningioma": "Meningioma Tumor",
            "pituitary": "Pituitary Tumor",
            "notumor": "No Tumor Detected"
        }

        prediction = labels[prediction]

        patient.prediction = prediction

        patient.save()

        return render(
            request,
            "result.html",
            {
                "patient": patient,
                "confidence": confidence
            }
        )

    return render(request, "brain.html")


@user_passes_test(
    doctor_required,
    login_url="/doctor-login/"
)
def history(request):

    search_query = request.GET.get("search")

    tumor_filter = request.GET.get("tumor")

    patients = Patient.objects.all()

    if search_query:

        patients = patients.filter(
            name__icontains=search_query
        )

    if tumor_filter:

        patients = patients.filter(
            prediction=tumor_filter
        )

    patients = patients.order_by(
        "-created_at"
    )

    context = {

        "patients": patients,

        "glioma": Patient.objects.filter(
            prediction="Glioma Tumor"
        ).count(),

        "meningioma": Patient.objects.filter(
            prediction="Meningioma Tumor"
        ).count(),

        "pituitary": Patient.objects.filter(
            prediction="Pituitary Tumor"
        ).count(),

        "no_tumor": Patient.objects.filter(
            prediction="No Tumor Detected"
        ).count(),

        "active_filter": tumor_filter,
    }

    return render(
        request,
        "history.html",
        context
    )


@user_passes_test(
    doctor_required,
    login_url="/doctor-login/"
)
def dashboard(request):

    patients = Patient.objects.all()

    total_scans = patients.count()

    glioma = patients.filter(
        prediction="Glioma Tumor"
    ).count()

    meningioma = patients.filter(
        prediction="Meningioma Tumor"
    ).count()

    pituitary = patients.filter(
        prediction="Pituitary Tumor"
    ).count()

    no_tumor = patients.filter(
        prediction="No Tumor Detected"
    ).count()

    today_scans = patients.filter(
        created_at__date=date.today()
    ).count()

    last_patient = patients.order_by(
        "-created_at"
    ).first()

    context = {

        "total_scans": total_scans,
        "glioma": glioma,
        "meningioma": meningioma,
        "pituitary": pituitary,
        "no_tumor": no_tumor,
        "today_scans": today_scans,
        "last_analysis": last_patient,
        "reports_generated": total_scans,
    }

    return render(
        request,
        "dashboard.html",
        context
    )


@user_passes_test(
    doctor_required,
    login_url="/doctor-login/"
)
def clear_history(request):

    Patient.objects.all().delete()

    return redirect("/history/")


@user_passes_test(
    doctor_required,
    login_url="/doctor-login/"
)
def download_report(request, patient_id):

    patient = Patient.objects.get(
        id=patient_id
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; filename="report.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.drawString(
        100,
        800,
        f"Patient Name: {patient.name}"
    )

    pdf.drawString(
        100,
        780,
        f"Age: {patient.age}"
    )

    pdf.drawString(
        100,
        760,
        f"Prediction: {patient.prediction}"
    )

    pdf.save()

    return response


def doctor_login(request):

    if request.method == "POST":

        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user and user.is_superuser:

            login(request, user)

            return redirect("/dashboard/")

    return render(
        request,
        "doctor_login.html"
    )


