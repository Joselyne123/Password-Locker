class User:
    """
    Class that generates new user instances
    """


    user_list = []

    def __init__(self,first_name, last_name, user_name, password):

        '''
        __init__ method that helps us define properties for our objects.
        Args:
            first_name: New user first name.
            last_name : New user last name.
            user_name: New user username.
            password : New user password.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes user objects from the user_list
        '''

        ser.user_list.remove(self)


    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.
        Args:
            username: Username to search for
        Returns :
            User details of person that matches the user.
        '''

        for user in cls.user_list:
            if user.user_name == username:
                return user


    @classmethod
    def find_by_userpassword(cls,userpassword):
        for password in cls.user_list:
            if password.password == userpassword:
                return password


    @classmethod
    def display_userInfo(cls):
        return cls.user_list




class Account:

    account_list = []

    def __init__(self, account_name, account_userName, account_password):

        self.account_name = account_name
        self.account_userName = account_userName
        self.account_password = account_password

    def save_account(self):
        Account.account_list.append(self)

    @classmethod
    def display_accounts(cls):
        return cls.account_list

    def delete_account(self):
        Account.account_list.remove(self)

    @classmethod
    def find_by_accountName(cls,accountname):
        for account in cls.account_list:
            if account.account_name == accountname:
                return account