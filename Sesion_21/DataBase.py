import sqlite3

def Registrar(nombre,apellido,edad,documento):
    db = sqlite3.connect("datos.s3db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    consulta = "insert into Personas (nombre,apellido,edad,documento) values ('"+ nombre +"','" + apellido + "'," + str(edad) +","+str(documento)+")"
    cursor.execute(consulta)
    db.commit()
    cursor.close()
    db.close()
    return "1"

def validar(usuario):
    db=sqlite3.connect("datos.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select * from Personas where apellido = '" + usuario +"'"
    cursor.execute(consulta)
    resultado=cursor.fetchone()
    print(list(resultado))
    cursor.close()
    db.close()
    return resultado

def main():
    nombre=input('Ingrese el nombre: ')
    apellido=input('Ingrese el apellido: ')
    edad=int(input('Ingrese la edad: '))
    documento=int(input('Ingrese su documento: '))
    Registrar(nombre,apellido,edad,documento)
    consulta = input('\nIngrese el apellido de busqueda: ')
    validar(consulta)


if __name__ == "__main__":
    main()