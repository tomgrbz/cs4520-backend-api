
# A very simple Flask Hello World app for you to get started with...

import datetime
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
        'imgHref': "https://m.media-amazon.com/images/I/31YObRg58fL._SY445_SX342_.jpg",
        'userID': user1_id,
        'password': 'password'
    },
    user2_id: {
        'username': 'thomas grbic',
        'imgHref': "https://m.media-amazon.com/images/I/31YObRg58fL._SY445_SX342_.jpg",
        'userID': user2_id,
        'password': 'password123'
    },
    user3_id: {
        'username': 'ben10',
        'imgHref': "https://i.pinimg.com/736x/7d/ca/ea/7dcaea1bdd02cc7f5a1d0723015227ff.jpg",
        'userID': user3_id,
        'password': 'qwerty'
    },
    user4_id: {
        'username': 'Official Spongebob',
        'imgHref': "https://nickelodeonuniverse.com/wp-content/uploads/Spongebob.png",
        'userID': user4_id,
        'password': 'abc123'
    },
    user5_id: {
        'username': 'Dora the Explorer',
        'imgHref': "https://pernilleripp.files.wordpress.com/2011/04/0d26c-dora_explorer_show.jpg?w=219&h=320",
        'userID': user5_id,
        'password': 'abc123'
    },
    '123': {
        'username': 'testuser',
        'imgHref': "https://m.media-amazon.com/images/I/31YObRg58fL._SY445_SX342_.jpg",
        'userID': '123',
        'password': 'password'
    },
    '1234': {
        'username': 'plankton',
        'imgHref': "https://m.media-amazon.com/images/I/31YObRg58fL._SY445_SX342_.jpg",
        'userID': '1234',
        'password': 'pass'
    },
}

bab_dict = {
    '12345': {
        'babID': 12345,
        'authorUser': user_dict[user1_id],
        'content': 'I love pokemon',
        'date': '2020-12-25',
        'likes': 2,
        'likedUserList': [user1_id, user2_id]
    },
    '12346': {
        'babID': 12346,
        'authorUser': user_dict[user2_id],
        'content': 'Isnt bable a great app?',
        'date': '2020-12-25',
        'likes': 4,
        'likedUserList': [user1_id, user3_id, user4_id, user5_id]
    },
    '12347': {
        'babID': 12347,
        'authorUser': user_dict[user3_id],
        'content': 'I think my favorite is pikachu!',
        'date': '2020-12-25',
        'likes': 2,
        'likedUserList': [user1_id, user2_id]
    },
    '12348': {
        'babID': 12348,
        'authorUser': user_dict[user4_id],
        'content': 'Twitter is like so 2014',
        'date': '2020-12-25',
        'likes': 4,
        'likedUserList': [user1_id, user3_id, user4_id, user5_id]
    },
    '12349': {
        'babID': 12349,
        'authorUser': user_dict[user5_id],
        'content': 'Looking to trade for my charizard!',
        'date': '2020-12-25',
        'likes': 2,
        'likedUserList': [user1_id, user2_id]
    },
    '12350': {
        'babID': 12350,
        'authorUser': user_dict[user1_id],
        'content': '.....THIS SEMESTER IS ALMOST OVER',
        'date': '2020-12-25',
        'likes': 2,
        'likedUserList': [user1_id, user2_id]
    },
    '12351': {
        'babID': 12351,
        'authorUser': user_dict['123'],
        'content': 'I love testing',
        'date': '2020-12-25',
        'likes': 4,
        'likedUserList': [user1_id, user3_id, user4_id, user5_id]
    },
    '12352': {
        'babID': 12352,
        'authorUser': user_dict['1234'],
        'content': 'Maximum overdrive!',
        'date': '2024-04-16',
        'likes': 2,
        'likedUserList': [user1_id, user2_id]
    },
}

