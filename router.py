class AuthRouter:
    route_app_labels = {'user', 'admin', 'contenttypes', 'sessions', }

    def db_read(self, model, **hints):  # read from user model in database
        # if model exists inside of self, we return user data base
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def db_write(self, model, **hints):  # write to user model
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    # makes sure the relations happen if the user model is involved
    def relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    # user only appears in user database
    def migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users'
        return None
