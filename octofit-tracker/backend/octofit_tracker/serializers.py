from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'team', 'is_superhero']

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty']
