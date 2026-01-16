from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.core.paginator import EmptyPage, PageNotAnInteger

from collections import OrderedDict


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_page_size(self, request):
        """
            Handle dynamic page_size via query parameter or fallback
            to default.
        """
        page_size = request.query_params.get(self.page_size_query_param)

        if page_size:
            try:
                page_size = int(page_size)
                if page_size < 1:
                    return self.page_size  # Default if invalid
                return min(page_size, self.max_page_size)
            except ValueError:
                return self.page_size  # Default if invalid

        return self.page_size

    def paginate_queryset(self, queryset, request, view=None):
        """
            Override paginate_queryset to return the last page if an invalid
            page number is given.
        """
        self.page_size = self.get_page_size(request)
        paginator = self.django_paginator_class(queryset, self.page_size)
        page_number = request.query_params.get(self.page_query_param, 1)

        try:
            self.page = paginator.page(page_number)
        except PageNotAnInteger:
            # If the page is not an integer, return the first page
            self.page = paginator.page(1)
        except EmptyPage:
            # If the page is out of range, return the last page
            self.page = paginator.page(paginator.num_pages)

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        """
            Custom response format for pagination.
        """
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('total_pages', self.page.paginator.num_pages),
            ('current_page', self.page.number),
            ('page_size', self.page_size),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
