from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Review, Category

def is_manager(user):
    return user.is_superuser or user.groups.filter(name='Managers').exists()

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

@user_passes_test(is_manager, login_url='login')
def manager_dashboard(request):
    # Querying MongoDB via Djongo
    reviews = Review.objects.all()
    pos = reviews.filter(sentiment='Positive').count()
    neu = reviews.filter(sentiment='Neutral').count()
    neg = reviews.filter(sentiment='Negative').count()
    
    context = {
        'total_products': Product.objects.count(),
        'total_reviews': reviews.count(),
        'chart_data': {'labels': ['Positive', 'Neutral', 'Negative'], 'values': [pos, neu, neg]},
        'reviews': reviews.order_by('-id')[:5],
    }
    return render(request, 'store/dashboard.html', context)
from django.shortcuts import get_object_or_404

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Get all AI-analyzed reviews for this specific product
    reviews = Review.objects.filter(product_name=product.name)
    
    return render(request, 'store/product_detail.html', {
        'product': product,
        'reviews': reviews
    })