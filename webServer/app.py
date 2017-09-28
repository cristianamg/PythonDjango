from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'cbhml20zhv3f08ts'
app.config['MYSQL_DATABASE_PASSWORD'] = 't7v33v230iwad5gj'
app.config['MYSQL_DATABASE_DB'] = 'oiu1isdqj1q4h2e5'
app.config['MYSQL_DATABASE_HOST'] = 'vvfv20el7sb2enn3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
mysql.init_app(app)

class CrearPartida(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID usuario')
            parser.add_argument('tamano', type=str, help='Tamano del tablero')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']
            _Tamano = args['tamano']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('crearPartida', (_ID,_Tamano))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CrearPartida, '/CrearPartida', methods=['POST'])

class CrearJugador(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID usuario')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('crearJugador', (_ID))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];


        except Exception as e:
            return {'error': str(e)}

api.add_resource(CrearJugador, '/CrearJugador', methods=['POST'])


class UpdateMisPartidas(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID usuario')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('updateMisPartidas', (_ID))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];


        except Exception as e:
            return {'error': str(e)}

api.add_resource(UpdateMisPartidas, '/UpdateMisPartidas', methods=['POST'])

class UpdateNickName(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID usuario')
            parser.add_argument('Nick', type=str, help='Nick usuario')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']
            _Nick = args['Nick']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('updateNickName', (_ID,_Nick))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];


        except Exception as e:
            return {'error': str(e)}

api.add_resource(UpdateNickName, '/UpdateNickName', methods=['POST'])

class Unirse(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID usuario')
            parser.add_argument('IDpartida', type=str, help='ID de la partida')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']
            _IDpartida = args['IDpartida']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('unirse', (_ID,_IDpartida))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];

        except Exception as e:
            return {'error': str(e)}

api.add_resource(Unirse, '/Unirse', methods=['POST'])

class Rendirse(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID usuario')
            parser.add_argument('IDpartida', type=str, help='ID de la partida')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']
            _IDpartida = args['IDpartida']

            conn = mysql.connect()
            cursor = conn.cursor()


            cursor.callproc('aumentarGane', (_ID))
            data = cursor.fetchall()
            cursor.callproc('rendirse', (_ID,_IDpartida))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];

        except Exception as e:
            return {'error': str(e)}

api.add_resource(Rendirse, '/Rendirse', methods=['POST'])

class Pausar(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID partida')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('pausar', (_ID))
            data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];

        except Exception as e:
            return {'error': str(e)}

api.add_resource(Pausar, '/Pausar', methods=['POST'])

class Movimiento(Resource):
    def get(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str, help='ID partida')
            parser.add_argument('Turno', type=str, help='turno jugador')
            parser.add_argument('x', type=str, help='x posicion')
            parser.add_argument('y', type=str, help='y posicion')
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']
            _Turno = args['Turno']
            _x = args['x']
            _y = args['y']

            conn = mysql.connect()
            cursor = conn.cursor()
            print( "asd")
            cursor.callproc('obtenerPartida', (_ID))
            data = cursor.fetchall()
            print(data+"asd2")


            #cursor.callproc('movimiento', (_ID))
            #data = cursor.fetchall()

            print(data)
            if len(data) is 0:
                conn.commit()
                return jsonify(True)

            else:
                return data[0][0];

        except Exception as e:
            return {'error': str(e)}

api.add_resource(Movimiento, '/Movimiento', methods=['GET'])
@app.route('/')
def index():
	return "N en Linea"

if __name__ == '__main__':
    app.run(
        host=app.config.get("HOST", 'localhost'),
        port=app.config.get("PORT", 8080),
        debug=True
    )

