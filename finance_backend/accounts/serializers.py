from rest_framework.simplejwt.serializers impoert TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(CustomTokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        data['user'] = {
            'id': self.user.id,
            'name': self.user.name,
            'email': self.user.email
        }
        
        return data