from rest_framework import serializers
from accounts.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from accounts.utils import Util

class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this because we need confirm password field in our Registration Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email', 'username','bio','profile_picture', 'password', 'password2']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    print(attrs)
    if not attrs.profile_picture or attrs.profile_picture=="":
      attrs.profile_picture='https://i.pravatar.cc/300'
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    if not validate_data.profile_picture:
      validate_data.profile_picture='https://i.pravatar.cc/300'
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username','bio','profile_picture']

class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    user = self.context.get('user')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password)
    user.save()
    return attrs

class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    fields = ['email']

  def validate(self, attrs):
    email = attrs.get('email')
    if User.objects.filter(email=email).exists():
      user = User.objects.get(email = email)
      uid = urlsafe_base64_encode(force_bytes(user.id))
      print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(user)
      print('Password Reset Token', token)
      link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
      print('Password Reset Link', link)
      # Send EMail
      body = 'Click Following Link to Reset Your Password '+link
      data = {
        'subject':'Reset Your Password',
        'body':body,
        'to_email':user.email
      }
      # Util.send_email(data)
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')

class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      user = User.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired')
  

class UserProfileUpdateSerializer(serializers.ModelSerializer):
  # We are writing this because we need confirm password field in our Registration Request
  class Meta:
      model = User
      fields=['email', 'username','bio','profile_picture']
  def validate(self, attrs):
    email = attrs.get('email') 
    username = attrs.get('username')
    bio = attrs.get('bio')
    profile_picture = attrs.get('profile_picture')
    user = self.context.get('user')

    if user.email!=email:
      user.email=email

    if user.username!=username:
      user.username=username


    user.bio=bio
    user.profile_picture=profile_picture

    user.save()
    return attrs
    



class UserProfilePictureUploadSerializer(serializers.ModelSerializer):
  # We are writing this because we need confirm password field in our Registration Request
  class Meta:
      model = User
      fields=['profile_picture']

  def validate(self, attrs):
    profile_picture = attrs.get('profile_picture')
    user = self.context.get('user')
    print(user,'user')
    if not profile_picture:
      raise serializers.ValidationError("Profile Picture is not provided")
  
    user.profile_picture=profile_picture
    print(user)
    user.save()
    return attrs