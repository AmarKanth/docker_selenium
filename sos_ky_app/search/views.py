from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from search.models import SearchQuery, SearchResult
from core.tasks import run_webscraper


class SearchView(View):
    def get(self, request):
        search_term = request.GET.get('query')
        
        if search_term:
            searc_query = SearchQuery.objects.create(search_term=search_term)
            run_webscraper.delay(searc_query.id)
        
        records = SearchQuery.objects.all()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('search/_records_table.html', {'records': records})
            return JsonResponse({'html': html})
        return render(request, 'search/index.html', {'records': records})


class SearchDetails(View):
    def get(self, request, id):
        results = SearchResult.objects.filter(search_query_id=id)
        return render(request, 'search/details.html', {'results': results})