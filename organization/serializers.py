from rest_framework import serializers

from . import models

#HyperlinkedModelSerializer۱
class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organization
        fields = (
            'city',
            'organization_name',
            'phone',
            'number_of_labor',
            'full_name',
            'Manufactured_products',
            'phone_number',
            'email',
            'user',
        )