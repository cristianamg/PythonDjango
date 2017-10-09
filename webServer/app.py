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
#app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)



'''Metodo de nuevo movimiento'''
'''
#def Gano(MatrizTamano,X,Y,Jugador,Movimientos):
def Gano(MatrizTamano,X,Y,Jugador,MovimientosJugador1,MovimientosJugador2):

    try:

        CantidadParaGanar = MatrizTamano/2
        EjeX = X
        EjeY = Y
        jugador = Jugador

        movimientos = []
        if jugador == 1:
            for element in MovimientosJugador1:
                movimientos.append(element)
        else:
            for element in MovimientosJugador2:
                movimientos.append(element)

        if MovimientosJugador1 == [] and MovimientosJugador2 == []:
            #print("NULL")
            return False

        #cambia X
        def BuscarMenorX(EjeY, jugador):
            for i in movimientos:
                if i[1] == EjeY:
                    return i[0]
            return False

        #cambia Y
        def BuscarMenorY(EjeX, jugador):
            for i in movimientos:
                if i[0] == EjeX:
                    return i[1]
            return False

        def ValidarMovimiento(ContadorParaGanar,CantidadParaGanar):
            if ContadorParaGanar == CantidadParaGanar:
                #print("TrueValidar")
                return True
            else:
                #print("FalseValidar")
                return False


        def ValidarHorizontal(EjeX,CantidadParaGanar,jugador):
            UltimaPosicion = str(BuscarMenorY(EjeX,jugador))  # Sirve para validar el ultimo movimiento de decidir en el contador
            if UltimaPosicion == False:
                #print("FalseValidarHorizontal")
                #print ("false")
                return False

            ContadorParaGanar = 0
            for i in movimientos:
                if int(UltimaPosicion) != i[1]:
                    #print(int(UltimaPosicion) + 1)
                    #print(i[1])
                    if int(UltimaPosicion) + 1 == i[1]:
                        ContadorParaGanar = ContadorParaGanar+1
                        UltimaPosicion = i[1]
                        #print(str(ContadorParaGanar) + 'aaaaasdfasdf')
                        if ValidarMovimiento(ContadorParaGanar, CantidadParaGanar-1) == True:
                           # print("return true")
                           #print ("true")
                            return True
                    else:
                        UltimaPosicion = i[1]
                        ContadorParaGanar = 0

        def ValidarVertical(EjeY,CantidadParaGanar,jugador):
            UltimaPosicion = str(BuscarMenorX(EjeY, jugador))  # Sirve para validar el ultimo movimiento de decidir en el contador
            if UltimaPosicion == False:
                #print("FalseValidarVertical")
                return False

            ContadorParaGanar = 0
            for i in movimientos:
                if int(UltimaPosicion) != i[0]:
                    # print(int(UltimaPosicion) + 1)
                    # print(i[1])
                    if int(UltimaPosicion) + 1 == i[0]:
                        ContadorParaGanar = ContadorParaGanar + 1
                        UltimaPosicion = i[0]
                        # print(str(ContadorParaGanar) + 'aaaaasdfasdf')
                        if ValidarMovimiento(ContadorParaGanar, CantidadParaGanar - 1) == True:
                            # print("return true")
                            return True
                    else:
                        UltimaPosicion = i[0]
                        ContadorParaGanar = 0

                        #print ("Entro")
        if ValidarHorizontal(EjeX,CantidadParaGanar,jugador) or ValidarVertical(EjeY,CantidadParaGanar,jugador):
            print ("EntroSi")
            return True
        else:
            print ("EntroNo")
            return False

    except Exception as e:
        print(e.message)
        return {'error': str(e)}

def Gano(MatrizTamano,X,Y,Jugador,MovesJugador1, MovesJugador2):
   # Gano(6, 2, 0, jugador, [[0, 1], [1, 1]], [[0 - 0], [1 - 0]])
      try:
        CantidadParaGanar = (MatrizTamano/2)-1
        print (CantidadParaGanar)

        EjeX = X
        EjeY = Y
        #if Jugador == 'Jugador1':
        if Jugador == 1:
            Movimientos = MovesJugador1
        else:
            Movimientos = MovesJugador2


        MovimientosJugador1 = MovesJugador1#Movimientos['jugador1']['movimientos']
        MovimientosJugador2 = MovesJugador2#Movimientos['jugador2']['movimientos']

        print(MovimientosJugador1)
        print(MovimientosJugador2)
        if MovimientosJugador1 == [] and MovimientosJugador2 == []:
            #print("NULL")
            return False

        #cambia X
        def BuscarMenorX(EjeY):
            for i in Movimientos:
                if i[1] == EjeY:
                    return i[0]
            return False

        #cambia Y
        def BuscarMenorY(EjeX):
            for i in Movimientos:
                if i[0] == EjeX:
                    return i[1]
            return False

        def ValidarMovimiento(ContadorParaGanar,CantidadParaGanar):
            if ContadorParaGanar >= CantidadParaGanar:
                #print("TrueValidar")
                return True
            else:
                #print("FalseValidar")
                return False


        def ValidarHorizontal(EjeX,CantidadParaGanar):
            UltimaPosicion = str(BuscarMenorY(EjeX))  # Sirve para validar el ultimo movimiento de decidir en el contador
            if UltimaPosicion == 'False':
                return False

            ContadorParaGanar = 0
            for i in Movimientos:
                if int(UltimaPosicion) != i[1]:
                    #print(int(UltimaPosicion) + 1)
                    #print(i[1])
                    if int(UltimaPosicion) + 1 == i[1]:
                        ContadorParaGanar = ContadorParaGanar+1
                        UltimaPosicion = i[1]
                        #print(str(ContadorParaGanar) + 'aaaaasdfasdf')
                        if ValidarMovimiento(ContadorParaGanar, CantidadParaGanar-1) == True:
                           # print("return true")
                            return True
                    else:
                        UltimaPosicion = i[1]
                        ContadorParaGanar = 0

        def ValidarVertical(EjeY,CantidadParaGanar):
            UltimaPosicion = str(BuscarMenorX(EjeY))  # Sirve para validar el ultimo movimiento de decidir en el contador
            if UltimaPosicion == 'False':
               # print("FalseValidarVertical")
                return False

            ContadorParaGanar = 0
            for i in Movimientos:
                if int(UltimaPosicion) != i[0]:
                    # print(int(UltimaPosicion) + 1)
                    # print(i[1])
                    if int(UltimaPosicion) + 1 == i[0]:
                        ContadorParaGanar = ContadorParaGanar + 1
                        UltimaPosicion = i[0]
                        # print(str(ContadorParaGanar) + 'aaaaasdfasdf')
                        if ValidarMovimiento(ContadorParaGanar, CantidadParaGanar - 1) == True:
                            # print("return true")
                            return True
                    else:
                        UltimaPosicion = i[0]
                        ContadorParaGanar = 0

        #print(ValidarVertical(EjeY, CantidadParaGanar, jugador))

        if ValidarHorizontal(EjeX,CantidadParaGanar) or ValidarVertical(EjeY,CantidadParaGanar):
           return True
        else:
            return False
        #   print(Gano(8,7,2,1,[[0,2],[2,2],[4,2],[5,2],[6,2],[7,2]],[[1,2],[3,2]]))
            #MatrizTamano,X,Y,Jugador,Movimientos
      except Exception as e:
          print (e)
    '''
