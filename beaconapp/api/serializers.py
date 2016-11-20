from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Beacon, LostBeacon, FoundBeacon, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('phone',)


class SignUpSerializer(serializers.ModelSerializer):
	# phone = serializers.Field()
	# phone = serializers.SlugRelatedField(read_only=True, allow_null=True, slug_field='phone')
	userprofile = UserProfileSerializer()
	class Meta:
		model = User
		fields = ('username', 'password', 'email', 'first_name', 'last_name' , 'userprofile')
		write_only_fields = ('password',)

	def create(self, validated_data):
		# user 
		userprofile_data =  validated_data.pop('userprofile')
		user = User()
		user.username = validated_data.get('username')
		user.email = validated_data.get('email')
		user.first_name = validated_data.get('first_name')
		user.last_name = validated_data.get('last_name')
		user.set_password(validated_data.get('password'))
		user.save()
		userprofile = UserProfile.objects.create(user=user, **userprofile_data)
		return user


class UserBeaconsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beacon
		fields = ('unique_id', 'description', 'name')

	def create(self, validated_data):
		beacon = Beacon()
		beacon.unique_id = validated_data.get('unique_id')
		beacon.description = validated_data.get('description')
		beacon.name = validated_data.get('name')
		beacon.user = self.context['request'].user
		beacon.save()
		return beacon



class UserSerializer(serializers.ModelSerializer):
	userprofile = UserProfileSerializer()
	class Meta:
		model = User
		fields = ('username' ,'first_name', 'last_name', 'userprofile')
		

class BeaconSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Beacon
		fields = ('user' ,'unique_id', 'description', 'name')


class LostBeaconSerializer(serializers.ModelSerializer):
	beacon = BeaconSerializer()
	class Meta:
		model = LostBeacon
		fields = ('beacon', 'description', 'date', 'lat', 'long', 'reward')


class CreateLostBeaconSerializer(serializers.ModelSerializer):
	beacon = serializers.SlugRelatedField(queryset=Beacon.objects.all(), allow_null=True, slug_field='unique_id')
	class Meta:
		model = LostBeacon
		fields = ('beacon', 'description', 'date', 'lat', 'long', 'reward')


class CreateFoundBeaconSerializer(serializers.ModelSerializer):
	beacon = serializers.SlugRelatedField(queryset=Beacon.objects.all(), allow_null=True, slug_field='unique_id')
	class Meta:
		model = LostBeacon
		fields = ('beacon', 'description', 'date', 'lat', 'long', 'reward')

	def create(self, validated_data):
		found_beacon = FoundBeacon()
		found_beacon.beacon = validated_data.get('beacon')
		found_beacon.description = validated_data.get('description')
		found_beacon.date = validated_data.get('date')
		found_beacon.lat = validated_data.get('lat')
		found_beacon.long = validated_data.get('long')
		found_beacon.user = self.context['request'].user
		found_beacon.save()
		return found_beacon

class BeaconLocationsSerializer(serializers.ModelSerializer):
	beacon = BeaconSerializer()
	user = UserSerializer()

	class Meta:
		model = FoundBeacon
		fields = ('beacon', 'description', 'date', 'lat', 'long', 'user', 'distance', 'reward')
