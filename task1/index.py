from flask import Blueprint, session, after_this_request

index_bp = Blueprint(
        name='index',
        import_name=__name__,
        url_prefix='/'
    )


# @index_bp.before_app_first_request
# def init_session():
#     session['active_connections'] = 1

@index_bp.route('/', methods=['GET'])
def index():
    if session:
        session['active_connections'] += 1
    else:
        session['active_connections'] = 1

    @after_this_request
    def remove_connection(response):
        session['active_connections'] -= 1
        return response

    return 'Welcome to our application'


