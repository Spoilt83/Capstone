from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import CommentForm
from .models import UserComments


# def form_view(request):
#     from = CommentForm()
#     if form.is_valid():
#         cd = form.cleaned_data
#         uc = UserComments(
#             first_name = cd['first_name'],
#             lsat_namme = cd['last_name'],
#             comment = cd['comment']
#             )
#         uc.save()
#         return JsonResponse({
#             'message': 'success'
#             })
        
#     return render(request, 'blog.html', {'form': form})


def index(request):
    return render(request, 'index.html', {})