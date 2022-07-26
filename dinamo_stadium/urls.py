"""dinamo_stadium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_dinamo import views
from employees.views import show_employee_articles, show_management
from history.views import show_history
from main.views import index, about_stadium, show_documents, how_to_get
from services.views import show_services_by_category, show_services_all
from vacancies.views import vacancies_list
from .yasg import urlpatterns as doc_urls


router = routers.DefaultRouter()
router.register('services', views.ServiceViewSet)
router.register('services_all', views.ServicesAllViewSet, basename='services_all')
router.register('service_detail', views.ServiceDetailViewSet, basename='service_detail')
router.register('services_by_category', views.ServicesByCategoryViewSet, basename='services_by_category')
router.register('category_services', views.CategoryServiceViewSet)
router.register('contact', views.ContactViewSet, basename='contact')
router.register('department_contacts', views.DepartmentContactsViewSet)
router.register('marketing_managers', views.MarketingMnagersViewSet)
router.register('payment_info', views.PaymentInfoViewSet)
router.register('news', views.NewsViewSet)
router.register('news_all', views.NewsAllViewSet, basename='news_all')
router.register('news_detail', views.NewsDetailViewSet, basename='news_detail')
router.register('employee_articles', views.EmployeeArticleViewSet)
router.register('employee_article_detail', views.EmployeeArticleDetailViewSet, basename='article_detail')
router.register('partners', views.PartnerViewSet)
router.register('documents', views.DocumentViewSet)
router.register('vacancies', views.VacancyViewSet)
router.register('vacancy_form', views.FeedbackForVacancyViewSet)
router.register('photo_album', views.PhotoViewSet)
router.register('photo_album_detail', views.PhotoDetailViewSet, basename='photo_album_detail')
router.register('video_album', views.VideoViewSet)
router.register('video_album_detail', views.VideoDetailViewSet, basename='video_album_detail')
router.register('social_links', views.SocialNetworkViewSet)
router.register('email_form', views.UserEmailViewSet)
router.register('feedback_form', views.FeedbackViewSet)
router.register('management', views.ManagementViewSet)
router.register('history_articles', views.HistoryArticleViewSet)
router.register('events', views.EventViewSet)
router.register('services_random', views.RandomServicesViewSet, basename='services_random' )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about_stadium/', about_stadium, name='about_stadium'),
    path('services/', show_services_all, name='show_services_all'),
    path('services/<slug:category_slug>/', show_services_by_category, name='show_services_by_category'),
    path('api_dinamo/', include(router.urls)),
    path('vacancies/', vacancies_list, name='vacancies_list'),
    path('history/', show_history, name='history'),
    path('management/', show_management, name='management'),
    path('documents/', show_documents, name='documents'),
    path('how_to_get/', how_to_get, name='how_to_get'),
    # path('employee_articles/', show_employee_articles, name='employee_articles'),
    # path('video/', show_video, name='video'),
    # path('video/<slug:category_slug>/', show_video_by_category, name='video_by_category'),
    # path('photo/', show_photo, name='photo'),
    # path('photo/<slug:category_slug>/', show_photo_by_category, name='photo_by_category'),
    # path('services/<slug:category_slug><slug:service_slug><int:service_id>/', service_detail, name='service_detail'),

]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
