from django.db import models

from account_module.models import User


def update_info(username, select_option, select_change_info):

    user = User.objects.get(username=username)

    user_info = user.get_user_info()

    match select_option:

        case 'firstname':
            user.update_user_info(first_name=select_change_info,
                                  last_name=user_info['lastname'],
                                  username=user_info['username'],
                                  password=user_info['password'],
                                  image=user_info['image'],
                                  email=user_info['email'],
                                  address=user_info['address'])

        case 'lastname':
            user.update_user_info(first_name=user_info['firstname'],
                                  last_name=select_change_info,
                                  username=user_info['username'],
                                  password=user_info['password'],
                                  image=user_info['image'],
                                  email=user_info['email'],
                                  address=user_info['address'])

        case 'username':
            user.update_user_info(first_name=user_info['firstname'],
                                  last_name=user_info['lastname'],
                                  username=select_change_info,
                                  password=user_info['password'],
                                  image=user_info['image'],
                                  email=user_info['email'],
                                  address=user_info['address'])

        case 'password':
            user.update_user_info(first_name=user_info['firstname'],
                                  last_name=user_info['lastname'],
                                  username=user_info['username'],
                                  password=select_change_info,
                                  image=user_info['image'],
                                  email=user_info['email'],
                                  address=user_info['address'])

        case 'image':
            user.update_user_info(first_name=user_info['firstname'],
                                  last_name=user_info['lastname'],
                                  username=user_info['username'],
                                  password=user_info['password'],
                                  image=select_change_info,
                                  email=user_info['email'],
                                  address=user_info['address'])

        case 'email':
            user.update_user_info(first_name=user_info['firstname'],
                                  last_name=user_info['lastname'],
                                  username=user_info['username'],
                                  password=user_info['password'],
                                  image=user_info['image'],
                                  email=select_change_info,
                                  address=user_info['address'])

        case 'address':
            user.update_user_info(first_name=user_info['firstname'],
                                  last_name=user_info['lastname'],
                                  username=user_info['username'],
                                  password=user_info['password'],
                                  image=user_info['image'],
                                  email=user_info['email'],
                                  address=select_change_info)
