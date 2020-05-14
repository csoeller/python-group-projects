def from_molars_to_miligrams_per_milimetre(miligrams_per_mililitre):
    molecular_weight = int(input("Enter Molecular Weight of the antibody: "))
    return miligrams_per_mililitre * molecular_weight


antibody_concentration_molar = 0
new_antibody_concentration_molar = 0
dbco_concentration = 0
oligo_concentration_molar = 0
absorption_coefficient = 0


def antibody_concentration_calc():
    question = input('Does antibody already have a dye on it (y/n)? ')
    print(question)
    y = True
    n = False
    if question:



    global antibody_concentration_molar
    global absorption_coefficient
    absorbance_280_1 = float(input("Enter 1st antibody absorbance value (280 nm): "))
    absorbance_280_2 = float(input("Enter 2nd antibody absorbance value (280 nm): "))
    absorbance_280_3 = float(input("Enter 3rd antibody absorbance value (280 nm): "))
    absorption_coefficient = int(input("Enter antibody absorption coefficient: "))
    length = 0.1
    absorbance_280 = (absorbance_280_1 + absorbance_280_2 + absorbance_280_3) / 3
    antibody_concentration_molar = absorbance_280 / (absorption_coefficient * length)
    antibody_concentration_mg_ml = from_molars_to_miligrams_per_milimetre(antibody_concentration_molar)  # antibody_concentration_molar * molecular_weight

    return {
        "Moles": '{:.10f}'.format(antibody_concentration_molar),
        "mg/mL": '{:.10f}'.format(antibody_concentration_mg_ml)
    }


print(antibody_concentration_calc())

# create a boolean which leads to if statement for calculation when antibody has a dye on it.


def dbco_concentration_calc():
    absorption_coefficient = 12000
    length = 0.1
    absorbance_309_1 = float(input("Enter 1st DBCO absorbance value (309 nm): "))
    absorbance_309_2 = float(input("Enter 2nd DBCO absorbance value (309 nm): "))
    absorbance_309_3 = float(input("Enter 3rd DBCO absorbance value (309 nm): "))
    absorbance_309 = (absorbance_309_1 + absorbance_309_2 + absorbance_309_3) / 3
    dbco_concentration = absorbance_309 / (absorption_coefficient * length)
    final_dbco_concentration = '{:.10f}'.format(dbco_concentration)
    print(final_dbco_concentration + ' Moles')
    global antibody_concentration_molar
    antibody_volume = int(input("Enter antibody volume used: "))
    dbco_volume_required = (antibody_volume * (float(antibody_concentration_molar) * 10)) / dbco_concentration

    return {
        "DBCO concentration": '{:.10f}'.format(dbco_concentration),
        "DBCO volume required": '{:.10f}'.format(dbco_volume_required)
    }


print(dbco_concentration_calc())


def oligo_concentration_calc():
    oligo_absorbance_260_1 = float(input("Enter 1st oligo absorbance value (260 nm): "))
    oligo_absorbance_dye_1 = float(input("Enter 1st absorbance value of the dye: "))
    oligo_absorbance_260_2 = float(input("Enter 2nd oligo absorbance value (260 nm): "))
    oligo_absorbance_dye_2 = float(input("Enter 2nd absorbance value of the dye: "))
    oligo_absorbance_260_3 = float(input("Enter 3rd oligo absorbance value (260 nm): "))
    oligo_absorbance_dye_3 = float(input('Enter 3rd absorbance value of the dye: '))
    dye_correction_factor = float(input('Enter the correction factor (CF) of the dye: '))
    dilution_factor = int(input('Enter the dilution factor (DF): '))
    extinction_coefficient = int(input('Enter oligo extinction coefficient: '))
    length = 0.1
    global oligo_concentration_molar
    oligo_absorbance_260 = (oligo_absorbance_260_1 + oligo_absorbance_260_2 + oligo_absorbance_260_3) / 3
    oligo_absorbance_dye = (oligo_absorbance_dye_1 + oligo_absorbance_dye_2 + oligo_absorbance_dye_3) / 3
    oligo_concentration_molar = ((oligo_absorbance_260 - (oligo_absorbance_dye * dye_correction_factor)) * dilution_factor) / (extinction_coefficient * length)
    oligo_concentration_micromolar = oligo_concentration_molar * 1000000

    return {
        "Oligo concentration (Moles)": '{:.10f}'.format(oligo_concentration_molar),
        "Oligo concentration (microMoles": '{:.10f}'.format(oligo_concentration_micromolar)
    }


print(oligo_concentration_calc())



def degree_dbco_inc_calc():
    global absorption_coefficient
    global new_antibody_concentration_molar
    absorbance_280_1 = float(input("Enter 1st antibody absorbance value (280 nm): "))
    absorbance_309_1 = float(input("Enter 1st DBCO absorbance value (309 nm): "))
    absorbance_280_2 = float(input("Enter 2nd antibody absorbance value (280 nm): "))
    absorbance_309_2 = float(input("Enter 2nd DBCO absorbance value (309 nm): "))
    absorbance_280_3 = float(input("Enter 3rd antibody absorbance value (280 nm): "))
    absorbance_309_3 = float(input("Enter 3rd DBCO absorbance value (309 nm): "))
    length = 0.1
    dbco_correction_factor = 1.089
    dbco_absorption_coefficient = 12000
    absorbance_280 = (absorbance_280_1 + absorbance_280_2 + absorbance_280_3) / 3
    absorbance_309 = (absorbance_309_1 + absorbance_309_2 + absorbance_309_3) / 3
    new_antibody_concentration_molar = (absorbance_280 - (absorbance_309 * dbco_correction_factor)) / (absorption_coefficient * length)
    new_dbco_concentration = absorbance_309 / (dbco_absorption_coefficient * length)
    ratio = (new_antibody_concentration_molar / new_dbco_concentration)
    print('Degree of DBCO incorporation - ' + str(ratio) + ' : 1')

    return {
        "Antibody concentration (Moles)": '{:.10f}'.format(new_antibody_concentration_molar),
        "DBCO concentration (Moles)": '{:.10f}'.format(new_dbco_concentration),
    }


print(degree_dbco_inc_calc())


def oligo_conjugation_calc():
    global new_antibody_concentration_molar
    global oligo_concentration_molar
    antibody_volume = int(input('Enter antibody volume used: '))
    oligo_volume_required = (antibody_volume * (new_antibody_concentration_molar * 10)) / oligo_concentration_molar

    return print('Oligo volume required: ' + str(oligo_volume_required) + ' microlitres')


print(oligo_conjugation_calc())
