from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from core.tasks import run_webscraper


class SearchView(View):
    def get(self, request):
        records = [
            {"search_query": "Eagle LLC", "status":"Found", "created_at":"2024-11-25 12:10:44"}, 
            {"search_query": "Tesla", "status":"Pending", "created_at":"2024-11-25 12:10:44"},
            {"search_query": "Zenwork", "status":"Not Found", "created_at":"2024-11-25 12:10:44"}
        ]
        run_webscraper.delay()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('search/_records_table.html', {'records': enumerate(records)})
            return JsonResponse({'html': html})
        return render(request, 'search/index.html', {'records': enumerate(records)})