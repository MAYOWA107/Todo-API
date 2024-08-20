from rest_framework import serializers 
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError






class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        extra_kwargs = {
         'password': {'write_only': True},   
        }


    def save(self):
        #Confirming Password
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise ValidationError("Passwords don't match.")
        
        # Making the email Unique in database
        email = self._validated_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exist.")
        
        #Creating the user
        username = self.validated_data['username']
        account = User(username=username, email=email)
        account.set_password(password)
        account.save()
        
        return account
