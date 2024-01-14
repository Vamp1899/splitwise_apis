from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateGroupApiView, CreateExpenseApiView, UserProfileApiView,\
AddUserToGroupApiView, ShowGroupMembersApiView, ShowGroupDetailsApiView, ShowUserDetailsApiView,\
DeleteUserApiView, DeleteGroupApiView, RecordPaymentApiView

urlpatterns = [
    path('createGroup', CreateGroupApiView.as_view()),
    path('createExpense', CreateExpenseApiView.as_view()),
    path('createUser', UserProfileApiView.as_view()),
    path('addUserToGroup', AddUserToGroupApiView.as_view()),
    path('showGroupMembers', ShowGroupMembersApiView.as_view()),
    path('userDetails', ShowUserDetailsApiView.as_view()),
    path('addExpense', CreateExpenseApiView.as_view()),
    path('groupDetails', ShowGroupDetailsApiView.as_view()),
    path('deleteUser', DeleteUserApiView.as_view()),
    path('deleteGroup', DeleteGroupApiView.as_view()),
    path('recordPayment', RecordPaymentApiView.as_view()),
]