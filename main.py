# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging

from flask import Flask


app = Flask(__name__)


@app.route('/')
#def hello():
#    """Return a friendly HTTP greeting."""
#    return 'Hello World!'

def imc():
    #Le pedimos el nombre y lo guardamos en un input (Si usara Python 2.7 seria raw_input y no input pero usa python 3.7)
    n = input("Su nombre por favor: ")
    #Se pide al edad que siempre es un entero por eso el int() 
    e = int(input("Su edad en años por favor: "))
    #como la altura es en metros y no centimetros hay que ponerle punto y por ende es un flotante float()
    a = float(input ("Su altura en metros por favor: "))
    #Aqui se duplica codigo pero bueno... decimos que est (de estatura) es igual a altura (No me diga)
    est = a
    #La masa en kilogramos si puede tener decimales asi que la dejamos flotante
    m = float (input("Su masa en kilogramos por favor :"))
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
    IMC = m / est**2
    #Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
    #Solo ruegue porque a nadie se le ocurra meter numeros negativos, le va a decir que es menor de edad
    if(e < 18):
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")
    #Le imprimos el IMC para que se ponga sad
    print("IMC: " + str(IMC) )

    #Hacemos las distintas validaciones
    if IMC >= 0 and IMC <= 15.99 :
        return ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        return ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        return ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        return ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        return ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        return ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        return ("obesidad media")
    elif IMC >= 40.00:
        return ("obesidad morbida")


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