def Gano(MatrizTamano,X,Y,Jugador,MovesJugador1, MovesJugador2):
    CantidadParaGanar = int(MatrizTamano/2)

    def validarHorizontal(Movimientos,CantidadparaGanar):
        print("ValidarHorizontal")
        if len(Movimientos) < CantidadparaGanar:
            return False
        listaNumeros = []
        for i in Movimientos:
            if listaNumeros.__contains__(i[0]) == False:
                listaNumeros.append(i[0])
            if listaNumeros.__contains__(i[1]) == False:
                listaNumeros.append(i[1])

        listasCompletas = []
        for i in listaNumeros:
            listatemp = []
            for x in Movimientos:
                if i == x[0]:
                    listatemp.append(x)
            if listatemp != []:
                listasCompletas.append(listatemp)

        listaOrdenada = []
        for i in sorted(listasCompletas):
            listaOrdenada.append(sorted(i))

        def validarMovimiento(FilaColumna, CantidadparaGanar):
            cont = 0
            valorActual = FilaColumna[0][1]
            i = 1
            while i < len(FilaColumna):
                if FilaColumna[i][1] == valorActual + 1:
                    valorActual = FilaColumna[i][1]
                    cont += 1
                else:
                    cont = 0
                    valorActual = FilaColumna[i][1]
                if cont == CantidadparaGanar - 1:
                    return True
                i += 1
            return False

        for i in listaOrdenada:
            if validarMovimiento(i, CantidadparaGanar):
                return True

        return False


    def validarVerticar(Movimientos,CantidadparaGanar):
        print("ValidarVertical")
        if len(Movimientos) < CantidadparaGanar:
            return False
        listaNumeros = []
        for i in Movimientos:
            if listaNumeros.__contains__(i[0]) == False:
                listaNumeros.append(i[0])
            if listaNumeros.__contains__(i[1]) == False:
                listaNumeros.append(i[1])

        listasCompletas = []
        for i in listaNumeros:
            listatemp = []
            for x in Movimientos:
                if i == x[1]:
                    listatemp.append(x)
            if listatemp != []:
                listasCompletas.append(listatemp)

        listaOrdenada = []
        for i in sorted(listasCompletas):
            listaOrdenada.append(sorted(i))

        def validarMovimiento(FilaColumna, CantidadparaGanar):
            cont = 0
            valorActual = FilaColumna[0][0]
            i = 1
            while i < len(FilaColumna):
                if FilaColumna[i][0] == valorActual + 1:
                    valorActual = FilaColumna[i][0]
                    cont += 1
                else:
                    cont = 0
                    valorActual = FilaColumna[i][0]
                if cont == CantidadparaGanar - 1:
                    return True
                i += 1
            return False

        for i in listaOrdenada:
            if validarMovimiento(i, CantidadparaGanar):
                return True

        return False

    def validarDiagonalPar(Movimientos,CantidadparaGanar):
        print("ValidarDiagonalPar")
        if len(Movimientos) < CantidadparaGanar:
            return False

        def validarMovimiento(FilaColumna, CantidadparaGanar):
            cont = 0
            valorActual = FilaColumna[0][0]
            i = 1
            while i < len(FilaColumna):
                if FilaColumna[i][0] == valorActual + 1:
                    valorActual = FilaColumna[i][0]
                    cont += 1
                else:
                    cont = 0
                    valorActual = FilaColumna[i][0]
                if cont == CantidadparaGanar - 1:
                    return True
                i += 1
            return False

        listaDiagonal = []
        for i in Movimientos:
            if i[0] == i[1]:
                listaDiagonal.append(i)

        listaDiagonalOrdenada = sorted(listaDiagonal)

        if validarMovimiento(listaDiagonalOrdenada, CantidadparaGanar):
            return True
        else:
            return False

    def validarDiagonalSum(Movimientos,CantidadparaGanar):
        print("ValidarDiagonalSum")
        if len(Movimientos) < CantidadparaGanar:
            return False

        def validarMovimiento(FilaColumna, CantidadparaGanar):
            cont = 0
            valorActual = FilaColumna[0][0]
            i = 1
            while i < len(FilaColumna):
                if FilaColumna[i][0] == valorActual + 1:
                    valorActual = FilaColumna[i][0]
                    cont += 1
                else:
                    cont = 0
                    valorActual = FilaColumna[i][0]
                if cont == CantidadparaGanar - 1:
                    return True
                i += 1
            return False

        listaDiagonal = []
        for i in Movimientos:
            if i[0] + i[1] == (CantidadparaGanar * 2) - 1:
                listaDiagonal.append(i)

        listaDiagonalOrdenada = sorted(listaDiagonal)

        if validarMovimiento(listaDiagonalOrdenada, CantidadparaGanar):
            return True
        else:
            return False


    if Jugador == 1:
        MovesJugador1.append([X, Y])
        if validarVerticar(MovesJugador1,CantidadParaGanar) or validarHorizontal(MovesJugador1, CantidadParaGanar) or validarDiagonalPar(MovesJugador1,CantidadParaGanar)or validarDiagonalSum(MovesJugador1,CantidadParaGanar):
            return True
        else:
            return False
    else:
        MovesJugador2.append([X,Y])
        if validarVerticar(MovesJugador2,CantidadParaGanar) or validarHorizontal(MovesJugador2, CantidadParaGanar) or validarDiagonalPar(MovesJugador2,CantidadParaGanar) or validarDiagonalSum(MovesJugador2,CantidadParaGanar):
            return True
        else:
            return False

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

