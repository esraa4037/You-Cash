from rest_framework import permissions


"""
Custom permission to only allow owners of an object or admin to view it.
"""
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Check if the user is authenticated and the owner of the transaction history or an admin.
        """
        return request.user.is_authenticated and (request.user.id == view.kwargs["account_id"] or request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the transaction history or an admin.
        """
        return obj.user == request.user or request.user.is_staff
    
     