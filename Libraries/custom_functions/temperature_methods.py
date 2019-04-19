# las funciones que van  a reemplazar a las de stundet_grade_methods.py#Son

def promedio_temperature(temperature):

    temperature_sum = 0
    temperature_count = len(temperature)


    for tempe in temperature:
        temperature_sum += tempe


    final_temperature = temperature_sum / temperature_count

    return final_temperature


#Funcion que halla la temperatura mas caliente#

def temperature_best(temperature):

    best_temperature = temperature[0]

    for tempe in temperature:

        if tempe > best_temperature:
            best_temperature = tempe

    return best_temperature