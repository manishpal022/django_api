from rest_framework import serializers
from .models import Customer, Profession, DataSheet, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'doc_type', 'doc_number', 'customer']

        read_only_fields = ('customer', )


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ['id', 'description', 'historical_data']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description', 'status']


class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()
    # data_sheet = serializers.SerializerMethodField()
    # data_sheet = serializers.PrimaryKeyRelatedField(read_only=True)
    data_sheet = DataSheetSerializer()
    professions = ProfessionSerializer(many=True)
    # professions = serializers.StringRelatedField(many=True)
    document_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'professions', 'data_sheet', 'active',
                  'status_message', 'num_professions', 'document_set']

    # we can use create method in views file also
    def create(self, validated_data):
        professions = validated_data['professions']
        del validated_data['professions']

        document_set = validated_data['document_set']
        del validated_data['document_set']

        data_sheet = validated_data['data_sheet']
        del validated_data['data_sheet']

        d_sheet = DataSheet.objects.create(**data_sheet)
        customer = Customer.objects.create(**validated_data)

        customer.data_sheet = d_sheet

        for doc in document_set:
            Document.objects.create(
                doc_type=doc['doc_type'],
                doc_number=doc['doc_number'],
                customer_id=customer.id
            )

        for profession in professions:
            prof = Profession.objects.create(**profession)
            customer.professions.add(prof)

        customer.save()
        return customer


    def get_num_professions(self, obj):
        return obj.num_professions()

    # def get_data_sheet(self, obj):
    #     return obj.data_sheet.description




