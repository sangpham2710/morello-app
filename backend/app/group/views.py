from rest_framework.response import Response

from .models import (
    Member,
    BalanceEntry,
    CollectEntry,
    CollectSession,
    Moderator
)
from .serializers import (
    GroupSerializer,
    MemberSerializer,
    BalanceEntrySerializer,
    CollectSessionSerializer,
    ModeratorSerializer
)
from rest_framework import viewsets
from django.db.models import (
    Sum,
)

from .mixins import GroupPermissionMixin
from rest_framework.decorators import action

# Create your views here.


class GroupViewSet(GroupPermissionMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = GroupSerializer


class MemberViewSet(GroupPermissionMixin, viewsets.ModelViewSet):
    serializer_class = MemberSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_pk']
        groups = super().get_queryset()
        if group_id not in groups.values_list('id', flat=True):
            return Member.objects.none()  # Return an empty queryset
        return Member.objects.filter(group_id=group_id)


class BalanceViewSet(GroupPermissionMixin, viewsets.ViewSet):
    def list(self, request, group_pk=None):
        book_balance = BalanceEntry.objects.filter(
            group_id=group_pk).aggregate(
            Sum('amount'))['amount__sum']
        actual_balance = CollectEntry.objects.filter(
            status=True,
            session_id__balance_entries__group_id=group_pk
        ).aggregate(Sum('amount'))['amount__sum']

        return Response({
            'book_balance': book_balance if book_balance is not None else 0,
            'actual_balance': actual_balance if actual_balance is not None else 0
        })


class BalanceEntryViewSet(GroupPermissionMixin, viewsets.ModelViewSet):
    serializer_class = BalanceEntrySerializer

    def get_queryset(self):
        group_id = self.kwargs['group_pk']
        return BalanceEntry.objects.filter(group_id=group_id)


class CollectSessionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectSessionSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_pk']
        return CollectSession.objects.filter(
            balance_entries__group_id=group_id)

    @action(detail=True, methods=['patch'])
    def status(self, request, group_pk=None, session_pk=None):
        session = self.get_object()
        member_status_data = request.data
        if member_status_data is None:
            return Response({'error': 'Invalid input'}, status=400)

        for data in member_status_data:
            member_id = data.get('member_id')
            status = data.get('status')
            if member_id is not None and status is not None:
                collect_entry = session.collect_entries.filter(
                    member_id=member_id).first()
                if collect_entry:
                    collect_entry.status = status
                    collect_entry.save()
        return Response({'status': 'status set for members'})


class ModeratorViewSet(GroupPermissionMixin, viewsets.ModelViewSet):
    serializer_class = ModeratorSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_pk']
        return Moderator.objects.filter(
            group_id=group_id).select_related('user_id')
