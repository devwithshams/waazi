from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from .models import Scholar, Category, Waazi
from .serializers import ScholarListSerializer, ScholarDetailSerializer, CategorySerializer, WaaziSerializer

def home(request):
    scholars = Scholar.objects.all()
    categories = Category.objects.all()
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    if search_query:
        scholars = scholars.filter(name__icontains=search_query)
    if category_id:
        scholars = scholars.filter(waazi__category_id=category_id).distinct()

    return render(request, "waazi/home.html", {
        "scholars": scholars,
        "categories": categories,
        "search_query": search_query,
        "selected_category": category_id
    })


def scholars(request):
    scholars = Scholar.objects.all()
    return render(request, "waazi/scholars.html", {"scholars": scholars})




def scholar_profile(request, scholar_id):
    scholar = get_object_or_404(Scholar, id=scholar_id)
    waazis = scholar.waazi_set.all()
    return render(request, "waazi/reciter-profile.html", {"scholar": scholar, "waazis": waazis})

# API Section (unchanged)
class ScholarViewSet(viewsets.ModelViewSet):
    queryset = Scholar.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ScholarListSerializer
        return ScholarDetailSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WaaziViewSet(viewsets.ModelViewSet):
    queryset = Waazi.objects.all().order_by('title')
    serializer_class = WaaziSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category__name']

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        waazi = self.get_object()
        waazi.downloads += 1
        waazi.save()
        return FileResponse(waazi.audio_file.open(), as_attachment=True)