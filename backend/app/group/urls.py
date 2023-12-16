from django.urls import path, include
from rest_framework_nested import routers
from .views import (
    GroupViewSet,
    ModeratorViewSet,
    MemberViewSet,
    BalanceViewSet,
    CollectSessionViewSet,
    BalanceEntryViewSet
)

router = routers.SimpleRouter()
router.register(r'groups', GroupViewSet, basename='groups')

groups_router = routers.NestedSimpleRouter(router, r'groups', lookup='group')
groups_router.register(r'members', MemberViewSet, basename='group-members')
groups_router.register(r'balance', BalanceViewSet, basename='group-balance')
groups_router.register(
    r'balance/entries',
    BalanceEntryViewSet,
    basename='group-balance-entries')
groups_router.register(
    r'sessions',
    CollectSessionViewSet,
    basename='group-sessions')
groups_router.register(
    r'sessions/(?P<session_pk>\d+)/status',
    CollectSessionViewSet,
    basename='group-session-set-status')
groups_router.register(
    r'moderators',
    ModeratorViewSet,
    basename='group-moderators')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(groups_router.urls)),
]
