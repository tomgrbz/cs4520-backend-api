
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from uuid import UUID
import random
from flask_uuid import FlaskUUID

rd = random.Random()
rd.seed(0)
app = Flask(__name__)

flask_uuid = FlaskUUID()
flask_uuid.init_app(app)


user1_id = UUID(int=rd.getrandbits(128), version=4)
user2_id = UUID(int=rd.getrandbits(128), version=4)
user3_id = UUID(int=rd.getrandbits(128), version=4)
user4_id = UUID(int=rd.getrandbits(128), version=4)
user5_id = UUID(int=rd.getrandbits(128), version=4)

user_dict = {
    user1_id: {
        'username': '#1pokemonfan',
        'img_href': "res/bear",
        'user_id': user1_id,
        'password': 'password'
    },
    user2_id: {
        'username': 'thomas grbic',
        'img_href': "res/bear",
        'user_id': user2_id,
        'password': 'password123'
    },
    user3_id: {
        'username': 'ben10',
        'img_href': "res/bear",
        'user_id': user3_id,
        'password': 'qwerty'
    },
    user4_id: {
        'username': 'Official Spongebob',
        'img_href': "res/bear",
        'user_id': user4_id,
        'password': 'abc123'
    },
    user5_id: {
        'username': 'Dora the Explorer',
        'img_href': "res/bear",
        'user_id': user5_id,
        'password': 'abc123'
    },
    '123': {
        'username': 'testuser',
        'img_href': "res/bear",
        'user_id': '123',
        'password': 'password'
    },
}

bab_dict = {
    '12345': {
        'bab_id': '12345',
        'author_user': user_dict[user1_id],
        'content': 'I love pokemon',
        'date': '2020-12-25',
        'likes': 2,
        'liked_user_list': [user1_id, user2_id]
    },
    '12346': {
        'bab_id': '12346',
        'author_user': user_dict[user2_id],
        'content': 'Isnt bable a great app?',
        'date': '2020-12-25',
        'likes': 4,
        'liked_user_list': [user1_id, user3_id, user4_id, user5_id]
    },
    '12347': {
        'bab_id': '12347',
        'author_user': user_dict[user3_id],
        'content': 'I think my favorite is pikachu!',
        'date': '2020-12-25',
        'likes': 2,
        'liked_user_list': [user1_id, user2_id]
    },
    '12348': {
        'bab_id': '12348',
        'author_user': user_dict[user4_id],
        'content': 'Twitter is like so 2014',
        'date': '2020-12-25',
        'likes': 4,
        'liked_user_list': [user1_id, user3_id, user4_id, user5_id]
    },
    '12349': {
        'bab_id': '12349',
        'author_user': user_dict[user5_id],
        'content': 'Looking to trade for my charizard!',
        'date': '2020-12-25',
        'likes': 2,
        'liked_user_list': [user1_id, user2_id]
    },
    '12350': {
        'bab_id': '12350',
        'author_user': user_dict[user1_id],
        'content': '.....THIS SEMESTER IS ALMOST OVER',
        'date': '2020-12-25',
        'likes': 2,
        'liked_user_list': [user1_id, user2_id]
    },
    '12351': {
        'bab_id': '12351',
        'author_user': user_dict['123'],
        'content': 'I love testing',
        'date': '2020-12-25',
        'likes': 4,
        'liked_user_list': [user1_id, user3_id, user4_id, user5_id]
    },
}

user_profile_dict = {
    '12345': {
        'user': user_dict[user1_id],
        'description': 'I love pokemon',
        'followers': [user_dict[user2_id], user_dict[user3_id]],
        'followers_count': 2,
        'following': [user_dict[user3_id], user_dict[user4_id]],
        'following_count': 2,
        'bab_count': 1,
    },
    '12346': {
        'user': user_dict[user2_id],
        'description': 'I love bable so much. #SoftwareEngineering #BableIsTheBest',
        'followers': [user_dict[user1_id], user_dict[user3_id]],
        'followers_count': 2,
        'following': [user_dict[user3_id]],
        'following_count': 1,
        'bab_count': 1,
    },
    '12347': {
        'user': user_dict['123'],
        'description': 'I am a test user',
        'followers': [user_dict[user2_id], user_dict[user3_id]],
        'followers_count': 2,
        'following': [user_dict[user3_id], user_dict[user4_id]],
        'following_count': 2,
        'bab_count': 1,
    },
    '12348': {
        'user': user_dict[user3_id],
        'description': 'I love ben10',
        'followers': [user_dict[user2_id], user_dict[user3_id]],
        'followers_count': 2,
        'following': [user_dict[user3_id], user_dict[user4_id]],
        'following_count': 2,
        'bab_count': 1,
    },
    '12349': {
        'user': user_dict[user4_id],
        'description': 'I love spongebob',
        'followers': [user_dict[user2_id], user_dict[user3_id]],
        'followers_count': 2,
        'following': [user_dict[user3_id], user_dict[user4_id]],
        'following_count': 2,
        'bab_count': 1,
    },
    '12350': {
        'user': user_dict[user5_id],
        'description': 'Anyone seen my map?',
        'followers': [user_dict[user2_id], user_dict[user3_id]],
        'followers_count': 2,
        'following': [user_dict[user3_id], user_dict[user4_id]],
        'following_count': 2,
        'bab_count': 1,
    },
}

