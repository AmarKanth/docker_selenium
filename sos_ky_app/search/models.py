from django.db import models


class SearchQuery(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    search_term = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.search_term} ({self.status})'

    class Meta:
        ordering = ['-created_at']


class SearchResult(models.Model):
    search_query = models.ForeignKey(SearchQuery, related_name='results', on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    result_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Result for "{self.search_query.search_term}"'

    class Meta:
        ordering = ['-created_at']