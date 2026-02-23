from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel_members = ['Iron Man', 'Spider-Man', 'Captain America']
        dc_members = ['Batman', 'Superman', 'Wonder Woman']

        Team.objects.create(name='marvel', members=marvel_members)
        Team.objects.create(name='dc', members=dc_members)

        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
        ]
        for user in users:
            user.save()

        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-02-23')
        Activity.objects.create(user='Spider-Man', type='cycle', duration=45, date='2026-02-22')
        Activity.objects.create(user='Batman', type='swim', duration=60, date='2026-02-21')
        Activity.objects.create(user='Superman', type='fly', duration=120, date='2026-02-20')

        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=200)

        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
