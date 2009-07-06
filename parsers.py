from datetime import datetime

try:
  import json
except ImportError:
  import simplejson as json

def parse_error(data):

  return json.loads(data)['error']

def _parse_datetime(str):

  return datetime.strptime(str, '%a %b %d %H:%M:%S +0000 %Y')

def _parse_user(obj, api):

  user = api.classes['user']()
  user._api = api
  for k,v in obj.items():
    if k == 'created_at':
      setattr(user, k, _parse_datetime(v))
    elif k == 'status':
      setattr(user, k, _parse_status(v, api))
    else:
      setattr(user, k, v)
  return user

def parse_user(data, api):

  return _parse_user(json.loads(data), api)

def parse_users(data, api):

  users = []
  for obj in json.loads(data):
    users.append(_parse_user(obj, api))
  return users

def _parse_status(obj, api):

  status = api.classes['status']()
  status._api = api
  for k,v in obj.items():
    if k == 'user':
      setattr(status, k, _parse_user(v, api))
    elif k == 'created_at':
      setattr(status, k, _parse_datetime(v))
    else:
      setattr(status, k, v)
  return status

def parse_status(data, api):

  return _parse_status(json.loads(data), api)

def parse_statuses(data, api):

  statuses = []
  for obj in json.loads(data):
    statuses.append(_parse_status(obj, api))
  return statuses