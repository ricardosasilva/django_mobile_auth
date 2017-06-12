from django.contrib.auth import get_user_model


class MobileAuthBackend(object):
    """Allows user to sign-in using email, username or phone_number."""

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            if '@' in username:
                user = UserModel._default_manager.get(email=username)
            elif '+' in username[0]:
                user = UserModel._default_manager.get(phone_number=username)
            else:
                user = UserModel._default_manager.get(username=username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def user_can_authenticate(self, user):
        """Reject users with is_active=False. Custom user models that don't have that attribute are allowed."""
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