@app.route('/')
def hello_world():
    return 'Hello from Babble!'

# Get some random subset of babs
@app.route('/babs', methods=['GET'])
def babs():
    num_babs = rd.randint(2, 4)
    random_babs = rd.sample(list(bab_dict.values()), num_babs)
    return {'babs': random_babs}

# Likes a bab given a bab id,
# requires user_id to be passed in request body
@app.route('/babs/<bab_id>/likes', methods=['POST'])
def like_bab(bab_id):
    # User id from request body
    user_id = request.json['user_id']
    bab = bab_dict[bab_id]
    if user_id in bab['liked_user_list']:
        return {'error': 'User has already liked this bab'}
    bab['liked_user_list'].append(user_id)
    bab['likes'] += 1
    return {'likes': bab['likes'], 'liked_user_list': bab['liked_user_list']}

# Deletes a bab given a bab id
@app.route('/babs/<bab_id>', methods=['DELETE'])
def delete_bab(bab_id):
    del bab_dict[bab_id]
    return {'success': True}

#  Get all babs from a user
@app.route('/users/babs/<uuid(strict=False):user_id>', methods=['GET'])
def get_user_babs(user_id):
    user_babs = get_babs_by_user(user_id)
    return {'babs': user_babs}

# Login, requires username and password in request body
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    for user in user_dict.values():
        if user['username'] == username and user['password'] == password:
            return {'user': user}
    return {'error': 'Invalid username or password'}

# Fresh sign up, requires username and password in request body
@app.route('/signup', methods=['POST'])
def sign_up():
    username = request.json['username']
    password = request.json['password']
    user_id = UUID(int=rd.getrandbits(128), version=4)
    user_dict[user_id] = {
        'username': username,
        'img_href': "res/bear",
        'user_id': user_id,
        'password': password
    }
    return {'user': user_dict[user_id]}

# Get user profile given user id
@app.route('/profiles/<uuid(strict=False):user_id>', methods=['GET'])
def get_user_profile(user_id):
    user_profile = get_user_profile_from_user_id(user_id)
    return {'profile': user_profile}

# Get user followering list and following count given user id
@app.route('/users/<uuid(strict=False):user_id>/following', methods=['GET'])
def get_user_following(user_id):
    user_profile = get_user_profile_from_user_id(user_id)
    return {'following': user_profile['following'], 'following_count': user_profile['following_count']}

# Follows a user given a user id, requires this user's user_id in request body
@app.route('/follows/<uuid(strict=False):to_follow_user_id>', methods=['POST'])
def follow_user(to_follow_user_id):
    this_user = request.json['this_user_id']
    to_follow_user_profile = get_user_profile_from_user_id(to_follow_user_id)
    this_user_profile = get_user_profile_from_user_id(this_user)
    
    to_follow_user_profile['followers'].append(user_dict[this_user])
    to_follow_user_profile['followers_count'] += 1

    this_user_profile['following'].append(user_dict[to_follow_user_id])
    this_user_profile['following_count'] += 1

    return {'success': True, 'to_follow_user_profile': to_follow_user_profile, 'this_user_profile': this_user_profile}

# Unfollows a user given a user id, requires this user's user_id in request body
@app.route('/follows/<uuid(strict=False):to_unfollow_user_id>', methods=['DELETE'])
def unfollow_user(to_unfollow_user_id):
    this_user = request.json['this_user_id']
    to_unfollow_user_profile = get_user_profile_from_user_id(to_unfollow_user_id)
    this_user_profile = get_user_profile_from_user_id(this_user)

    to_unfollow_user_profile['followers'].remove(user_dict[this_user])
    to_unfollow_user_profile['followers_count'] -= 1
    
    this_user_profile['following'].remove(user_dict[to_unfollow_user_id])
    this_user_profile['following_count'] -= 1
    return {'success': True, 'to_unfollow_user_profile': to_unfollow_user_profile, 'this_user_profile': this_user_profile}


# utility method to get user profile from given user id
def get_user_profile_from_user_id(user_id):
    user_profile = None
    for profile in user_profile_dict.values():
        if profile['user']['user_id'] == user_id:
            user_profile = profile
            break
    return user_profile

# Utility method to get all babs from specified user
def get_babs_by_user(user_id):
    user_babs = []
    for bab in bab_dict.values():
        if bab['author_user']['user_id'] == user_id:
            user_babs.append(bab)
    return user_babs