class Movimiento(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('ID', type=str)
            parser.add_argument('Turno', type=str)
            parser.add_argument('x', type=str)
            parser.add_argument('y', type=str)
            parser.add_argument('ListaJugadas1', type=str)
            parser.add_argument('ListaJugadas2', type=str)
            parser.add_argument('Tamano', type=str)
            parser.add_argument('IdJugador', type=str)
            args = parser.parse_args()

            print(args.items())
            _ID = args['ID']
            _Turno = args['Turno']
            _x= args['x']
            _y = args['y']
            _ListaJugadas1 = args['ListaJugadas1']
            _ListaJugadas2 = args['ListaJugadas2']
            _Tamano = args['Tamano']
            _IdJugador = args['IdJugador']

            ListaJugadas1 = []
            ListaJugadas2 = []

            ListaJugadas1s= _ListaJugadas1.replace("[","").replace("]","");
            ListaJugadas2s= _ListaJugadas2.replace("[","").replace("]","");


            if(len(_ListaJugadas1)>2):
                for jugada in ListaJugadas1s.split(','):
                    lista = []
                    lista.append(int(jugada.replace("[","").replace("]","").split('-')[0]))
                    lista.append(int(jugada.replace("[","").replace("]","").split('-')[1]))
                    ListaJugadas1.append(lista)

            if (len(_ListaJugadas2)>2):
                for jugada in ListaJugadas2s.split(','):
                    lista = []
                    lista.append(int(jugada.replace("[","").replace("]","").split('-')[0]))
                    lista.append(int(jugada.replace("[","").replace("]","").split('-')[1]))
                    ListaJugadas2.append(lista)


            if Gano(int(_Tamano),int(_x),int(_y),int(_Turno),ListaJugadas1,ListaJugadas2):
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc('aumentarGane', (_IdJugador))
                data = cursor.fetchall()
                conn.commit()
                print(data)

                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc('gano', (_ID, _IdJugador))
                data = cursor.fetchall()
                conn.commit()
                print(data)
            else:
                print ("noooo")

            if (int(_Turno) == 1):
                conn = mysql.connect()
                cursor = conn.cursor()
                if(len(_ListaJugadas1)<3):
                    jugada = _ListaJugadas1.replace("]", "") + _x + "-" + _y + "]"
                    cursor.callproc('movimientoJ1', (_ID, jugada))
                    data = cursor.fetchall()
                    print(data)
                    conn.commit()
                else:
                    jugada = _ListaJugadas1.replace("]", ",") + _x + "-" + _y + "]"
                    cursor.callproc('movimientoJ1', (_ID, jugada))
                    data = cursor.fetchall()
                    print(data)
                    conn.commit()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

                if (len(_ListaJugadas2) < 3):
                    jugada = _ListaJugadas2.replace("]", "") + _x + "-" + _y + "]"
                    cursor.callproc('movimientoJ2', (_ID, jugada))
                    data = cursor.fetchall()
                    print(data)
                    conn.commit()
                else:
                    jugada = _ListaJugadas2.replace("]", ",") + _x + "-" + _y + "]"
                    cursor.callproc('movimientoJ2', (_ID, jugada))
                    data = cursor.fetchall()
                    print(data)
                    conn.commit()

        except Exception as e:
            print (e)
            return {'error': str(e)}

            return True

api.add_resource(Movimiento, '/Movimiento', methods=['POST'])

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

@app.route('/')
def index():
	return "N en Linea"

if __name__ == '__main__':
    app.run(
        host=app.config.get("HOST", 'localhost'),
        port=app.config.get("PORT", 8080),
        debug=True
    )

