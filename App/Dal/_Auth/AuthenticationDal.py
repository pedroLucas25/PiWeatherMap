from database import Database

class AuthDAL:

    def verify_access(self, email, token):
        response = dict()
        try:
            dbase = Database()
            with dbase.open() as cursor:
                sql = 'SELECT func_Token_Validate(%s, %s)'
                cursor.execute(sql, (email, token))
                response = cursor.fetchone()
                response = response["func_Token_Validate('{}', '{}')".format(email, token)]
        except Exception as e:
            raise Exception(str(e))
        finally:
            dbase.close()

        return response

    def get_token_from_social(self, token):
        response = dict()
        try:
            dbase = Database()
            with dbase.open() as cursor:
                sql = 'SELECT func_TokenSocial_GetToken(%s)'
                cursor.execute(sql, (token))
                response = cursor.fetchone()
                response = response["func_TokenSocial_GetToken('{}".format(token[0:228])]
        except Exception as e:
            raise Exception(str(e))
        finally:
            dbase.close()

        return response
