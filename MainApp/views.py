import csv
import json
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import default_storage
from django.contrib import messages
from .forms import UploadFileForm

def upload_file(request):
    """
        Function to receive GET and POST request
        GET Request responses with rendering index page
        POST request responses with JSON data to download
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            timeframe = int(request.POST.get('timeframe', 0))
            if not (timeframe and file.name.endswith(".csv")):
                messages.warning(request, "CSV File not entered or Timeframe value not entered")
                return redirect("/")
            file_name = default_storage.save(file.name, file)
            data = handle_uploaded_file(file)
            if len(data) <= timeframe:
                messages.error(request, "Not enough sufficient data")
                return redirect("/")
            data_within_timeframe = data[:timeframe]
            result = generate_timeframe(data_within_timeframe)
            json_result = json.dumps(result, indent = 2)
            filepath = f"{file_name}.json"
            default_storage.save(filepath, ContentFile(json_result))
            response = HttpResponse(json_result, content_type = 'application/json')
            response['Content-Disposition'] = f'attachment; filename = {filepath}'
            return response
    else:
        form = UploadFileForm()
    return render(request, "MainApp/index.html", {"form": form})

def handle_uploaded_file(f):
    """
    This function processes the uploaded CSV file and returns a list
    """
    data = []
    try:
        processed_file = f.read().decode('utf-8').splitlines()
        reader = csv.reader(processed_file)
        headers = next(reader)
        for row in reader:
            processed_row = dict(zip(headers, row))
            data.append(processed_row)
    except:
        return data
    return data

def generate_timeframe(data):
    """
    This function processes the input list and returns result dictionary
    """
    max_high = max(data, key = lambda x: x["HIGH"])['HIGH']
    min_low = min(data, key = lambda x: x["LOW"])['LOW']
    result = {
        "BANKNIFTY": data[0]["BANKNIFTY"],
        "DATE": data[0]["DATE"],
        "TIME": data[0]["TIME"],
        "OPEN": data[0]["OPEN"],
        "HIGH": max_high,
        "LOW": min_low,
        "VOLUME": data[-1]["VOLUME"],
        "CLOSE": data[-1]["CLOSE"]
    }
    return result