user_profile_dict = {
    '12345': {
        'user': user_dict[user1_id],
        'description': 'I love pokemon',
        'followerList': [user_dict[user2_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id], user_dict[user4_id]],
        'followingListCount': 2,
        'babCount': 1,
    },
    '12346': {
        'user': user_dict[user2_id],
        'description': 'I love bable so much. #SoftwareEngineering #BableIsTheBest',
        'followerList': [user_dict[user1_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id]],
        'followingListCount': 1,
        'babCount': 1,
    },
    '12347': {
        'user': user_dict['123'],
        'description': 'I am a test user',
        'followerList': [user_dict[user2_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id], user_dict[user4_id]],
        'followingListCount': 2,
        'babCount': 1,
    },
    '12348': {
        'user': user_dict[user3_id],
        'description': 'I love ben10',
        'followerList': [user_dict[user2_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id], user_dict[user4_id]],
        'followingListCount': 2,
        'babCount': 1,
    },
    '12349': {
        'user': user_dict[user4_id],
        'description': 'I love spongebob',
        'followerList': [user_dict[user2_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id], user_dict[user4_id]],
        'followingListCount': 2,
        'babCount': 1,
    },
    '12350': {
        'user': user_dict[user5_id],
        'description': 'Anyone seen my map?',
        'followerList': [user_dict[user2_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id], user_dict[user4_id]],
        'followingListCount': 2,
        'babCount': 1,
    },
    '12351': {
        'user': user_dict['1234'],
        'description': 'I will steal the krabby patty formula!!',
        'followerList': [user_dict[user2_id], user_dict[user3_id]],
        'followerCount': 2,
        'followingList': [user_dict[user3_id], user_dict[user4_id]],
        'followingListCount': 2,
        'babCount': 1,
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
# requires userID to be passed in request body
@app.route('/babs/<babID>/likes', methods=['POST'])
def like_bab(babID):
    # User id from request body
    userID = request.json['userID']
    bab = bab_dict[babID]
    if userID in bab['likedUserList']:
        return {'error': 'User has already liked this bab'}
    bab['likedUserList'].append(userID)
    bab['likes'] += 1
    return {'likes': bab['likes'], 'likedUserList': bab['likedUserList']}

# Unlikes a bab given a bab id
@app.route('/babs/<babID>/unlikes', methods=['POST'])
def unlike_bab(babID):
    # User id from request body
    userID = request.json['userID']
    bab = bab_dict[babID]
    if userID not in bab['likedUserList']:
        return {'error': 'User has not liked this bab'}
    bab['likedUserList'].remove(userID)
    bab['likes'] -= 1
    return {'likes': bab['likes'], 'likedUserList': bab['likedUserList']}

# Deletes a bab given a bab id
@app.route('/babs/<babID>', methods=['DELETE'])
def delete_bab(babID):
    del bab_dict[babID]
    return {'success': True}

@app.route('/babs/<uuid(strict=False):userID>', methods=['POST'])
def add_bab(userID):
    content = request.json['content']
    babID = rd.randint(10000, 99999)
    date = datetime.date.today().strftime('%Y-%m-%d')
    bab_dict[babID] = {
        'babID': babID,
        'authorUser': user_dict[userID],
        'content': content,
        'date': date,
        'likes': 0,
        'likedUserList': []
    }
    return {'bab': bab_dict[babID], 'allBabsByUser': get_babs_by_user(userID)}
    

#  Get all babs from a user
@app.route('/users/babs/<uuid(strict=False):userID>', methods=['GET'])
def get_user_babs(userID):
    user_babs = get_babs_by_user(userID)
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
    userID = UUID(int=rd.getrandbits(128), version=4)
    user_dict[userID] = {
        'username': username,
        'imgHref': "res/bear",
        'userID': userID,
        'password': password
    }
    random_profile_id = rd.randint(10000, 99999)
    user_profile_dict[random_profile_id] = {
        'user': user_dict[userID],
        'description': '',
        'followerList': [],
        'followerCount': 0,
        'followingList': [],
        'followingListCount': 0,
        'babCount': 0,
    }
    return {'user': user_dict[userID]}

# Get user profile given user id
@app.route('/profiles/<uuid(strict=False):userID>', methods=['GET'])
def get_user_profile(userID):
    user_profile = get_user_profile_from_userID(userID)
    return {'profile': user_profile}

# Change description of user profile
@app.route('/profiles/<uuid(strict=False):userID>/description', methods=['POST'])
def change_description(userID):
    user_profile = get_user_profile_from_userID(userID)
    user_profile['description'] = request.json['description']
    return {'profile': user_profile}

@app.route('/profiles/<uuid(strict=False):userID>/username', methods=['POST'])
def change_username(userID):
    user = user_dict[userID]
    user['username'] = request.json['username']
    get_user_profile_from_userID(userID)['user'] = user
    return {'user': user}

# Get user followering list and followingList count given user id
@app.route('/users/<uuid(strict=False):userID>/following', methods=['GET'])
def get_user_followingList(userID):
    user_profile = get_user_profile_from_userID(userID)
    return {'followingList': user_profile['followingList'], 'followingListCount': user_profile['followingListCount']}

# Follows a user given a user id, requires this user's userID in request body
@app.route('/follows/<uuid(strict=False):to_follow_userID>', methods=['POST'])
def follow_user(to_follow_userID):
    this_user = request.json['thisUserID']
    to_follow_user_profile = get_user_profile_from_userID(to_follow_userID)
    this_user_profile = get_user_profile_from_userID(this_user)
    
    to_follow_user_profile['followerList'].append(user_dict[this_user])
    to_follow_user_profile['followerCount'] += 1

    this_user_profile['followingList'].append(user_dict[to_follow_userID])
    this_user_profile['followingListCount'] += 1

    return {'success': True, 'toFollowUserProfile': to_follow_user_profile, 'thisUserProfile': this_user_profile}

# Unfollows a user given a user id, requires this user's userID in request body
@app.route('/follows/<uuid(strict=False):to_unfollow_userID>', methods=['DELETE'])
def unfollow_user(to_unfollow_userID):
    this_user = request.json['thisUserID']
    to_unfollow_user_profile = get_user_profile_from_userID(to_unfollow_userID)
    this_user_profile = get_user_profile_from_userID(this_user)

    to_unfollow_user_profile['followerList'].remove(user_dict[this_user])
    to_unfollow_user_profile['followerCount'] -= 1
    
    this_user_profile['followingList'].remove(user_dict[to_unfollow_userID])
    this_user_profile['followingListCount'] -= 1
    return {'success': True, 'toUnfollowUserProfile': to_unfollow_user_profile, 'thisUserProfile': this_user_profile}

# utility method to get user profile from given user id
def get_user_profile_from_userID(userID):
    user_profile = None
    for profile in user_profile_dict.values():
        if profile['user']['userID'] == userID:
            user_profile = profile
            break
    return user_profile

# Utility method to get all babs from specified user
def get_babs_by_user(userID):
    user_babs = []
    for bab in bab_dict.values():
        if bab['authorUser']['userID'] == userID:
            user_babs.append(bab)
    return user_babs